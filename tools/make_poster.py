#!/usr/bin/env python3
"""Compose the promo poster and the README banner: generated art plus real typography.

    python3 tools/make_poster.py          # writes two HTML files under assets/art/
    node ../studio-harness/shot-poster.mjs # renders them to PNG at 2x

Type is set here in CSS rather than asked of the image model. Image models garble letterforms, and
garbled letterforms on a repository about removing AI tells would be the loudest tell available.
"""
import base64, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "assets", "art")

SANS = ('-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans CJK SC",'
        '"PingFang SC","Microsoft YaHei",sans-serif')
MONO = '"DejaVu Sans Mono",ui-monospace,Menlo,Consolas,monospace'
SERIF = '"Noto Serif CJK SC",Georgia,"Songti SC",serif'
INK, MUTED, AMBER, PAPER = "#17191d", "#7e7a72", "#b0651a", "#f3f1ec"


def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()


POSTER = f"""<!doctype html><meta charset="utf-8">
<style>
  @page {{ margin:0 }}
  body {{ margin:0; width:1024px; height:1536px; position:relative; background:{PAPER};
         font-family:{SANS}; -webkit-font-smoothing:antialiased }}
  .art {{ position:absolute; inset:0; background:url('{{ART}}') center/cover no-repeat }}
  .veil {{ position:absolute; inset:0;
           background:linear-gradient(180deg,{PAPER}cc 0%,transparent 30%,
                     transparent 70%,{PAPER}cc 100%) }}
  .top {{ position:absolute; top:0; left:0; right:0; padding:92px 96px 56px;
          background:linear-gradient(180deg,{PAPER} 0%,{PAPER} 72%,{PAPER}d9 88%,transparent 100%) }}
  .eyebrow {{ font:600 13px/1 {MONO}; letter-spacing:.34em; text-transform:uppercase; color:{AMBER} }}
  h1 {{ margin:26px 0 0; font:600 92px/0.94 {SANS}; letter-spacing:-.035em; color:{INK} }}
  .rule {{ margin:30px 0 0; height:1px; background:{INK}; opacity:.22 }}
  .lede {{ margin:26px 0 0; font:400 21px/1.65 {SERIF}; color:{INK}; max-width:660px }}
  .bot {{ position:absolute; bottom:0; left:0; right:0; padding:56px 96px 92px;
          background:linear-gradient(0deg,{PAPER} 0%,{PAPER} 72%,{PAPER}d9 88%,transparent 100%) }}
  .nums {{ display:flex; gap:56px; margin-bottom:34px }}
  .n b {{ display:block; font:600 46px/1 {SANS}; letter-spacing:-.03em; color:{INK} }}
  .n span {{ display:block; margin-top:9px; font:12px/1.5 {MONO}; letter-spacing:.12em; color:{MUTED} }}
  .n i {{ color:{AMBER}; font-style:normal }}
  .foot {{ display:flex; justify-content:space-between; align-items:baseline;
           border-top:1px solid {INK}33; padding-top:20px;
           font:13px/1 {MONO}; letter-spacing:.1em; color:{MUTED} }}
</style>
<div class="art"></div><div class="veil"></div>
<div class="top">
  <div class="eyebrow">a claude code skill</div>
  <h1>deslop</h1>
  <div class="rule"></div>
  <p class="lede">检查并改写文本里的模型腔，交出前后可核对的数字。<br>
  判据只有一句：这句话是在说事，还是在显得聪明。</p>
</div>
<div class="bot">
  <div class="nums">
    <div class="n"><b>38 <i>→</i> 0</b><span>EM DASH</span></div>
    <div class="n"><b>7 <i>→</i> 1</b><span>STAGED REVERSAL</span></div>
    <div class="n"><b>553</b><span>LEXICON ROWS</span></div>
    <div class="n"><b>100%</b><span>EVAL RECALL</span></div>
  </div>
  <div class="foot"><span>github.com/shuxueshuxue/deslop</span><span>中文 · ENGLISH · MIT</span></div>
</div>"""

BANNER = f"""<!doctype html><meta charset="utf-8">
<style>
  body {{ margin:0; width:1400px; height:440px; position:relative; background:{PAPER};
         font-family:{SANS}; -webkit-font-smoothing:antialiased }}
  .art {{ position:absolute; inset:0; background:url('{{ART}}') center/cover no-repeat }}
  .veil {{ position:absolute; inset:0;
           background:linear-gradient(90deg,{PAPER}fa 0%,{PAPER}e8 34%,{PAPER}55 52%,transparent 68%) }}
  .t {{ position:absolute; left:0; top:0; bottom:0; width:660px; padding:0 60px 0 74px;
        display:flex; flex-direction:column; justify-content:center;
        background:linear-gradient(90deg,{PAPER} 0%,{PAPER} 68%,{PAPER}cc 86%,transparent 100%) }}
  .eyebrow {{ font:600 11.5px/1 {MONO}; letter-spacing:.34em; text-transform:uppercase; color:{AMBER} }}
  h1 {{ margin:16px 0 0; font:600 74px/0.94 {SANS}; letter-spacing:-.035em; color:{INK} }}
  p {{ margin:18px 0 0; font:400 18px/1.6 {SERIF}; color:{INK}; max-width:520px }}
  .meta {{ margin:22px 0 0; font:12px/1 {MONO}; letter-spacing:.14em; color:{MUTED} }}
</style>
<div class="art"></div><div class="veil"></div>
<div class="t">
  <div class="eyebrow">a claude code skill</div>
  <h1>deslop</h1>
  <p>检查并改写文本里的模型腔，交出前后可核对的数字。</p>
  <div class="meta">中文 · ENGLISH　　破折号 38 → 0　　553 行词表　　MIT</div>
</div>"""


def main():
    poster = POSTER.replace("{ART}", data_uri(os.path.join(ART, "poster-base.png")))
    banner = BANNER.replace("{ART}", data_uri(os.path.join(ART, "banner.png")))
    open(os.path.join(ART, "_poster.html"), "w", encoding="utf-8").write(poster)
    open(os.path.join(ART, "_banner.html"), "w", encoding="utf-8").write(banner)
    print("wrote _poster.html and _banner.html")


if __name__ == "__main__":
    main()
