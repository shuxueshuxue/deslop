#!/usr/bin/env python3
"""Emit the nine-step flow diagram in three forms from one geometry.

    python3 tools/make_flow.py

  assets/flow-light.svg   standalone, baked light palette, for a README <picture>
  assets/flow-dark.svg    standalone, baked dark palette
  docs/_flow.svg          fragment using var(--token), for the HTML page

Typographic rather than schematic: no boxes, no dashed panels, no repeated arrowheads.
A hairline rail, one node per step, type carrying the hierarchy. The only colour is on the
nodes, and it encodes who runs the step, which is the one fact worth seeing at a glance.
"""
import os

W = 960
STEP_X, COL_B, RIGHT = 132, 430, 884
RAIL, NUM_X = 100, 46

STEPS = [
    dict(n="01", y=124, name="入口判定", who="agent", tone="agent",
         d=["这段文本该不该改。要逐字翻译的，要仿模板的，", "主体是代码日志的，要事实校对的，都退回"]),
    dict(n="02", y=220, name="判场景", who="agent", tone="agent",
         d=["六个场景选一个。它决定合格标准是什么，", "聊天的标准和论文的标准不是同一条线"]),
    dict(n="03", y=316, name="划保护片段", who="agent · 产出冻结层", tone="freeze",
         d=["数字，引用，命令，报错，责任归属。", "另记一份关系账本，这层没有词表能替代"]),
    dict(n="04", y=440, name="前测", who="脚本 · measure.py", tone="script",
         d=["读数存成 JSON。第 09 步要和它对照，", "这是整条流程里唯一能证伪的部分"]),
    dict(n="05", y=536, name="词面扫描", who="脚本 + agent", tone="agent",
         d=["物理动词（中）／抬高词（英），再过 570 行词表。", "出候选，不出判定"]),
    dict(n="06", y=632, name="逐行审计", who="agent · 必须换上下文", tone="fresh",
         d=["逐行出表，一行一条命中，宁可多报。", "写的那个 agent 审不了自己写的，所以换一个空白上下文"]),
    dict(n="07", y=816, name="应用替换", who="agent", tone="agent",
         d=["换成字面动作。文本只在这一步被改，", "不许用另一个花哨词换掉这个花哨词"]),
    dict(n="08", y=918, name="四遍回读", who="agent · 不许合并", tone="agent",
         d=["四遍看的不是同一种东西，所以不许合并。", "B 或 D 命中，回到 07 重改"]),
    dict(n="09", y=1052, name="后测与报告", who="脚本 + agent，交给人", tone="script",
         d=["交前后两个数，每个还留在表上的命中", "逐条写明为什么留"]),
]
PHASES = [("框定", 70, 80), ("查找", 386, 396), ("修改与验证", 762, 772)]
REREADS = [("A", "保真", "保护片段没漂"), ("B", "过校正", "查你刚写下的"),
           ("C", "残留", "固定只查五类"), ("D", "通读", "看两处修改的交界")]
ASIDE = ("不是语域问题，本流程不处理", "悬空指代 · 前后矛盾 · 引文误读 · 数字错")
LEGEND = [("script", "脚本"), ("agent", "agent"), ("fresh", "换上下文"), ("freeze", "冻结不许改")]

LIGHT = dict(bg="#ffffff", panel="#ffffff", ink="#15171b", ink2="#4a5058", muted="#8a919b",
             rule="#e3dfd6", rail="#d6d1c6", agent="#a8b0ba", fresh="#b26a00",
             script="#1b4fa8", freeze="#5f3ab5", red="#a8241c")
DARK = dict(bg="#0d1117", panel="#0d1117", ink="#e9ecf1", ink2="#b2bbc6", muted="#868f9c",
            rule="#2a3038", rail="#39414b", agent="#5d6672", fresh="#e0952f",
            script="#6fa0f0", freeze="#a98cf0", red="#e06a60")
TOKENS = dict(bg="var(--panel)", panel="var(--panel)", ink="var(--ink)", ink2="var(--ink-2)",
              muted="var(--muted)", rule="var(--rule)", rail="var(--rule-2)",
              agent="var(--steel)", fresh="var(--amber)", script="var(--blue)",
              freeze="var(--violet)", red="var(--red)")

SANS = ('system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",'
        '"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif')
MONO = ('ui-monospace,"SF Mono","JetBrains Mono",Menlo,Consolas,'
        '"Liberation Mono",monospace')
H = 1098


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(c, standalone):
    o = []
    a = o.append
    if standalone:
        a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
          f'viewBox="0 0 {W} {H}" role="img" aria-label="prose-deslop 九步流程">')
        a(f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>')
    else:
        a(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
          f'aria-label="prose-deslop 九步流程：入口判定、判场景、划保护片段、前测、词面扫描、'
          f'逐行审计、应用替换、四遍回读、后测与报告">')
    a('<defs><marker id="fa" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" '
      f'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 z" fill="{c["red"]}"/></marker></defs>')
    a("<style>")
    a(f'.num{{fill:{c["muted"]};font:300 25px {SANS};opacity:.5;font-variant-numeric:tabular-nums}}')
    a(f'.nm{{fill:{c["ink"]};font:600 17px {SANS}}}')
    a(f'.wh{{fill:{c["muted"]};font:10.5px {MONO};letter-spacing:.1em}}')
    a(f'.de{{fill:{c["ink2"]};font:13.5px {SANS}}}')
    a(f'.ph{{fill:{c["muted"]};font:600 10.5px {MONO};letter-spacing:.18em}}')
    a(f'.as{{fill:{c["muted"]};font:12.5px {SANS}}}')
    a(f'.asb{{fill:{c["ink2"]};font:600 12.5px {SANS}}}')
    a(f'.rk{{fill:{c["ink"]};font:600 13px {SANS}}}')
    a(f'.rc{{fill:{c["muted"]};font:11.5px {SANS}}}')
    a(f'.rl{{fill:{c["red"]};font:600 11px {MONO};letter-spacing:.08em}}')
    a(f'.lg{{fill:{c["muted"]};font:10.5px {MONO};letter-spacing:.1em}}')
    a("</style>")

    # legend, right-aligned, quiet
    def tw(t):
        return sum(11.6 if ord(ch) > 0x2000 else 6.6 for ch in t)
    items = [(tone, lab, 11 + tw(lab)) for tone, lab in LEGEND]
    x = RIGHT - sum(w for _, _, w in items) - 26 * (len(items) - 1)
    for tone, label, w in items:
        a(f'<circle cx="{x:.0f}" cy="34" r="4" fill="{c[tone]}"/>')
        a(f'<text class="lg" x="{x + 11:.0f}" y="38">{esc(label)}</text>')
        x += w + 26
    # phase rules
    for name, ty, ry in PHASES:
        a(f'<text class="ph" x="{STEP_X}" y="{ty}">{esc(name)}</text>')
        a(f'<line x1="{STEP_X}" y1="{ry}" x2="{RIGHT}" y2="{ry}" stroke="{c["rule"]}" stroke-width="1"/>')
    # rail
    a(f'<line x1="{RAIL}" y1="{STEPS[0]["y"] - 5}" x2="{RAIL}" y2="{STEPS[-1]["y"] - 5}" '
      f'stroke="{c["rail"]}" stroke-width="1"/>')
    # return edge: 08 back to 07, drawn quietly in the number gutter
    a(f'<path d="M{RAIL} 913 C 66 913, 66 811, {RAIL - 6} 811" fill="none" stroke="{c["red"]}" '
      f'stroke-width="1.2" opacity=".75" marker-end="url(#fa)"/>')

    for s in STEPS:
        y = s["y"]
        a(f'<text class="num" x="{NUM_X}" y="{y + 2}" text-anchor="end">{s["n"]}</text>')
        a(f'<circle cx="{RAIL}" cy="{y - 5}" r="4.5" fill="{c[s["tone"]]}" '
          f'stroke="{c["panel"]}" stroke-width="3"/>')
        a(f'<text class="nm" x="{STEP_X}" y="{y}">{esc(s["name"])}</text>')
        a(f'<text class="wh" x="{STEP_X}" y="{y + 21}">{esc(s["who"])}</text>')
        a(f'<text class="de" x="{COL_B}" y="{y - 1}">{esc(s["d"][0])}</text>')
        a(f'<text class="de" x="{COL_B}" y="{y + 20}">{esc(s["d"][1])}</text>')

    # the aside hanging off step 06
    a(f'<line x1="{COL_B - 6}" y1="668" x2="{COL_B - 6}" y2="710" stroke="{c["rule"]}" stroke-width="2"/>')
    a(f'<text class="asb" x="{COL_B + 12}" y="682">{esc(ASIDE[0])}</text>')
    a(f'<text class="as" x="{COL_B + 12}" y="704">{esc(ASIDE[1])}</text>')

    # the four rereads, set as four compact items rather than four boxes
    x = COL_B
    for k, name, cap in REREADS:
        a(f'<text class="rl" x="{x}" y="{970}">{k}</text>')
        a(f'<text class="rk" x="{x + 16}" y="{970}">{esc(name)}</text>')
        a(f'<text class="rc" x="{x}" y="{990}">{esc(cap)}</text>')
        x += 114
    return "\n".join(o) + "\n</svg>\n"


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(here, "assets"), exist_ok=True)
    os.makedirs(os.path.join(here, "docs"), exist_ok=True)
    for name, pal, alone in (("assets/flow-light.svg", LIGHT, True),
                             ("assets/flow-dark.svg", DARK, True),
                             ("docs/_flow.svg", TOKENS, False)):
        p = os.path.join(here, name)
        open(p, "w", encoding="utf-8").write(build(pal, alone))
        print(f"{name}  {os.path.getsize(p)} bytes")


if __name__ == "__main__":
    main()
