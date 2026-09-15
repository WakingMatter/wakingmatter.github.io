#!/usr/bin/env python3
"""Logo finish pass 3. Source geometry frozen in plan.

Wider slot-facing inner plane; bead is the object in the slot on both
grounds (brighter matte pole; void pole lighter than the column).
No chrome tubes, no glow, no teal. 1-bit members+ring is mono fallback
only. Type not frozen.

Shipping lockups keep Newsreader outlines (type not frozen).
Candidate lockups this pass outline Fraunces (opsz 144, SOFT 0).
Does not start Phase B.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]  # brand/
REPO = ROOT.parent
LOGOS = ROOT / "logos"
PUBLIC_BRAND = REPO / "public" / "brand"
STUDY = Path(__file__).resolve().parent / "finish"
FRAUNCES = Path("/tmp/fraunces/Fraunces-opsz144-SOFT0.ttf")
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
# Inner plane ~40% of pillar, slot-facing. Distinct value, not a chrome roll.
IVORY_INNER = CHARCOAL
VOID_INNER = MIST
VOID_OUTER = "#8E928F"

# Bead: pewter body/terminator kept; brighter matte pole. Void pole lighter
# than the column so the bead is the object in the slot, not a hole.
IVORY_POLE = "#B8BCBA"
IVORY_BODY = "#3A3E3C"
IVORY_TERM = "#1A1C1B"
VOID_POLE = "#E2E4E1"
VOID_BODY = "#3A3E3C"
VOID_TERM = "#1A1C1B"

# Column: outer plane then inner plane. Short join, no vertical metal.
COL_L_OUTER_END = "0.58"
COL_L_INNER_START = "0.62"
COL_R_INNER_END = "0.38"
COL_R_OUTER_START = "0.42"

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


def modeled(
    prefix: str,
    *,
    outer: str,
    inner: str,
    pole: str,
    body: str,
    term: str,
    ground: str | None = None,
    label: str,
    title: str | None = None,
    desc: str | None = None,
) -> str:
    g = f'  <rect width="100%" height="100%" fill="{ground}"/>\n' if ground else ""
    head = ""
    if title:
        head += f"  <title>{title}</title>\n"
    if desc:
        head += f"  <desc>{desc}</desc>\n"
    defs = defs_block(prefix, outer, inner, pole, body, term)
    body_el = (
        f'  <rect x="{L:.2f}" y="{Y:.2f}" width="{W:.2f}" height="{H:.2f}" '
        f'rx="{RX:.2f}" fill="url(#{prefix}ColL)"/>\n'
        f'  <rect x="{R_X:.2f}" y="{Y:.2f}" width="{W:.2f}" height="{H:.2f}" '
        f'rx="{RX:.2f}" fill="url(#{prefix}ColR)"/>\n'
        f'  <circle cx="{CX:.2f}" cy="{CY:.2f}" r="{R:.2f}" fill="url(#{prefix}Bead)"/>\n'
    )
    return svg(head + defs + g + body_el, label)


def one_bit(label: str, ground: str | None = None, ink: str = "currentColor") -> str:
    g = f'  <rect width="100%" height="100%" fill="{ground}"/>\n' if ground else ""
    return svg(
        g
        + f'  <g fill="{ink}">\n    {MEMBERS}\n  </g>\n'
        + f"  {ring(ink)}\n",
        label,
    )


def modeled_group(prefix: str) -> str:
    return (
        f'  <rect x="{L:.2f}" y="{Y:.2f}" width="{W:.2f}" height="{H:.2f}" '
        f'rx="{RX:.2f}" fill="url(#{prefix}ColL)"/>\n'
        f'  <rect x="{R_X:.2f}" y="{Y:.2f}" width="{W:.2f}" height="{H:.2f}" '
        f'rx="{RX:.2f}" fill="url(#{prefix}ColR)"/>\n'
        f'  <circle cx="{CX:.2f}" cy="{CY:.2f}" r="{R:.2f}" fill="url(#{prefix}Bead)"/>\n'
    )


def defs_block(prefix: str, outer: str, inner: str, pole: str, body: str, term: str) -> str:
    return f'''  <defs>
    <linearGradient id="{prefix}ColL" x1="{L:.2f}" y1="{Y:.2f}" x2="{L + W:.2f}" y2="{Y:.2f}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{outer}"/>
      <stop offset="{COL_L_OUTER_END}" stop-color="{outer}"/>
      <stop offset="{COL_L_INNER_START}" stop-color="{inner}"/>
      <stop offset="1" stop-color="{inner}"/>
    </linearGradient>
    <linearGradient id="{prefix}ColR" x1="{R_X:.2f}" y1="{Y:.2f}" x2="{R_X + W:.2f}" y2="{Y:.2f}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{inner}"/>
      <stop offset="{COL_R_INNER_END}" stop-color="{inner}"/>
      <stop offset="{COL_R_OUTER_START}" stop-color="{outer}"/>
      <stop offset="1" stop-color="{outer}"/>
    </linearGradient>
    <radialGradient id="{prefix}Bead" cx="34%" cy="28%" r="72%">
      <stop offset="0" stop-color="{pole}"/>
      <stop offset="0.36" stop-color="{body}"/>
      <stop offset="1" stop-color="{term}"/>
    </radialGradient>
  </defs>
'''


files: dict[str, str] = {}

IVORY_ARGS = dict(
    outer=VOID,
    inner=IVORY_INNER,
    pole=IVORY_POLE,
    body=IVORY_BODY,
    term=IVORY_TERM,
)
VOID_ARGS = dict(
    outer=VOID_OUTER,
    inner=VOID_INNER,
    pole=VOID_POLE,
    body=VOID_BODY,
    term=VOID_TERM,
)

files["mark.svg"] = modeled(
    "m",
    **IVORY_ARGS,
    label="Waking Matter mark",
    title="Waking Matter mark",
    desc="Two stadium columns around a slot, and a modelled pewter bead. "
    "Never a single fill. 1-bit ring lives in mark-mono.svg.",
)

files["mark-on-ivory.svg"] = modeled(
    "iv", **IVORY_ARGS, label="Waking Matter mark on ivory"
)

files["mark-on-void.svg"] = modeled(
    "vd", **VOID_ARGS, label="Waking Matter mark on void"
)

files["mark-small.svg"] = modeled(
    "sm", **IVORY_ARGS, label="Waking Matter mark, small sizes"
)

files["favicon.svg"] = modeled(
    "fk", **IVORY_ARGS, ground=IVORY, label="Waking Matter"
)

files["mark-mono.svg"] = one_bit("Waking Matter mark, one-bit fallback")

# App icon: same Source geometry, placed larger toward 04 occupancy.
# Parent occupancy unchanged. Height 348 / 512 (was 300).
ICON_H = 348.0
s = ICON_H / H
tx, ty = 256 - CX * s, 256 - CY * s
files["icon-app.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none" role="img" aria-label="Waking Matter app icon">
  <rect width="512" height="512" rx="112" fill="{VOID}"/>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})">
{defs_block("ic", **VOID_ARGS)}{modeled_group("ic")}  </g>
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
{defs_block("cn", **IVORY_ARGS)}{modeled_group("cn")}  </g>
  <g font-family="ui-monospace, monospace" font-size="9" fill="{CHARCOAL}">
    <text x="80" y="34">11</text>
    <text x="128" y="34">26.2</text>
    <text x="176" y="34">11</text>
    <text x="272" y="52">height 94</text>
    <text x="272" y="108">sphere r 11.4</text>
    <text x="272" y="128">bead: pole / body / terminator</text>
    <text x="272" y="148">members: inner-edge step</text>
    <text x="272" y="168">1-bit: members + ring (mono)</text>
  </g>
</svg>
'''

# Shipping lockups: Newsreader outlines, type not frozen.
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


def lockup_newsreader(*, prefix: str, modeled_mark: bool, void: bool, word_fill: str, label: str) -> str:
    if modeled_mark:
        args = VOID_ARGS if void else IVORY_ARGS
        mark = (
            f'  <g transform="{XFORM}">\n'
            f"{defs_block(prefix, **args)}"
            f"{modeled_group(prefix)}"
            f"  </g>\n"
        )
    else:
        mark = (
            f'  <g transform="{XFORM}" fill="{word_fill}">\n'
            f"    {MEMBERS}\n"
            f"    {ring(word_fill)}\n"
            f"  </g>\n"
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W:.3f} {VB_H:.3f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        f"{mark}"
        f'  <path fill="{word_fill}" transform="translate({WM_X:.3f}, 0)" d="{WM_D}"/>\n'
        f"</svg>\n"
    )


files["lockup.svg"] = lockup_newsreader(
    prefix="lk", modeled_mark=True, void=False, word_fill=VOID, label="Waking Matter"
)
files["lockup-on-ivory.svg"] = lockup_newsreader(
    prefix="lki", modeled_mark=True, void=False, word_fill=VOID, label="Waking Matter"
)
files["lockup-on-void.svg"] = lockup_newsreader(
    prefix="lkv", modeled_mark=True, void=True, word_fill=IVORY, label="Waking Matter"
)
files["lockup-mono.svg"] = lockup_newsreader(
    prefix="lkm",
    modeled_mark=False,
    void=False,
    word_fill="currentColor",
    label="Waking Matter, one-bit",
)


def outline_fraunces(text: str, tracking_em: float = -0.03):
    font = TTFont(FRAUNCES)
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upem = font["head"].unitsPerEm
    cap = font["OS/2"].sCapHeight
    x = 0.0
    glyphs = []
    for i, ch in enumerate(text):
        if ch == " ":
            x += gs[cmap[ord(" ")]].width
            continue
        name = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[name].draw(pen)
        glyphs.append((x, pen.getCommands()))
        x += gs[name].width
        if i < len(text) - 1 and text[i + 1] != " ":
            x += tracking_em * upem
    descent = -font["hhea"].descent
    return glyphs, x, cap, descent, upem


def lockup_fraunces(*, prefix: str, void: bool, word_fill: str, label: str) -> str:
    glyphs, width_u, cap_u, descent_u, upem = outline_fraunces("Waking Matter")
    scale = CAP / cap_u
    args = VOID_ARGS if void else IVORY_ARGS
    # Cap top at Y_OFF, baseline at Y_OFF+CAP. Flip y for SVG.
    ty = Y_OFF + CAP
    parts = []
    for gx, d in glyphs:
        parts.append(
            f'  <path fill="{word_fill}" transform="translate({WM_X:.3f} {ty:.3f}) '
            f'scale({scale:.8f} {-scale:.8f}) translate({gx:.2f} 0)" d="{d}"/>'
        )
    type_w = width_u * scale
    vb_w = WM_X + type_w + 2
    vb_h = Y_OFF + CAP + descent_u * scale + 1.2
    mark = (
        f'  <g transform="{XFORM}">\n'
        f"{defs_block(prefix, **args)}"
        f"{modeled_group(prefix)}"
        f"  </g>\n"
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.3f} {vb_h:.3f}" '
        f'fill="none" role="img" aria-label="{label}">\n'
        f"{mark}"
        + "\n".join(parts)
        + "\n</svg>\n"
    )


files["lockup-fraunces-ivory.svg"] = lockup_fraunces(
    prefix="fi", void=False, word_fill=VOID, label="Waking Matter, Fraunces candidate"
)
files["lockup-fraunces-void.svg"] = lockup_fraunces(
    prefix="fv", void=True, word_fill=IVORY, label="Waking Matter, Fraunces candidate"
)

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

STUDY_ONLY = {"lockup-fraunces-ivory.svg", "lockup-fraunces-void.svg"}

for name, contents in files.items():
    if name not in STUDY_ONLY:
        (LOGOS / name).write_text(contents)
    (STUDY / name).write_text(contents)
    print("wrote", name)

for name in PUBLIC_FILES:
    shutil.copy2(LOGOS / name, PUBLIC_BRAND / name)
    print("public", name)

shutil.copy2(LOGOS / "favicon.svg", REPO / "public" / "favicon.svg")
print("public favicon.svg")

print("geometry L,Y,W,H,RX", L, Y, W, H, RX, "R_X", R_X, "circle", CX, CY, R)
print("icon scale", s, "height", ICON_H, "tx,ty", tx, ty)
print("lockup scale", SCALE, "mark_w", MARK_DRAW_W, "wm_x", WM_X)
