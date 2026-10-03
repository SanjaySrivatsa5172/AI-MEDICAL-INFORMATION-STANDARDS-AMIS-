---
title: "OpenEvidence errs on the safe side in a structured test of triage recommendations"
authors: "Jia E, Omar M, Barash Y, Brook OR, Ahmed M, Kruskal JB, Gorenshtein A, Klang E."
journal: "International Journal of Medical Informatics"
year: 2026
doi: "10.1016/j.ijmedinf.2026.106687"
pmid: "42673790"
url: "https://doi.org/10.1016/j.ijmedinf.2026.106687"
type: "journal-article"
tier: "ancillary"
design-overlap: true
date-added: 2026-09-01
source: "pubmed+scite-verified"
tags: [emergency-triage-ai, ai-safety-failure-modes, physician-evaluation, benchmark-methodology, ancillary, design-overlap, critical]
---
# OpenEvidence errs on the safe side in a structured test of triage recommendations

**Jia E, Omar M, Barash Y, Brook OR, Ahmed M, Kruskal JB, Gorenshtein A, Klang E.** — *International Journal of Medical Informatics* (2026)

> [!warning] Critical — design overlap
> This work overlaps the study design of the Cedars-Sinai protocol. Reference explicitly in methods differentiation.

> [!note] Clinical relevance
> DIRECT COMPANION to the standing Ramaswamy alert (#1, resolved): this study re-runs the IDENTICAL structured triage-safety benchmark that produced Ramaswamy's ChatGPT Health finding (51.6% emergency under-triage + social-anchoring susceptibility) -- the protocol's foundational result -- on OpenEvidence, a retrieval-augmented PHYSICIAN-FACING clinical-decision-support platform, to ask whether the failure mode is platform-general or deployment-context-specific. BRIDGE GenAI Lab / Beth Israel Deaconess-Harvard (Jia, Omar, ... Klang senior; same group as the Omar 2026 register-framing work). Design: 60 clinician-authored vignettes from 30 scenarios across 21 domains, each written with/without objective clinical data and crossed with demographic + contextual modifiers in a 2x2x2x2 factorial (960 prompts: 480 clear-case, 480 edge-case); responses classified vs a clinician gold standard as CORRECT / UNDER-triage / OVER-triage / EVIDENCE-SEEKING REFUSAL; cluster-bootstrap + mixed-effects logistic regression + Holm-Bonferroni. Results (clear-case, 449 recommending responses): accuracy 71.3%; OpenEvidence UNDER-triaged only 12.5% of emergencies vs 51.6% for ChatGPT Health, but OVER-triaged 68.0% of nonurgent 'Home' presentations (ChatGPT Health 64.8%); ANCHORING statements did NOT change recommendations (OR 1.08, 95% CI 0.62-1.88; Holm p=1.0) -- i.e. anchoring-RESISTANT, opposite to ChatGPT Health; adding objective clinical data ELIMINATED emergency under-triage (25%->0%; p=0.005) and reduced nonurgent over-triage (78.7%->57.8%; p=0.014); the platform declined to assign a triage level in 6.8% (65/960), exclusively in symptom-only Home/Routine prompts. Bears directly on Topic 1 and on the interpretation of alert #1: it shows the 51.6% undertriage figure is strongly DEPLOYMENT-CONTEXT-dependent (physician-facing RAG CDS under-triages ~4x less and resists anchoring), reframes the primary safety endpoint around the symptom-only-vs-data-complete axis (cf. ED-triage-agent pre-vital vs post-vital), and formalizes EVIDENCE-SEEKING REFUSAL as a distinct output category needing its own clinical assessment. design_overlap flagged TRUE (same structured triage-safety benchmark lineage / under-over-triage + anchoring + factorial-modifier design as the Ramaswamy alert the protocol is built around). CAVEAT / why NOT auto-alerted: OpenEvidence is PHYSICIAN-facing CDS, not patient-facing everyday-language; the direction is FAVORABLE/reassuring (fewer missed emergencies); and this is a methods-differentiation/replication that supports evaluating health AI within its deployment context, not a benchmark that scoops the protocol's specific patient-facing dual-register harm-weighted design -- SURFACED to the PI as a companion to alert #1 for an escalation decision, handled like the Patwardhan/Verily PHA (design_overlap:true, PI-decision-pending, not auto-fired). Verified via PubMed metadata (PMID 42673790) and Scite (authors Jia/Omar/Barash confirmed; no editorialNotices -- not retracted/corrected/flagged); source pubmed+scite-verified.

**Link:** https://doi.org/10.1016/j.ijmedinf.2026.106687
**DOI:** `10.1016/j.ijmedinf.2026.106687`
**PMID:** `42673790`

Topics: Emergency triage AI · AI safety failure modes · Physician evaluation · Benchmark methodology

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
