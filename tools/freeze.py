#!/usr/bin/env python3
"""Refuse to apply a rewrite to an input that has moved since it was audited.

    python3 tools/freeze.py stamp FILE            # print the hash to record
    python3 tools/freeze.py check FILE <sha256>   # exit 1 if the file has changed
    python3 tools/freeze.py check FILE <sha256> --also LIVE_FILE

Why this is a hard gate and not a note. A rewrite applied to a moved input fails silently: no error,
no conflict, the audit table still reads clean, and the output quietly restores whatever the author
retracted in between. It happened on this repository's own worked example, where the source moved
between the snapshot and the report, and two claims the author had withdrawn would have come back.

The risk is highest exactly when the pass went well, which is the same reason SKILL.md §10 makes the
scope line mandatory rather than optional.
"""
import hashlib, sys


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    if len(argv) < 3 or argv[1] not in ("stamp", "check"):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    path = argv[2]
    if argv[1] == "stamp":
        print(sha(path))
        return 0
    if len(argv) < 4:
        print("check needs an expected sha256", file=sys.stderr)
        return 2
    expected, actual = argv[3], sha(path)
    if actual != expected:
        print(f"REFUSED: {path} has changed since it was audited.\n"
              f"  expected {expected}\n  actual   {actual}\n"
              f"Re-audit against the current file. Edit pairs that land in a changed region no longer\n"
              f"apply, and the ones that still match will restore whatever was changed around them.",
              file=sys.stderr)
        return 1
    if "--also" in argv:
        live = argv[argv.index("--also") + 1]
        live_sha = sha(live)
        if live_sha != expected:
            print(f"WARNING: the snapshot is intact but the live source has moved.\n"
                  f"  snapshot {expected}\n  live     {live_sha}  ({live})\n"
                  f"The rewrite still applies to the snapshot. It does not apply to the live file.",
                  file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
