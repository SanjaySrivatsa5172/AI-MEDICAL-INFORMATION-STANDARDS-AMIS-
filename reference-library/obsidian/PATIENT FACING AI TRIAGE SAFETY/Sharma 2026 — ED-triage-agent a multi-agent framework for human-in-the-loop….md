---
title: "ED-triage-agent: a multi-agent framework for human-in-the-loop emergency triage"
authors: "Sharma K, Sivadas H, Edwards C, et al."
journal: "International Journal of Medical Informatics"
year: 2026
doi: "10.1016/j.ijmedinf.2026.106652"
pmid: "42612553"
url: "https://doi.org/10.1016/j.ijmedinf.2026.106652"
type: "journal-article"
tier: "ancillary"
design-overlap: false
date-added: 2026-08-19
source: "pubmed-verified"
tags: [emergency-triage-ai, benchmark-methodology, triage-standards, ai-safety-failure-modes, ancillary]
---
# ED-triage-agent: a multi-agent framework for human-in-the-loop emergency triage

**Sharma K, Sivadas H, Edwards C, et al.** — *International Journal of Medical Informatics* (2026)

> [!note] Clinical relevance
> Multi-agent LLM emergency-triage architecture (ED-Triage-Agent / ETA): five specialised agents orchestrated via LangGraph, grounded in the ESI Implementation Handbook v4 by retrieval-augmented generation, calibrated on 30 ESI Handbook Practice Cases. Two-phase design directly relevant to this protocol's endpoints: Phase 1 produces a provisional ESI-scaled acuity signal from SYMPTOM-ONLY data for pre-vital queue prioritisation (deciding who is seen next before vital signs exist -- an information-incomplete, symptom-text setting close to patient-facing lay-language triage); Phase 2 gives a criterion-linked ESI recommendation once vitals are available. On the external TRIAGEAGENT benchmark: Phase 1 76.39% exact-match (quadratic-weighted kappa 0.8787) with 95.52% high-priority sensitivity; Phase 2 87.04% exact-match (kappa 0.9090) with 0.00% significant over-triage and 0.46% significant under-triage (97.22% of misclassifications within +/-1 ESI level), versus 10.00% significant under-triage for a chain-of-thought baseline. Bears on Topic 1 (ESI-scaled undertriage/overtriage and high-priority sensitivity as safety endpoints; the CoT-vs-agentic contrast quantifies architecture-driven undertriage). CAVEAT: technical-feasibility study on standardized ESI Handbook / benchmark cases, not real ED data or clinician users; the authors state clinical utility, safety, and workflow integration remain to be established by prospective validation. Verified via PubMed metadata (source pubmed-verified); DOI not yet in Scite's index this run (brand-new), so no Scite editorialNotices check -- none can exist for a day-old article.

**Link:** https://doi.org/10.1016/j.ijmedinf.2026.106652
**DOI:** `10.1016/j.ijmedinf.2026.106652`
**PMID:** `42612553`

Topics: Emergency triage AI · Benchmark methodology · Triage standards · AI safety failure modes

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
