#!/usr/bin/env python3
"""Crop, resize and compress the generated artwork into the files the README uses.

    python3 tools/compose_art.py

Raw output from the image model is ~2.7 MB per file, which has no business in a repository whose
whole subject is not spending more than you need. These are two-colour prints on paper texture, so a
palette of 96 colours is visually lossless and roughly twenty times smaller.
"""
import os
from PIL import Image

ART = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "art")
RAW = os.path.join(ART, "raw")

# name, source, crop box on the source (or None), output width, palette size
JOBS = [
    ("banner",       "banner-a.png", (0, 232, 1536, 792), 1400, 96),
    ("banner-alt",   "banner-b.png", (0, 300, 1536, 724), 1400, 64),
    ("poster-base",  "poster-a.png", None,                1024, 128),
    ("phase-frame",  "phase-frame.png", None,              760, 96),
    ("phase-find",   "phase-find.png",  None,              760, 96),
    ("phase-apply",  "phase-apply.png", None,              760, 96),
    ("measure",      "measure.png",     None,              760, 96),
]


def main():
    total_in = total_out = 0
    for name, src, box, width, colors in JOBS:
        p = os.path.join(RAW, src)
        if not os.path.exists(p):
            print(f"missing {src}"); continue
        total_in += os.path.getsize(p)
        im = Image.open(p).convert("RGB")
        if box:
            im = im.crop(box)
        if im.width != width:
            h = round(im.height * width / im.width)
            im = im.resize((width, h), Image.LANCZOS)
        q = im.quantize(colors=colors, method=Image.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
        out = os.path.join(ART, f"{name}.png")
        q.save(out, optimize=True)
        total_out += os.path.getsize(out)
        print(f"{name:<14} {im.width}x{im.height}  {os.path.getsize(out)/1024:6.0f} KB")
    print(f"\nraw {total_in/1024/1024:.1f} MB -> {total_out/1024:.0f} KB")


if __name__ == "__main__":
    main()
