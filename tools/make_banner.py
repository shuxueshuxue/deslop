#!/usr/bin/env python3
"""Compose the README banner: generated artwork plus real typography.

    python3 tools/make_banner.py     # writes assets/_banner.html
                                     # render it to PNG at 2x with any headless browser

The artwork behind the banner was generated with an image model. The type is set here in CSS instead,
because image models garble letterforms, and garbled letterforms on a repository about removing AI
tells would be the loudest tell available.

The prompt asked for no letters at all: two-colour letterpress on paper, a dense field of ink rules
carrying small ornamental flourishes on the left, thinning to a few clean rules on the right. That is
the subject drawn as itself rather than as an analogy for itself, which is the one exemption H6 grants.

banner-art.png is not kept in the repository, so the shipped assets/banner.png cannot be rebuilt from
here. It still carries a lexicon row count from the version that composed it; the strapline no longer
prints one, so a future rebuild will not age the same way.
"""
import base64, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "assets")

SANS = ('-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans CJK SC",'
        '"PingFang SC","Microsoft YaHei",sans-serif')
MONO = '"DejaVu Sans Mono",ui-monospace,Menlo,Consolas,monospace'
SERIF = '"Noto Serif CJK SC",Georgia,"Songti SC",serif'
INK, MUTED, AMBER, PAPER = "#17191d", "#7e7a72", "#b0651a", "#f3f1ec"


def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()


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
  <div class="meta">中文 · ENGLISH　　破折号 38 → 0　　MIT</div>
</div>"""


def main():
    art = os.path.join(ART, "banner-art.png")
    if not os.path.exists(art):
        raise SystemExit(f"missing {art}: the generated artwork is not kept in the repository, "
                         f"only the composed assets/banner.png is")
    open(os.path.join(ART, "_banner.html"), "w", encoding="utf-8").write(
        BANNER.replace("{ART}", data_uri(art)))
    print("wrote _banner.html")


if __name__ == "__main__":
    main()
