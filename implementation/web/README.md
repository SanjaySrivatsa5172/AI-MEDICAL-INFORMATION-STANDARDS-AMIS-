# AMIS Claim Calculator

Local web UI that scores pasted abstracts or uploaded papers (PDF / plain text)
against the five AMIS standards and two aggregate axes:

- **Uncertainty vs certainty** — calibration / productive uncertainty vs false confidence
- **Methodological failure** — contaminated graders, Goodhart gaming, shortcut learning, fabricated reasoning

The calculator **does not prescribe treatment** (Standard 5).

## Public source

https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-

This is the citation URL for letters and papers. The calculator lives in this repository (not a second schema repo).

Standard 2 treats GitHub, ORCID, and Hugging Face as Tier 4 reproducibility hosts —
bibliography noise, not YouTube-tier excluded sources. YouTube / TikTok / social
media still fail.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-)

The scorer is FastAPI, so GitHub Pages cannot host it. One-click Render: [docs/deploy.md](../../docs/deploy.md). After deploy, the public URL is `https://amis-claim-calculator.onrender.com`.

## Run locally

From the repository root:

```bash
python3 -m pip install -r implementation/web/requirements.txt
python3 -m implementation.web.app
```

Open [http://127.0.0.1:8765](http://127.0.0.1:8765).

## Docker (shareable / hostable)

```bash
docker build -t amis-calculator .
docker run --rm -p 8765:8765 amis-calculator
```

Render uses native Python and `$PORT` from `render.yaml`. Do not pin `PORT` to 8765 on Render. The app binds `0.0.0.0`.

Headless scoring (same engine as the UI):

```bash
PYTHONPATH=. python3 -m implementation.python.calculator examples/calculator/srivatsa_abstract.txt
PYTHONPATH=. python3 -m implementation.python.calculator examples/calculator/craftmd_excerpt.txt
PYTHONPATH=. python3 -m implementation.python.calculator examples/calculator/agentclinic_excerpt.txt
```

Tooth-paper fixtures (excerpts only; publisher PDFs are not in the repository):

- `craftmd_excerpt.txt` — Johri et al., *Nat Med* 2025 (DOI 10.1038/s41591-024-03328-5). Grader-AI + vignette→conversation drop.
- `agentclinic_excerpt.txt` — Schmidgall et al., *npj Digit Med* 2026 (DOI 10.1038/s41746-026-02674-7). LLM moderator + MedQA-in-dialogue drop.

Batch a manifest of papers (no second schema):

```bash
PYTHONPATH=. python3 -m implementation.python.batch_score \
  examples/calculator/patient_sim_2025/manifest.json --table-only
```

See `examples/calculator/patient_sim_2025/REPORT.md`.

## Tests

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

## What is reused

`AMISValidator`, `SourceClassifier`, `HarmCascadeAnalyzer`, and
`standards/*.yaml|json`. Claim extraction and the methodological-failure
axis are thin Python classes; they do not add a second compliance schema.
