# Waking Matter — standalone landing site

A sparse, typography-first identity page for **Waking Matter**. It is a static folder of HTML, CSS, and a few assets. It is not part of the existing Next.js application in this repository.

Copy:

- **Waking Matter**
- Building systems for cumulative intelligence.
- Intelligence should accumulate.
- Contact: [hello@wakingmatter.com](mailto:hello@wakingmatter.com)

The page does not describe products, a team, funding, customers, or research results.

## Isolation

This site lives only in `waking-matter-site/`. Nothing elsewhere in `avs-io/Website` needs to change for it to work. The Next.js app does not route or compile this folder.

The page is static: HTML, CSS, and assets. There is no JavaScript and no build step.

To publish it, transplant **the contents of this folder** (not the parent Website repo) into a dedicated GitHub Pages repository or onto `wakingmatter.com`.

## Local preview

From this directory:

```bash
cd waking-matter-site
python3 -m http.server 4173
```

Then open [http://127.0.0.1:4173/](http://127.0.0.1:4173/).

Any other static server is equivalent (`npx serve`, Caddy, nginx). Open `index.html` as a file if you only need a glance; a local server is better for fonts, the manifest, and paths.

## Deploy to GitHub Pages

1. Create a repository (for example `wakingmatter/wakingmatter.github.io` or a project Pages repo).
2. Copy every file in this folder to the repository **root**. Keep `index.html` at `/index.html`.
3. In the repo settings, enable GitHub Pages from the default branch, `/ (root)`.
4. `CNAME` is already set to `wakingmatter.com`. Point the domain’s DNS to GitHub Pages and wait for HTTPS.
5. `.nojekyll` is included so GitHub will not process the files through Jekyll.

After transplant, Open Graph tags assume the public origin `https://wakingmatter.com/`. If you serve the site from a project URL instead (for example `https://user.github.io/repo/`), update:

- `link rel="canonical"`
- `og:url`, `og:image`, `twitter:image`
- `robots.txt` sitemap URL
- `sitemap.xml`
- JSON-LD `url`

## Files

| Path | Role |
| --- | --- |
| `index.html` | Identity page |
| `404.html` | Sparse not-found page |
| `styles.css` | Type, layout, motion, reduced-motion |
| `assets/` | Favicon, Open Graph image, grain, self-hosted fonts |
| `robots.txt`, `sitemap.xml`, `site.webmanifest` | Discovery metadata |
| `CNAME` | Custom domain for GitHub Pages |

## Identity notes

- Wordmark is the name set in Newsreader. There is no logo mark.
- Palette: warm off-white paper, near-black ink, one muted mineral-teal accent.
- The right-hand column is an abstract core of accumulating layers, not a product diagram.
- Motion is a slight rise of the type and a bottom-up settling of the layers. It is disabled when `prefers-reduced-motion: reduce`.

Fonts are [Newsreader](https://fonts.google.com/specimen/Newsreader) and [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans), both SIL Open Font License, self-hosted as Latin and Latin-ext `woff2` files under `assets/fonts/`.
