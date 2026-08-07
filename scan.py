#!/usr/bin/env python3
"""Scan text for AI-favored vocabulary. Reports candidates; never rewrites.

    python3 scan.py FILE...          # or: cat draft.md | python3 scan.py
    python3 scan.py --lines FILE     # one row per hit, with line numbers
    python3 scan.py --lang zh FILE   # restrict to one language's rows
    python3 scan.py --strip FILE     # drop HTML/markdown markup before scanning

The lexicon lives in references/lexicon.tsv. A hit is a candidate, not a verdict:
some entries are legitimate in context and say so in their note column.
"""
import sys, re, os, argparse
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LEXICON = os.path.join(HERE, "references", "lexicon.tsv")

# Counted indicators, reported before and after an edit pass so the result is falsifiable.
# An indicator earns its place only if its hits are almost always real. The rule-of-three tell is
# real but was cut from this list: on the first document scanned, all 5 hits were ordinary
# enumerations ("需求文档、Gherkin、wiki 设计文档、OpenAPI"). A number you cannot trust is worse
# than no number, so triads stay a judgment call in the audit rather than a counter here.
INDICATORS = [
    ("staged reversal", r"(不是[^，。]{2,20}，(而)?是|不(只|仅)(是)?[^，。]{2,20}，(更|还)(是)?"
                        r"|not just [^,.]{2,40}, but|(isn'?t|is not) (just )?[^,.]{2,40}, (it'?s|but))"),
    ("em dash", r"——|(?<= )—(?= )"),
]


def load_lexicon(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.startswith(">") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if parts[0] == "lang":
                continue
            if len(parts) < 4:
                sys.stderr.write(f"lexicon.tsv:{n}: need 4+ columns, got {len(parts)}\n")
                continue
            lang, pattern, category, repl = parts[:4]
            note = parts[4] if len(parts) > 4 else ""
            # ASCII patterns get word boundaries; CJK has no word boundary to anchor to.
            body = rf"\b(?:{pattern})\b" if pattern.isascii() else f"(?:{pattern})"
            try:
                rx = re.compile(body, re.IGNORECASE if pattern.isascii() else 0)
            except re.error as e:
                sys.stderr.write(f"lexicon.tsv:{n}: bad regex {pattern!r}: {e}\n")
                continue
            rows.append(dict(lang=lang, rx=rx, src=pattern, cat=category, repl=repl, note=note))
    return rows


def strip_markup(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    return text


def scan(text, lexicon, langs):
    hits = defaultdict(list)  # key -> [(lineno, matched, line)]
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        for e in lexicon:
            if langs and e["lang"] not in langs:
                continue
            for m in e["rx"].finditer(line):
                hits[(e["lang"], e["src"], e["cat"], e["repl"], e["note"])].append(
                    (i, m.group(0), line.strip()))
    return hits


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--lines", action="store_true", help="one row per hit, with line numbers")
    ap.add_argument("--lang", action="append", choices=["en", "zh"], help="restrict to a language")
    ap.add_argument("--strip", action="store_true", help="remove HTML/markdown markup first")
    ap.add_argument("--lexicon", default=LEXICON)
    args = ap.parse_args()

    lexicon = load_lexicon(args.lexicon)
    text = "".join(open(f, encoding="utf-8").read() for f in args.files) if args.files \
        else sys.stdin.read()
    if args.strip:
        text = strip_markup(text)

    hits = scan(text, lexicon, set(args.lang or []))
    total = sum(len(v) for v in hits.values())
    chars = len(re.sub(r"\s", "", text))

    if args.lines:
        print("line\tterm\tcategory\treplacement\tnote\tcontext")
        rows = sorted(((occ[0], k, occ) for k, v in hits.items() for occ in v))
        for lineno, (lang, src, cat, repl, note), (_, matched, ctx) in rows:
            print(f"{lineno}\t{matched}\t{cat}\t{repl}\t{note}\t{ctx[:80]}")
    else:
        print("count\tterm\tcategory\treplacement\tnote")
        for k, v in sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0][1])):
            lang, src, cat, repl, note = k
            shown = sorted({m for _, m, _ in v})
            print(f"{len(v)}\t{'/'.join(shown)}\t{cat}\t{repl}\t{note}")

    print(f"\n# lexicon hits: {total}  ({total / max(chars, 1) * 1000:.1f} per 1000 chars, "
          f"{chars} chars scanned)", file=sys.stderr)
    for name, pat in INDICATORS:
        n = len(re.findall(pat, text))
        print(f"# {name}: {n}", file=sys.stderr)


if __name__ == "__main__":
    main()
