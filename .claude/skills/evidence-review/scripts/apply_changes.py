"""Fetch, test-run and write an approved change set to the live article (WP-CLI over the WP Engine SSH gateway).

  python3 apply_changes.py 10 --fetch     read-only: save the live post content to work/10/before.html
  python3 apply_changes.py 10 --dry       upload work/10/changes.json and report what would change; writes nothing
  python3 apply_changes.py 10 --write     write it (only after the user approved the change set), then confirm

The server script (apply/apply.php) changes a block only if its current value still matches the change set's "old"
value, backs up the post content first, and copies the hero ACF fields to the new revision. --write re-fetches the post
afterwards and confirms every change landed. Each step is recorded with state.py.
"""

import json
import os
import re
import subprocess
import sys

from common import SKILL, article_dir, env

E = env()
REMOTE = "/sites/attck/_wpeprivate/evidence-review"


def ssh(cmd, stdin=None):
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
            cmd,
        ],
        input=stdin,
        capture_output=True,
    )
    if p.returncode:
        sys.exit(
            f"remote command failed: {p.stderr.decode()[:400] or p.stdout.decode()[:400]}"
        )
    return p.stdout.decode()


def blocks_changed(before, after, changes):
    A = after.split("\n")
    ok = 0
    for c in changes:
        m = re.match(r"<!-- wp:flexlayout/[\w-]+ (\{.*\}) /-->$", A[c["line"]])
        ok += bool(m) and json.loads(m.group(1)).get(c["field"]) == c["new"]
    diff = sum(1 for b, a in zip(before.split("\n"), A) if b != a)
    return ok, diff


def main(n, mode):
    d = article_dir(n)
    meta = json.load(open(os.path.join(d, "meta.json")))
    post = meta["id"]
    if mode == "--fetch":
        open(os.path.join(d, "before.html"), "w").write(
            ssh(f"wp post get {post} --field=post_content --path=/sites/attck")
        )
        print("saved before.html")
        return
    changes = json.load(open(os.path.join(d, "changes.json")))
    rdir = f"{REMOTE}/{int(n):02d}"
    ssh(f"mkdir -p {rdir}")
    ssh(
        f"cat > {rdir}/changes.json", open(os.path.join(d, "changes.json"), "rb").read()
    )
    ssh(
        f"cat > {rdir}/apply.php",
        open(os.path.join(SKILL, "apply", "apply.php"), "rb").read(),
    )
    run = f"cd {rdir} && DIR={rdir} POST={post} {{}} wp eval-file apply.php --path=/sites/attck"
    print(ssh(run.format("DRY=1")).strip())
    if mode != "--write":
        return
    print(ssh(run.format("")).strip())
    after = ssh(f"wp post get {post} --field=post_content --path=/sites/attck")
    open(os.path.join(d, "after-live.html"), "w").write(after)
    ok, diff = blocks_changed(
        open(os.path.join(d, "before.html")).read(), after, changes
    )
    lines = len({c["line"] for c in changes})
    print(
        f"confirmed {ok} of {len(changes)} changes landed; {diff} lines changed (expected {lines})"
    )
    json.dump(
        changes,
        open(os.path.join(d, "applied.json"), "w"),
        indent=1,
        ensure_ascii=False,
    )
    if ok != len(changes) or diff != lines:
        sys.exit(
            "MISMATCH: compare work/NN/after-live.html with the change set before going further"
        )


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in ("--fetch", "--dry", "--write"):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
