---
title: "Exposing the fragility of LLM reasoning through bias-inducing prompts: evidence from BiasMedQA"
authors: "Kim SH, Ziegelmayer S, Busch F, Mertens CJ, Keicher M, Adams LC, Bressem KK, Braren R, Makowski MR, Kirschke JS, Hedderich DM, Wiestler B."
journal: "BMJ Digital Health & AI"
year: 2026
doi: "10.1136/bmjdhai-2025-000189"
pmid: "42712292"
url: "https://doi.org/10.1136/bmjdhai-2025-000189"
type: "journal-article"
tier: "ancillary"
design-overlap: false
date-added: 2026-09-10
source: "pubmed+scite-verified"
tags: [ai-safety-failure-modes, benchmark-methodology, ancillary]
---
# Exposing the fragility of LLM reasoning through bias-inducing prompts: evidence from BiasMedQA

**Kim SH, Ziegelmayer S, Busch F, Mertens CJ, Keicher M, Adams LC, Bressem KK, Braren R, Makowski MR, Kirschke JS, Hedderich DM, Wiestler B.** — *BMJ Digital Health & AI* (2026)

> [!note] Clinical relevance
> Cognitive-bias / anchoring robustness benchmark for medical LLMs (TU Munich / Klinikum rechts der Isar), added under the search strategy's standing anchoring / false-reassurance / sycophancy / epistemic-resilience carve-out -- the same lane as the already-included MedMisBench (misleading-context resilience), MED-STRESS (clinical-pressure epistemic resilience, Xiao et al.), and the Ping medical-sycophancy study. Design: evaluates susceptibility to SEVEN established cognitive biases (the BiasMedQA public dataset, 1,273 clinical case vignettes) across Llama-3.3-70B, Qwen3-32B and Gemini-2.5-Flash plus their REASONING-enhanced variants, under a base prompt, a debiasing prompt, and a few-shot prompt; mixed-effects logistic regression on each model pair. Key findings bearing on Topic-1 anchoring: 'reasoning' did NOT consistently reduce vulnerability to bias-inducing prompts and in Llama-3.3-70B and Gemini-2.5-Flash reasoning AMPLIFIED vulnerability to several biases (only Qwen3-32B improved on one of seven); explicit debiasing and few-shot prompting significantly cut biased responses across all three; and Gemini-2.5-Flash's accuracy collapsed from 80.0-88.6% to 47.4-86.1% when exposed to four UNPUBLISHED bias-inducing prompts, exposing benchmark-contamination-masked brittleness. Bears on the protocol's anchoring failure mode (cf. Ramaswamy's social-anchoring OR 11.7 and the Jaarsma framing-bias contrast): it shows that the cognitive-bias fragility the protocol probes in patient-facing triage persists in current reasoning LLMs, that mitigation prompts help, and -- methodologically important for any LLM-triage benchmark -- that public bias benchmarks can be contaminated, so held-out/unpublished prompts are needed to measure true robustness. CAVEAT / why ancillary and NOT auto-alerted: it uses clinician-facing exam-style clinical vignettes (MedQA-lineage), not patient-facing everyday-language triage, and reports no ESI-style undertriage/harm metric or physician-authored dual-register design -- it is a cognitive-bias-robustness benchmark on the anchoring carve-out, not a benchmark that overlaps this protocol's specific patient-facing harm-weighted design (design_overlap false). Verified via PubMed (PMID 42712292; title/authors/venue/year/DOI confirmed) and Scite (authors Kim/Ziegelmayer/Busch, BMJ Digital Health & AI 2026;2(1):e000189, OA diamond cc-by-nc confirmed; no editorialNotices -- not retracted/corrected/flagged); source pubmed+scite-verified; no identifier invented.

**Link:** https://doi.org/10.1136/bmjdhai-2025-000189
**DOI:** `10.1136/bmjdhai-2025-000189`
**PMID:** `42712292`

Topics: AI safety failure modes · Benchmark methodology

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
