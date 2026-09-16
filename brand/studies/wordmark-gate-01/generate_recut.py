#!/usr/bin/env python3
"""Type revise: one Gloock-derived outlined recut.

Geometry/finish frozen. No zoo. No spacing-only second Gloock.
Gloock Regular is the structural parent; this recut is narrower and
less inky, with a contained closed g. Mixed-case, 04-tight gap.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from fontTools.pens.basePen import BasePen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_wordmark import (  # noqa: E402
    CAP,
    GAP_04,
    GLYPH,
    IVORY,
    LOCK,
    LOGOS,
    STUDY,
    VOID,
    WM,
    lockup_svg,
    type_paths,
    wordmark_svg,
)

FONT = Path("/tmp/wm-type/Gloock-Regular.ttf")
SLUG = "gloock-recut"
TEXT = "Waking Matter"
TRACKING = -0.03  # 04-tight
# Horizontal scale: thins vertical (inky) stems and narrows the word.
SX = 0.85
# g: pull the descender loop toward the join; retract the ear.
G_JOIN_Y = 118.0
G_LOOP_CX = 268.0
G_LOOP = 0.66
G_LOOP_X = 0.84
G_EAR_X = 384.0
G_EAR = 0.18


class RecutPen(BasePen):
    def __init__(self, glyphSet, fn, out):
        super().__init__(glyphSet)
        self.fn = fn
        self.out = out

    def _moveTo(self, pt):
        self.out.moveTo(self.fn(pt))

    def _lineTo(self, pt):
        self.out.lineTo(self.fn(pt))

    def _curveToOne(self, p1, p2, p3):
        self.out.curveTo(self.fn(p1), self.fn(p2), self.fn(p3))

    def _qCurveToOne(self, p1, p2):
        self.out.qCurveTo(self.fn(p1), self.fn(p2))

    def _closePath(self):
        self.out.closePath()

    def _endPath(self):
        if hasattr(self.out, "endPath"):
            self.out.endPath()


def recut_point(ch: str, pt: tuple[float, float]) -> tuple[float, float]:
    x, y = pt
    if ch == "g":
        if y < G_JOIN_Y:
            y = G_JOIN_Y + (y - G_JOIN_Y) * G_LOOP
            x = G_LOOP_CX + (x - G_LOOP_CX) * G_LOOP_X
        if y > 458 and x > G_EAR_X:
            x = G_EAR_X + (x - G_EAR_X) * G_EAR
    return (x * SX, y)


def glyph_path(gs, cmap, ch: str) -> tuple[str, float]:
    name = cmap[ord(ch)]
    src = gs[name]
    svg_pen = SVGPathPen(gs)
    src.draw(RecutPen(gs, lambda pt, c=ch: recut_point(c, pt), svg_pen))
    return svg_pen.getCommands(), src.width * SX


def outline_recut(font: TTFont, text: str, tracking_em: float):
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upem = font["head"].unitsPerEm
    cap = font["OS/2"].sCapHeight or font["hhea"].ascent
    x = 0.0
    glyphs = []
    min_y = 0.0
    for i, ch in enumerate(text):
        if ch == " ":
            space = cmap.get(ord(" "))
            adv = (gs[space].width if space else upem * 0.25) * SX
            x += adv
            continue
        d, w = glyph_path(gs, cmap, ch)
        glyphs.append((x, d))
        bp = BoundsPen(gs)
        gs[cmap[ord(ch)]].draw(RecutPen(gs, lambda pt, c=ch: recut_point(c, pt), bp))
        if bp.bounds:
            min_y = min(min_y, bp.bounds[1])
        x += w
        if i < len(text) - 1 and text[i + 1] != " ":
            x += tracking_em * upem * SX
    descent = max(-min_y, 0)
    return glyphs, x, cap, descent, upem


def glyphs_card(font: TTFont, letters: str, fill: str, label: str) -> str:
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    cap = font["OS/2"].sCapHeight or font["hhea"].ascent
    s = 72 / cap
    parts = []
    x = 12.0
    min_y = 0.0
    for ch in letters:
        d, w = glyph_path(gs, cmap, ch)
        bp = BoundsPen(gs)
        gs[cmap[ord(ch)]].draw(RecutPen(gs, lambda pt, c=ch: recut_point(c, pt), bp))
        if bp.bounds:
            min_y = min(min_y, bp.bounds[1])
        parts.append(
            f'  <path fill="{fill}" transform="translate({x:.2f} {12 + 72:.2f}) '
            f'scale({s:.6f} {-s:.6f})" d="{d}"/>'
        )
        x += max(w * s, 48) + 28
    vb_h = 12 + 72 + max(-min_y, 0) * s + 16
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x:.1f} {vb_h:.1f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        + "\n".join(parts)
        + "\n</svg>\n"
    )


def main() -> None:
    if not FONT.exists():
        raise SystemExit("missing Gloock; run fetch_fonts.sh")
    font = TTFont(FONT)
    glyphs, width_u, cap_u, descent_u, _ = outline_recut(font, TEXT, TRACKING)
    (LOCK / f"{SLUG}-ivory.svg").write_text(
        lockup_svg(
            prefix=f"{SLUG}i",
            mark_path=LOGOS / "mark.svg",
            glyphs=glyphs,
            width_u=width_u,
            cap_u=cap_u,
            descent_u=descent_u,
            gap=GAP_04,
            fill=VOID,
            label="Waking Matter, Gloock recut on ivory",
        )
    )
    (LOCK / f"{SLUG}-void.svg").write_text(
        lockup_svg(
            prefix=f"{SLUG}v",
            mark_path=LOGOS / "mark-on-void.svg",
            glyphs=glyphs,
            width_u=width_u,
            cap_u=cap_u,
            descent_u=descent_u,
            gap=GAP_04,
            fill=IVORY,
            label="Waking Matter, Gloock recut on void",
        )
    )
    (WM / f"{SLUG}.svg").write_text(
        wordmark_svg(glyphs, width_u, cap_u, descent_u, VOID, "Gloock recut")
    )
    (GLYPH / f"{SLUG}.svg").write_text(
        glyphs_card(font, "WagM", VOID, "Gloock recut W a g M")
    )
    print(
        "wrote",
        SLUG,
        "sx",
        SX,
        "cap",
        cap_u,
        "width_u",
        round(width_u, 1),
        "descent",
        round(descent_u, 1),
        "gap",
        GAP_04,
    )


if __name__ == "__main__":
    main()
