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
#
# 、 and ： join —— as counted marks because all three do one job: let a sentence carry more than
# one thought without committing to a second sentence. The em dash joins clauses so it is visible;
# 、 joins list items and ： stages a reveal, so both hide behind being grammatical. Legality was
# never the test — every one of these is legal Chinese. Each mark is a place the document declined
# to build structure: 、 is a list not written as a list, a mid-prose ： is a second sentence or a
# heading. Counting them is how the structure gets found.
INDICATORS = [
    ("staged reversal", r"(不是[^，。]{2,20}，(而)?是|不(?:只|仅)+(?:是)?[^，。]{2,20}，(?:而|更|还)?是"
                        r"|not just [^,.]{2,40}, but|(isn'?t|is not) (just )?[^,.]{2,40}, (it'?s|but))"),
    ("em dash", r"——|(?<= )—(?= )"),
    ("顿号", lambda text: _count_dunhao(text)),
    ("句中冒号", lambda text: _count_staging_colon(text)),
]

# A mark inside 「」/『』 is quoted UI text or someone else's sentence — not the author's punctuation.
QUOTED_RE = re.compile(r"[「『][^」』]*[」』]")
# `- **附件**：说明` is a label, not a staged reveal; a line-final ： introduces the block below it.
LABEL_COLON_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*[^*]+\*\*|[^：\s]{1,12})：")


def _uncounted(line):
    """Drop quoted spans so reproducing a product string never inflates the author's own count."""
    return QUOTED_RE.sub("", line)


def _count_dunhao(text):
    return sum(_uncounted(line).count("、") for line in text.split("\n"))


def _count_staging_colon(text):
    """Count only the ： that stages: not a label colon, not one introducing the block below."""
    n = 0
    for line in text.split("\n"):
        body = _uncounted(line)
        if body.lstrip().startswith("|"):      # a table row's ： belongs to the cell, not the prose
            continue
        body = LABEL_COLON_RE.sub("", body, count=1)
        n += len(re.findall(r"：(?=\s*\S)", body))
    return n


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
    """Return one most-specific candidate for each overlapping span.

    A phrase rule such as ``In today's fast-paced landscape`` says more than
    three separate word rules inside it. Showing all four makes a worklist
    noisier without giving the editor another decision to make.
    """
    hits = defaultdict(list)  # key -> [(lineno, matched, line)]
    for i, line in enumerate(text.split("\n"), 1):
        candidates = []
        for order, e in enumerate(lexicon):
            if langs and e["lang"] not in langs:
                continue
            for m in e["rx"].finditer(line):
                candidates.append((m.start(), m.end(), order, e, m.group(0)))

        # Prefer a longer phrase. Exact ties keep the earlier lexicon row,
        # allowing a specific entry to override a general catch-all pattern.
        candidates.sort(key=lambda hit: (-(hit[1] - hit[0]), hit[2], hit[0]))
        selected = []
        for candidate in candidates:
            start, end, _, _, _ = candidate
            if any(start < kept[1] and kept[0] < end for kept in selected):
                continue
            selected.append(candidate)

        for _, _, _, e, matched in selected:
            hits[(e["lang"], e["src"], e["cat"], e["repl"], e["note"])].append(
                (i, matched, line.strip()))
    return hits



# ---------------------------------------------------------------- pipeline mode

PUNCT_CHECKS = [
    ("——", "em dash", "改成逗号、冒号或句号"),
    ("—", "em dash", "改成逗号、冒号或句号"),
    ("！", "感叹号", "技术文档里删掉；只有推文/社交场景且确有情绪才留"),
    ("!", "exclamation", "same as 感叹号"),
    ("……", "省略号", "说清楚省掉的是什么，或删"),
    ("；", "分号", "多数情况下断成两句更清楚"),
    ("、", "顿号", "只用于并列名词。连接两个分句要用逗号"),
    ("：", "冒号", "后面必须是它引出的东西；不要用来制造停顿"),
    ("“", "弯引号", "中文用直角引号「」"),
    ("”", "弯引号", "中文用直角引号「」"),
]

# One-syllable physical verb roots. The object decides: if it is not a thing in space, this is a
# metaphor and the literal action is what the sentence needs.
PHYS_ROOTS = "跑扫抓压砍拉打接扛烧啃撕掰拧堵卡踩撑顶捞碾劈磨捏揪抠扒挖撬盘捋铺摊掀戳穿兜咬踢滚翻"
PHYS_RE = re.compile(f"[{PHYS_ROOTS}](?:掉|住|下|上|开|通|穿|爆|满|齐|平|出|回|一遍|一下)?")

SENT_RE = re.compile(r"[^。！？；\n]*[。！？；]|[^。！？；\n]+")


def pipeline(text, lexicon, langs):
    """Emit a per-sentence worksheet: every token candidate and every punctuation mark, each with a
    verdict column for the editor to fill. The script decides nothing; it refuses to let a unit go
    unexamined."""
    n = 0
    for raw in text.split("\n"):
        line = raw.strip()
        if not line:
            continue
        for m in SENT_RE.finditer(line):
            sent = m.group(0).strip()
            if not sent:
                continue
            n += 1
            chars = len(re.sub(r"\s", "", sent))
            print(f"\nS{n}  ({chars} 字)  {sent}")

            verbs = sorted({v.group(0) for v in PHYS_RE.finditer(sent)})
            if verbs:
                print(f"  动作动词  {' · '.join(verbs)}")
                print("            → 逐个问：它作用的东西在物理空间里存在吗？不存在就换成字面动作。")

            marks = []
            for ch, name, fix in PUNCT_CHECKS:
                c = sent.count(ch)
                if c:
                    marks.append(f"{ch} ×{c}（{name}：{fix}）")
            tail = sent[-1] if sent else ""
            if tail not in "。！？；":
                marks.append("句末无标点（是断句还是漏了？）")
            if re.search(r"[\u4e00-\u9fff][A-Za-z0-9]|[A-Za-z0-9][\u4e00-\u9fff]", sent):
                marks.append("中英/中数之间缺空格")
            if re.search(r"[\u4e00-\u9fff][,.;:?]", sent):
                marks.append("中文句子里混入半角标点")
            if marks:
                print("  标点      " + "\n            ".join(marks))

            hits = []
            for e in lexicon:
                if langs and e["lang"] not in langs:
                    continue
                for hm in e["rx"].finditer(sent):
                    hits.append(f"{hm.group(0)} → {e['repl']}" + (f"（{e['note']}）" if e["note"] else ""))
            if hits:
                print("  词表      " + "\n            ".join(dict.fromkeys(hits)))

            print("  判定      [ ]")
    print(f"\n共 {n} 句。每句的「判定」都要填：保留 / 改写（写出改成什么）/ 删除。")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--lines", action="store_true", help="one row per hit, with line numbers")
    ap.add_argument("--lang", action="append", choices=["en", "zh"], help="restrict to a language")
    ap.add_argument("--strip", action="store_true", help="remove HTML/markdown markup first")
    ap.add_argument("--pipeline", action="store_true",
                    help="per-sentence worksheet: tokens, verbs, punctuation, one verdict each")
    ap.add_argument("--lexicon", default=LEXICON)
    args = ap.parse_args()

    lexicon = load_lexicon(args.lexicon)
    text = "".join(open(f, encoding="utf-8").read() for f in args.files) if args.files \
        else sys.stdin.read()
    if args.strip:
        text = strip_markup(text)

    if args.pipeline:
        pipeline(text, lexicon, set(args.lang or []))
        return

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
        n = pat(text) if callable(pat) else len(re.findall(pat, text))
        print(f"# {name}: {n}", file=sys.stderr)


if __name__ == "__main__":
    main()
