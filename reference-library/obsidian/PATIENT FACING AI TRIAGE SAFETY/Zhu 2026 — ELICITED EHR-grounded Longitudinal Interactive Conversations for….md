---
title: "ELICITED: EHR-grounded Longitudinal Interactive Conversations for Information-seeking Triage Evaluation and Decision-making"
authors: "Zhu H, Shi X, Zhou J."
journal: "arXiv"
year: 2026
doi: "10.48550/arxiv.2608.09024"
pmid: ""
url: "https://arxiv.org/abs/2608.09024"
type: "preprint"
tier: "ancillary"
design-overlap: false
date-added: 2026-09-30
source: "scite-verified"
tags: [emergency-triage-ai, benchmark-methodology, ancillary]
---
# ELICITED: EHR-grounded Longitudinal Interactive Conversations for Information-seeking Triage Evaluation and Decision-making

**Zhu H, Shi X, Zhou J.** — *arXiv* (2026)

> [!note] Clinical relevance
> arXiv preprint introducing EHR2Dial-Triage, an agentic conversation-generation framework and BENCHMARK for CONVERSATIONAL emergency-department triage grounded in MIMIC-IV-ED -- on Topic 1's interactive-information-gathering dimension (how acuity is established through focused conversation, not just from a fixed snapshot). The authors argue most existing ED benchmarks evaluate acuity prediction from a fixed clinical snapshot and miss the interactive process by which triage-relevant evidence is elicited; EHR2Dial-Triage instead constructs triage conversations under explicit role-based and TEMPORAL information boundaries, linking each accepted patient disclosure to its supporting EHR event and to the first dialogue turn at which it becomes available, and supports controlled evaluation of INFORMATION ELICITATION, evidence use, FIVE-LEVEL EMERGENCY SEVERITY INDEX (ESI) prediction, and patient communication across models and patient personas. Bears on the protocol's core question (conversational symptom disclosure -> acuity/ESI; identifying information gaps and asking appropriate follow-ups; communicating the plan and deterioration-reporting to the patient). CAVEAT / why ancillary and design_overlap FALSE: the scenarios are EHR-DERIVED (MIMIC-IV-ED) with agentic/LLM-generated conversations rather than physician-authored dual-register lay-language cases, and the benchmark targets ESI-prediction + elicitation quality rather than a harm-weighted undertriage/critical-miss endpoint -- it complements, does not overlap, the protocol's design (design_overlap false), same ancillary posture as the CARE-Bench patient-facing-triage benchmark. NOT auto-alerted: a benchmark contribution consistent with the protocol's premise; not a regulatory action or retraction. RECOVERED from the 2026-09-30 fresh-session scan (added to the dashboard with source 'websearch' and an invalid topic tag 'benchmark', then not pushed to git); this run INDEPENDENTLY VERIFIED it via Scite (DOI 10.48550/arxiv.2608.09024 indexed; authors [Haohao Zhu, Xiaolin Shi, Jiayu Zhou] confirmed; full abstract byte-matched; NO editorialNotices -- not retracted/corrected/flagged), corrected the topic tag to benchmark-methodology; arXiv preprint, not PubMed-indexed so pmid stays null; source upgraded websearch -> scite-verified; no identifier invented.

**Link:** https://arxiv.org/abs/2608.09024
**DOI:** `10.48550/arxiv.2608.09024`

Topics: Emergency triage AI · Benchmark methodology

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
