"""Shared paths, settings and HTTP helpers for the evidence-review scripts."""

import hashlib
import json
import os
import subprocess
import time
import urllib.parse

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.abspath(os.path.join(SKILL, "..", "..", ".."))
WORK = os.path.join(REPO, "work")
CACHE = os.path.join(REPO, ".cache")
LOGS = os.path.join(REPO, "logs")
DOCS = os.path.join(REPO, "docs")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"

# Minimum seconds between calls to each host, shared by every process through files in .cache/throttle
MIN_INTERVAL = {
    "api.openalex.org": 0.2,
    "api.semanticscholar.org": 1.1,
    "api.crossref.org": 0.3,
    "api.opencitations.net": 2.0,
    "www.ebi.ac.uk": 0.3,
    "eutils.ncbi.nlm.nih.gov": 0.4,
}
# Without a key, Semantic Scholar answers from a pool shared by every keyless caller, so call it less often
KEYLESS_INTERVAL = {"api.semanticscholar.org": 3.0}


def env():
    """Settings from the repo's .env file, overridden by real environment variables."""
    out = {}
    p = os.path.join(REPO, ".env")
    if os.path.exists(p):
        for line in open(p):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip()
    out.update(
        {
            k: v
            for k, v in os.environ.items()
            if k in out or k.startswith(("OPENALEX", "SEMANTIC", "WPE_", "SERIES_"))
        }
    )
    return out


def article_dir(n):
    d = os.path.join(WORK, f"{int(n):02d}")
    os.makedirs(d, exist_ok=True)
    return d


def budget_spent(host):
    """True while a service has said its daily free budget is used up (OpenAlex without a key: $0.10 a day per IP,
    reset at midnight UTC). Single-record lookups stay free, so only list and search calls should check this."""
    f = os.path.join(CACHE, "budget", host)
    try:
        return float(open(f).read()) > time.time()
    except (OSError, ValueError):
        return False


def _mark_budget_spent(host):
    d = os.path.join(CACHE, "budget")
    os.makedirs(d, exist_ok=True)
    reset = (time.time() // 86400 + 1) * 86400  # next midnight UTC
    open(os.path.join(d, host), "w").write(str(reset))


def _throttle(host, keyed):
    gap = (
        MIN_INTERVAL.get(host)
        if keyed
        else KEYLESS_INTERVAL.get(host, MIN_INTERVAL.get(host))
    )
    if not gap:
        return
    d = os.path.join(CACHE, "throttle")
    os.makedirs(d, exist_ok=True)
    f = os.path.join(d, host)
    try:
        last = os.path.getmtime(f)
    except OSError:
        last = 0
    wait = last + gap - time.time()
    if wait > 0:
        time.sleep(wait)
    open(f, "w").close()


def get(url, headers=None, cache=True, retries=4, timeout=40):
    """GET with per-host throttling, backoff on 429/5xx and an on-disk cache of successful bodies."""
    key = hashlib.sha1(
        (url + json.dumps(headers or {}, sort_keys=True)).encode()
    ).hexdigest()
    cp = os.path.join(CACHE, "http", key[:2], key)
    if cache and os.path.exists(cp):
        return 200, open(cp, "rb").read()
    host = urllib.parse.urlparse(url).netloc
    args = ["curl", "-sL", "--compressed", "-m", str(timeout), "-A", UA, "-w", "\n%{http_code}"]
    for k, v in (headers or {}).items():
        args += ["-H", f"{k}: {v}"]
    keyed = bool(headers and "x-api-key" in headers) or "api_key=" in url
    code, body = 0, b""
    for attempt in range(retries):
        _throttle(host, keyed)
        p = subprocess.run(args + [url], capture_output=True)
        body, _, tail = p.stdout.rpartition(b"\n")
        code = int(tail) if tail.strip().isdigit() else 0
        if code == 429 and b"Insufficient budget" in body:
            _mark_budget_spent(host)  # retrying won't help before the reset
            break
        if code == 429 or code >= 500 or code == 0:
            time.sleep(min(60, 3 * 2**attempt))
            continue
        break
    if cache and code == 200 and len(body) > 100:
        os.makedirs(os.path.dirname(cp), exist_ok=True)
        open(cp, "wb").write(body)
    return code, body


def get_json(url, headers=None, **kw):
    """(code, parsed JSON) for a 200 response; (code, None) for refusals, errors and non-JSON bodies."""
    code, body = get(url, headers, **kw)
    if code != 200:
        return code, None
    try:
        return code, json.loads(body)
    except ValueError:
        return code, None
