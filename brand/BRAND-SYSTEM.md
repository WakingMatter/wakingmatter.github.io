# Waking Matter brand system

> **Logo checkpoint (open).** The marks in `logos/` are the shipped stadium geometry. They are **not frozen.** A 4–6 one-colour study against Direction 04 lives in [`studies/logo-checkpoint-04/`](studies/logo-checkpoint-04/index.html). Do not treat the corporate-H aperture as canonical until that checkpoint is independently reviewed.

This is the first production identity we can credibly keep. It is not a campaign, a product UI kit, or a speculative future state.

**Visual source of truth, in rank order:** Direction 04 Impeccable Craft (north star) → Direction 03 Systems Lab (grid, construction, numbered rigor) → Direction 01 Quiet Research Institution (editorial air). Direction 02 is a negative reference: do not drift toward luminous sci-fi or generic AI.

**Core descriptor:** Building systems for cumulative intelligence.

**Definition we may use in public:** We explore systems that can preserve, inherit, and compound useful learning across agents, models, and time.

**Contact:** [hello@wakingmatter.com](mailto:hello@wakingmatter.com)

Do not invent a team, customers, funding, products, partnerships, publications, or research results in order to fill a layout.

---

## 1. Mark

The mark is two restrained vertical stadiums — rounded pillars, or an aperture — with a small sphere in the gap between them. It should read as calm, ambiguous, and ownable. It is not a letter H that needs to be explained, and it is not a picture of a thing.

**Concept:** a holding structure and a unit of matter. The gap is as important as the ink.

**Do not let it become:** a brain, a robot, a circuit, a glowing orb, a planet, a spark, a stacked pyramid, a neural node, or a cosmic gradient.

### Construction

Master viewBox: `0 0 120 120`.

| Part | Value |
| --- | --- |
| Left pillar | `rect x=32 y=16 width=16 height=88 rx=8` |
| Right pillar | `rect x=72 y=16 width=16 height=88 rx=8` |
| Sphere | `circle cx=60 cy=60 r=10` |
| Pillar width | 16 |
| Gap | 24 (1.5 × pillar width) |
| Sphere diameter | 20 |
| Optical center | `60, 60` |

The sphere sits in the aperture and does not overlap the pillars. Caps are full half-circles (stadiums). Do not square the ends. Do not add a crossbar.

A **small-size** cut (`mark-small.svg`, 32×32) thickens the pillars slightly (`width=5` on a 32-unit grid) so the mark still reads at 16px.

### Clearspace

Minimum clearspace is **one pillar width** on all sides — `16` units in the 120-unit grid, equal to `0.2×` the mark’s frame. Do not let type, rules, or photography enter this margin.

Exception: the primary lockup, where the wordmark is locked to the mark at a fixed gap of **0.38 × cap height**.

### Minimum sizes

| Use | Minimum |
| --- | --- |
| Mark in UI / print | 24 px / 8 mm tall |
| Favicon | 16 px (use `mark-small` / `favicon.svg`) |
| App icon / avatar | 180 px (use `icon-app`) |
| Primary lockup | 120 px wide |
| Wordmark alone | 80 px wide |

If the lockup would fall below 120 px wide, use the **mark only**.

### Colorways

| File | Ground | Ink |
| --- | --- | --- |
| `mark.svg` / `mark-mono.svg` / `lockup.svg` | any | `currentColor` |
| `mark-on-ivory.svg` / `lockup-on-ivory.svg` | Ivory | Void pillars, matte sphere |
| `mark-on-void.svg` / `lockup-on-void.svg` | Void | Mist pillars, pearl sphere with a **trace** of Resonance |
| `icon-app.svg` | Void rounded square | Dimensional mark |
| `icon-app-mono.svg` | Void rounded square | Ivory mark |

Resonance appears in the sphere of the **void** colorway only, as a shaded mid-tone, never as a glow. The ivory colorway is essentially black and pale stone.

---

## 2. Wordmark

The wordmark is **Waking Matter** in Newsreader at display optical size, regular weight, tracking slightly tight. It is not Canela, Sora, or Neue Montreal.

Primary lockup: mark to the left of the wordmark. Align the mark to the **cap height** of the type, not to the descender of *g*. Gap = `0.38 × cap-height`.

Do not outline, extra-letterspace, or stack the words except in a display setting where the name is the headline (and then it is typesetting, not the logo).

Do not pair the mark with a different typeface.

---

## 3. Color

| Name | Hex | Role |
| --- | --- | --- |
| Void | `#0A0A0A` | Primary ink, dark grounds, hero |
| Charcoal | `#2A2A2A` | Secondary ink, diagrams |
| Ivory | `#F7F6F3` | Paper, light grounds, type on Void |
| Resonance | `#5C8F8A` | Rare accent. Not a brand fill. |
| Mist | `#D6D9D7` | Rules on Void, sphere highlight, hairlines |

**Most surfaces are Void or Ivory.** Charcoal is for quieter text on Ivory when Void would be too emphatic. Mist is not body text on Ivory (contrast is insufficient). Resonance is not a button color, not a section wash, and not a gradient background.

Approximate mix: if a composition feels more than a few percent teal, it has drifted.

Hairlines: `rgba(10,10,10,0.12)` on Ivory, `rgba(247,246,243,0.14)` on Void.

---

## 4. Typography

| Role | Face | License | Notes |
| --- | --- | --- | --- |
| Display, wordmark, article body | [Newsreader](https://fonts.google.com/specimen/Newsreader) | SIL OFL 1.1 | Optical size on. Regular for display; italic for emphasis. |
| UI, navigation, decks, labels | [Inter](https://rsms.me/inter/) | SIL OFL 1.1 | Variable weight 400–500. |
| Metadata, dates, codes | [IBM Plex Mono](https://github.com/IBM/plex) | SIL OFL 1.1 | Optional. 400/500 only. |

No proprietary Canela. No Neue Montreal. No Sora.

### Scale

| Token | Size | Face | Use |
| --- | --- | --- | --- |
| `display` | `clamp(2.75rem, 7vw, 5.5rem)` | Newsreader 400 | Homepage headline |
| `h1` | `clamp(2rem, 4vw, 3.25rem)` | Newsreader 400 | Page titles |
| `h2` | `clamp(1.5rem, 2.4vw, 2rem)` | Newsreader 400 | Section titles |
| `h3` | `1.25rem` | Newsreader 400 | Subheads |
| `body` | `1.0625rem / 1.65` | Inter 400 | UI body |
| `article` | `1.25rem / 1.6` | Newsreader 400 | Notes |
| `deck` | `clamp(1.05rem, 1.4vw, 1.2rem) / 1.5` | Inter 400 | Hero supporting line |
| `label` | `0.6875rem` | Inter 500, `0.16em` tracking, uppercase | Eyebrows, nav, indexes |
| `meta` | `0.75rem / 1.45` | IBM Plex Mono 400 | Dates, slugs |

Line length for articles: about 60–68 characters (`max-width: 38em`).

---

## 5. Grid and spacing

Borrow Direction 03’s discipline, not its stacked-layer mark.

- Base unit: **8 px**.
- Page padding: `clamp(1.25rem, 5vw, 4.5rem)`.
- Content width: `72rem` (1152 px) for most pages; homepage hero is full bleed.
- Interior grid: 12 columns, 24 px gutter, collapse to 4 then 1.
- Section padding: `6–10` units vertical on mobile, `10–16` on desktop.
- Numbered blocks (`01 02 03`) sit on a hairline top rule, never in filled cards with shadows.

Corners: hairline frames may use `0–2px` radius. App icons use a large squircle. Marketing “cards” with 16 px radius and drop shadow are out of system.

---

## 6. Motion

Direction 04 is composure, not spectacle.

- Duration: 400–900 ms.
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)`.
- Allowed: a short rise/fade of type on first paint; focus states; link underlines.
- Forbidden: looping glows, parallax planets, particle fields, hover scale on the mark, animated gradients.

Honor `prefers-reduced-motion: reduce` by disabling entrance motion and non-essential transitions.

---

## 7. Imagery

Prefer empty architecture, material close-ups, and quiet interior light — Direction 01’s air, Direction 04’s craft. Black and white or near-monochrome. No neon, no UI mockups of invented products, no generative “AI art” clichés (glass brains, infinite servers, glowing faces).

Until we have commissioned photography, the site should use **type, rules, and the mark at architectural scale** rather than stock. A missing photograph is more honest than a borrowed one.

---

## 8. Voice

**Traits:** Precision. Depth. Composure.

Write as a long-lived institution that has not yet said much in public, not as a startup that needs to sound large.

- Prefer short declarative sentences. Do not stack claims.
- Use the core descriptor and the safe definition. Do not escalate them into a mission to transform humanity.
- Do not claim novelty, priority, or empirical results unless we are actually publishing them.
- Do not name a team, a lab roster, customers, or partners that do not exist.
- “We” is allowed. Invented biographies are not.
- Headlines may be quiet and large. They should not be clever at the expense of meaning.

### Examples

**Do:** Building systems for cumulative intelligence.

**Do not:** Unlocking the future of autonomous compounding AI.

**Do:** We explore systems that can preserve, inherit, and compound useful learning across agents, models, and time.

**Do not:** Our platform delivers state-of-the-art memory for agents.

**Do:** Intelligence should accumulate.

**Do not:** The last algorithm you’ll ever need.

---

## 9. Logo files

All masters live in `brand/logos/`. Site copies of the public marks live in `public/`.

| File | Use |
| --- | --- |
| `mark.svg` | Master, `currentColor` |
| `mark-mono.svg` | Same, production mono |
| `mark-small.svg` | 16–32 px |
| `mark-on-ivory.svg` | Color mark on light |
| `mark-on-void.svg` | Color mark on dark |
| `wordmark.svg` | Name, no mark |
| `lockup.svg` | Primary logo, `currentColor` |
| `lockup-mono.svg` | Primary, single color |
| `lockup-on-ivory.svg` | Primary on light |
| `lockup-on-void.svg` | Primary on dark |
| `icon-app.svg` | App / social, dimensional |
| `icon-app-mono.svg` | App / social, mono |
| `favicon.svg` | Browser icon on Ivory |

---

## 10. What we rejected from Direction 02

Do not introduce: luminous cores, sci-fi bloom, circuit traces, neural graphs, cosmic orbs, saturated teal-to-violet ramps, intern-grade rounded product cards, or “AI” as a visual style. If a composition would look at home on a model-launch splash page, it is wrong for us.
