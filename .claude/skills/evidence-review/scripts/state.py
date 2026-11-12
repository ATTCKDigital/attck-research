"""Checkpoint, log and resume state for evidence-review batches.

  python3 state.py start 10 judge            mark a stage started
  python3 state.py done 10 judge             mark it finished
  python3 state.py fail 10 judge "message"   mark it failed
  python3 state.py next 10-17 [--resume]     print the next pending stage for each article (resume after interruption)
  python3 state.py summary 10-17             processed / succeeded / failed / skipped counts and per-article minutes

State lives in work/state.json (written after every event). Every event is appended to
logs/evidence-review-<YYYYMMDD>.jsonl as {"timestamp","item_id","stage","status","error"}.
"""

import datetime
import json
import os
import sys

from common import LOGS, WORK

STAGES = [
    "fetch",
    "claims",
    "citations",
    "challenge",
    "judge",
    "recheck",
    "verify",
    "report",
]
SP = os.path.join(WORK, "state.json")


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def load():
    return json.load(open(SP)) if os.path.exists(SP) else {}


def save(s):
    os.makedirs(WORK, exist_ok=True)
    tmp = SP + ".tmp"
    json.dump(s, open(tmp, "w"), indent=1)
    os.replace(tmp, SP)


def log(item, stage, status, error=None):
    os.makedirs(LOGS, exist_ok=True)
    f = os.path.join(LOGS, f"evidence-review-{datetime.date.today():%Y%m%d}.jsonl")
    with open(f, "a") as fh:
        fh.write(
            json.dumps(
                {
                    "timestamp": now(),
                    "item_id": item,
                    "stage": stage,
                    "status": status,
                    "error": error,
                }
            )
            + "\n"
        )


def mark(n, stage, status, error=None):
    if stage not in STAGES:
        sys.exit(f"unknown stage {stage}; stages: {', '.join(STAGES)}")
    key = f"{int(n):02d}"
    s = load()
    a = s.setdefault(key, {})
    rec = a.setdefault(stage, {})
    rec["status"] = status
    rec["started" if status == "started" else "ended"] = now()
    if error:
        rec["error"] = error
    save(s)
    log(key, stage, status, error)


def arts(spec):
    lo, _, hi = spec.partition("-")
    return [f"{i:02d}" for i in range(int(lo), int(hi or lo) + 1)]


def pending(spec):
    s = load()
    out = {}
    for k in arts(spec):
        a = s.get(k, {})
        nxt = next(
            (st for st in STAGES if (a.get(st) or {}).get("status") != "done"), None
        )
        out[k] = {
            "next": nxt,
            "state": (a.get(nxt) or {}).get("status") if nxt else "complete",
        }
    return out


def minutes(a):
    t = [
        datetime.datetime.fromisoformat(v[x])
        for v in a.values()
        for x in ("started", "ended")
        if v.get(x)
    ]
    return round((max(t) - min(t)).total_seconds() / 60) if len(t) > 1 else None


def summary(spec):
    s = load()
    done = failed = skipped = processed = 0
    rows = []
    for k in arts(spec):
        a = s.get(k, {})
        if not a:
            skipped += 1
            continue
        processed += 1
        if any((v or {}).get("status") == "failed" for v in a.values()):
            failed += 1
        elif all((a.get(st) or {}).get("status") == "done" for st in STAGES):
            done += 1
        rows.append(
            f"{k}: {minutes(a)} min, last stage {max(a, key=lambda st: STAGES.index(st))}"
        )
    print("\n".join(rows))
    print(
        f"processed {processed}, succeeded {done}, failed {failed}, skipped {skipped}"
    )


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] in ("start", "done", "fail"):
        mark(
            a[1],
            a[2],
            {"start": "started", "done": "done", "fail": "failed"}[a[0]],
            a[3] if len(a) > 3 else None,
        )
    elif a[0] == "next":
        print(json.dumps(pending(a[1]), indent=1))
    elif a[0] == "summary":
        summary(a[1])
    else:
        sys.exit(__doc__)
