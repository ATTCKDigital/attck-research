"""Research database lookups with API keys, throttling and a shared cache.

Review agents call this instead of fetching the APIs directly, so parallel reviews share one cache and one rate budget.
Prints JSON to stdout.

  python3 research_api.py work DOI                       title, abstract, ids and citation count (OpenAlex)
  python3 research_api.py cites DOI [TERM] [--n 50]      papers citing DOI, newest first, optionally filtered by TERM
  python3 research_api.py search "QUERY" [--n 25]        OpenAlex topic search (one or two terms works best)
  python3 research_api.py s2-cites DOI [--n 100]         Semantic Scholar citing papers with abstracts
  python3 research_api.py s2-search "QUERY" [--n 25]
  python3 research_api.py epmc "QUERY" [--n 25]          Europe PMC search (DOI:"…", EXT_ID:… AND SRC:MED syntax)
  python3 research_api.py epmc-cites DOI [--n 25]        Europe PMC citing papers (biomedical and psychology journals)
  python3 research_api.py crossref DOI                   Crossref record (title, abstract when deposited)
  python3 research_api.py pubmed PMID                    PubMed abstract text
Falls back from OpenAlex to Semantic Scholar to Europe PMC when a service refuses, and says which one answered.
"""

import json
import sys
import urllib.parse

from common import env, get, get_json

E = env()
OA = "https://api.openalex.org"
S2 = "https://api.semanticscholar.org/graph/v1"


def oa_params(**kw):
    if E.get("OPENALEX_API_KEY"):
        kw["api_key"] = E["OPENALEX_API_KEY"]
    return urllib.parse.urlencode(kw)


def s2_headers():
    return (
        {"x-api-key": E["SEMANTIC_SCHOLAR_API_KEY"]}
        if E.get("SEMANTIC_SCHOLAR_API_KEY")
        else None
    )


def oa_abstract(w):
    inv = w.get("abstract_inverted_index") or {}
    return " ".join(t for _, t in sorted((i, t) for t, ii in inv.items() for i in ii))


def oa_slim(w):
    return {
        "title": w.get("title"),
        "year": w.get("publication_year"),
        "doi": w.get("doi"),
        "openalex": w.get("id"),
        "cited_by": w.get("cited_by_count"),
        "abstract": oa_abstract(w)[:1500],
    }


def work(doi):
    code, j = get_json(f"{OA}/works/doi:{doi}?{oa_params()}")
    if j:
        return {"source": "openalex", **oa_slim(j)}
    code, j = get_json(
        f"{S2}/paper/DOI:{doi}?fields=title,year,abstract,externalIds,citationCount",
        s2_headers(),
    )
    if j:
        return {
            "source": "semanticscholar",
            "title": j.get("title"),
            "year": j.get("year"),
            "doi": doi,
            "cited_by": j.get("citationCount"),
            "abstract": j.get("abstract"),
        }
    return crossref(doi)


def cites(doi, term=None, n=50):
    code, w = get_json(f"{OA}/works/doi:{doi}?{oa_params()}")
    if w:
        flt = f"cites:{w['id'].rsplit('/', 1)[1]}" + (
            f",title_and_abstract.search:{term}" if term else ""
        )
        code, j = get_json(
            f"{OA}/works?{oa_params(filter=flt, sort='publication_date:desc', per_page=n)}"
        )
        if j:
            return {
                "source": "openalex",
                "cited": w.get("title"),
                "results": [oa_slim(x) for x in j.get("results", [])],
            }
    for fetch in (s2_cites, epmc_cites):
        r = fetch(doi, n * 4 if term else n)
        if r.get("results") and term:
            t = term.lower()
            r["results"] = [
                x
                for x in r["results"]
                if t
                in ((x.get("title") or "") + " " + (x.get("abstract") or "")).lower()
            ][:n]
            r["filter"] = term
        if r.get("results"):
            return r
    return r


def epmc_cites(doi, n=25):
    """Europe PMC citing papers, newest first. Resolves the DOI to a PubMed id (Europe PMC stores some older DOIs
    with a doubled slash), then reads the citations endpoint and fetches abstracts for the newest citers."""
    hit = []
    for v in (doi, doi.replace("/", "//", 1)):
        hit = epmc(f'DOI:"{v}"', 1).get("results") or []
        if hit and hit[0].get("pmid"):
            break
    if not hit or not hit[0].get("pmid"):
        return {
            "source": "europepmc",
            "results": [],
            "note": "DOI not indexed in Europe PMC",
        }
    code, j = get_json(
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/MED/{hit[0]['pmid']}/citations?format=json&pageSize=1000"
    )
    rows = ((j or {}).get("citationList") or {}).get("citation") or []
    rows = sorted(rows, key=lambda r: r.get("pubYear") or 0, reverse=True)[:n]
    ids = " OR ".join(f"EXT_ID:{r['id']}" for r in rows if r.get("source") == "MED")
    abstracts = (
        {r.get("pmid"): r for r in epmc(f"({ids}) AND SRC:MED", n).get("results", [])}
        if ids
        else {}
    )
    return {
        "source": "europepmc",
        "cited": hit[0].get("title"),
        "hits": (j or {}).get("hitCount"),
        "results": [
            {
                "title": r.get("title"),
                "year": r.get("pubYear"),
                "pmid": r.get("id"),
                "doi": (abstracts.get(r.get("id")) or {}).get("doi"),
                "abstract": (abstracts.get(r.get("id")) or {}).get("abstract"),
            }
            for r in rows
        ],
    }


def search(q, n=25):
    code, j = get_json(f"{OA}/works?{oa_params(search=q, per_page=n)}")
    if j:
        return {
            "source": "openalex",
            "results": [oa_slim(x) for x in j.get("results", [])],
        }
    return s2_search(q, n)


def s2_cites(doi, n=100):
    code, j = get_json(
        f"{S2}/paper/DOI:{doi}/citations?fields=title,year,abstract,externalIds&limit={min(n, 1000)}",
        s2_headers(),
    )
    rows = [c.get("citingPaper", {}) for c in (j or {}).get("data", [])]
    return {
        "source": "semanticscholar",
        "http": code,
        "results": [
            {
                "title": p.get("title"),
                "year": p.get("year"),
                "doi": (p.get("externalIds") or {}).get("DOI"),
                "abstract": (p.get("abstract") or "")[:1500],
            }
            for p in rows
        ],
    }


def s2_search(q, n=25):
    code, j = get_json(
        f"{S2}/paper/search?{urllib.parse.urlencode({'query': q, 'limit': n, 'fields': 'title,year,abstract,externalIds'})}",
        s2_headers(),
    )
    if j and j.get("data"):
        return {
            "source": "semanticscholar",
            "results": [
                {
                    "title": p.get("title"),
                    "year": p.get("year"),
                    "doi": (p.get("externalIds") or {}).get("DOI"),
                    "abstract": (p.get("abstract") or "")[:1500],
                }
                for p in j["data"]
            ],
        }
    return epmc(q, n)


def epmc(q, n=25):
    code, j = get_json(
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
        + urllib.parse.urlencode(
            {"query": q, "format": "json", "resultType": "core", "pageSize": n}
        )
    )
    rows = ((j or {}).get("resultList") or {}).get("result") or []
    return {
        "source": "europepmc",
        "http": code,
        "hits": (j or {}).get("hitCount"),
        "results": [
            {
                "title": r.get("title"),
                "year": r.get("pubYear"),
                "doi": r.get("doi"),
                "pmid": r.get("pmid"),
                "abstract": (r.get("abstractText") or "")[:1500],
            }
            for r in rows
        ],
    }


def crossref(doi):
    code, j = get_json(
        "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    )
    m = (j or {}).get("message") or {}
    return {
        "source": "crossref",
        "http": code,
        "title": " ".join(m.get("title") or []),
        "doi": doi,
        "year": ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0],
        "abstract": m.get("abstract"),
    }


def pubmed(pmid):
    code, body = get(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&rettype=abstract&retmode=text"
    )
    return {
        "source": "pubmed",
        "http": code,
        "pmid": pmid,
        "text": body.decode("utf-8", "ignore"),
    }


def main(a):
    n = int(a[a.index("--n") + 1]) if "--n" in a else None
    a = [x for i, x in enumerate(a) if x != "--n" and (i == 0 or a[i - 1] != "--n")]
    cmd, rest = a[0], a[1:]
    kw = {"n": n} if n else {}
    out = {
        "work": lambda: work(rest[0]),
        "cites": lambda: cites(rest[0], rest[1] if len(rest) > 1 else None, **kw),
        "search": lambda: search(rest[0], **kw),
        "s2-cites": lambda: s2_cites(rest[0], **kw),
        "s2-search": lambda: s2_search(rest[0], **kw),
        "epmc-cites": lambda: epmc_cites(rest[0], **kw),
        "epmc": lambda: epmc(rest[0], **kw),
        "crossref": lambda: crossref(rest[0]),
        "pubmed": lambda: pubmed(rest[0]),
    }[cmd]()
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1:])
