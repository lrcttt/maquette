#!/bin/bash
# Kit v6 hors ligne (dépôt lrcttt/maquette, dossier _kit) : copie le kit et les polices dans /home/claude/kit.
# Aucun téléchargement de code. Usage : bash /home/claude/maquette/_kit/install.sh
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
mkdir -p /home/claude/kit
cp -r "$SRC"/. /home/claude/kit/
rm -f /home/claude/kit/install.sh
python3 -c "import PIL" 2>/dev/null || pip install pillow --break-system-packages -q
node -e "require('playwright')" >/dev/null 2>&1 && echo "playwright node OK" || echo "playwright node ABSENT (chk.js)"
python3 -c "import playwright" 2>/dev/null && echo "playwright python OK" || echo "playwright python ABSENT (prepare.py)"
echo "polices : $(ls /home/claude/kit/fonts | wc -l) familles"
echo "kit installé : $(ls /home/claude/kit | tr '\n' ' ')"
