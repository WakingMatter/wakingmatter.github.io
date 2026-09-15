#!/usr/bin/env python3
"""Wordmark / type gate. Finish and Source occupancy are frozen.

Reads brand/logos/mark.svg and mark-on-void.svg as-is. Does not rewrite
masters, does not start Phase B, does not freeze type.
"""

from __future__ import annotations

import re
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

REPO = Path(__file__).resolve().parents[3]
LOGOS = REPO / "brand" / "logos"
STUDY = Path(__file__).resolve().parent
LOCK = STUDY / "lockups"
GLYPH = STUDY / "glyphs"
WM = STUDY / "wordmarks"
FONT_DIR = Path("/tmp/wm-type")
INST = FONT_DIR / "instanced"

LOCK.mkdir(parents=True, exist_ok=True)
GLYPH.mkdir(parents=True, exist_ok=True)
WM.mkdir(parents=True, exist_ok=True)
INST.mkdir(parents=True, exist_ok=True)

# Frozen Source occupancy (do not change)
L, Y, W, H = 35.90, 13.00, 11.00, 94.00
R_X = 73.10
MARK_W = (R_X + W) - L  # 48.30

VOID = "#0A0A0A"
IVORY = "#F7F6F3"
CHARCOAL = "#2A2A2A"

CAP = 52.2
Y_OFF = 1.944
GAP_04 = 0.38 * CAP  # current 04-tight lockup
GAP_02 = 0.58 * CAP  # Direction 02 air: more mark-to-type negative space
SCALE = CAP / H
MARK_DRAW_W = MARK_W * SCALE
XFORM = (
    f"translate(0, {Y_OFF}) scale({SCALE:.12f}) "
    f"translate({-L:.2f}, {-Y:.2f})"
)


def instance(src: Path, loc: dict, dest: Path) -> Path:
    if dest.exists():
        return dest
    font = TTFont(src)
    out = instancer.instantiateVariableFont(font, loc, overlap=True)
    out.save(dest)
    return dest


def prepare_fonts() -> dict[str, Path]:
    files = {
        "gloock": FONT_DIR / "Gloock-Regular.ttf",
        "bellefair": FONT_DIR / "Bellefair-Regular.ttf",
        "bodoni": instance(
            FONT_DIR / "BodoniModa[opsz,wght].ttf",
            {"opsz": 96, "wght": 400},
            INST / "BodoniModa-opsz96-wght400.ttf",
        ),
        "noto": instance(
            FONT_DIR / "NotoSerifDisplay[wdth,wght].ttf",
            {"wght": 400, "wdth": 100},
            INST / "NotoSerifDisplay-wght400.ttf",
        ),
        "cinzel": instance(
            FONT_DIR / "Cinzel[wght].ttf",
            {"wght": 400},
            INST / "Cinzel-wght400.ttf",
        ),
        "fraunces": instance(
            FONT_DIR / "Fraunces[SOFT,WONK,opsz,wght].ttf",
            {"opsz": 144, "wght": 400, "SOFT": 0, "WONK": 0},
            INST / "Fraunces-opsz144-SOFT0.ttf",
        ),
        "newsreader": instance(
            FONT_DIR / "Newsreader[opsz,wght].ttf",
            {"opsz": 72, "wght": 400},
            INST / "Newsreader-opsz72-wght400.ttf",
        ),
    }
    missing = [k for k, p in files.items() if not Path(p).exists()]
    if missing:
        raise SystemExit(f"missing fonts {missing}; run the Google Fonts fetch first")
    return files


PATHS = [
    {
        "slug": "gloock",
        "font_key": "gloock",
        "text": "Waking Matter",
        "tracking": -0.03,
        "gap": GAP_04,
        "label": "Gloock",
    },
    {
        "slug": "gloock-air",
        "font_key": "gloock",
        "text": "Waking Matter",
        "tracking": -0.01,
        "gap": GAP_02,
        "label": "Gloock + 02 air",
    },
    {
        "slug": "bodoni",
        "font_key": "bodoni",
        "text": "Waking Matter",
        "tracking": -0.035,
        "gap": GAP_04,
        "label": "Bodoni Moda",
    },
    {
        "slug": "bellefair",
        "font_key": "bellefair",
        "text": "Waking Matter",
        "tracking": -0.01,
        "gap": GAP_04,
        "label": "Bellefair",
    },
    {
        "slug": "noto",
        "font_key": "noto",
        "text": "Waking Matter",
        "tracking": -0.03,
        "gap": GAP_04,
        "label": "Noto Serif Display",
    },
    {
        "slug": "cinzel",
        "font_key": "cinzel",
        "text": "WAKING MATTER",
        "tracking": 0.10,
        "gap": GAP_04,
        "label": "Cinzel caps",
    },
]

CONTROLS = [
    {
        "slug": "fraunces",
        "font_key": "fraunces",
        "text": "Waking Matter",
        "tracking": -0.03,
        "gap": GAP_04,
        "label": "Fraunces (too soft)",
    },
    {
        "slug": "newsreader",
        "font_key": "newsreader",
        "text": "Waking Matter",
        "tracking": -0.03,
        "gap": GAP_04,
        "label": "Newsreader (not a candidate)",
    },
]


def outline(font: TTFont, text: str, tracking_em: float):
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upem = font["head"].unitsPerEm
    cap = font["OS/2"].sCapHeight or font["hhea"].ascent
    x = 0.0
    glyphs = []
    for i, ch in enumerate(text):
        if ch == " ":
            space = cmap.get(ord(" "))
            x += gs[space].width if space else upem * 0.25
            continue
        name = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[name].draw(pen)
        glyphs.append((x, pen.getCommands()))
        x += gs[name].width
        if i < len(text) - 1 and text[i + 1] != " ":
            x += tracking_em * upem
    descent = max(-font["hhea"].descent, 0)
    return glyphs, x, cap, descent, upem


def mark_inner(path: Path, prefix: str) -> str:
    raw = path.read_text()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    inner = re.sub(r"\s*<title>.*?</title>\s*", "\n", inner, flags=re.S)
    inner = re.sub(r"\s*<desc>.*?</desc>\s*", "\n", inner, flags=re.S)
    # Unique gradient ids per file
    inner = inner.replace('id="m', f'id="{prefix}')
    inner = inner.replace("url(#m", f"url(#{prefix}")
    inner = inner.replace('id="vd', f'id="{prefix}')
    inner = inner.replace("url(#vd", f"url(#{prefix}")
    return inner.strip()


def type_paths(glyphs, scale: float, ty: float, x0: float, fill: str) -> str:
    parts = []
    for gx, d in glyphs:
        parts.append(
            f'  <path fill="{fill}" transform="translate({x0:.3f} {ty:.3f}) '
            f'scale({scale:.8f} {-scale:.8f}) translate({gx:.2f} 0)" d="{d}"/>'
        )
    return "\n".join(parts)


def lockup_svg(
    *,
    prefix: str,
    mark_path: Path,
    glyphs,
    width_u: float,
    cap_u: float,
    descent_u: float,
    gap: float,
    fill: str,
    label: str,
) -> str:
    scale = CAP / cap_u
    ty = Y_OFF + CAP
    type_w = width_u * scale
    wm_x = MARK_DRAW_W + gap
    vb_w = wm_x + type_w + 2
    vb_h = Y_OFF + CAP + descent_u * scale + 1.2
    mark = (
        f'  <g transform="{XFORM}">\n'
        f"{mark_inner(mark_path, prefix)}\n"
        f"  </g>\n"
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.3f} {vb_h:.3f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        f"{mark}"
        f"{type_paths(glyphs, scale, ty, wm_x, fill)}\n"
        f"</svg>\n"
    )


def wordmark_svg(glyphs, width_u, cap_u, descent_u, fill: str, label: str) -> str:
    scale = CAP / cap_u
    ty = 4 + CAP
    vb_w = width_u * scale + 8
    vb_h = 4 + CAP + descent_u * scale + 4
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.3f} {vb_h:.3f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        f"{type_paths(glyphs, scale, ty, 4.0, fill)}\n"
        f"</svg>\n"
    )


def glyphs_svg(font: TTFont, letters: str, fill: str, label: str) -> str:
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    cap = font["OS/2"].sCapHeight or font["hhea"].ascent
    descent = max(-font["hhea"].descent, 0)
    s = 72 / cap
    parts = []
    x = 12.0
    for ch in letters:
        name = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[name].draw(pen)
        w = gs[name].width * s
        parts.append(
            f'  <path fill="{fill}" transform="translate({x:.2f} {12 + 72:.2f}) '
            f'scale({s:.6f} {-s:.6f})" d="{pen.getCommands()}"/>'
        )
        x += max(w, 48) + 28
    vb_h = 12 + 72 + descent * s + 16
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x:.1f} {vb_h:.1f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        + "\n".join(parts)
        + "\n</svg>\n"
    )


def emit(spec: dict, fonts: dict[str, Path]) -> None:
    font = TTFont(fonts[spec["font_key"]])
    glyphs, width_u, cap_u, descent_u, _ = outline(font, spec["text"], spec["tracking"])
    slug = spec["slug"]
    (LOCK / f"{slug}-ivory.svg").write_text(
        lockup_svg(
            prefix=f"{slug}i",
            mark_path=LOGOS / "mark.svg",
            glyphs=glyphs,
            width_u=width_u,
            cap_u=cap_u,
            descent_u=descent_u,
            gap=spec["gap"],
            fill=VOID,
            label=f"Waking Matter, {spec['label']} on ivory",
        )
    )
    (LOCK / f"{slug}-void.svg").write_text(
        lockup_svg(
            prefix=f"{slug}v",
            mark_path=LOGOS / "mark-on-void.svg",
            glyphs=glyphs,
            width_u=width_u,
            cap_u=cap_u,
            descent_u=descent_u,
            gap=spec["gap"],
            fill=IVORY,
            label=f"Waking Matter, {spec['label']} on void",
        )
    )
    (WM / f"{slug}.svg").write_text(
        wordmark_svg(glyphs, width_u, cap_u, descent_u, VOID, spec["label"])
    )
    letters = "WAGM" if spec["text"].isupper() else "WagM"
    (GLYPH / f"{slug}.svg").write_text(
        glyphs_svg(font, letters, VOID, f"{spec['label']} W a g M")
    )
    print("wrote", slug, "cap", cap_u, "width_u", round(width_u, 1))


def main() -> None:
    fonts = prepare_fonts()
    for spec in PATHS + CONTROLS:
        emit(spec, fonts)
    print("wordmark gate SVGs", STUDY)


if __name__ == "__main__":
    main()
