#!/usr/bin/env python3
"""Three-cut logo gate — Source occupancy as law.

Study only. Does not replace brand/logos/.
Do not revive Throat, High, Catch, chrome, or the 62% Flare.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent / "marks"
OUT.mkdir(parents=True, exist_ok=True)
VB = 120

# Source occupancy (04 icon, one colour):
#   pillar 11 / gap 26.2 / height 94 / y0 13 / r 11.4
#   gap/pillar = 2.38   orb fill = 87%
PILLAR = 11.0
GAP = 26.2
HEIGHT = 94.0
Y0 = 13.0
Y1 = Y0 + HEIGHT
SPHERE_R = 11.4
CX = 60.0
CY_SOURCE = 60.0


def wrap(name, inner: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB} {VB}" '
        f'fill="none" role="img" aria-label="{name}">\n'
        f'  <g fill="currentColor">\n{inner}  </g>\n</svg>\n'
    )


def stadium(x, y, w, h, rx=None):
    if rx is None:
        rx = w / 2
    rx = min(rx, w / 2, h / 2)
    return (
        f'    <rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" '
        f'height="{h:.2f}" rx="{rx:.2f}"/>\n'
    )


def circle(cx, cy, r):
    return f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}"/>\n'


def pair(pillar_w, gap, height, y0, sphere_r, sphere_cy, rx=None):
    total = pillar_w * 2 + gap
    x0 = (VB - total) / 2
    return (
        stadium(x0, y0, pillar_w, height, rx)
        + stadium(x0 + pillar_w + gap, y0, pillar_w, height, rx)
        + circle(CX, sphere_cy, sphere_r)
    )


def tapered_outer(pillar_top, pillar_bot, gap, y0, y1, sphere_r, sphere_cy):
    """Outer edges only. Inner slit stays parallel. Round caps."""

    def pillar(out_t, in_t, out_b, in_b):
        wt = abs(in_t - out_t)
        wb = abs(in_b - out_b)
        rt, rb = wt / 2, wb / 2
        top_cx = (out_t + in_t) / 2
        bot_cx = (out_b + in_b) / 2
        poly = (
            f'    <polygon points="'
            f'{out_t:.2f},{y0 + rt:.2f} {in_t:.2f},{y0 + rt:.2f} '
            f'{in_b:.2f},{y1 - rb:.2f} {out_b:.2f},{y1 - rb:.2f}"/>\n'
        )
        return poly + circle(top_cx, y0 + rt, rt) + circle(bot_cx, y1 - rb, rb)

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
        + circle(CX, sphere_cy, sphere_r)
    )


# Parent — occupancy law. Not a candidate. Shown so the three deltas are readable.
source = pair(PILLAR, GAP, HEIGHT, Y0, SPHERE_R, CY_SOURCE)

# 1 RAISED SOURCE — identical occupancy, orb lifted off the crossbar.
raised = pair(PILLAR, GAP, HEIGHT, Y0, SPHERE_R, 51.0)

# 2 WORN SOURCE — identical occupancy, terminals rx = 0.4 × width.
# Source is half-pill (0.50). Tablet was ~0.26. This sits between.
worn = pair(PILLAR, GAP, HEIGHT, Y0, SPHERE_R, CY_SOURCE, rx=PILLAR * 0.4)

# 3 OPTICAL FLARE — inner slit parallel, outer foot +10% (not Flare’s +62%).
optical_flare = tapered_outer(
    pillar_top=PILLAR,
    pillar_bot=PILLAR * 1.10,
    gap=GAP,
    y0=Y0,
    y1=Y1,
    sphere_r=SPHERE_R,
    sphere_cy=CY_SOURCE,
)

files = {
    "0-source.svg": wrap("Source — occupancy law, not a candidate", source),
    "1-raised.svg": wrap("Raised Source — identical, orb cy 51", raised),
    "2-worn.svg": wrap("Worn Source — identical, rx 0.4 × width", worn),
    "3-optical-flare.svg": wrap(
        "Optical Flare — parallel slit, outer foot +10%", optical_flare
    ),
}

for old in OUT.glob("*.svg"):
    old.unlink()

for name, svg in files.items():
    (OUT / name).write_text(svg)
    print("wrote", name)
