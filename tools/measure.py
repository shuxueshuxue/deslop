#!/usr/bin/env python3
"""Mechanical indicators for a deslop pass. Reports numbers; never rewrites.

    python3 tools/measure.py FILE                 # full report
    python3 tools/measure.py FILE --json          # machine-readable
    python3 tools/measure.py FILE --worksheet     # per-sentence audit worksheet
    python3 tools/measure.py --diff before.json after.json

Three tiers, and the tiering is the honest part of this file:

  GATED     hits are almost always real. Drive to zero or name every survivor.
  CAPPED    legitimate below a length-normalised cap; only the excess is a finding.
  REPORTED  printed, never gated, because measurement showed the number does not
            separate text that should change from text that should not.

An indicator earns a place in GATED only if its hits are almost always real. Two indicators lost
that place by being run on this repository's own prose: the trailing contrastive tail and the
inline-title list item. `references/field-reports.md` records the counts.
Two were demoted on evidence, and both notes are printed in the report so nobody
silently re-promotes them:

  * rule-of-three — on the first document deslop scanned, all five hits were ordinary
    enumerations. A number you cannot trust is worse than no number.
  * conjunction density — shuorenhua calibrated it on 95 passages and the criterion
    inverted: the median for text that should NOT change (5.26/1000) was higher than
    for text that should (0.00), and its max (81.08) was higher too. A global threshold
    would preferentially damage docs and status text, which carry condition and cause
    on explicit connectives.

Quoted material is excluded from every count. Someone else's staged reversal is theirs.
"""
import argparse, json, math, os, re, statistics, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LEXICON = os.path.join(HERE, "..", "references", "lexicon.tsv")

# ---------------------------------------------------------------- masking

FENCE = re.compile(r"```.*?```", re.S)
# An HTML page's stylesheet and scripts are not its prose. Without this, every CSS custom
# property (`var(--ink)`) reads as an em dash and the page scores in the hundreds.
STYLE_SCRIPT = re.compile(r"<(style|script)\b[^>]*>.*?</\1\s*>", re.S | re.I)
INLINE_CODE = re.compile(r"`[^`\n]*`")
FRONTMATTER = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.S)
LINK_TARGET = re.compile(r"\]\([^\n)]*\)")
URL = re.compile(r"https?://[^\s)>\]]+")
# Multiline so a wrapped SVG element does not leak its attributes into the prose.
HTML = re.compile(r"<[^<>]{0,4000}>", re.S)
# Quoted spans: blockquote lines, 「」/『』, and "…"/“…” runs. All are someone else's words.
CJK_QUOTE = re.compile(r"[「『][^」』]*[」』]")
STRAIGHT_QUOTE = re.compile(r"“[^”]{4,}”|\"[^\"\n]{12,}\"")


def _blank(match):
    return "".join("\n" if ch == "\n" else " " for ch in match.group())


def mask(text, drop_quotes=True):
    """Blank out everything that is not the author's running prose, preserving offsets."""
    out = text
    for pattern in (FRONTMATTER, STYLE_SCRIPT, FENCE, INLINE_CODE, LINK_TARGET, URL, HTML):
        out = pattern.sub(_blank, out)
    lines = []
    for line in out.split("\n"):
        stripped = line.lstrip()
        if drop_quotes and stripped.startswith(">"):      # blockquote = quoted source
            lines.append(" " * len(line))
        elif stripped.startswith("|"):                    # table row: cells, not prose
            lines.append(" " * len(line))
        else:
            lines.append(line)
    out = "\n".join(lines)
    if drop_quotes:
        out = CJK_QUOTE.sub(_blank, out)
        out = STRAIGHT_QUOTE.sub(_blank, out)
    return out


def prose_only(text):
    """Drop headings and list markers too — used for cadence, where a heading is not a sentence."""
    kept = []
    for line in mask(text).split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        s = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", s)
        kept.append(s)
    return "\n".join(kept)


# ---------------------------------------------------------------- GATED

REVERSAL = re.compile(
    r"不是[^，。！？\n]{2,24}，(?:而)?是"
    r"|不(?:只|仅|光)+(?:是)?[^，。！？\n]{2,24}，(?:而|更|还)?是"
    r"|与其[^，。\n]{2,20}，?不如"
    r"|不在于[^，。\n]{2,24}(?:，|而)在于"
    r"|(?:isn'?t|is not|was not|wasn'?t|are not|aren'?t) (?:just |merely |only |simply )?"
    r"[^,.;\n]{2,60}[,;] (?:it'?s|they'?re|but|it is)"
    r"|not (?:just|merely|only|simply) [^,.;\n]{2,60}[,;]? but"
    r"|it'?s not (?:about|that) [^,.;\n]{2,60}[,;] it'?s"
    # `A is not B: it is C` — the colon/semicolon form of the same move
    r"|\b(?:is|are|was|were) not [^,.;:\n]{2,60}[:;] (?:it|they|the)\b"
    r"|(?:^|[.;] )not [A-Za-z][^,.;\n]{2,40} — [a-z]",
    re.M)

# `Y, not X.` — capped, not gated. It was a GATED branch of REVERSAL until deslop was run on its
# own prose (references/field-reports.md): 6 hits, 1 real. A contrastive tail is ordinary in both
# languages and only becomes a tell by density; the staged move it was meant to catch is already
# covered by the `不是X而是Y` / `not just X but Y` / `isn't X, it's Y` branches above.
CONTRAST_TAIL = re.compile(
    r", not (?:because|that|a |an |the |to |for |by |from )[^,.;\n]{2,50}[.]", re.M)

# Deslop marker 5 / markers-en 3: the author grading their own sentence instead of writing it.
# Scene-sensitive: academic register licenses a few of these (`we note that`), chat does not.
STANCE = re.compile(
    r"\bthe (?:honest|hard|uncomfortable) (?:answer|truth|assessment|version)\b"
    r"|\bto be (?:honest|frank|blunt)\b|\b(?:frankly|candidly)\b|\bI'?ll be direct\b"
    r"|\bit(?:'s| is) worth (?:noting|saying|keeping|stressing)\b|\bworth keeping\b"
    r"|\bthe (?:real|key|central) (?:insight|question|point|issue) (?:is|here)\b"
    r"|\bthis is not a joke\b|\bthe one that matters most\b|\bthe sharpest\b"
    r"|\bwe (?:stress|emphasi[sz]e) that\b|\bthe strongest (?:feature|available evidence)\b"
    r"|\bmake no mistake\b|\blet that sink in\b|\bread that again\b"
    r"|老实说|诚实地讲|说句实话|坦白讲|不得不说|说得对|值得一提|关键在于|核心是"
    r"|我必须(?:很)?认真地说|这次我(?:真的)?懂了", re.I)
EM_DASH = re.compile(r"——|(?<=[^\s])—(?=[^\s])|(?<= )—(?= )|(?<=[^\s])--(?=[^\s])")
# Table and status glyphs are structure, not decoration: a ✓/✗ column is a table, not an emoji.
TABLE_GLYPH = "✓✔✗✘×○●◦□■◆★☆–—"
EMOJI = re.compile("[" + "".join(
    ch for ch in "".join(chr(c) for c in list(range(0x2600, 0x2700)) + list(range(0x2700, 0x27C0)))
    if ch not in TABLE_GLYPH) + "\U0001F000-\U0001FAFF]")
INLINE_TITLE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?\*\*[^*\n]{1,28}\*\*\s*[:：]\s*\S")
CUTOFF = re.compile(r"as of my (?:last )?(?:training|knowledge)|根据我(?:最后)?的训练|截至我(?:最后)?的(?:知识|训练)"
                    r"|based on (?:the )?available information|基于(?:现有|可用)信息", re.I)
ASSISTANT = re.compile(
    r"作为(?:一个)?(?:AI|人工智能|语言模型)|希望(?:这)?.{0,10}(?:帮助|有用|对你有)|好问题|感谢(?:你的)?提问"
    r"|让我(?:来|为你)|综上所述|由此可见|拆一拆|盘一盘|划重点|敲黑板"
    r"|as an ai\b|i hope (?:this|that) helps|great question|let me know if"
    r"|let'?s (?:dive in|break this down)|without further ado|you'?re absolutely right"
    r"|certainly!|of course!", re.I)
CURLY = re.compile(r"[“”‘’]")

# 、 and ： are counted for Chinese only: both let one sentence carry more than one thought
# without committing to a second sentence, which is the tell. Legality was never the test.
LABEL_COLON = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*[^*]+\*\*|[^：\s]{1,12})：")


def count_dunhao(masked):
    return sum(line.count("、") for line in masked.split("\n"))


def count_staging_colon(masked):
    n = 0
    for line in masked.split("\n"):
        body = LABEL_COLON.sub("", line, count=1)
        n += len(re.findall(r"：(?=\s*\S)", body))
    return n


# ---------------------------------------------------------------- CAPPED

SIGNPOST = re.compile(
    r"值得注意的是|值得一提的是|需要强调的是|更(?:关键|重要)的是|事实上|实际上|换句话说|说白了"
    r"|本质上|归根(?:结底|到底)|与此同时|总(?:的来说|而言之)"
    r"|it'?s worth noting|at the end of the day|the (?:truth|reality) is"
    r"|here'?s the thing|more importantly|in conclusion|that said\b|crucially\b"
    r"|^(?:Additionally|Moreover|Furthermore|Notably|Importantly|Ultimately),", re.I | re.M)
LECTURE = re.compile(r"首先[^。\n]{0,40}其次|让我(?:来|们)|接下来(?:我|我们)|捋一捋"
                     r"|first(?:ly)?,[^.\n]{0,80}second(?:ly)?,|in this (?:essay|section) we will", re.I)
EXCL = re.compile(r"[!！]")
HEDGE_STACK = re.compile(
    r"(?:可能|也许|或许|大概|大致|应该)[^，。\n]{0,10}(?:可能|也许|或许|大概|大致|应该)"
    r"|(?:might|may|could|possibly|potentially|arguably|somewhat|perhaps)\W+(?:\w+\W+){0,3}"
    r"(?:might|may|could|possibly|potentially|arguably|somewhat|perhaps)\b", re.I)
BOLD = re.compile(r"\*\*[^*\n]+\*\*")


# ---------------------------------------------------------------- REPORTED

CONJ_ZH = ("因为", "所以", "但是", "然而", "同时", "此外", "而且", "并且", "因此",
           "不仅", "于是", "另外", "总之", "首先", "其次", "如果", "否则")
CONJ_EN = ("because", "therefore", "however", "moreover", "furthermore", "additionally",
           "thus", "hence", "meanwhile", "nevertheless", "consequently", "although",
           "whereas", "otherwise")

NOMINAL_ZH = [re.compile(p) for p in (
    r"进行(?:了|一次|一场|着)?[^。，！？\n]{0,10}(?:调整|优化|升级|分析|讨论|沟通|梳理|复盘|迭代|探索|尝试|思考|规划|布局|评估|排查|验证|判定|隔离)",
    r"实现了?[^。，！？\n]{0,14}的?[^。，！？\n]{0,6}(?:提升|增长|突破|转变|跃升|落地|改善|隔离)",
    r"完成了?对[^。，！？\n]{0,16}的", r"起到了?[^。，！？\n]{0,12}的?作用",
    r"具有[^。，！？\n]{0,10}(?:意义|价值)", r"开展[^。，！？\n]{0,10}(?:工作|建设|研究|合作)")]
NOMINAL_EN = [re.compile(p, re.I) for p in (
    r"\b(?:perform|conduct|carry out|undertake|make|provide)s?\s+(?:an?|the)\s+\w+(?:tion|sis|ment|ance|ence|ing)\b",
    r"\bachieve[sd]?\s+(?:an?|the)?\s*\w*\s*(?:improvement|reduction|increase|decrease)\b",
    r"\bit is imperative that\b", r"\bhas the (?:ability|capability) to\b")]

# A present participle parked at the end of a clause to add depth that is not there.
# Wikipedia:Signs of AI writing lists this as one of the most reliable English markers.
ING_TAIL = re.compile(
    r",\s+(?:highlighting|underscoring|emphasi[sz]ing|reflecting|symbolis|symboliz|showcasing|"
    r"demonstrating|ensuring|contributing|fostering|cementing|solidifying|marking|"
    r"cementing|illustrating|reinforcing|signalling|signaling)\w*\b", re.I)
COPULA_DODGE = re.compile(
    r"\b(?:serves?|stands?|functions?|acts?)\s+as\b|\brepresents?\s+an?\b|\bboasts?\b"
    r"|作为[^，。\n]{2,16}(?:存在|出现)|标志着|见证了", re.I)
FALSE_RANGE = re.compile(r"\bfrom\s+[a-z][^,.\n]{3,40}\s+to\s+[a-z][^,.\n]{3,40},\s+(?:from|and)\b", re.I)

# Source domains an author reaches for when the subject is not in them. Under the principle-layer
# ban (SKILL.md 0.1 rule 6, taxonomy H6) every hit is a candidate, not just clustered ones.
# Reported, never gated: literal uses are real and common, so hits are NOT almost-always-real.
METAPHOR_FIELDS = {
    "道路竞赛": ("赛道", "跑道", "岔路", "十字路口", "终点线", "起跑线", "弯道超车", "回头路", "上车"),
    "战争攻防": ("护城河", "壁垒", "厮杀", "血战", "阵地", "弹药", "突围", "打法", "防线", "阵营", "火力"),
    "建筑灾害": ("坍塌", "崩塌", "地基", "支柱", "废墟", "基石", "add-on", "支撑起"),
    "温度": ("降温", "升温", "冷却", "余温", "白热化", "点燃", "冰山", "熔炉"),
    "仓储": ("仓库", "库存", "抽屉", "货架", "囤积"),
    "海洋航行": ("蓝海", "红海", "浪潮", "潮水", "灯塔", "彼岸", "风口", "掌舵", "触礁", "水面之下"),
    "机器器官": ("齿轮", "引擎", "发动机", "血管", "骨架", "神经末梢", "心脏", "动脉"),
    "工厂车间": ("流水线", "工位", "夹具", "产线", "车间", "工件", "量具", "上料", "出厂", "返工线",
                 "传送带", "装配线", "遮蔽胶带", "通止规", "公差带", "落刀", "打磨", "抛光"),
    "医疗": ("病灶", "把脉", "对症下药", "手术刀", "止血", "疗法", "解剖"),
    "法庭": ("判死", "定罪", "无罪", "举证责任", "陪审"),
    "农事烹饪": ("土壤", "生根", "发芽", "开花结果", "火候", "调味", "熬"),
    "road/race": ("racetrack", "fast lane", "crossroads", "finish line", "starting line", "on track"),
    "war": ("moat", "battleground", "arsenal", "frontline", "trenches", "playbook", "silver bullet"),
    "building": ("cornerstone", "foundation", "pillar", "bedrock", "scaffolding", "crumbling", "load-bearing"),
    "journey": ("journey", "roadmap", "milestone", "voyage", "trajectory", "north star"),
    "ecology": ("ecosystem", "landscape", "fertile ground", "seeds of", "organic growth"),
    "factory": ("assembly line", "conveyor", "production line", "shop floor", "widget"),
    "medicine": ("diagnose", "symptom", "surgical", "triage", "autopsy"),
}

# One-syllable physical verb roots. The object decides: an abstract object means the image is
# standing in for an operation the sentence should name. From deslop's scan.py.
PHYS_ROOTS = "跑扫抓压砍拉打接扛烧啃撕掰拧堵卡踩撑顶捞碾劈磨捏揪抠扒挖撬盘捋铺摊掀戳穿兜咬踢滚翻钉塌"
PHYS_RE = re.compile(f"[{PHYS_ROOTS}](?:掉|住|下|上|开|通|穿|爆|满|齐|平|出|回|一遍|一下|出来)?")
METAPHOR_LITERAL_PREFIX = {
    "引擎": ("搜索", "渲染", "游戏", "物理", "推荐", "规则", "模板", "查询", "存储"),
    "仓库": ("代码", "git", "Git", "远程", "本地", "私有", "镜像"),
    "库存": ("商品", "实际", "系统", "剩余"),
    "打法": ("战术",),
    "foundation": ("the foundation of the", "software foundation", "linux foundation"),
    "landscape": ("landscape orientation",),
}

TRIAD_ZH = re.compile(r"[^，。；\n]{2,10}、[^，。；\n]{2,10}、[^，。；\n]{2,10}[，。和与]")
TRIAD_EN = re.compile(r"\b\w[\w\- ]{2,24}, \w[\w\- ]{2,24},? and \w[\w\- ]{2,24}\b")

SENT_SPLIT_ZH = re.compile(r"[^。！？；\n]+[。！？；]?")
SENT_SPLIT_EN = re.compile(r"[^.!?\n]+[.!?]?")


def detect_lang(text):
    han = len(re.findall(r"[一-鿿]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    return "zh" if han * 3 > latin else "en"


def sentences(masked, lang):
    rx = SENT_SPLIT_ZH if lang == "zh" else SENT_SPLIT_EN
    out = []
    for line in masked.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for m in rx.finditer(line):
            s = m.group(0).strip()
            if len(s) >= (6 if lang == "zh" else 12):
                out.append(s)
    return out


def sent_len(s, lang):
    return len(re.sub(r"\s", "", s)) if lang == "zh" else len(s.split())


def load_lexicon(path, lang=None):
    """lang=None loads every row; a language code filters to that language."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith(">") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if p[0] == "lang" or len(p) < 4:
                continue
            if lang and p[0] != lang:
                continue
            body = rf"\b(?:{p[1]})\b" if p[1].isascii() else f"(?:{p[1]})"
            try:
                rx = re.compile(body, re.IGNORECASE if p[1].isascii() else 0)
            except re.error:
                continue
            rows.append(dict(lang=p[0], rx=rx, src=p[1], cat=p[2], repl=p[3],
                             note=p[4] if len(p) > 4 else "", source=p[5] if len(p) > 5 else ""))
    return rows


def scan(text, lexicon, langs=()):
    """One most-specific candidate per overlapping span, per line.

    A phrase rule such as ``In today's fast-paced landscape`` says more than the three word rules
    inside it. Showing all four makes a worklist noisier without giving the editor another decision.
    Kept byte-compatible with the older standalone scanner so eval numbers stay comparable.
    """
    hits = defaultdict(list)
    for i, line in enumerate(text.split("\n"), 1):
        cands = []
        for order, e in enumerate(lexicon):
            if langs and e["lang"] not in langs:
                continue
            for m in e["rx"].finditer(line):
                cands.append((m.start(), m.end(), order, e, m.group(0)))
        cands.sort(key=lambda h: (-(h[1] - h[0]), h[2], h[0]))
        kept = []
        for c in cands:
            if any(c[0] < k[1] and k[0] < c[1] for k in kept):
                continue
            kept.append(c)
        for _, _, _, e, matched in kept:
            hits[(e["lang"], e["src"], e["cat"], e["repl"], e["note"])].append(
                (i, matched, line.strip()))
    return hits


def metaphor_fields(masked):
    found = {}
    for field, terms in METAPHOR_FIELDS.items():
        for t in terms:
            for m in re.finditer(re.escape(t), masked, re.I):
                pre = masked[max(0, m.start() - 12):m.start()]
                if any(p.lower() in pre.lower() for p in METAPHOR_LITERAL_PREFIX.get(t, ())):
                    continue
                found.setdefault(field, []).append(t)
    return found



# A bold run opening a paragraph or a list item is a label; the tell is bold INSIDE a sentence.
# Bold inside a blockquote belongs to the person being quoted and is never charged to the author.
LABEL_BOLD = re.compile(r"^(\s*(?:[-*+]\s+|\d+[.)]\s+)?)\*\*[^*\n]{1,60}\*\*", re.M)


def _prose_paragraphs(text):
    out = []
    for p in re.split(r"\n\s*\n", text):
        if not p.strip():
            continue
        lines = [l for l in p.split("\n") if l.strip()]
        if all(l.lstrip().startswith((">", "|", "#")) for l in lines):
            continue
        out.append("\n".join(l for l in lines if not l.lstrip().startswith((">", "|"))))
    return [p for p in out if p.strip()]


def _strip_label_bold(paragraph):
    return LABEL_BOLD.sub(r"\1", paragraph)


def measure(text, lang=None, scene="docs"):
    lang = lang or detect_lang(text)
    masked = mask(text)
    body = prose_only(text)
    units = len(re.sub(r"\s", "", body)) if lang == "zh" else len(body.split())
    # natural-talk's caps are calibrated on a 300-500 character reply. In `chat` they are the
    # absolute numbers it published; in a document they become a density at the same ratio.
    scale = 1 if scene == "chat" else max(1, math.ceil(units / (300 if lang == "zh" else 220)))
    sents = sentences(masked, lang)
    lens = [sent_len(s, lang) for s in sents]

    gated = {
        "staged reversal": len(REVERSAL.findall(masked)),
        "em dash": len(EM_DASH.findall(masked)),
        "assistant residue": len(ASSISTANT.findall(masked)),
        "knowledge-cutoff disclaimer": len(CUTOFF.findall(masked)),
        "emoji": len(EMOJI.findall(masked)),
    }
    inline_title = sum(1 for l in text.split("\n") if INLINE_TITLE.match(l))
    if lang == "zh":
        gated["顿号"] = count_dunhao(masked)
        gated["句中冒号"] = count_staging_colon(masked)
        gated["curly quote"] = len(CURLY.findall(masked))
    else:
        gated["-ing pseudo-analysis tail"] = len(ING_TAIL.findall(masked))
        gated["copula dodge"] = len(COPULA_DODGE.findall(masked))
        gated["false range"] = len(FALSE_RANGE.findall(masked))

    stance = len(STANCE.findall(masked))
    if scene in ("chat", "public-writing"):
        gated["editorial stance"] = stance
    paras, bold_heavy = _prose_paragraphs(text), 0
    for p in paras:
        if len(BOLD.findall(_strip_label_bold(p))) > 1:
            bold_heavy += 1
    capped = {
        "signpost": (len(SIGNPOST.findall(masked)), 2 * scale),
        **({} if scene in ("chat", "public-writing") else {"editorial stance": (stance, scale)}),
        "lecture tone": (len(LECTURE.findall(masked)), 1),
        "exclamation": (len(EXCL.findall(masked)), 3 * scale),
        "hedge stacking": (len(HEDGE_STACK.findall(masked)), 0),
        "contrastive tail": (len(CONTRAST_TAIL.findall(masked)), scale),
        "inline-title list item": (inline_title, 2 * scale),
        "paragraphs with mid-sentence bold": (bold_heavy, max(1, len(paras) // 10)),
    }

    conj = CONJ_ZH if lang == "zh" else CONJ_EN
    conj_hits = sum(len(re.findall(re.escape(c) if lang == "zh" else rf"\b{c}\b", masked, re.I))
                    for c in conj)
    nominal = sum(len(p.findall(masked)) for p in (NOMINAL_ZH if lang == "zh" else NOMINAL_EN))
    triad = len((TRIAD_ZH if lang == "zh" else TRIAD_EN).findall(masked))
    fields = metaphor_fields(masked)

    lex = load_lexicon(LEXICON, lang)
    by_cat, lex_hits = {}, []
    for e in lex:
        for m in e["rx"].finditer(masked):
            by_cat[e["cat"]] = by_cat.get(e["cat"], 0) + 1
            lex_hits.append(dict(term=m.group(0), cat=e["cat"], repl=e["repl"],
                                 note=e["note"], source=e["source"]))

    reported = {
        "sentences": len(sents),
        "sentence length mean": round(statistics.fmean(lens), 1) if lens else None,
        "sentence length CV": (round(statistics.pstdev(lens) / statistics.fmean(lens), 3)
                               if len(lens) >= 12 and statistics.fmean(lens) else None),
        "conjunction density /1000": round(conj_hits * 1000 / units, 2) if units else 0,
        "nominalisation": nominal,
        "metaphor candidates": sum(len(v) for v in fields.values()),
        "metaphor fields touched": len(fields),
        "rule-of-three candidates": triad,
        "lexicon hits": len(lex_hits),
    }
    return dict(lang=lang, scene=scene, units=units, scale=scale, gated=gated, capped=capped,
                reported=reported, metaphor_detail={k: sorted(set(v)) for k, v in fields.items()},
                lexicon_by_category=dict(sorted(by_cat.items(), key=lambda kv: -kv[1])),
                lexicon_hits=lex_hits)


NOTES = {
    "rule-of-three candidates":
        "never gated — on the first document deslop scanned, 5/5 hits were ordinary enumerations",
    "conjunction density /1000":
        "never gated — shuorenhua calibration inverted it (SNF median 5.26 > SF median 0.00, "
        "SNF max 81.08 > SF max 80.00); judge by scene and distribution, not by total",
    "sentence length CV":
        "report-only; needs >=12 sentences, and no human-written control corpus exists to set a threshold",
}


def gated_hits(text, lang=None, scene="docs"):
    """Every GATED hit with a line number. Same regexes measure() counts, one entry per match.

    tools/selfcheck.py uses this to hold deslop's own prose to the rule deslop states: drive the
    gates to zero, or name every survivor.
    """
    lang = lang or detect_lang(text)
    masked = mask(text)
    raw = text.split("\n")
    checks = [("staged reversal", REVERSAL), ("em dash", EM_DASH),
              ("assistant residue", ASSISTANT), ("knowledge-cutoff disclaimer", CUTOFF),
              ("emoji", EMOJI)]
    if lang == "zh":
        checks.append(("curly quote", CURLY))
    else:
        checks += [("-ing pseudo-analysis tail", ING_TAIL), ("copula dodge", COPULA_DODGE),
                   ("false range", FALSE_RANGE)]
    if scene in ("chat", "public-writing"):
        checks.append(("editorial stance", STANCE))

    out = []
    for i, line in enumerate(masked.split("\n"), 1):
        for name, rx in checks:
            for m in rx.finditer(line):
                out.append(dict(indicator=name, line=i, match=m.group(0), text=raw[i - 1].strip()))
        if lang == "zh":
            for _ in range(line.count("、")):
                out.append(dict(indicator="顿号", line=i, match="、", text=raw[i - 1].strip()))
            body = LABEL_COLON.sub("", line, count=1)
            for m in re.finditer(r"：(?=\s*\S)", body):
                out.append(dict(indicator="句中冒号", line=i, match="：", text=raw[i - 1].strip()))
    out.sort(key=lambda h: (h["line"], h["indicator"]))
    return out


def render(r, path):
    L = []
    L.append(f"# {path}  [{r['lang']} · {r.get('scene','docs')}]  {r['units']} "
             f"{'chars' if r['lang']=='zh' else 'words'} of prose  (cap scale x{r['scale']})")
    L.append("  caps come from natural-talk's 300-500 char chat baseline, held as a density here")
    L.append("")
    L.append("## GATED — drive to zero or name every survivor")
    for k, v in r["gated"].items():
        L.append(f"  {'!!' if v else '  '} {k:<32} {v}")
    L.append("")
    L.append("## CAPPED — only the excess is a finding")
    for k, (v, cap) in r["capped"].items():
        L.append(f"  {'!!' if v > cap else '  '} {k:<32} {v}  (cap {cap})")
    L.append("")
    L.append("## REPORTED — never gates a pass/fail")
    for k, v in r["reported"].items():
        line = f"     {k:<32} {v}"
        if k in NOTES:
            line += f"\n         ^ {NOTES[k]}"
        L.append(line)
    if r["metaphor_detail"]:
        L.append("")
        L.append("     metaphor fields: " + "; ".join(
            f"{k}({','.join(v)})" for k, v in r["metaphor_detail"].items()))
    if r["lexicon_by_category"]:
        L.append("")
        L.append("## lexicon candidates by category (a hit is a candidate, not a verdict)")
        for k, v in r["lexicon_by_category"].items():
            L.append(f"     {k:<32} {v}")
    return "\n".join(L)


def render_hits(r, limit=None):
    L = ["", "## lexicon hits"]
    seen = {}
    for h in r["lexicon_hits"]:
        seen.setdefault((h["term"].lower(), h["cat"]), h).setdefault("n", 0)
        seen[(h["term"].lower(), h["cat"])]["n"] += 1
    rows = sorted(seen.values(), key=lambda h: -h["n"])
    for h in rows[:limit]:
        note = f"   [{h['note']}]" if h["note"] else ""
        L.append(f"  {h['n']:>2}x  {h['term']:<28} {h['cat']:<12} -> {h['repl']}{note}")
    return "\n".join(L)


def worksheet(text, lang=None):
    lang = lang or detect_lang(text)
    masked = mask(text)
    lex = load_lexicon(LEXICON, lang)
    out, n = [], 0
    for s in sentences(masked, lang):
        n += 1
        flags = []
        for name, rx in (("staged reversal", REVERSAL), ("em dash", EM_DASH),
                         ("signpost", SIGNPOST), ("assistant", ASSISTANT),
                         ("hedge stack", HEDGE_STACK), ("copula dodge", COPULA_DODGE),
                         ("stance", STANCE),
                         ("-ing tail", ING_TAIL), ("lecture", LECTURE)):
            if rx.search(s):
                flags.append(name)
        if lang == "zh":
            if "、" in s:
                flags.append(f"顿号 x{s.count('、')}")
            if re.search(r"：(?=\s*\S)", LABEL_COLON.sub("", s, count=1)):
                flags.append("句中冒号")
        hits = []
        for e in lex:
            for m in e["rx"].finditer(s):
                hits.append(f"{m.group(0)}→{e['repl']}")
        out.append(f"\nS{n} ({sent_len(s, lang)}) {s}")
        if flags:
            out.append("   shape  " + " · ".join(flags))
        if hits:
            out.append("   lex    " + " · ".join(dict.fromkeys(hits)))
        if not flags and not hits:
            out.append("   clean  (still ask: delete it — is any information lost?)")
    return "\n".join(out)



# ---------------------------------------------------------------- taxonomy M (comments)

# taxonomy.md M1: the comment narrates the change instead of stating the state.
TEMPORAL = re.compile(
    r"\b(?:used to|previously|formerly|no longer|instead of|rather than before)\b"
    r"|\b(?:was|were|had been)\s+(?:previously|originally|earlier)\b"
    r"|\bthis (?:fixes|fixed|addresses|resolves)\b|\bneeded because otherwise\b"
    r"|\bnote that we (?:no longer|now)\b|\bwe (?:now|used to)\b|\bchanged (?:from|to)\b"
    r"|\b(?:now|originally) (?:returns|uses|handles|calls|does)\b"
    r"|以前|原来是|之前是|不再|改成了|这里修复|曾经", re.I)

# taxonomy.md M2: a reference only someone in the session can resolve.
ROOM = re.compile(
    r"\b(?:per|see|from) (?:the )?(?:AC|acceptance criteri\w+)\s*\d"
    r"|\b(?:PLAN|TASK|STEP|PHASE)[-_ ]?\d+(?:[.\-_][A-Za-z0-9]+)+"
    r"|\b\w*(?:PLAN|FEATURE|DESIGN|NOTES|SCRATCH|TODO)\.(?:md|MD|txt)\b"
    r"|\bas (?:discussed|we discussed|agreed|noted) (?:above|earlier|previously)\b"
    r"|\bthe (?:campaign|saga|era|epic|sprint) \w+|\b\w+[- ](?:saga|campaign|era)\b"
    r"|\bper (?:our|the) (?:conversation|discussion|plan)\b", re.I)

LINE_COMMENT = re.compile(r"(?:^|\s)(?://|#(?!!)|--(?!-)|;;)\s?(.*)$")
BLOCK_COMMENT = re.compile(r"/\*(.*?)\*/|<!--(.*?)-->|\"\"\"(.*?)\"\"\"", re.S)


def comment_lines(text):
    """(line number, comment body) for every line that carries one.

    A line-level heuristic, not a parser: a `#` inside a string literal will be offered as a
    candidate. That is the right trade for a lister whose output a person reads.
    """
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        m = LINE_COMMENT.search(line)
        if m and m.group(1).strip():
            out.append((i, m.group(1).strip()))
    for m in BLOCK_COMMENT.finditer(text):
        body = next(g for g in m.groups() if g is not None)
        start = text.count("\n", 0, m.start()) + 1
        for j, line in enumerate(body.split("\n")):
            if line.strip():
                out.append((start + j, line.strip(" *\t")))
    return sorted(set(out))


def comment_worklist(text):
    """taxonomy.md M1/M2 candidates in comments. Never a count: outside a comment this
    vocabulary is ordinary prose, so nothing here can gate anything."""
    L = ["## taxonomy M candidates in comments (a hit is a candidate, not a verdict)"]
    n = 0
    for line, body in comment_lines(text):
        hits = [f"M1:{m.group(0)}" for m in TEMPORAL.finditer(body)]
        hits += [f"M2:{m.group(0)}" for m in ROOM.finditer(body)]
        if hits:
            n += 1
            L.append(f"  L{line:<5d} {body[:76]}")
            L.append(f"         {' · '.join(hits)}")
    L.append(f"\n  {n} comment line(s) flagged of {len(comment_lines(text))} scanned.")
    L.append("  M1: state the current behaviour, or move the history to the commit body.")
    L.append("  M2: inline the fact, or cite something a reader can resolve a year from now.")
    return "\n".join(L)


def metaphor_worklist(text, lang=None):
    """Every borrowed-domain term and every physical verb, with line numbers.

    The principle-layer ban on live metaphor (SKILL.md 0.1 rule 6) cannot be gated: a name the
    field has frozen (`死锁`, `back-pressure`, `pipeline`) and a literal use (`代码仓库`) look
    identical to a word list. So this refuses to let a candidate go unexamined and decides nothing.
    """
    lang = lang or detect_lang(text)
    lines = mask(text).split("\n")
    out, n = ["# metaphor worklist — candidates only. A name is not a metaphor; see taxonomy H6."], 0
    for i, line in enumerate(lines, 1):
        hits = []
        for field, terms in METAPHOR_FIELDS.items():
            for t in terms:
                for m in re.finditer(re.escape(t), line, re.I):
                    pre = line[max(0, m.start() - 12):m.start()]
                    if any(p.lower() in pre.lower() for p in METAPHOR_LITERAL_PREFIX.get(t, ())):
                        continue
                    hits.append(f"{t}[{field}]")
        if lang == "zh":
            for v in sorted({v.group(0) for v in PHYS_RE.finditer(line)}):
                if len(v) > 1:
                    hits.append(f"{v}[物理动词]")
        if hits:
            n += len(hits)
            out.append(f"L{i:>4}  {' · '.join(dict.fromkeys(hits))}")
            out.append(f"        {line.strip()[:96]}")
    out.append(f"\n{n} candidates. Each needs one decision: a name the field froze, a literal use, "
               f"or a live metaphor the author introduced. Only the third is a hit.")
    return "\n".join(out)

def diff(a, b):
    L = ["| indicator | before | after |", "|---|---|---|"]
    for tier in ("gated",):
        for k in a[tier]:
            L.append(f"| {k} | {a[tier][k]} | {b[tier].get(k, '-')} |")
    for k in a["capped"]:
        L.append(f"| {k} (cap {a['capped'][k][1]}) | {a['capped'][k][0]} | {b['capped'].get(k, ['-'])[0]} |")
    for k in ("nominalisation", "metaphor candidates", "lexicon hits",
              "sentence length CV", "conjunction density /1000", "rule-of-three candidates"):
        L.append(f"| {k} | {a['reported'].get(k)} | {b['reported'].get(k)} |")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--lang", choices=["zh", "en"])
    ap.add_argument("--scene", default="docs",
                    choices=["chat", "status", "docs", "public-writing", "academic", "code-context"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--hits", nargs="?", type=int, const=0, default=None,
                    help="list lexicon hits (optionally top N)")
    ap.add_argument("--worksheet", action="store_true")
    ap.add_argument("--comments", action="store_true",
                    help="taxonomy M1/M2 candidates in a source file's comments")
    ap.add_argument("--metaphor", action="store_true",
                    help="list every borrowed-domain term and physical-verb candidate, with line numbers")
    ap.add_argument("--diff", nargs=2, metavar=("BEFORE.json", "AFTER.json"))
    a = ap.parse_args()

    if a.diff:
        with open(a.diff[0]) as f1, open(a.diff[1]) as f2:
            print(diff(json.load(f1), json.load(f2)))
        return 0
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    if a.worksheet:
        print(worksheet(text, a.lang))
        return 0
    if a.comments:
        print(comment_worklist(text))
        return 0
    if a.metaphor:
        print(metaphor_worklist(text, a.lang))
        return 0
    r = measure(text, a.lang, a.scene)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(render(r, a.file or "-"))
        if a.hits is not None:
            print(render_hits(r, a.hits or None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
