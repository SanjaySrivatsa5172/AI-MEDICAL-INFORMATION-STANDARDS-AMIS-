# AMIS scores: ten 2025–26 patient-simulation / communication papers

Engine: `AMISCalculator` on `main` (PR #5). No sixth standard. PDFs not committed.

**How to read Standard 2.** Every full-text run is **Std2 = 0.50** and
`conformance = none` because the existing validator treats GitHub, Hugging Face,
ORCID, vendor blogs, and similar bibliography / repo-host URLs as Tier 5. That
is **bibliography noise**, not a claim that the papers cite YouTube for medical
advice. Standards 1/3/4/5 stay high. Compare papers on uncertainty, certainty
excess, method failure, and the extracted claims — not on the shared Std2 hit.

Excerpt-only reruns will not match these full-text numbers exactly.

## Comparison table (full text)

| Paper | Overall | Std1 | Std2 | Std3 | Std4 | Std5 | Uncertainty | Certainty excess | Method failure | Claims | ACCESS | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Elhilali 2025 — LLM patient sim / usability | 0.90 | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | 92 | 8 | 0 | 20 | open-html | https://mededu.jmir.org/2025/1/e81271 |
| Haider 2025 — synthetic conversations | 0.87 | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | 85 | 15 | 0 | 20 | open-pdf | https://www.mdpi.com/1424-8220/25/14/4305/pdf |
| Kyung 2025 — PatientSim | 0.88 | 1.00 | 0.50 | 1.00 | 0.90 | 1.00 | 79 | 21 | **44** | 20 | open-pdf | https://arxiv.org/pdf/2505.17818 |
| Busch 2025 — LLM patient-care review | 0.90 | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | 100 | 0 | 0 | 14 | open-pdf | https://www.nature.com/articles/s43856-024-00717-2.pdf |
| Li 2025/26 — VP history-taking review | 0.90 | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | 89 | 11 | 0 | 20 | open-pdf | https://doi.org/10.2196/79039 |
| Zohny 2025 — GPT-4 communication models | 0.88 | 1.00 | 0.50 | 1.00 | 0.90 | 1.00 | 76 | 24 | 0 | 6 | open-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC7618332/ |
| Huo 2025 — chatbot health advice review | 0.90 | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | 89 | 11 | 0 | 20 | open-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC11795331/ |
| Saggar 2025 — ChatGPT OSCE agents | 0.87 | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | 62 | 38 | 0* | 5 | open-pdf | https://eprints.whiterose.ac.uk/id/eprint/238861/1/archdischild-2025-329846.full.pdf |
| Richter 2025/26 — communication meta-analysis | 0.84 | 1.00 | 0.50 | 0.70 | 1.00 | 1.00 | 62 | 38 | 0 | 20 | open-html | https://www.jmir.org/2026/1/e77307/PDF |
| Luo 2025 — ophthalmology digital patient | 0.90 | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | 70 | 30 | 0 | 17 | open-pdf | https://www.nature.com/articles/s41746-025-01841-6.pdf |

\*Saggar uses ChatGPT as patient, doctor, **and examiner**. The current engine
does not fire `contaminated_grader` on “examiner agent” wording (that alias is
PR #10, not this PR). Human note: asserted contamination is present; engine
score remains 0.

## Score cards

### 1. Elhilali et al. — JMIR Medical Education 2025
**ACCESS=open-html** · https://mededu.jmir.org/2025/1/e81271 · DOI 10.2196/81271

| Axis | Score |
|---|---|
| Overall | 0.90 · Std2 bibliography only |
| Uncertainty / certainty excess | 92 / 8 |
| Method failure (asserted) | 0 |

**Claims.** LLM patient simulator for history-taking; SUS 91.5 in n=5 students;
four physicians rated Grok 3 / GPT-4 / Claude 3 Opus; Kendall W 0–0.19; ceiling
effect; no didactic feedback loop.

**Contamination.** Human physician raters, not an in-family judge. Small
formative sample. Paper itself flags overreliance on scripted LLM behavior.

### 2. Haider et al. — Sensors (Basel) 2025
**ACCESS=open-pdf** · https://www.mdpi.com/1424-8220/25/14/4305/pdf · DOI 10.3390/s25144305

| Axis | Score |
|---|---|
| Overall | 0.87 · Std3 0.85 (lexical “100%”) |
| Uncertainty / certainty excess | 85 / 15 |
| Method failure (asserted) | 0 |

**Claims.** Four LLMs generate plastic-surgery consults; blinded human raters;
means >4.5/5; ANOVA non-significant; demographic homogeneity.

**Contamination.** Blinded clinicians, not an autorater. High ceiling +
non-significant ANOVA limit model-ranking claims. No independent diagnostic
accuracy endpoint.

### 3. Kyung et al. — PatientSim (arXiv / NeurIPS 2025)
**ACCESS=open-pdf** · https://arxiv.org/pdf/2505.17818

| Axis | Score |
|---|---|
| Overall | 0.88 |
| Uncertainty / certainty excess | 79 / 21 |
| Method failure (asserted) | **44** · contaminated grader + automation-bias hit |

**Claims.** MIMIC-grounded personas (37 combinations); eight LLM backbones;
Llama 3.3 70B selected; four clinicians later score 3.89/4.

**Contamination.** Paper **uses** an LLM-as-judge / LLM sentence classifier
(asserted). A later clinician audit does not un-contaminate the classifier.
This is the tooth that matches ResidencyRL / CRAFT-MD grader-AI.

### 4. Busch et al. — Communications Medicine 2025
**ACCESS=open-pdf** · https://www.nature.com/articles/s43856-024-00717-2.pdf · DOI 10.1038/s43856-024-00717-2 · PMC11751060

| Axis | Score |
|---|---|
| Overall | 0.90 |
| Uncertainty / certainty excess | **100 / 0** |
| Method failure (asserted) | 0 |

**Claims.** 89 studies; GPT-3.5/4 dominate; taxonomy of design and output
failures (non-reproducibility, incorrectness, unsafety, bias).

**Contamination.** Review of other systems. Correctly scores no asserted
method failure. Highest calibration in the batch.

### 5. Li — JMIR Medical Informatics 2025/26
**ACCESS=open-pdf** · https://doi.org/10.2196/79039

| Axis | Score |
|---|---|
| Overall | 0.90 |
| Uncertainty / certainty excess | 89 / 11 |
| Method failure (asserted) | 0 |

**Claims.** 39 VP history-taking studies; KG +16% top-k; hallucination
0.31–5%; small student/expert samples; MIMIC ICU bias.

**Contamination.** Field-level critique, not the authors’ own in-family grader.

### 6. Zohny et al. — Journal of Medical Ethics 2025
**ACCESS=open-html** · https://pmc.ncbi.nlm.nih.gov/articles/PMC7618332/ · DOI 10.1136/jme-2024-110256

| Axis | Score |
|---|---|
| Overall | 0.88 |
| Uncertainty / certainty excess | 76 / 24 |
| Method failure (asserted) | 0 |

**Claims.** GPT-4 can emulate Emanuel & Emanuel’s four communication models.
Risks: bias reinforcement, persuasion → manipulation, overreliance, liability.

**Contamination.** Ethics proof-of-concept. No LLM judge of clinical
correctness. Flags Standard 5-adjacent therapeutic-advice risk in prose.

### 7. Huo et al. — JAMA Network Open 2025
**ACCESS=open-html** · https://pmc.ncbi.nlm.nih.gov/articles/PMC11795331/ · DOI 10.1001/jamanetworkopen.2024.57879

| Axis | Score |
|---|---|
| Overall | 0.90 |
| Uncertainty / certainty excess | 89 / 11 |
| Method failure (asserted) | 0 |

**Claims.** 137 chatbot-health-advice studies; 99.3% closed-source; 65%
subjective success criteria; informed CHART.

**Contamination.** Documents that the literature uses subjective preference
instead of independent endpoints. Does not assert the authors’ own scores.

### 8. Saggar et al. — Archives of Disease in Childhood 2025
**ACCESS=open-pdf** · https://eprints.whiterose.ac.uk/id/eprint/238861/1/archdischild-2025-329846.full.pdf · DOI 10.1136/archdischild-2025-329846

| Axis | Score |
|---|---|
| Overall | 0.87 · Std3 0.85 |
| Uncertainty / certainty excess | 62 / **38** |
| Method failure (asserted, engine) | 0 |
| Method failure (human read) | ChatGPT examiner marks ChatGPT doctor |

**Claims.** Four paediatric OSCEs; PatientGPT / DoctorGPT / ExaminerGPT;
ExaminerGPT correlates with clinicians; moderate educational support.

**Contamination.** Same model family plays patient, doctor, and examiner.
Human–ExaminerGPT correlation does not make the examiner independent.
Engine miss: wording is “examiner agent,” not “autorater / LLM judge.”
This PR does not change `method_failure.py` (avoids colliding with PR #10).

### 9. Richter et al. — JMIR 2025/26
**ACCESS=open-html** · https://www.jmir.org/2026/1/e77307/PDF · DOI 10.2196/77307

| Axis | Score |
|---|---|
| Overall | **0.84** (lowest) · Std3 **0.70** |
| Uncertainty / certainty excess | 62 / **38** |
| Method failure (asserted) | 0 |

**Claims.** 10 studies; pooled empathy SMD +1.02; no long-term trust measure;
I² 73%. Authors also warn that overreliance could erode authentic empathy.

**Contamination.** Endpoint is perceived empathy, not correctness.
Persuasiveness without an accuracy endpoint is the Standard 3 tooth.

### 10. Luo et al. — npj Digital Medicine 2025
**ACCESS=open-pdf** · https://www.nature.com/articles/s41746-025-01841-6.pdf · DOI 10.1038/s41746-025-01841-6

| Axis | Score |
|---|---|
| Overall | 0.90 |
| Uncertainty / certainty excess | 70 / 30 |
| Method failure (asserted) | 0 |

**Claims.** Single-center RCT N=84; LLMDP +10.50 MHTA points (95% CI
4.66–16.33); greater empathy; BLEU/ROUGE used in model selection.

**Contamination.** Educational endpoint scored by human doctors. BLEU/ROUGE
can Goodhart fluency; that is model-selection, not the RCT grader.

## Reproduce

```bash
PYTHONPATH=. python -m implementation.python.batch_score \
  examples/calculator/patient_sim_2025/manifest.json --table-only

python3 -m implementation.web.app   # then paste an excerpt or upload a local PDF
```
