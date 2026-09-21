# AMIS Claim Calculator

Local web UI that scores pasted abstracts or uploaded papers (PDF / plain text)
against the five AMIS standards and two aggregate axes:

- **Uncertainty vs certainty** — calibration / productive uncertainty vs false confidence
- **Methodological failure** — contaminated graders, Goodhart gaming, shortcut learning, fabricated reasoning

The calculator **does not prescribe treatment** (Standard 5).

## Public source

https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-

This is the citation URL for letters and papers. The calculator lives in this repository (not a second schema repo).

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

Set `PORT` for Render or any PaaS (`render.yaml` is in the repo root). The app binds `0.0.0.0`.

Headless scoring (same engine as the UI):

```bash
PYTHONPATH=. python3 -m implementation.python.calculator examples/calculator/srivatsa_abstract.txt
```

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
