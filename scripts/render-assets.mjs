import { Resvg } from "@resvg/resvg-js";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const logos = join(root, "brand/logos");
const out = join(root, "public");
mkdirSync(out, { recursive: true });

function render(svg, width, dest, fontFiles = []) {
  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: width },
    font: {
      fontFiles,
      loadSystemFonts: true,
    },
    background: undefined,
  });
  writeFileSync(dest, resvg.render().asPng());
  console.log("wrote", dest, "w=", width);
}

const favicon = readFileSync(join(logos, "favicon.svg"), "utf8");
render(favicon, 32, join(out, "favicon-32.png"));

const iconApp = readFileSync(join(logos, "icon-app.svg"), "utf8");
render(iconApp, 180, join(out, "apple-touch-icon.png"));
render(iconApp, 192, join(out, "icon-192.png"));
render(iconApp, 512, join(out, "icon-512.png"));
render(iconApp, 512, join(out, "avatar-512.png"));

const touch = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180">
  <rect width="180" height="180" fill="#0A0A0A"/>
  <g fill="#F7F6F3" transform="translate(41 28) scale(0.82)">
    <rect x="32" y="16" width="16" height="88" rx="8"/>
    <rect x="72" y="16" width="16" height="88" rx="8"/>
    <circle cx="60" cy="60" r="11"/>
  </g>
</svg>`;
render(touch, 180, join(out, "apple-touch-icon.png"));

const newsreader = "/tmp/Newsreader-Display-Regular.ttf";
const lockup = readFileSync(join(logos, "lockup-on-void.svg"), "utf8");
const lockupInner = lockup
  .replace(/<\?xml[^>]*>/, "")
  .replace(/<svg[^>]*>/, "")
  .replace("</svg>", "");

const og = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <rect width="1200" height="630" fill="#0A0A0A"/>
  <g transform="translate(72, 72) scale(1.05)" fill="#F7F6F3">
    ${lockupInner}
  </g>
  <text x="72" y="360" fill="#F7F6F3" font-family="Newsreader" font-size="64" font-weight="400">Intelligence should accumulate.</text>
  <text x="72" y="430" fill="#D6D9D7" font-family="Newsreader" font-size="24">Building systems for cumulative intelligence.</text>
  <g transform="translate(980, 200) scale(2.1)">
    <defs>
      <linearGradient id="pillarVoid" x1="40" y1="16" x2="40" y2="104" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#3A3E3D"/>
        <stop offset="0.42" stop-color="#D6D9D7"/>
        <stop offset="1" stop-color="#1C1F1E"/>
      </linearGradient>
      <radialGradient id="sphereVoid" cx="40%" cy="32%" r="68%">
        <stop offset="0" stop-color="#F7F6F3"/>
        <stop offset="0.38" stop-color="#A7B0AD"/>
        <stop offset="0.72" stop-color="#5C8F8A"/>
        <stop offset="1" stop-color="#2A2A2A"/>
      </radialGradient>
    </defs>
    <rect x="32" y="16" width="16" height="88" rx="8" fill="url(#pillarVoid)"/>
    <rect x="72" y="16" width="16" height="88" rx="8" fill="url(#pillarVoid)"/>
    <circle cx="60" cy="60" r="11" fill="url(#sphereVoid)"/>
  </g>
</svg>`;
writeFileSync(join(out, "og-image.svg"), og);
render(og, 1200, join(out, "og-image.png"), [newsreader]);
