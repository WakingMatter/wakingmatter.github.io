#!/usr/bin/env python3
"""One-color mark studies for the Direction 04 checkpoint.

These geometries are for the study board only. They do not replace
brand/logos production masters.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent / "marks"
OUT.mkdir(parents=True, exist_ok=True)

VB = 120


def wrap(name, inner: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB} {VB}" fill="none" role="img" aria-label="{name}">
  <g fill="currentColor">
{inner}
  </g>
</svg>
'''


def circle(cx, cy, r):
    return f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}"/>'


# ---------------------------------------------------------------------------
# CONTROL — current production (stadium + centered sphere). Not a candidate.
# ---------------------------------------------------------------------------
control = """    <rect x="32" y="16" width="16" height="88" rx="8"/>
    <rect x="72" y="16" width="16" height="88" rx="8"/>
    <circle cx="60" cy="60" r="11"/>"""


# ---------------------------------------------------------------------------
# A RELIC — closest reconstruction of the 04 board in one colour.
# Parallel outer edges, slight inner scoop around a large sphere sitting
# a little above geometric centre. Caps are columns, not cartoon pills:
# the end radius is less than half the shaft width. Gap ≈ shaft width.
# ---------------------------------------------------------------------------
def relic():
    # Outer edges bow in 1.2 units (worn shaft, not a stadium).
    # Inner edges scoop 3.5 units toward the sphere. Gap at the waist
    # is only a hair wider than the sphere — 04's fill-the-aperture read.
    left = """    <path d="M34.2 21.0
      C34.2 16.0 37.8 13.5 41.2 13.5
      C44.6 13.5 47.8 16.0 47.8 21.0
      C47.8 30.0 49.6 41.0 50.4 54.0
      C49.6 67.0 47.8 80.0 47.8 99.0
      C47.8 104.0 44.6 106.5 41.2 106.5
      C37.8 106.5 34.2 104.0 34.2 99.0
      C33.0 80.0 33.0 40.0 34.2 21.0
      Z"/>"""
    right = """    <path d="M85.8 21.0
      C85.8 16.0 82.2 13.5 78.8 13.5
      C75.4 13.5 72.2 16.0 72.2 21.0
      C72.2 30.0 70.4 41.0 69.6 54.0
      C70.4 67.0 72.2 80.0 72.2 99.0
      C72.2 104.0 75.4 106.5 78.8 106.5
      C82.2 106.5 85.8 104.0 85.8 99.0
      C87.0 80.0 87.0 40.0 85.8 21.0
      Z"/>"""
    return left + "\n" + right + "\n" + circle(60, 54, 9.4)


# ---------------------------------------------------------------------------
# B THROAT — aperture pinches; sphere is held at the narrowest point.
# Top and bottom flare open. The sphere cannot slide without deforming
# the throat. This is the tension variant.
# ---------------------------------------------------------------------------
def throat():
    left = """    <path d="M30.0 23.0
      C30.0 16.8 34.8 13.0 40.2 13.0
      C45.4 13.0 49.0 16.6 49.0 23.0
      C49.0 32.0 52.6 42.0 53.2 52.5
      C52.6 63.0 49.0 74.0 49.0 97.0
      C49.0 103.4 45.2 107.0 40.2 107.0
      C34.8 107.0 30.0 103.2 30.0 97.0
      Z"/>"""
    right = """    <path d="M90.0 23.0
      C90.0 16.8 85.2 13.0 79.8 13.0
      C74.6 13.0 71.0 16.6 71.0 23.0
      C71.0 32.0 67.4 42.0 66.8 52.5
      C67.4 63.0 71.0 74.0 71.0 97.0
      C71.0 103.4 74.8 107.0 79.8 107.0
      C85.2 107.0 90.0 103.2 90.0 97.0
      Z"/>"""
    return left + "\n" + right + "\n" + circle(60, 52.5, 6.4)


# ---------------------------------------------------------------------------
# C MENHIR — standing stones. Wider at the base, round only at the head.
# Right stone slightly heavier. Sphere high, like something caught in a
# lintel-less gate. Asymmetry is small enough to survive 24px, large
# enough to kill a corporate H at lockup size.
# ---------------------------------------------------------------------------
def menhir():
    # Heads close; bases step outward. Sphere is the lintel — wedged
    # where the stones are nearest, not floating in a wide sky-gap.
    left = """    <path d="M35.5 19.5
      C35.5 15.0 39.2 12.8 42.8 12.8
      C46.4 12.8 50.6 15.0 50.6 19.5
      L53.8 99.0
      C53.8 103.4 50.6 106.2 46.2 106.2
      L34.0 106.2
      C29.8 106.2 27.2 103.4 27.2 99.0
      Z"/>"""
    right = """    <path d="M85.2 20.4
      C85.2 15.6 81.4 13.4 77.6 13.4
      C73.8 13.4 69.2 15.6 69.2 20.4
      L65.6 99.4
      C65.6 103.8 68.8 106.8 73.4 106.8
      L86.8 106.8
      C91.0 106.8 93.4 103.8 93.4 99.4
      Z"/>"""
    return left + "\n" + right + "\n" + circle(60, 35.0, 9.0)


# ---------------------------------------------------------------------------
# D CATCH — inner bays. Straight outer shafts; the inner faces are
# scalloped so the sphere sits in a carved pocket. The pocket is the
# holding, not a crossbar. Sphere slightly below centre (gravity + catch).
# ---------------------------------------------------------------------------
def catch():
    # Lips closer than the sphere's diameter: a captured bearing.
    # The bay cuts into the shaft, not out into the gap.
    left = """    <path d="M31.0 21.5
      C31.0 16.4 35.0 13.6 39.4 13.6
      C43.8 13.6 47.6 16.4 47.6 21.5
      L50.8 52.0
      C51.0 57.0 47.4 61.0 47.2 66.0
      C47.4 71.0 51.0 75.0 50.8 80.0
      L47.6 98.5
      C47.6 103.6 43.8 106.4 39.4 106.4
      C35.0 106.4 31.0 103.6 31.0 98.5
      Z"/>"""
    right = """    <path d="M89.0 21.5
      C89.0 16.4 85.0 13.6 80.6 13.6
      C76.2 13.6 72.4 16.4 72.4 21.5
      L69.2 52.0
      C69.0 57.0 72.6 61.0 72.8 66.0
      C72.6 71.0 69.0 75.0 69.2 80.0
      L72.4 98.5
      C72.4 103.6 76.2 106.4 80.6 106.4
      C85.0 106.4 89.0 103.6 89.0 98.5
      Z"/>"""
    return left + "\n" + right + "\n" + circle(60, 66, 10.4)


# ---------------------------------------------------------------------------
# E TOKEN — heavy, short, close. A carved seal rather than a letter.
# Small sphere, low in a tight well. Monumental as mass, not as type.
# ---------------------------------------------------------------------------
def token():
    left = """    <path d="M24.0 30.0
      C24.0 22.8 29.6 18.5 36.0 18.5
      C42.4 18.5 49.6 22.8 49.6 30.0
      L51.0 92.0
      C51.0 99.4 45.4 103.5 38.5 103.5
      C31.4 103.5 24.0 99.4 24.0 92.0
      Z"/>"""
    right = """    <path d="M96.0 30.0
      C96.0 22.8 90.4 18.5 84.0 18.5
      C77.6 18.5 70.4 22.8 70.4 30.0
      L69.0 92.0
      C69.0 99.4 74.6 103.5 81.5 103.5
      C88.6 103.5 96.0 99.4 96.0 92.0
      Z"/>"""
    return left + "\n" + right + "\n" + circle(60, 74, 8.6)


# ---------------------------------------------------------------------------
# F TAPER — blades. Outer edges slant in toward the head; inner faces
# nearly vertical. Sphere high-mid. Reads as two worn obelisks, not an H.
# ---------------------------------------------------------------------------
def taper():
    left = """    <path d="M39.0 18.0
      C39.0 14.2 42.2 12.4 45.2 12.4
      C48.2 12.4 51.2 14.2 51.2 18.0
      C51.6 32.0 52.4 44.0 52.8 48.5
      L53.4 97.0
      C53.4 102.8 48.6 107.4 41.4 107.4
      L29.0 107.4
      C23.8 107.4 21.0 103.0 21.0 98.2
      Z"/>"""
    right = """    <path d="M81.0 18.0
      C81.0 14.2 77.8 12.4 74.8 12.4
      C71.8 12.4 68.8 14.2 68.8 18.0
      C68.4 32.0 67.6 44.0 67.2 48.5
      L66.6 97.0
      C66.6 102.8 71.4 107.4 78.6 107.4
      L91.0 107.4
      C96.2 107.4 99.0 103.0 99.0 98.2
      Z"/>"""
    return left + "\n" + right + "\n" + circle(60, 48.5, 7.2)


files = {
    "0-control.svg": wrap("Control — current production, not a candidate", control),
    "a-relic.svg": wrap("Study A — Relic", relic()),
    "b-throat.svg": wrap("Study B — Throat", throat()),
    "c-menhir.svg": wrap("Study C — Menhir", menhir()),
    "d-catch.svg": wrap("Study D — Catch", catch()),
    "e-token.svg": wrap("Study E — Token", token()),
    "f-taper.svg": wrap("Study F — Taper", taper()),
}

for name, svg in files.items():
    (OUT / name).write_text(svg)
    print("wrote", name)
