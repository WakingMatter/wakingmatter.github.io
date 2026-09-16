# Identity application — Phase B identity-only

**Status:** HISTORICAL. This sheet recorded the identity-application gate (including the 390 aperture omission). It is not current shipping truth. Design later returned **PASS PHASE B IDENTITY APPLICATION** and **PASS BROADER SITE APPLICATION**. Frozen core remains closed. See [`../../VISUAL-FIDELITY.md`](../../VISUAL-FIDELITY.md).

Geometry + modeled two-value finish + outlined Gloock-derived recut (04-tight 0.38×cap) are frozen together. This pass replaced shipping Newsreader lockups and site identity surfaces only.

Open [`index.html`](index.html).

## Applied

| Surface | Treatment |
| --- | --- |
| `brand/logos/lockup*.svg`, `wordmark.svg` | Frozen recut + modeled mark |
| `src/components/Mark.astro` | Source occupancy, modeled two-value, ivory/void |
| `src/components/Aperture.astro` | Void modeled mark at architectural scale |
| `src/components/Header.astro` | Frozen lockup SVG (not Newsreader word) |
| Favicon / app / apple-touch / 192 / 512 | Frozen mark rasters |
| `public/og-image.svg` | Void + recut lockup at inscription scale. No teal. No Newsreader outlines. |

## Held at the time of this sheet (do not treat as current site status)

- Geometry, finish, color, mono fallback, type — still closed.
- Editorial copy and broader pages were later completed on the same PR; this sheet does not document them.
- Merge / live `main` remain human-gated.

## Inspect first

1440 home keeps the architectural mark beside the headline. Below 900px `.hero-figure` is omitted: the recut lockup in the header already carries identity, so a 12rem centered H above the headline is not used. Never `order: -1`.

Compare 390 home to Direction 04 (inscription first), 03 (no logo splash), 01 (editorial air). Then stop.

Historical. Do not use this sheet as the live site.
