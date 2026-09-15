#!/usr/bin/env python3
"""Direction 04 mark family — study only, does not replace brand/logos/.

Six one-colour refinements of two vertical members + one suspended sphere.
Visually distinct from each other. Tightly related to the 04 board.
The shipped stadium+centred-sphere is a rejected baseline, not a candidate.
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
    rx = min(rx, w / 2, h / 2)
    return (
        f'    <rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" '
        f'height="{h:.2f}" rx="{rx:.2f}"/>\n'
    )


def circle(cx, cy, r):
    return f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}"/>\n'


def pair(pillar_w, gap, height, y0, sphere_r, sphere_cy, rx=None, cx=None):
    total = pillar_w * 2 + gap
    x0 = (VB - total) / 2
    if cx is None:
        cx = VB / 2
    return (
        stadium(x0, y0, pillar_w, height, rx)
        + stadium(x0 + pillar_w + gap, y0, pillar_w, height, rx)
        + circle(cx, sphere_cy, sphere_r)
    )


def two_members(
    left_w,
    right_w,
    gap,
    left_y0,
    left_h,
    right_y0,
    right_h,
    sphere_r,
    sphere_cx,
    sphere_cy,
    left_rx=None,
    right_rx=None,
):
    """Asymmetric pair. Optical centre is not assumed."""
    total = left_w + gap + right_w
    x0 = (VB - total) / 2
    return (
        stadium(x0, left_y0, left_w, left_h, left_rx)
        + stadium(x0 + left_w + gap, right_y0, right_w, right_h, right_rx)
        + circle(sphere_cx, sphere_cy, sphere_r)
    )


def tapered_outer(pillar_top, pillar_bot, gap, y0, y1, sphere_r, sphere_cy, cx=None):
    """Outer edges flare to the foot. Inner slit stays parallel. Round caps."""

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
    if cx is None:
        cx = VB / 2
    return (
        pillar(left_out_t, left_in_t, left_out_b, left_in_b)
        + pillar(right_out_t, right_in_t, right_out_b, right_in_b)
        + circle(cx, sphere_cy, sphere_r)
    )


def throat(pillar_w, gap_end, gap_waist, y0, y1, sphere_r, sphere_cy):
    """Outer edges vertical. Inner faces pinch at the orb. Aperture, not a pocket."""
    total = pillar_w * 2 + gap_end
    x0 = (VB - total) / 2
    inset = (gap_end - gap_waist) / 2
    rt = pillar_w / 2
    left_out = x0
    left_in_end = x0 + pillar_w
    left_in_w = left_in_end + inset
    right_out = x0 + total
    right_in_end = right_out - pillar_w
    right_in_w = right_in_end - inset
    y_w = sphere_cy

    def member(out, in_end, in_w, left):
        # shaft: outer vertical, inner with a waist
        if left:
            pts = (
                f"{out:.2f},{y0 + rt:.2f} {in_end:.2f},{y0 + rt:.2f} "
                f"{in_w:.2f},{y_w:.2f} {in_end:.2f},{y1 - rt:.2f} "
                f"{out:.2f},{y1 - rt:.2f}"
            )
            top_cx = out + rt
            bot_cx = out + rt
        else:
            pts = (
                f"{out:.2f},{y0 + rt:.2f} {in_end:.2f},{y0 + rt:.2f} "
                f"{in_w:.2f},{y_w:.2f} {in_end:.2f},{y1 - rt:.2f} "
                f"{out:.2f},{y1 - rt:.2f}"
            )
            top_cx = out - rt
            bot_cx = out - rt
        return (
            f'    <polygon points="{pts}"/>\n'
            + circle(top_cx, y0 + rt, rt)
            + circle(bot_cx, y1 - rt, rt)
        )

    return (
        member(left_out, left_in_end, left_in_w, True)
        + member(right_out, right_in_end, right_in_w, False)
        + circle(VB / 2, sphere_cy, sphere_r)
    )


# --- 0 CONTROL : shipped. Not approved. Shown so the H is visible. ---
control = pair(16, 24, 88, 16, 11, 60)

# --- 1 SOURCE : closest to the 04 image. Do not over-rationalise. ---
# 04 icon: pillar 13 / gap 31 / Ø 27 / fill 87% / height 112 / sphere centred.
# Scale into 120: keep parallel full-round stadiums, large orb, dead centre.
source = pair(11.0, 26.2, 94, 13, 11.4, 60)

# --- 2 FLARE : threshold / standing stone. Outer foot is visibly wider. ---
flare = tapered_outer(
    pillar_top=10.0,
    pillar_bot=16.2,
    gap=25.5,
    y0=11.5,
    y1=108.5,
    sphere_r=10.8,
    sphere_cy=50,
)

# --- 3 THROAT : ritual aperture. Slit pinches; sphere is held there. ---
throat_cut = throat(
    pillar_w=11.4,
    gap_end=28.0,
    gap_waist=21.2,
    y0=12.5,
    y1=107.5,
    sphere_r=10.1,
    sphere_cy=52,
)

# --- 4 ASYM : recovered, not machine-perfect. Quiet L/R imbalance. ---
# Heavier left member, sphere pulled toward it and slightly high.
asym = two_members(
    left_w=12.8,
    right_w=10.2,
    gap=24.6,
    left_y0=12.5,
    left_h=95,
    right_y0=14.5,
    right_h=91,
    sphere_r=10.6,
    sphere_cx=58.6,
    sphere_cy=51,
)

# --- 5 TABLET : worn caps. Not UI pills. Cut-stone terminals. ---
tablet = pair(11.2, 25.8, 94, 13, 11.0, 54, rx=2.9)

# --- 6 HIGH : long ritual void below a clearly suspended orb. ---
high = pair(10.6, 26.0, 98, 11, 11.0, 46)

files = {
    "0-control.svg": wrap("Control — shipped stadium H, not approved", control),
    "1-source.svg": wrap("Source — closest one-colour of Direction 04", source),
    "2-flare.svg": wrap("Flare — standing threshold, outer foot wider", flare),
    "3-throat.svg": wrap("Throat — slit pinches; sphere held at the waist", throat_cut),
    "4-asym.svg": wrap("Asym — quiet recovered imbalance", asym),
    "5-tablet.svg": wrap("Tablet — worn caps, not extruded pills", tablet),
    "6-high.svg": wrap("High — orb suspended over a long slit", high),
}

for old in OUT.glob("*.svg"):
    old.unlink()

for name, svg in files.items():
    (OUT / name).write_text(svg)
    print("wrote", name)
