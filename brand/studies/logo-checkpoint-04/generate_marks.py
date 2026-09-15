#!/usr/bin/env python3
"""Controlled one-colour refinements of the Direction 04 stadium + sphere.

Family rule: two vertical members, one suspended sphere, nothing else.
The shipped stadium is the baseline, not a freeze. These cuts only move
proportion, slit, sphere, a whisper of taper. They do not invent a new mark.

04 icon (chrome visible on void) measured:
  pillar 13, gap 31, height ~112, sphere Ø 27 (87% of gap), 2px hair
  each side, sphere on the vertical centre. Pillars are monuments, not
  letter-stems. Baseline's failure is thick stems (16 vs 11) making an H,
  not a too-small orb.

Study only. Does not replace brand/logos/.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent / "marks"
OUT.mkdir(parents=True, exist_ok=True)
VB = 120


def wrap(name, inner: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB} {VB}" '
        f'fill="none" role="img" aria-label="{name}">\n'
        f'  <g fill="currentColor">\n{inner}  </g>\n</svg>\n'
    )


def stadium(x, y, w, h, rx=None):
    if rx is None:
        rx = w / 2
    return (
        f'    <rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" '
        f'height="{h:.2f}" rx="{rx:.2f}"/>\n'
    )


def circle(cx, cy, r):
    return f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}"/>\n'


def pair(pillar_w, gap, height, y0, sphere_r, sphere_cy, rx=None):
    """Two stadiums, optically centered on 60."""
    total = pillar_w * 2 + gap
    x0 = (VB - total) / 2
    left = stadium(x0, y0, pillar_w, height, rx)
    right = stadium(x0 + pillar_w + gap, y0, pillar_w, height, rx)
    return left + right + circle(VB / 2, sphere_cy, sphere_r)


def tapered_outer(pillar_top, pillar_bot, gap, y0, y1, sphere_r, sphere_cy):
    """Whisper taper: extra mass goes to the outer edges. Inner slit stays parallel.

    Caps are true circles so this remains a stadium, not a wedge.
    """

    def pillar(out_t, in_t, out_b, in_b):
        wt = abs(in_t - out_t)
        wb = abs(in_b - out_b)
        rt, rb = wt / 2, wb / 2
        top_cx = (out_t + in_t) / 2
        bot_cx = (out_b + in_b) / 2
        # shaft: outer and inner edges between cap tangent heights
        poly = (
            f'    <polygon points="'
            f'{out_t:.2f},{y0 + rt:.2f} {in_t:.2f},{y0 + rt:.2f} '
            f'{in_b:.2f},{y1 - rb:.2f} {out_b:.2f},{y1 - rb:.2f}"/>\n'
        )
        caps = circle(top_cx, y0 + rt, rt) + circle(bot_cx, y1 - rb, rb)
        return poly + caps

    total_top = pillar_top * 2 + gap
    total_bot = pillar_bot * 2 + gap
    left_out_t = (VB - total_top) / 2
    left_in_t = left_out_t + pillar_top
    right_in_t = left_in_t + gap
    right_out_t = right_in_t + pillar_top
    left_out_b = (VB - total_bot) / 2
    left_in_b = left_out_b + pillar_bot
    right_in_b = left_in_b + gap
    right_out_b = right_in_b + pillar_bot
    return (
        pillar(left_out_t, left_in_t, left_out_b, left_in_b)
        + pillar(right_out_t, right_in_t, right_out_b, right_in_b)
        + circle(VB / 2, sphere_cy, sphere_r)
    )


# Parent for the 04-derived cuts. Slightly thicker than the 10.7 true-scale
# icon so 16px has a chance; ratio still monument, not letter.
#   04 icon:  pillar 13 / gap 31 / Ø 27 / fill 87% / height 112  (gap/p = 2.38)
#   parent:   pillar 11.5 / gap 25 / Ø 21.8 / fill 87% / height 92 (gap/p = 2.17)

# 0 BASELINE — shipped production. Mathematically neat. Useful. Not frozen.
# Thick stems (16) + centered ball = corporate H, even with a large sphere.
baseline = pair(16, 24, 88, 16, 11, 60)

# 1 OPTICAL — 04 reconstruction in one colour. Slender monuments, large
# orb occupying the doorway, still on the vertical centre like the board.
optical = pair(11.5, 25, 92, 14, 10.9, 60)

# 2 SUSPENDED — same 04 cut, sphere lifted off the letter's crossbar.
# One-colour has no chrome to say "this is an object in space"; lift is
# how the orb stays a hanging instrument rather than an H-bar.
suspended = pair(11.5, 25, 92, 14, 10.9, 49)

# 3 HELD — tighter slit, hair clearance. Compensates for lost 3D metal
# with structural tension. Sphere slightly high so it is held, not pasted.
held = pair(12, 21.6, 92, 14, 10.2, 54)

# 4 SLENDER — even more monolith. Narrower shafts, same filling orb,
# a little more height. Tests whether 04's archaeological read is mostly
# the pillar:height ratio.
slender = pair(10.4, 25.2, 96, 12, 10.9, 53)

# 5 THRESHOLD — 04 slit with a 2-unit wider foot on the outer edges only.
# Inner faces stay a parallel doorway. Ritual gate, not a menhir.
threshold = tapered_outer(
    pillar_top=11.4,
    pillar_bot=13.4,
    gap=25.0,
    y0=13.5,
    y1=107.5,
    sphere_r=10.9,
    sphere_cy=52,
)

files = {
    "0-baseline.svg": wrap("Baseline — shipped stadium construction", baseline),
    "1-optical.svg": wrap("Optical — 04 reconstruction, centred", optical),
    "2-suspended.svg": wrap("Suspended — 04 cut, sphere off the crossbar", suspended),
    "3-held.svg": wrap("Held — tighter slit, hair clearance", held),
    "4-slender.svg": wrap("Slender — narrower monolith", slender),
    "5-threshold.svg": wrap("Threshold — 04 slit plus whisper outer taper", threshold),
}

for old in OUT.glob("*.svg"):
    old.unlink()

for name, svg in files.items():
    (OUT / name).write_text(svg)
    print("wrote", name)
