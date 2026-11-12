"""Read-only: pull series articles from WordPress (WP-CLI over the WP Engine SSH gateway).

  python3 fetch_article.py 10          writes work/10/article.txt and work/10/meta.json
  python3 fetch_article.py 10-17
  python3 fetch_article.py list        prints the numbered series

Articles are numbered by publish date within the series category (scheduled posts included). Only `wp post list`
and `wp post get` are run; nothing is written to the site.
"""

import html
import json
import os
import re
import subprocess
import sys

from common import article_dir, env

E = env()


def wp(*args):
    key = os.path.expanduser(E.get("WPE_SSH_KEY", "~/.ssh/wpe_attck"))
    target = E.get("WPE_SSH_TARGET", "attck@attck.ssh.wpengine.net")
    p = subprocess.run(
        [
            "ssh",
            "-i",
            key,
            "-o",
            "IdentitiesOnly=yes",
            "-o",
            "ConnectTimeout=20",
            target,
            "wp",
            *args,
        ],
        capture_output=True,
        text=True,
    )
    if p.returncode:
        sys.exit(f"WP-CLI failed: {p.stderr.strip()[:300]}")
    return p.stdout


def series():
    cat = E.get("SERIES_CATEGORY_ID", "229")
    rows = json.loads(
        wp(
            "post",
            "list",
            f"--cat={cat}",
            "--post_type=post",
            "--post_status=publish,future",
            "--orderby=date",
            "--order=ASC",
            "--posts_per_page=-1",
            "--fields=ID,post_title,post_name,post_status,post_date",
            "--format=json",
        )
    )
    return [dict(r, n=i) for i, r in enumerate(rows, 1)]


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def to_text(content):
    """Article body as plain text with [n] citation markers, plus the numbered Sources list."""
    i = content.find('"content":"Frequently asked questions"')
    content = content[:i] if i > 0 else content
    out, sources, in_sources = [], [], False
    for m in re.finditer(r"<!-- wp:([\w/-]+) (\{.*?\}) /?-->", content):
        try:
            a = json.loads(m.group(2))
        except ValueError:
            continue
        if re.search(r"\bhide\b|caption2", a.get("className") or ""):
            continue
        name, v = m.group(1), a.get("content")
        if (
            name == "flexlayout/heading"
            and isinstance(v, str)
            and strip(v) == "Sources"
        ):
            in_sources = True
            continue
        if in_sources and name == "flexlayout/list":
            for li in re.findall(r"<li>(.*?)</li>", v, re.S):
                url = re.findall(r'href="([^"]+)"', li)
                sources.append(
                    {
                        "n": len(sources) + 1,
                        "text": strip(li),
                        "url": url[0] if url else None,
                    }
                )
            in_sources = False
            continue
        for field in ("content", "contentSource", "contentCompany"):
            v = a.get(field)
            if isinstance(v, str) and v.strip():
                t = v.replace("</li>", "\n").replace("</p><p>", "\n\n")
                t = (
                    html.unescape(re.sub(r"<(?!/?sup)[^>]+>", "", t))
                    .replace("<sup>", "")
                    .replace("</sup>", "")
                    .strip()
                )
                out.append("\n## " + t if name == "flexlayout/heading" else t)
    return "\n\n".join(out), sources


def fetch(row):
    content = wp("post", "get", str(row["ID"]), "--field=post_content")
    text, sources = to_text(content)
    d = article_dir(row["n"])
    open(os.path.join(d, "article.txt"), "w").write(text)
    meta = {
        "n": row["n"],
        "id": row["ID"],
        "title": row["post_title"],
        "slug": row["post_name"],
        "status": row["post_status"],
        "date": row["post_date"],
        "url": f"https://attck.com/blog/{row['post_name']}/",
        "sources": sources,
    }
    json.dump(
        meta, open(os.path.join(d, "meta.json"), "w"), indent=1, ensure_ascii=False
    )
    print(
        f"{row['n']:02d} {row['post_title']} ({len(text.split())} words, {len(sources)} sources)"
    )


def main(arg):
    rows = series()
    if arg == "list":
        for r in rows:
            print(
                f"{r['n']:02d} {r['post_status']:7s} {r['post_date'][:10]} {r['post_title']}"
            )
        return
    lo, _, hi = arg.partition("-")
    want = range(int(lo), int(hi or lo) + 1)
    for r in rows:
        if r["n"] in want:
            fetch(r)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
