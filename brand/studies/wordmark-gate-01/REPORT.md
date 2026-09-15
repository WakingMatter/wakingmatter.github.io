# Wordmark gate — type only

**Status:** type not frozen. Geometry and finish provisionally frozen. Phase B held.

Open [`index.html`](index.html). Generator: [`generate_wordmark.py`](generate_wordmark.py).

Independent finish-gate verdict on pass 3: **PASS GEOMETRY + FINISH TO PROVISIONAL FREEZE.** This sheet does not reopen occupancy, small-size occupancy, color, or mono fallback.

## Frozen (do not touch)

Source occupancy: pillar 11 / gap 26.2 / r 11.4 / height 94. Modeled two-value finish in `brand/logos/mark.svg`. 1-bit members+ring remains mono-only.

## Not candidates

- Shipping Newsreader outlines in `brand/logos/lockup*.svg`
- Fraunces (opsz 144, SOFT 0) — closer than Newsreader, still too calligraphic / soft
- Canela — proprietary, cannot ship
- Playfair / generic luxury-fashion Didone as the answer
- Sci-fi display / Orbitron-class gimmick

## Six production paths

All OFL 1.1. Outlined. Mixed-case except Cinzel.

| # | Path | Why it is here | Risk |
| --- | --- | --- | --- |
| 01 | **Gloock** | Deliberately closest to 04 Canela. *W a g M* match. 04-tight gap. | Editorial-fashion adjacency |
| 02 | **Gloock + 02 air** | Same wordmark, restrained spacing only (tracking −0.01, gap 0.58 × cap) | Looser than 04 |
| 03 | Bodoni Moda opsz 96 | Thin / severe carved Didone pole | Generic luxury-fashion |
| 04 | Bellefair | Inscriptional mixed-case, archaeological, not Trajan | Light against the columns |
| 05 | Noto Serif Display | Institutional high-contrast display, not a fashion face | Book-display, less 04 |
| 06 | Cinzel caps | Dune / Trajan inscriptional pole | Costume; not 04 mixed-case |

## Recommendation

**Gloock, 04-tight lockup.** Outline as the production wordmark if critic passes. Do not freeze until that review. Do not replace shipping Newsreader lockups in this pass.

If Gloock is too editorial-fashion: Bellefair (archaeological) then Noto (institutional). Not Bodoni. Not Cinzel.

## Not this pass

- Geometry / finish recut
- Phase B / `src/`
- Editorial copy must-fixes
- Type freeze
- Merge / live `main`

Stop for independent design-critic review of this wordmark gate only.
