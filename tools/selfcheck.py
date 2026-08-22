#!/usr/bin/env python3
"""Run deslop's gates on deslop's own prose.

    python3 tools/selfcheck.py            # check against the ledger; exit 1 on any drift
    python3 tools/selfcheck.py --write    # regenerate the ledger, keeping reasons already written
    python3 tools/selfcheck.py --list     # print every hit with its line number

SKILL.md 5.1 says a GATED indicator must be driven to zero or every survivor named. This applies
the same rule to this repository. A survivor with no reason fails the check, and a reason left in
the ledger after its hit is gone fails too, so the file cannot drift into a blanket exemption.

The tool that removes AI register from other people's text has to hold for its own, and the check
is cheap. It has already earned its keep twice: the first run demoted two GATED indicators whose
hits here were almost all false (references/field-reports.md).
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import measure  # noqa: E402

LEDGER = ROOT / "references" / "selfcheck.tsv"

# The files that speak in deslop's own voice. worked-example/ is deliberately absent: those files
# are a run on someone else's draft, and its input is frozen by hash, so deslop's gates have no
# standing over them.
FILES = ["SKILL.md", "README.md", "README.en.md", "evals/README.md"] + [
    f"references/{n}.md" for n in (
        "taxonomy", "decisions", "overcorrection", "provenance", "titles",
        "nofluff", "worked-example", "markers-zh", "markers-en", "field-reports",
        "code-comments")]

SNIP = 60


def snippet(text):
    s = " ".join(text.split())
    return (s[:SNIP] + "…") if len(s) > SNIP else s


def collect():
    """{(file, indicator, snippet): [line numbers]} for every GATED hit in the repo's own prose.

    A CAPPED indicator over its cap is added as one row per (file, indicator), with no line and no
    count. The amount of the excess moves whenever the file grows, and a check that fails on that
    would be noise; what needs a reason is the fact that this file exceeds this cap at all.
    """
    found = {}
    for name in FILES:
        path = ROOT / name
        if not path.exists():
            continue
        text = path.read_text()
        for hit in measure.gated_hits(text):
            key = (name, hit["indicator"], snippet(hit["text"]))
            found.setdefault(key, []).append(hit["line"])
        r = measure.measure(text)
        for indicator, (value, cap) in r["capped"].items():
            if value > cap:
                found.setdefault((name, "over cap: " + indicator, ""), []).append(0)
    return found


def read_ledger():
    rows = {}
    if not LEDGER.exists():
        return rows
    for line in LEDGER.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        f, ind, count, snip, reason = line.split("\t")
        rows[(f, ind, snip)] = (int(count), reason)
    return rows


def write_ledger(found, old):
    out = ["# Named survivors of tools/selfcheck.py. One row per (file, indicator, line).",
           "# Regenerate with `python3 tools/selfcheck.py --write`; reasons are kept.",
           "# columns: file\tindicator\tcount\tsnippet\treason"]
    for key in sorted(found):
        reason = old.get(key, (0, "TODO"))[1]
        out.append("\t".join([key[0], key[1], str(len(found[key])), key[2], reason]))
    LEDGER.write_text("\n".join(out) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    found = collect()
    if args.list:
        for key in sorted(found):
            print(f"{key[0]}:{','.join(str(n) for n in found[key])}  {key[1]:<28} {key[2]}")
        return 0
    if args.write:
        write_ledger(found, read_ledger())
        print(f"wrote {LEDGER.relative_to(ROOT)}: {len(found)} rows, "
              f"{sum(len(v) for v in found.values())} hits")
        return 0

    ledger, bad = read_ledger(), []
    for key, lines in sorted(found.items()):
        if key not in ledger:
            bad.append(f"unnamed  {key[0]}:{lines[0]}  {key[1]}  {key[2]}")
        elif ledger[key][1].strip() in ("", "TODO"):
            bad.append(f"no reason {key[0]}:{lines[0]}  {key[1]}  {key[2]}")
        elif not key[2]:
            pass                                   # over-cap rows carry no count on purpose
        elif ledger[key][0] != len(lines):
            bad.append(f"count {ledger[key][0]}→{len(lines)}  {key[0]}  {key[1]}  {key[2]}")
    for key in sorted(ledger):
        if key not in found:
            bad.append(f"stale    {key[0]}  {key[1]}  {key[2]}")

    total = sum(len(v) for v in found.values())
    if bad:
        print(f"selfcheck FAIL — {len(bad)} problem(s)")
        for b in bad:
            print("  " + b)
        print("\nFix the prose, or name the survivor in " + str(LEDGER.relative_to(ROOT)))
        return 1
    over = sum(1 for k in found if not k[2])
    print(f"selfcheck ok — {total - over} GATED hits and {over} over-cap indicators across "
          f"{len(FILES)} files, all named ({len(found)} ledger rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
