#!/usr/bin/env bash
# Fetch OFL fonts used by generate_wordmark.py into /tmp/wm-type.
set -euo pipefail
DEST=/tmp/wm-type
mkdir -p "$DEST"
base=https://github.com/google/fonts/raw/main
curl -fsSL -o "$DEST/Gloock-Regular.ttf" "$base/ofl/gloock/Gloock-Regular.ttf"
curl -fsSL -o "$DEST/Bellefair-Regular.ttf" "$base/ofl/bellefair/Bellefair-Regular.ttf"
curl -fsSL -o "$DEST/BodoniModa[opsz,wght].ttf" "$base/ofl/bodonimoda/BodoniModa%5Bopsz%2Cwght%5D.ttf"
curl -fsSL -o "$DEST/NotoSerifDisplay[wdth,wght].ttf" "$base/ofl/notoserifdisplay/NotoSerifDisplay%5Bwdth%2Cwght%5D.ttf"
curl -fsSL -o "$DEST/Cinzel[wght].ttf" "$base/ofl/cinzel/Cinzel%5Bwght%5D.ttf"
curl -fsSL -o "$DEST/Fraunces[SOFT,WONK,opsz,wght].ttf" "$base/ofl/fraunces/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf"
curl -fsSL -o "$DEST/Newsreader[opsz,wght].ttf" "$base/ofl/newsreader/Newsreader%5Bopsz%2Cwght%5D.ttf"
echo "fonts in $DEST"
