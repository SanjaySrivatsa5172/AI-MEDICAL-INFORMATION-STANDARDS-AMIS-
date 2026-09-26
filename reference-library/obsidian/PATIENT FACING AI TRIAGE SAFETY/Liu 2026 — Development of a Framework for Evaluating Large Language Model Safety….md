---
title: "Development of a Framework for Evaluating Large Language Model Safety and Reliability: a Proof-of-Concept Evaluation"
authors: "Liu F, Liu Z, Fei X, et al."
journal: "Journal of Medical Systems"
year: 2026
doi: "10.1007/s10916-026-02459-1"
pmid: "42776332"
url: "https://doi.org/10.1007/s10916-026-02459-1"
type: "journal-article"
tier: "ancillary"
design-overlap: false
date-added: 2026-09-24
source: "pubmed-verified"
tags: [benchmark-methodology, ai-safety-failure-modes, emergency-triage-ai, ancillary]
---
# Development of a Framework for Evaluating Large Language Model Safety and Reliability: a Proof-of-Concept Evaluation

**Liu F, Liu Z, Fei X, et al.** — *Journal of Medical Systems* (2026)

> [!note] Clinical relevance
> Physician-scored LLM-safety EVALUATION-METHODOLOGY paper applied to EMERGENCY cases, from an emergency-medicine group (Dept. of Emergency, Xuanwu Hospital / Capital Medical University, Beijing) -- directly on the protocol's benchmark-methodology + ai-safety-failure-modes axes and its central methodological thesis that aggregate accuracy is inadequate for safety and that evaluation must be HARM-WEIGHTED and failure-mode-resolved. Design: the authors build a framework that scores LLM safety/reliability by CATASTROPHIC-FAILURE FREQUENCY and RESPONSE REPRODUCIBILITY (rather than aggregate accuracy), using a pre-specified error taxonomy, difficulty-stratified analysis, and two-layer response consistency, explicitly motivated by Software-as-a-Medical-Device (SaMD) and EU AI Act deployment frameworks. It was applied to 54 diagnostically challenging EMERGENCY cases from non-public institutional records; 6 LLMs were queried 3x each (text-only, zero-shot, defaults; Aug-Dec 2025) yielding 972 PHYSICIAN-SCORED responses. Findings bearing on the protocol's harm-weighted premise: aggregate scores concealed heterogeneity -- ANCHORING-BIAS failure (score <=3) varied ~4-fold across models (6.9%-26.4%) and rare-disease recognition ~6-fold (6.1%-37.9%); CATASTROPHIC (dangerous-recommendation, score <=2) rates were two-tiered (1.5% for the safest two models vs 6.0% for the rest; p<0.001); and 31 of 34 dangerous model-case combinations were STOCHASTIC rather than systematic -- a failure mode invisible to aggregate metrics and only exposed by reproducibility profiling (GPT-5.1 was middle-tier on mean accuracy yet least reproducible, within-case SD 2.69, and fell in the higher catastrophic-failure tier). Bears on the protocol's design rationale that a patient-facing emergency-triage evaluation must weight dangerous misses and measure consistency, not just mean accuracy, and that anchoring bias is a first-class failure mode to quantify. CAVEAT / why ancillary and design_overlap FALSE: this is a CLINICIAN-FACING clinical-decision-support evaluation (text-only diagnostic-reasoning on emergency cases, physician-scored), NOT a patient-facing lay-language triage/disposition study, and it is a single-centre proof-of-concept (54 cases, 6 models); it therefore COMPLEMENTS -- and does not overlap -- the protocol's physician-authored, dual-register (lay vs clinical), harm-weighted, patient-facing triage-accuracy design (design_overlap false). It is a methodology sibling in the same ancillary posture as the library's other harm-weighted emergency safety benchmarks (e.g. the NOHARM clinical-safety benchmark and the PrIME-LLM incomplete-information reasoning benchmark), not the protocol's design twin. NOT auto-alerted: a methodology contribution CONSISTENT with (reinforcing, not overturning) the protocol's premise that aggregate accuracy hides catastrophic LLM failures; it is neither a regulatory action nor a retraction and does not overturn the primary endpoint's interpretation. Verified via PubMed (PMID 42776332; title/authors [Liu F, Liu Z, Fei X, He J, Xing J, Li J, Chan P]/venue [J Med Syst 2026;50]/DOI 10.1007/s10916-026-02459-1 confirmed; article_type Journal Article; no correction/retraction on the record); Scite has not yet indexed the day-old DOI so editorialNotices could not be pulled and a day-old article cannot carry a retraction; source pubmed-verified; no identifier invented.

**Link:** https://doi.org/10.1007/s10916-026-02459-1
**DOI:** `10.1007/s10916-026-02459-1`
**PMID:** `42776332`

Topics: Benchmark methodology · AI safety failure modes · Emergency triage AI

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
