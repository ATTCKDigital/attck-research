"""Confirm every evidence quote in an article's pass files (no model involved).

  python3 verify_quotes.py 10 [--resume]

Re-fetches each URL in work/NN/pass2-5*.json and checks the quote appears, after normalizing case, quotes, dashes and
whitespace. Order per URL: the page itself, then (for DOIs, PubMed and Europe PMC links) OpenAlex, Crossref,
Europe PMC, Semantic Scholar and PubMed abstracts. Writes work/NN/verify.json after every item; with --resume only
items not yet confirmed are rechecked. Status: confirmed, close (85%+ of the quote's 5-word runs found), unconfirmed,
fetch-failed. Prints a summary line.
"""

import concurrent.futures as cf
import hashlib
import html
import json
import os
import re
import subprocess
import unicodedata
import sys
import urllib.parse

from common import article_dir, get
import research_api as api


def items(d):
    out = []

    def walk(x, src):
        if isinstance(x, dict):
            q = x.get("quote") or x.get("passage")
            if x.get("url") and q:
                out.append((x["url"].strip(), q.strip(), src))
            for v in x.values():
                walk(v, src)
        elif isinstance(x, list):
            for v in x:
                walk(v, src)

    for f in sorted(os.listdir(d)):
        if re.match(r"pass[2-5].*\.json$", f):
            walk(json.load(open(os.path.join(d, f))), f)
    return out


def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s)).lower().replace("\\n", " ")  # NFKC splits PDF ligatures  # some records store literal "\n"
    s = re.sub(r"[‘’‚′`]", "'", s)
    s = re.sub(r"[“”„″]", '"', s)
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"\[[^\]]{0,12}\]|\.\.\.|…", " ", s)
    s = re.sub(r"[^a-z0-9%$'\- ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def page_text(url):
    code, body = get(url)
    if body[:4] == b"%PDF":
        return subprocess.run(
            ["pdftotext", "-q", "-", "-"], input=body, capture_output=True
        ).stdout.decode("utf-8", "ignore").replace("-\n", "")  # rejoin words split across lines
    t = body.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    return re.sub(r"<[^>]+>", " ", t)


def record_texts(url):
    out = []
    u = urllib.parse.unquote(url)
    m = re.search(r"(10\.\d{4,9}/[^\s?#]+)", u)
    if m:
        doi = m.group(1).rstrip("/.")
        for f in (api.work, api.crossref):
            r = f(doi)
            out.append(f"{r.get('title') or ''} {r.get('abstract') or ''}")
        out += [
            f"{x.get('title')} {x.get('abstract')}"
            for x in api.epmc(f'DOI:"{doi}"', 2).get("results", [])
        ]
        if not any(len(t) > 300 for t in out):  # no abstract yet: try Semantic Scholar
            r = api.s2_paper(f"DOI:{doi}")
            out.append(f"{r.get('title') or ''} {r.get('abstract') or ''}")
    s2 = re.search(r"semanticscholar\.org/(?:graph/v1/)?paper/(?:[^/?#]+/)?([0-9a-f]{40})", u)
    if s2:
        r = api.s2_paper(s2.group(1))
        out.append(f"{r.get('title') or ''} {r.get('abstract') or ''}")
    ax = re.search(r"arxiv\.org/abs/([\w.]+)", u)
    if ax:  # the abstract page holds only the abstract; quotes are often from the full text
        out.append(page_text(f"https://arxiv.org/pdf/{ax.group(1)}"))
    oa = re.search(r"openalex\.org/(?:works/)?(W\d+)", u)
    if oa:
        code, w = api.get_json(f"{api.OA}/works/{oa.group(1)}?{api.oa_params()}")
        if w:
            out.append(f"{w.get('title') or ''} {api.oa_abstract(w)}")
    pm = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", u)
    if pm:
        out.append(api.pubmed(pm.group(1))["text"])
    pmc = re.search(r"(?:pmc\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pmc)/articles/(PMC\d+)", u)
    if pmc:  # NCBI serves a bot check; Europe PMC has the same open-access full text
        out.append(
            page_text(
                f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc.group(1)}/fullTextXML"
            )
        )
    ep = re.search(r"europepmc\.org/(?:article|abstract)/(MED|PMC|PPR)/(\w+)", u)
    if ep:
        q = (
            f"PMCID:{ep.group(2)}"
            if ep.group(1) == "PMC"
            else f"EXT_ID:{ep.group(2)} AND SRC:{ep.group(1)}"
        )
        out += [
            f"{x.get('title')} {x.get('abstract')}"
            for x in api.epmc(q, 2).get("results", [])
        ]
    return [t for t in out if t and len(t) > 40]


def check(q, texts):
    nq = norm(q)
    w = nq.split()
    grams = {" ".join(w[i : i + 5]) for i in range(max(1, len(w) - 4))}
    best = 0
    for t in texts:
        nt = norm(t)
        if nq and nq in nt:
            return "confirmed"
        if grams:
            best = max(best, sum(g in nt for g in grams) / len(grams))
    return "close" if best >= 0.85 else "unconfirmed"


def main(n, resume):
    d = article_dir(n)
    vp = os.path.join(d, "verify.json")
    res = json.load(open(vp)) if resume and os.path.exists(vp) else {}
    todo = {}
    for u, q, src in items(d):
        k = hashlib.sha1((u + "\n" + q).encode()).hexdigest()
        if k in res and res[k]["status"] in ("confirmed", "close"):
            continue
        todo.setdefault(k, (u, q, src))
    urls = sorted({u for u, _, _ in todo.values()})
    with cf.ThreadPoolExecutor(4) as ex:
        pages = dict(zip(urls, ex.map(page_text, urls)))
    ok = bad = 0
    archived = {}
    for k, (u, q, src) in todo.items():
        st = check(q, [pages[u]])
        if st == "unconfirmed" or len(pages[u]) < 200:
            texts = [pages[u]] + record_texts(u)
            st = check(q, texts) if any(len(t) > 200 for t in texts) else "fetch-failed"
        if st in ("unconfirmed", "fetch-failed"):
            # blocked or bot-checked page: try the Internet Archive's latest copy
            if u not in archived:
                archived[u] = page_text(f"https://web.archive.org/web/2id_/{u}")
            if len(archived[u]) > 200:
                st = check(q, texts + [archived[u]] if st == "unconfirmed" else [archived[u]])
        res[k] = {"url": u, "quote": q, "file": src, "status": st}
        ok += st in ("confirmed", "close")
        bad += st not in ("confirmed", "close")
        json.dump(res, open(vp, "w"), indent=1, ensure_ascii=False)
    total = len(res)
    good = sum(v["status"] in ("confirmed", "close") for v in res.values())
    print(
        f"processed {ok + bad}, succeeded {ok}, failed {bad}, skipped {total - ok - bad}; {good} of {total} unique quotes confirmed"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], "--resume" in sys.argv)
