import { Resvg } from "@resvg/resvg-js";
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const dir = dirname(fileURLToPath(import.meta.url));
const marks = join(dir, "marks");
const out = join(dir, "raster");
mkdirSync(out, { recursive: true });

function render(svg, size, dest, background) {
  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: size },
    background,
    font: { loadSystemFonts: false },
  });
  writeFileSync(dest, resvg.render().asPng());
}

for (const file of readdirSync(marks).filter((f) => f.endsWith(".svg"))) {
  const raw = readFileSync(join(marks, file), "utf8");
  const stem = file.replace(".svg", "");
  const colored = raw.replace("<svg", `<svg style="color:#0A0A0A"`);
  for (const size of [16, 24, 32, 180, 400]) {
    render(colored, size, join(out, `${stem}-${size}.png`), "#F7F6F3");
  }
  const onVoid = raw.replace("<svg", `<svg style="color:#F7F6F3"`);
  render(onVoid, 180, join(out, `${stem}-180-void.png`), "#0A0A0A");
  render(onVoid, 400, join(out, `${stem}-400-void.png`), "#0A0A0A");
  console.log("raster", stem);
}
