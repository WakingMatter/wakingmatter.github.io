import { Resvg } from "@resvg/resvg-js";
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const dir = dirname(fileURLToPath(import.meta.url));
const out = join(dir, "raster");
mkdirSync(out, { recursive: true });

function render(svg, dest, { width, height, background }) {
  const fitTo = width
    ? { mode: "width", value: width }
    : { mode: "height", value: height };
  const resvg = new Resvg(svg, {
    fitTo,
    background,
    font: { loadSystemFonts: false },
  });
  writeFileSync(dest, resvg.render().asPng());
}

const slugs = [
  "gloock",
  "gloock-air",
  "bodoni",
  "bellefair",
  "noto",
  "cinzel",
  "fraunces",
  "newsreader",
];

for (const slug of slugs) {
  const ivory = readFileSync(join(dir, "lockups", `${slug}-ivory.svg`), "utf8");
  const onVoid = readFileSync(join(dir, "lockups", `${slug}-void.svg`), "utf8");
  const wm = readFileSync(join(dir, "wordmarks", `${slug}.svg`), "utf8");
  const gl = readFileSync(join(dir, "glyphs", `${slug}.svg`), "utf8");
  render(ivory, join(out, `${slug}-lockup-ivory-720.png`), {
    width: 720,
    background: "#F7F6F3",
  });
  render(ivory, join(out, `${slug}-lockup-ivory-145.png`), {
    height: 145,
    background: "#F7F6F3",
  });
  render(ivory, join(out, `${slug}-lockup-ivory-200.png`), {
    width: 200,
    background: "#F7F6F3",
  });
  render(onVoid, join(out, `${slug}-lockup-void-720.png`), {
    width: 720,
    background: "#0A0A0A",
  });
  render(onVoid, join(out, `${slug}-lockup-void-145.png`), {
    height: 145,
    background: "#0A0A0A",
  });
  render(onVoid, join(out, `${slug}-lockup-void-200.png`), {
    width: 200,
    background: "#0A0A0A",
  });
  render(wm, join(out, `${slug}-wordmark.png`), {
    height: 72,
    background: "#F7F6F3",
  });
  render(gl, join(out, `${slug}-glyphs.png`), {
    height: 140,
    background: "#F7F6F3",
  });
}
console.log("wordmark rasters", out);
