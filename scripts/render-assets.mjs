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

const newsreader = "/tmp/Newsreader-Display-Regular.ttf";
const lockup = readFileSync(join(logos, "lockup-on-void.svg"), "utf8");
const lockupInner = lockup
  .replace(/<\?xml[^>]*>/, "")
  .replace(/<svg[^>]*>/, "")
  .replace("</svg>", "");
const markVoid = readFileSync(join(logos, "mark-on-void.svg"), "utf8");
const markVoidInner = markVoid
  .replace(/<\?xml[^>]*>/, "")
  .replace(/<svg[^>]*>/, "")
  .replace("</svg>", "");

const og = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <rect width="1200" height="630" fill="#0A0A0A"/>
  <g transform="translate(72, 72) scale(1.05)">
    ${lockupInner}
  </g>
  <text x="72" y="360" fill="#F7F6F3" font-family="Newsreader" font-size="64" font-weight="400">Intelligence should accumulate.</text>
  <text x="72" y="430" fill="#D6D9D7" font-family="Newsreader" font-size="24">Building systems for cumulative intelligence.</text>
  <g transform="translate(980, 200) scale(2.1)">
    ${markVoidInner}
  </g>
</svg>`;
writeFileSync(join(out, "og-image.svg"), og);
render(og, 1200, join(out, "og-image.png"), [newsreader]);
