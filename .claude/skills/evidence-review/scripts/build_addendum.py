"""Write the public addendum for an article after its approved edits are applied.

  python3 build_addendum.py 2        writes docs/<slug>.md and updates docs/index.md

Inputs in work/NN/: meta.json, claims.json, pass4.json, pass5.json (overrides), verify.json, applied.json
(the change set that was written: [{"claim", "summary"}] or the raw changes.json with "why" fields).
Only Supported / Supported-with-caveats claims with an addendum note become background research, and only sources
whose quotes the script confirmed are listed. Contested and Not supported claims appear only under "What changed".
"""

import datetime
import json
import os
import re
import sys

from common import DOCS, article_dir

KEEP = ("Supported", "Supported with caveats")


def J(d, f, default=None):
    p = os.path.join(d, f)
    return json.load(open(p)) if os.path.exists(p) else default


def section_title(s):
    return "Introduction" if s.strip().lower() in ("intro", "introduction") else s


def no_refs(s):
    """Old citation numbers ("source [1]") go stale once the article is renumbered."""
    return re.sub(r"\s*\[\d+\]", "", s)


def source_label(s):
    """Drop reviewer notes that go stale once the article is renumbered or that only matter internally."""
    s = re.sub(r"\s*\((?:the article's|article) source \[\d+\]\)", "", s)
    s = re.sub(r",?\s*\(?(?:abstract|record) via [A-Za-z ]+\)?", "", s)
    s = re.sub(r",?\s*(?:the )?(?:cited|article's) source", "", s)
    return no_refs(s).strip(" ,")


def main(n):
    d = article_dir(n)
    meta, claims = J(d, "meta.json"), J(d, "claims.json")
    final = {x["id"]: x for x in J(d, "pass4.json")}
    for x in J(d, "pass5.json", []):
        final[x["id"]] = x
    ok = {
        (v["url"].strip(), v["quote"].strip())
        for v in J(d, "verify.json", {}).values()
        if v["status"] in ("confirmed", "close")
    }
    applied = J(d, "applied.json", [])
    changed = sorted(
        {
            m
            for a in applied
            for m in re.findall(
                r"\bC\d+\b", a.get("why", "") + " " + a.get("claim", "")
            )
        },
        key=lambda c: int(c[1:]),
    )

    out = [
        "---",
        f'title: "Evidence review: {meta["title"]}"',
        "---",
        "",
        f"# Evidence review: {meta['title']}",
        "",
        f"Article: [{meta['title']}]({meta['url']})  ",
        f"Reviewed: {datetime.date.today():%B %Y} · Method version 2 · "
        "[How these reviews work](https://github.com/ATTCKDigital/attck-research/blob/main/.claude/skills/evidence-review/METHOD.md)",
        "",
        "## How this review works",
        "",
        "Each factual claim in the article was checked against the source it cites, then challenged by reviewers whose "
        "job was to find the strongest evidence against it: replication attempts, meta-analyses, later papers that cite "
        "the original work, and research from other fields that study the same mechanism. A separate reviewer weighed "
        "both sides, and a script re-checked every quoted source. Where a claim was overstated or misattributed, the "
        "article was corrected. The research below supports the article as it now reads.",
        "",
        "## Background research",
        "",
    ]
    by_section = {}
    for c in claims:
        j = final[c["id"]]
        if j["verdict"] in KEEP and j.get("addendum_note"):
            by_section.setdefault(c["section"], []).append((c, j))
    for sec, js in by_section.items():
        items = []
        seen = set()
        for c, j in js:
            note = no_refs(j["addendum_note"]).strip()
            if re.fullmatch(r"(Confirmed|Checked|Verified)[^.]{0,60}\.", note):
                note = ""  # reviewer shorthand such as "Confirmed against the abstract." says nothing to a reader
            srcs = []
            for e in j.get("key_for") or []:
                k = ((e.get("url") or "").strip(), (e.get("quote") or "").strip())
                if k in ok and e["url"] not in seen:
                    seen.add(e["url"])
                    srcs.append(f"- [{source_label(e['source'])}]({e['url']}): “{e['quote']}”")
            if note or srcs:  # a claim with neither adds nothing to the page
                # a claim the article rewrote is shown as it now reads, so the page never repeats corrected wording
                lead = j["suggested_edit"] if c["id"] in changed and j.get("suggested_edit") else c["claim"]
                items += [f"**{no_refs(re.sub(r'<[^>]+>', '', lead))}**", ""] + ([note, ""] if note else []) + srcs + ([""] if srcs else [])
        if items:
            out += [f"### {section_title(sec)}", ""] + items
    if changed:
        out += [
            "## What changed in the article",
            "",
            f"These edits were made on {datetime.date.today():%B %-d, %Y} after the review.",
            "",
        ]
        cl = {c["id"]: c for c in claims}
        for cid in changed:
            j = final.get(cid)
            if not j or cid not in cl:
                continue
            if not j.get("suggested_edit"):
                continue
            src = j.get("suggested_citation")
            out += [
                f"### {section_title(cl[cid]['section'])}: {j['verdict'].lower()}",
                "",
                f"**Claim reviewed:** {no_refs(cl[cid]['claim'])}",
                "",
                f"**Now reads:** {no_refs(j['suggested_edit'])}",
                "",
                f"**Why:** {no_refs(j['why'])}"
                + (
                    f" Now cites [{source_label(src['source'])}]({src['url']})."
                    if src
                    else ""
                ),
                "",
            ]
    os.makedirs(DOCS, exist_ok=True)
    path = os.path.join(DOCS, f"{meta['slug']}.md")
    open(path, "w").write("\n".join(out))

    idx = os.path.join(DOCS, "index.md")
    lines = (
        open(idx).read().rstrip("\n").split("\n")
        if os.path.exists(idx)
        else ["# Evidence reviews", ""]
    )
    lines = [l for l in lines if not l.startswith("Reviews are added here")]
    entry = f"- [{meta['n']:02d}. {meta['title']}]({meta['slug']}.md)"
    lines = [l for l in lines if f"]({meta['slug']}.md)" not in l] + [entry]
    head = [l for l in lines if not l.startswith("- [")]
    items = sorted(l for l in lines if l.startswith("- ["))
    open(idx, "w").write(
        "\n".join(head).rstrip("\n") + "\n\n" + "\n".join(items) + "\n"
    )
    print(
        path,
        f"{sum(len(v) for v in by_section.values())} background notes, {len(changed)} changes listed",
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
