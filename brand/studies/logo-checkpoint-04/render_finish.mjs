import { Resvg } from "@resvg/resvg-js";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const dir = dirname(fileURLToPath(import.meta.url));
const finish = join(dir, "finish");
const out = join(finish, "raster");
mkdirSync(out, { recursive: true });

function render(svg, size, dest, background) {
  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: size },
    background,
    font: { loadSystemFonts: false },
  });
  writeFileSync(dest, resvg.render().asPng());
}

function read(name) {
  return readFileSync(join(finish, name), "utf8");
}

const ivory = read("mark-on-ivory.svg");
const onVoid = read("mark-on-void.svg");
const oneBit = read("mark-mono.svg").replace("<svg", `<svg style="color:#0A0A0A"`);
const oneBitVoid = read("mark-mono.svg").replace(
  "<svg",
  `<svg style="color:#F7F6F3"`,
);
const rejected = read("rejected-one-fill.svg").replace(
  "<svg",
  `<svg style="color:#0A0A0A"`,
);
const icon = read("icon-app.svg");
const favicon = read("favicon.svg");
const lockIvory = read("lockup-fraunces-ivory.svg");
const lockVoid = read("lockup-fraunces-void.svg");
const lockNews = read("lockup-on-ivory.svg");

for (const size of [16, 24, 32, 180, 400]) {
  render(ivory, size, join(out, `ivory-${size}.png`), "#F7F6F3");
  render(onVoid, size, join(out, `void-${size}.png`), "#0A0A0A");
  render(oneBit, size, join(out, `onebit-${size}.png`), "#F7F6F3");
  render(rejected, size, join(out, `rejected-${size}.png`), "#F7F6F3");
}
render(oneBitVoid, 180, join(out, "onebit-180-void.png"), "#0A0A0A");
render(oneBitVoid, 400, join(out, "onebit-400-void.png"), "#0A0A0A");
render(icon, 180, join(out, "icon-180.png"));
render(icon, 400, join(out, "icon-400.png"));
render(favicon, 16, join(out, "favicon-16.png"));
render(favicon, 32, join(out, "favicon-32.png"));
render(lockIvory, 720, join(out, "lockup-fraunces-ivory.png"), "#F7F6F3");
render(lockVoid, 720, join(out, "lockup-fraunces-void.png"), "#0A0A0A");
render(lockNews, 720, join(out, "lockup-newsreader-ivory.png"), "#F7F6F3");
console.log("finish rasters", out);
