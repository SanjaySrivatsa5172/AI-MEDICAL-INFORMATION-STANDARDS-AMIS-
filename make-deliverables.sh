#!/usr/bin/env bash
# Regenerate PDF and Word deliverables from the markdown sources.
# Requires: pip install pypandoc-binary ; Chromium at $CHROME
set -euo pipefail
cd "$(dirname "$0")"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
mkdir -p deliverables
python3 - <<'PY'
import pypandoc, os
os.chdir(os.path.dirname(os.path.abspath("make-deliverables.sh")) or ".")
CSS = "deliverables/print.css"
jobs = [
 ("evidence-reviews/lipoedema-ultrasound-ml-IRB-protocol.md","deliverables/Sparkle-Study-IRB-Protocol",
  "The Sparkle Study — Full Research Protocol for IRB Submission", True),
 ("evidence-reviews/statistician-onboarding-letter.md","deliverables/Sparkle-Study-Statistician-Onboarding-Letter",
  "The Sparkle Study — Statistician Onboarding Letter", False),
 ("evidence-reviews/lipoedema-ultrasound-ml-protocol.md","deliverables/Sparkle-Study-Technical-Acquisition-Standard",
  "The Sparkle Study — Technical Ultrasound Acquisition Standard", True),
 ("evidence-reviews/lipoedema-ultrasound-ml.md","deliverables/Lipoedema-Ultrasound-ML-Evidence-Review",
  "Evidence Review — Machine Learning for Ultrasound Detection of Lipoedema", True),
]
for src,out,title,toc in jobs:
    for fmt,ext in [("docx","docx"),("html5","html")]:
        a=["--standalone",f"--metadata=title:{title}","--metadata=lang:en-GB",
           "--from=markdown+pipe_tables+grid_tables+raw_html"]
        if fmt=="html5": a+=["--embed-resources",f"--css={CSS}"]
        if toc: a+=["--toc","--toc-depth=3"]
        pypandoc.convert_file(src,fmt,outputfile=f"{out}.{ext}",extra_args=a)
        print("built",f"{out}.{ext}")
PY
cd deliverables
for f in *.html; do
  b="${f%.html}"
  "$CHROME" --headless --no-sandbox --disable-gpu --virtual-time-budget=25000 \
    --print-to-pdf-no-header --print-to-pdf="$PWD/$b.pdf" "file://$PWD/$f" >/dev/null 2>&1
  echo "built $b.pdf"
done
rm -f *.html
