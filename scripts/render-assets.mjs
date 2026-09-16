import { Resvg } from "@resvg/resvg-js";
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const logos = join(root, "brand/logos");
const out = join(root, "public");
const brandOut = join(out, "brand");
mkdirSync(out, { recursive: true });
mkdirSync(brandOut, { recursive: true });

function render(svg, width, dest) {
  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: width },
    font: { loadSystemFonts: false },
    background: undefined,
  });
  writeFileSync(dest, resvg.render().asPng());
  console.log("wrote", dest, "w=", width);
}

function inner(svg) {
  return svg.replace(/<\?xml[^>]*>/, "").replace(/<svg[^>]*>/, "").replace("</svg>", "");
}

const ship = [
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
];
for (const name of ship) {
  copyFileSync(join(logos, name), join(brandOut, name));
}
copyFileSync(join(logos, "favicon.svg"), join(out, "favicon.svg"));

const favicon = readFileSync(join(logos, "favicon.svg"), "utf8");
render(favicon, 32, join(out, "favicon-32.png"));

const iconApp = readFileSync(join(logos, "icon-app.svg"), "utf8");
render(iconApp, 180, join(out, "apple-touch-icon.png"));
render(iconApp, 192, join(out, "icon-192.png"));
render(iconApp, 512, join(out, "icon-512.png"));
render(iconApp, 512, join(out, "avatar-512.png"));

const lockupInner = inner(readFileSync(join(logos, "lockup-on-void.svg"), "utf8"));
const markVoidInner = inner(readFileSync(join(logos, "mark-on-void.svg"), "utf8"));

const og = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <rect width="1200" height="630" fill="#0A0A0A"/>
  <g transform="translate(72, 268) scale(1.48)">
    ${lockupInner}
  </g>
  <g transform="translate(868, 168) scale(2.45)">
    ${markVoidInner}
  </g>
</svg>`;
writeFileSync(join(out, "og-image.svg"), og);
render(og, 1200, join(out, "og-image.png"));
