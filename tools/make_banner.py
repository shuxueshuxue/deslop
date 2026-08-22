#!/usr/bin/env python3
"""Compose the README banner: generated artwork plus real typography.

    python3 tools/make_banner.py                 # writes assets/_banner.html
    # render that file to PNG at 1400x440, deviceScaleFactor 2, with any headless browser
    python3 tools/make_banner.py --compose SHOT.png   # downscales it into assets/banner.png

The artwork behind the banner was generated with an image model. The type is set here in CSS instead,
because image models garble letterforms, and garbled letterforms on a repository about removing AI
tells would be the loudest tell available.

The prompt asked for no letters at all: two-colour letterpress on paper, a dense field of ink rules
carrying small ornamental flourishes on the left, thinning to a few clean rules on the right. That is
the subject drawn as itself rather than as an analogy for itself, which is the one exemption H6 grants.

assets/banner-art.jpg is the generated artwork, kept here so the banner can be rebuilt. It is already
cropped to the 1400x440 box and stored as JPEG, because it is a grainy paper texture and a palette
PNG of it costs three times as much for no visible gain. The composed banner stays PNG, where the
type is.

The strapline carries no counts. An earlier version printed the lexicon row count and the shipped
image went stale the next time the lexicon grew, with no way to rebuild it.

banner.png stays 24-bit rather than a palette PNG. Palette quantisation costs about 120 KB less and
loses the amber eyebrow every time: the paper grain holds thousands of near-identical shades that
take the whole palette, and the accent is a few thousand thin pixels with no population to defend
itself. The shipped banner before this rebuild had lost it that way.
"""
import base64, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "assets")

SANS = ('-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans CJK SC",'
        '"PingFang SC","Microsoft YaHei",sans-serif')
MONO = '"DejaVu Sans Mono",ui-monospace,Menlo,Consolas,monospace'
SERIF = '"Noto Serif CJK SC",Georgia,"Songti SC",serif'
INK, MUTED, AMBER, PAPER = "#17191d", "#7e7a72", "#b0651a", "#f3f1ec"


def data_uri(path):
    mime = "jpeg" if path.endswith((".jpg", ".jpeg")) else "png"
    return f"data:image/{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


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


def compose(shot):
    from PIL import Image
    im = Image.open(shot).convert("RGB")
    if im.size != (2800, 880):
        raise SystemExit(f"{shot} is {im.size}, expected (2800, 880): 1400x440 at 2x")
    out = os.path.join(ART, "banner.png")
    im.resize((1400, 440), Image.LANCZOS).save(out, optimize=True)
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--compose":
        return compose(sys.argv[2])
    art = os.path.join(ART, "banner-art.jpg")
    if not os.path.exists(art):
        raise SystemExit(f"missing {art}")
    open(os.path.join(ART, "_banner.html"), "w", encoding="utf-8").write(
        BANNER.replace("{ART}", data_uri(art)))
    print("wrote _banner.html")


if __name__ == "__main__":
    main()
