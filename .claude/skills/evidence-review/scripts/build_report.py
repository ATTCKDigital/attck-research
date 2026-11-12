"""Build the private evidence-review report for one article.

  python3 build_report.py 10        writes work/reports/report-10.html (publish it as a private Artifact)

Final verdict per claim: pass5.json when present, else pass4.json. Each evidence item is marked with its quote check
from verify.json. Review time comes from work/state.json.
"""

import datetime
import json
import os
import sys

from common import SKILL, WORK, article_dir

METHOD_VERSION = "2"


def J(d, f, default=None):
    p = os.path.join(d, f)
    return json.load(open(p)) if os.path.exists(p) else default


def main(n):
    d = article_dir(n)
    meta, cl = J(d, "meta.json"), J(d, "claims.json")
    p2 = {x["id"]: x for x in J(d, "pass2.json", [])}
    p3 = {x["id"]: x for x in J(d, "pass3.json", [])}
    final = {x["id"]: x for x in J(d, "pass4.json")}
    for x in J(d, "pass5.json", []):
        final[x["id"]] = x
    sm = J(d, "summary.json")
    ver = {
        (v["url"].strip(), v["quote"].strip()): v["status"]
        for v in J(d, "verify.json", {}).values()
    }
    counts = {}
    for c in cl:
        j = final[c["id"]]
        counts[j["verdict"]] = counts.get(j["verdict"], 0) + 1
        for k in ("key_for", "key_against"):
            for e in j.get(k) or []:
                e["v"] = ver.get(
                    ((e.get("url") or "").strip(), (e.get("quote") or "").strip())
                )
        x = p3.get(c["id"], {})
        c.update(
            p2=p2.get(c["id"]),
            judge=j,
            log=x.get("search_log") or [],
            p3={
                "challenge_strength": x.get("challenge_strength", ""),
                "notes": j.get("changed_from_pass4") or "",
            },
        )
    sm["counts"] = counts
    st = (J(WORK, "state.json", {}) or {}).get(f"{int(n):02d}", {})
    ts = [
        datetime.datetime.fromisoformat(v[k])
        for v in st.values()
        for k in ("started", "ended")
        if v.get(k)
    ]
    timing = (
        f" Review time: {round((max(ts) - min(ts)).total_seconds() / 60)} minutes."
        if len(ts) > 1
        else ""
    )
    good = sum(v in ("confirmed", "close") for v in ver.values())
    R = {
        "n": meta["n"],
        "post": meta["id"],
        "title": meta["title"],
        "url": meta["url"],
        "date": datetime.date.today().strftime("%b %-d, %Y"),
        "models": "Passes 1-4: Opus · Doubtful claims re-checked: Fable · Quotes: script",
        "claims": cl,
        "summary": sm,
        "footer": f"Evidence review method v{METHOD_VERSION}, article {meta['n']}. Quotes checked by script: {good} of {len(ver)} confirmed; unconfirmed quotes are never used to decide a verdict.{timing}",
    }
    tpl = open(os.path.join(SKILL, "report.tpl.html")).read()
    s = tpl.replace(
        "/*DATA*/ {}", json.dumps(R, ensure_ascii=False).replace("</", "<\\/")
    ).replace("__N__", str(meta["n"]))
    s = s.replace(
        "<b>Challenge strength:</b> ${esc(p3.challenge_strength)}. ",
        "<b>Challenge:</b> ${esc(p3.challenge_strength)}. ",
    )
    out = os.path.join(WORK, "reports", f"report-{int(n):02d}.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(s)
    print(out, counts)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
