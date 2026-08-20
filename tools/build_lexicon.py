#!/usr/bin/env python3
"""Build the merged lexicon from the four upstream projects.

    python3 tools/build_lexicon.py --sources <dir-with-the-four-checkouts> [-o references/lexicon.tsv]

Base is deslop's `references/lexicon.tsv` (already regex, already sourced, already carries the
"legitimate in context" note column). On top of it we add rows harvested from shuorenhua's two
phrase tables and a hand-kept supplement for the items only Humanizer-zh and natural-talk have.

Dedupe test is by MATCH, not by string equality: a harvested literal is dropped when a row already
in the table matches it. That is the only test that stops the merged table from carrying four rows
for the same word under four names.

Every row keeps a `source` column. A merged word list whose provenance is lost cannot be audited,
and the four upstreams disagree about several words on purpose.
"""
import argparse, os, re, sys

COLS = ["lang", "pattern", "category", "replacement", "note", "source"]

HEADER = """\
> prose-deslop merged lexicon — one candidate per row. The scanner reports hits; it never rewrites.
> Columns: lang  pattern  category  replacement  note  source
> lang: en | zh   ·   pattern: Python regex (ASCII patterns get \\b…\\b added automatically)
> category: vocab puffery editorial transition template shape jargon hedge assistant physical
>           borrowed unsettled-term stance opener closer empathy debug violence
> note: when the word is legitimate. A blank note does NOT mean "always wrong" — see SKILL.md.
> source: deslop | shuorenhua | humanizer-zh | natural-talk (first table it entered from)
> Upstream sources of the words themselves: WP:AIVOCAB · Wikipedia:Signs of AI writing ·
> Kobak et al. 2025 (Science Advances 11(27)) · Juzek & Ward 2025 · HN 48905248 ·
> awesome-ai-research-writing · Chinese community lists (Linux.do / X / 即刻).
"""

# shuorenhua's phrase tables group by `### heading`; map those to the merged category vocabulary.
ZH_SECTION_CATEGORY = {
    "开场套话": "opener", "渲染性强调": "puffery", "商业/互联网黑话": "jargon",
    "工程师腔 / 调试腔（AI 模仿程序员说话）": "debug",
    "庸医问诊腔（AI 模仿诊断专家口吻）": "debug",
    "暴力动作腔（AI 用激烈动词表达普通操作）": "violence",
    "自媒体 / 小红书 AI 腔": "puffery", "洞见感 / 价值拔高骨架": "shape",
    "过渡废话": "transition", "正能量收尾模板": "closer",
    "无源引用（公开写作中尤其像 AI）": "editorial", "谄媚/元评论": "assistant",
    "AI 主动出击腔（血压升高类）": "assistant",
    "过度接住 / 心理判断腔": "empathy",
    "郑重预告 / 身份认证式夸奖": "stance",
    "单音节命令词（编程辅助场景中 AI 喜欢用短促单字当动词/状语）": "physical",
    "连接词": "transition", "形容/修饰": "vocab",
    "抒情词给抽象概念穿衣服": "puffery", "翻译腔（中文特有 AI 味）": "borrowed",
}
EN_SECTION_CATEGORY = {
    "Throat-clearing openers": "opener", "Emphasis crutches": "closer",
    "Business jargon": "jargon", "Inflated verbs (use simpler alternatives)": "vocab",
    "Significance inflation": "puffery", "Copula avoidance (just use \"is/are/has\")": "shape",
    "Filler phrases": "template", "Sycophantic / meta": "assistant",
    "Adverbs (-ly words)": "hedge",
}

BULLET = re.compile(r"^\s*-\s+(.*\S)\s*$")
ARROW = re.compile(r"\s*(?:→|->)\s*")


def load_tsv(path, default_source):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.startswith(">") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if parts[0] == "lang":
                continue
            if len(parts) < 4:
                sys.stderr.write(f"{path}:{n}: need 4+ columns, got {len(parts)}\n")
                continue
            row = dict(zip(COLS, parts + [""] * (len(COLS) - len(parts))))
            row["source"] = row["source"] or default_source
            rows.append(row)
    return rows


def compile_pattern(pattern):
    body = rf"\b(?:{pattern})\b" if pattern.isascii() else f"(?:{pattern})"
    try:
        return re.compile(body, re.IGNORECASE if pattern.isascii() else 0)
    except re.error:
        return None


def harvest_phrase_table(path, lang, section_map, source):
    """Parse `- 命中 → 替换` bullets under `### section` headings."""
    rows, section, tier = [], None, None
    if not os.path.exists(path):
        sys.stderr.write(f"missing {path}; skipped\n")
        return rows
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            tier = line[3:].strip()
            section = None
            continue
        if line.startswith("### "):
            section = line[4:].strip()
            continue
        m = BULLET.match(line)
        if not m or section is None:
            continue
        body = m.group(1)
        parts = ARROW.split(body, maxsplit=1)
        hit = parts[0].strip()
        repl = parts[1].strip() if len(parts) > 1 else "(cut)"
        note = ""
        # the tables carry their exemption inline after a full-width semicolon
        if "；" in repl:
            repl, note = [s.strip() for s in repl.split("；", 1)]
        # a parenthetical scope qualifier on the hit is a note, not part of the pattern
        qual = re.search(r"[（(]([^）)]*)[）)]\s*$", hit)
        if qual:
            note = (note + " · " if note else "") + qual.group(1)
            hit = hit[: qual.start()].strip()
        hit = hit.replace("……", "\uE000").replace("…", "\uE000")
        # `A / B / C` in a bullet is three spellings of one tell, not one literal with slashes
        alts = [x.strip() for x in re.split(r"\s+/\s+", hit) if x.strip()]
        alts = [x for x in alts if 2 <= len(x) <= 24 and not (lang == "en" and len(x) < 4)
                and not (lang == "zh" and re.search(r"[A-Za-z]{4,}", x))]
        if not alts:
            continue
        body = "|".join(re.escape(x).replace("\uE000", ".{0,12}") for x in alts)
        pattern = f"(?:{body})" if len(alts) > 1 else body
        rows.append(dict(lang=lang, pattern=pattern,
                         category=section_map.get(section, "vocab"),
                         replacement=repl or "(cut)", note=note,
                         source=f"{source}:{tier.split('：')[0].split(':')[0]}" if tier else source))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", required=True, help="dir holding deslop/ shuorenhua/ checkouts")
    ap.add_argument("--extra", default=None, help="hand-kept supplement TSV")
    ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()

    base = load_tsv(os.path.join(a.sources, "deslop", "references", "lexicon.tsv"), "deslop")
    harvested = []
    harvested += harvest_phrase_table(
        os.path.join(a.sources, "shuorenhua", "references", "phrases-zh.md"),
        "zh", ZH_SECTION_CATEGORY, "shuorenhua")
    harvested += harvest_phrase_table(
        os.path.join(a.sources, "shuorenhua", "references", "phrases-en.md"),
        "en", EN_SECTION_CATEGORY, "shuorenhua")
    if a.extra and os.path.exists(a.extra):
        harvested += load_tsv(a.extra, "supplement")

    merged, compiled = list(base), [(r["lang"], compile_pattern(r["pattern"])) for r in base]
    kept = dropped = 0
    for row in harvested:
        literal = re.sub(r"\\(.)", r"\1", row["pattern"])
        literal = re.sub(r"\.\{0,\d+\}", "xxxx", literal)
        if any(lang == row["lang"] and rx and rx.search(literal) for lang, rx in compiled):
            dropped += 1
            continue
        rx = compile_pattern(row["pattern"])
        if rx is None:
            dropped += 1
            continue
        merged.append(row)
        compiled.append((row["lang"], rx))
        kept += 1

    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(HEADER)
        fh.write("\t".join(COLS) + "\n")
        for r in merged:
            fh.write("\t".join(r[c] for c in COLS).rstrip("\t") + "\n")
    print(f"base {len(base)} + harvested {len(harvested)} "
          f"→ kept {kept}, dropped {dropped} already-covered → {len(merged)} rows")


if __name__ == "__main__":
    main()
