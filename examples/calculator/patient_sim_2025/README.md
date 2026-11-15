# Patient-simulation paper batch (2025)

Ten 2025–26 LLM patient-simulation / communication papers scored with the
**existing** AMIS calculator. No sixth standard. PDFs are **not** in git.

## Design (subtract first)

The engine on `main` already extracts AI medical claims, scores Standards 1–5,
and labels asserted vs critiqued methodological failure. This folder adds only:

- a JSON manifest of open-access source URLs
- short public excerpts so the batch is reproducible without publisher PDFs
- frozen full-text scores from the runs in `REPORT.md`

Do not reopen PR #5. Do not pile onto PR #6 (CRAFT-MD / AgentClinic).
This PR does **not** alias `examiner agent` into `method_failure.py`
(that change lives on the parallel draft PR #10). Saggar's ChatGPT-as-examiner
is documented in the score card even though the current engine scores
method-failure 0 on that wording.

## How to run

```bash
# Score the committed excerpts (no PDF download required)
PYTHONPATH=. python -m implementation.python.batch_score \
  examples/calculator/patient_sim_2025/manifest.json --table-only

# Score locally downloaded open PDFs (names in manifest.local_filename)
PYTHONPATH=. python -m implementation.python.batch_score \
  examples/calculator/patient_sim_2025/manifest.json \
  --input-dir /tmp/amis-papers --table-only
```

Single paper, same engine as the UI:

```bash
PYTHONPATH=. python -m implementation.python.calculator \
  examples/calculator/patient_sim_2025/kyung_excerpt.txt
```

Web UI: `python3 -m implementation.web.app` then paste an excerpt or upload
a locally downloaded PDF.

## How to read the numbers

- **Std2 = 0.50 on every full text** is bibliography / repo-host noise
  (GitHub, Hugging Face, ORCID, vendor blogs). It is a critical Standard 2
  hit, so conformance is `none` even when Std1/3/4/5 are 1.00. That is the
  existing validator, not a new rule.
- **Method failure** is asserted evaluation contamination in the paper's
  own methods. Reviews that *describe* other people's weak evals score 0.
- Excerpt-only reruns will not match `scores.fulltext.json` exactly.

Full comparison table and per-paper cards: [REPORT.md](REPORT.md).
