#!/usr/bin/env python3
"""Promote the frozen Gloock-derived recut into shipping lockup masters.

Does not reopen geometry, finish, color, mono fallback construction, or type.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LOGOS = REPO / "brand" / "logos"
PUBLIC = REPO / "public"
STUDY = REPO / "brand" / "studies" / "wordmark-gate-01"
XFORM = "translate(0, 1.944) scale(0.555319148936) translate(-35.90, -13.00)"


def retitle(svg: str, label: str, idmap: dict[str, str]) -> str:
    svg = re.sub(r'aria-label="[^"]*"', f'aria-label="{label}"', svg)
    for old, new in idmap.items():
        svg = svg.replace(old, new)
    return svg


def main() -> None:
    ivory = (STUDY / "lockups" / "gloock-recut-ivory.svg").read_text()
    void = (STUDY / "lockups" / "gloock-recut-void.svg").read_text()
    word = (STUDY / "wordmarks" / "gloock-recut.svg").read_text()

    (LOGOS / "lockup.svg").write_text(
        retitle(
            ivory,
            "Waking Matter",
            {
                "gloock-recutiColL": "lkColL",
                "gloock-recutiColR": "lkColR",
                "gloock-recutiBead": "lkBead",
            },
        )
    )
    (LOGOS / "lockup-on-ivory.svg").write_text(
        retitle(
            ivory,
            "Waking Matter on ivory",
            {
                "gloock-recutiColL": "lkiColL",
                "gloock-recutiColR": "lkiColR",
                "gloock-recutiBead": "lkiBead",
            },
        )
    )
    (LOGOS / "lockup-on-void.svg").write_text(
        retitle(
            void,
            "Waking Matter on void",
            {
                "gloock-recutvColL": "lkvColL",
                "gloock-recutvColR": "lkvColR",
                "gloock-recutvBead": "lkvBead",
            },
        )
    )
    (LOGOS / "wordmark.svg").write_text(
        word.replace('aria-label="Gloock recut"', 'aria-label="Waking Matter wordmark"')
    )

    vb = re.search(r'viewBox="[^"]+"', ivory).group(0)
    paths = re.search(r"(  <path fill=\"#0A0A0A\".*)", ivory, re.S).group(1)
    paths = paths.replace('fill="#0A0A0A"', 'fill="currentColor"')
    mono = (
        f'<svg xmlns="http://www.w3.org/2000/svg" {vb} fill="none" '
        f'role="img" aria-label="Waking Matter, one-bit">\n'
        f'  <g transform="{XFORM}">\n'
        f'    <g fill="currentColor">\n'
        f'      <rect x="35.90" y="13.00" width="11.00" height="94.00" rx="5.50"/>\n'
        f'      <rect x="73.10" y="13.00" width="11.00" height="94.00" rx="5.50"/>\n'
        f"    </g>\n"
        f'    <circle cx="60.00" cy="60.00" r="11.40" fill="none" '
        f'stroke="currentColor" stroke-width="2.20"/>\n'
        f"  </g>\n"
        f"{paths}"
    )
    (LOGOS / "lockup-mono.svg").write_text(mono)

    brand_pub = PUBLIC / "brand"
    brand_pub.mkdir(parents=True, exist_ok=True)
    ship = [
        "mark.svg",
        "mark-on-ivory.svg",
        "mark-on-void.svg",
        "mark-small.svg",
        "mark-mono.svg",
        "favicon.svg",
        "icon-app.svg",
        "icon-app-mono.svg",
        "wordmark.svg",
        "lockup.svg",
        "lockup-on-ivory.svg",
        "lockup-on-void.svg",
        "lockup-mono.svg",
    ]
    for name in ship:
        shutil.copyfile(LOGOS / name, brand_pub / name)
    shutil.copyfile(LOGOS / "favicon.svg", PUBLIC / "favicon.svg")
    print("promoted recut lockups → brand/logos and public/brand")


if __name__ == "__main__":
    main()
