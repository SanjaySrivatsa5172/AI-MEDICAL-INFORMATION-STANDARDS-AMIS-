---
title: "CARE-Bench: Benchmarking Patient-Facing LLM Triage"
authors: "Hua Y, Na H, Ayubcha C"
journal: "arXiv preprint"
year: 2026
doi: "10.48550/arxiv.2608.03731"
pmid: ""
url: "https://arxiv.org/abs/2608.03731"
type: "preprint"
tier: "ancillary"
design-overlap: true
date-added: 2026-08-10
source: "websearch+scite-verified"
tags: [emergency-triage-ai, benchmark-methodology, ancillary, design-overlap, critical]
---
# CARE-Bench: Benchmarking Patient-Facing LLM Triage

**Hua Y, Na H, Ayubcha C** — *arXiv preprint* (2026)

> [!warning] Critical — design overlap
> This work overlaps the study design of the Cedars-Sinai protocol. Reference explicitly in methods differentiation.

> [!note] Clinical relevance
> Source-grounded benchmark evaluating sequential patient-facing triage as a four-label per-turn current-action task (500 cases, 1,059 patient-disclosure prefixes reconstructed from medical dialogue/consultation/follow-up-question sources); 11 models evaluated on 269 held-out rounds under unprompted and minimally prompted open-ended protocols. Unprompted macro-F1 only 31.2-50.4 across models; when the correct action was to ask for more information, only 33.5% of prompted outputs preserved that step, indicating patient-facing triage failures persist after prompting rather than resolving as a simple prompting problem. Directly on this protocol's core question (what action a patient-facing AI should direct given ambiguous/everyday symptom language) though grading uses a fixed LLM mapper rather than physician adjudication -- methodologically adjacent, not a physician-authored evaluation.

**Link:** https://arxiv.org/abs/2608.03731
**DOI:** `10.48550/arxiv.2608.03731`

Topics: Emergency triage AI · Benchmark methodology

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
