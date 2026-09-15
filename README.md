# Waking Matter

Public site for [wakingmatter.com](https://wakingmatter.com). Building systems for cumulative intelligence.

This repository is a **static** Astro project. The build emits HTML, CSS, SVG, and font files. There is no client framework, no React, and no tracker.

## Pages and copy

- `/` — identity and current definition
- `/about/` — what this effort is, without a team or a catalogue
- `/research/` — questions, not findings
- `/notes/` — essays, with RSS at `/rss.xml`
- Contact: [hello@wakingmatter.com](mailto:hello@wakingmatter.com)

The site does not describe products, customers, funding, partnerships, a roster, or research results.

## Local

```bash
npm install
npm run dev
```

Production build:

```bash
npm run build
npm run preview
```

`npm run assets` regenerates favicons, the app icon, and the Open Graph image from `brand/logos/`.

## Brand

See [`brand/BRAND-SYSTEM.md`](brand/BRAND-SYSTEM.md). Masters live in `brand/logos/`. Public copies are in `public/brand/` and at the site root for icons.

Type: Newsreader, Inter, and IBM Plex Mono, all SIL OFL 1.1, self-hosted. See `brand/fonts/LICENSE.txt`. There is no Canela dependency.

## GitHub Pages

The live site on `main` is still the previous root-static folder, deployed with Pages **legacy / branch** hosting (`main`, `/`). This Astro tree must be published with **GitHub Actions**.

The workflow in `.github/workflows/pages.yml` builds on pull requests and deploys only from `main`.

**Before merging this architecture to `main`:** in the repository Pages settings, set the source to **GitHub Actions**. If `main` is updated while Pages is still “Deploy from a branch / root”, GitHub will serve `package.json` instead of the site.

`public/CNAME` keeps the custom domain `wakingmatter.com`. HTTPS stays with GitHub Pages. `.nojekyll` is in `public/` so the `_astro` directory is not ignored.

## Notes

Essays are Markdown in `src/content/notes/`. Frontmatter:

```yaml
title: ...
description: ...
pubDate: YYYY-MM-DD
```

Rebuild to refresh `/notes/`, RSS, and the sitemap.
