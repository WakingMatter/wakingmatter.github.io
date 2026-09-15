#!/usr/bin/env python3
"""Production-candidate logo finish. Source geometry frozen in plan.

Two-value structure vs bead. No chrome, no glow, no teal.
Does not start Phase B. Independent review before freeze.

1-bit parent is members + ring: Source occupancy does not overlap, so a
boolean hole in the aperture is invisible. Never all-one-fill as parent.
Small sizes keep this geometry and use two-value fills.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # brand/
REPO = ROOT.parent
LOGOS = ROOT / "logos"
PUBLIC_BRAND = REPO / "public" / "brand"
STUDY = Path(__file__).resolve().parent / "finish"
LOGOS.mkdir(parents=True, exist_ok=True)
STUDY.mkdir(parents=True, exist_ok=True)
PUBLIC_BRAND.mkdir(parents=True, exist_ok=True)

# Source occupancy (frozen in plan)
L, Y, W, H, RX = 35.90, 13.00, 11.00, 94.00, 5.50
R_X = 73.10
CX, CY, R = 60.00, 60.00, 11.40
MARK_W = (R_X + W) - L  # 48.30
RING_SW = 2.2

VOID = "#0A0A0A"
CHARCOAL = "#2A2A2A"
IVORY = "#F7F6F3"
MIST = "#D6D9D7"
# Mist darkened toward charcoal — matte stone, not metal
STONE = "#7A7F7C"
# Darker matte bead on void — distinct from Mist members and from Void ground
BEAD_DARK = "#4E5451"

MEMBERS = (
    f'<rect x="{L:.2f}" y="{Y:.2f}" width="{W:.2f}" height="{H:.2f}" rx="{RX:.2f}"/>\n'
    f'<rect x="{R_X:.2f}" y="{Y:.2f}" width="{W:.2f}" height="{H:.2f}" rx="{RX:.2f}"/>'
)
BEAD = f'<circle cx="{CX:.2f}" cy="{CY:.2f}" r="{R:.2f}"/>'


def ring(stroke: str, sw: float = RING_SW) -> str:
    return (
        f'<circle cx="{CX:.2f}" cy="{CY:.2f}" r="{R:.2f}" '
        f'fill="none" stroke="{stroke}" stroke-width="{sw:.2f}"/>'
    )


def svg(inner: str, label: str, vb: str = "0 0 120 120") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" '
        f'role="img" aria-label="{label}">\n{inner}</svg>\n'
    )


def two_value(member_fill: str, bead_fill: str, ground: str | None = None, label: str = "") -> str:
    g = f'  <rect width="100%" height="100%" fill="{ground}"/>\n' if ground else ""
    return svg(
        g
        + f'  <g fill="{member_fill}">\n    {MEMBERS}\n  </g>\n'
        + f'  <g fill="{bead_fill}">\n    {BEAD}\n  </g>\n',
        label,
    )


def one_bit(label: str, ground: str | None = None, ink: str = "currentColor") -> str:
    g = f'  <rect width="100%" height="100%" fill="{ground}"/>\n' if ground else ""
    fill_attr = f' fill="{ink}"'
    return svg(
        g
        + f"  <g{fill_attr}>\n    {MEMBERS}\n  </g>\n"
        + f"  {ring(ink)}\n",
        label,
    )


files: dict[str, str] = {}

files["mark.svg"] = svg(
    "  <title>Waking Matter mark</title>\n"
    "  <desc>Two stadium members (structure) and a ring bead (matter). "
    "Never a single fill.</desc>\n"
    f'  <g fill="currentColor">\n    {MEMBERS}\n  </g>\n'
    f"  {ring('currentColor')}\n",
    "Waking Matter mark",
)

files["mark-mono.svg"] = one_bit("Waking Matter mark, one-bit")

files["mark-on-ivory.svg"] = two_value(
    VOID, STONE, label="Waking Matter mark on ivory"
)

files["mark-on-void.svg"] = two_value(
    MIST, BEAD_DARK, label="Waking Matter mark on void"
)

# Small-size: same geometry, two-value, not a thickened parent
files["mark-small.svg"] = two_value(
    VOID, STONE, label="Waking Matter mark, small sizes"
)

files["favicon.svg"] = two_value(
    VOID, STONE, ground=IVORY, label="Waking Matter"
)

# App icon: Source geometry scaled into 512, two-value, no chrome
s = 300 / 94
tx, ty = 256 - CX * s, 256 - CY * s
files["icon-app.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none" role="img" aria-label="Waking Matter app icon">
  <rect width="512" height="512" rx="112" fill="{VOID}"/>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})">
    <g fill="{MIST}">
      {MEMBERS}
    </g>
    <g fill="{BEAD_DARK}">
      {BEAD}
    </g>
  </g>
</svg>
'''

files["icon-app-mono.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none" role="img" aria-label="Waking Matter monochrome app icon">
  <rect width="512" height="512" rx="112" fill="{VOID}"/>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})" fill="{IVORY}">
    {MEMBERS}
  </g>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})">
    {ring(IVORY)}
  </g>
</svg>
'''

files["construction.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" fill="none" role="img" aria-label="Mark construction grid">
  <rect width="360" height="200" fill="{IVORY}"/>
  <g stroke="{MIST}" stroke-width="0.5">
    <line x1="40" y1="20" x2="40" y2="180"/>
    <line x1="80" y1="20" x2="80" y2="180"/>
    <line x1="120" y1="20" x2="120" y2="180"/>
    <line x1="160" y1="20" x2="160" y2="180"/>
    <line x1="200" y1="20" x2="200" y2="180"/>
    <line x1="240" y1="20" x2="240" y2="180"/>
    <line x1="20" y1="40" x2="260" y2="40"/>
    <line x1="20" y1="80" x2="260" y2="80"/>
    <line x1="20" y1="100" x2="260" y2="100"/>
    <line x1="20" y1="120" x2="260" y2="120"/>
    <line x1="20" y1="160" x2="260" y2="160"/>
  </g>
  <g transform="translate(80 40) scale(1.2766) translate(-35.9 -13)">
    <g fill="{VOID}">{MEMBERS}</g>
    <g fill="{STONE}">{BEAD}</g>
  </g>
  <g font-family="ui-monospace, monospace" font-size="9" fill="{CHARCOAL}">
    <text x="80" y="34">11</text>
    <text x="128" y="34">26.2</text>
    <text x="176" y="34">11</text>
    <text x="272" y="52">height 94</text>
    <text x="272" y="108">sphere r 11.4</text>
    <text x="272" y="128">two-value: structure / bead</text>
    <text x="272" y="164">1-bit: members + ring</text>
  </g>
</svg>
'''

# Lockups: Source mark aligned to Newsreader cap height. Type is not frozen;
# Fraunces remains the inscriptional candidate. SVG paths stay Newsreader.
wm_src = (LOGOS / "wordmark.svg").read_text()
wm_match = re.search(r'<path[^>]*\sd="([^"]+)"', wm_src)
if not wm_match:
    raise SystemExit("wordmark path missing")
WM_D = wm_match.group(1)
CAP = 52.2
SCALE = CAP / H
Y_OFF = 1.944
GAP = 0.38 * CAP
MARK_DRAW_W = MARK_W * SCALE
WM_X = MARK_DRAW_W + GAP
WM_PATH_W = 487.872
VB_W = WM_X + WM_PATH_W
VB_H = 70.164
XFORM = (
    f"translate(0, {Y_OFF}) scale({SCALE:.12f}) "
    f"translate({-L:.2f}, {-Y:.2f})"
)


def lockup_svg(
    *,
    members_fill: str,
    bead_fill: str | None,
    bead_ring: bool,
    word_fill: str,
    label: str,
) -> str:
    if bead_ring:
        bead_el = f"    {ring(members_fill)}\n"
    else:
        bead_el = f'    <g fill="{bead_fill}">{BEAD}</g>\n'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W:.3f} {VB_H:.3f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        f'  <g transform="{XFORM}">\n'
        f'    <g fill="{members_fill}">\n      {MEMBERS}\n    </g>\n'
        f"{bead_el}"
        f"  </g>\n"
        f'  <path fill="{word_fill}" transform="translate({WM_X:.3f}, 0)" d="{WM_D}"/>\n'
        f"</svg>\n"
    )


files["lockup.svg"] = lockup_svg(
    members_fill="currentColor",
    bead_fill=None,
    bead_ring=True,
    word_fill="currentColor",
    label="Waking Matter",
)
files["lockup-mono.svg"] = files["lockup.svg"]
files["lockup-on-ivory.svg"] = lockup_svg(
    members_fill=VOID,
    bead_fill=STONE,
    bead_ring=False,
    word_fill=VOID,
    label="Waking Matter",
)
files["lockup-on-void.svg"] = lockup_svg(
    members_fill=MIST,
    bead_fill=BEAD_DARK,
    bead_ring=False,
    word_fill=IVORY,
    label="Waking Matter",
)

# Study-only rejected parent: one fill of members + bead (the corporate H)
STUDY.mkdir(parents=True, exist_ok=True)
rejected = svg(
    f'  <g fill="currentColor">\n    {MEMBERS}\n    {BEAD}\n  </g>\n',
    "Rejected one-fill parent",
)
(STUDY / "rejected-one-fill.svg").write_text(rejected)

PUBLIC_FILES = [
    "mark.svg",
    "mark-mono.svg",
    "mark-on-ivory.svg",
    "mark-on-void.svg",
    "mark-small.svg",
    "lockup.svg",
    "lockup-mono.svg",
    "lockup-on-ivory.svg",
    "lockup-on-void.svg",
    "icon-app.svg",
    "icon-app-mono.svg",
]

for name, contents in files.items():
    (LOGOS / name).write_text(contents)
    (STUDY / name).write_text(contents)
    print("wrote", name)

for name in PUBLIC_FILES:
    shutil.copy2(LOGOS / name, PUBLIC_BRAND / name)
    print("public", name)

shutil.copy2(LOGOS / "favicon.svg", REPO / "public" / "favicon.svg")
print("public favicon.svg")

print("geometry L,Y,W,H,RX", L, Y, W, H, RX, "R_X", R_X, "circle", CX, CY, R)
print("gap", R_X - L - W, "fill", 2 * R / (R_X - L - W))
print("lockup scale", SCALE, "mark_w", MARK_DRAW_W, "wm_x", WM_X, "vb", VB_W, VB_H)
