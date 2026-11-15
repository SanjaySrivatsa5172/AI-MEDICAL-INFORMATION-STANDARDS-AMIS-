---
title: "Large language models are unstable as autonomous medical evaluators across clinical tasks"
authors: "Carvalho E Silva M, Carvalho E Silva F, de Paula Gomes Nunes de Castro R, Gonçalves A, Figueiredo Delgado A"
journal: "Journal of the American Medical Informatics Association"
year: 2026
doi: "10.1093/jamia/ocag190"
pmid: "42995166"
url: "https://doi.org/10.1093/jamia/ocag190"
type: "journal-article"
tier: "ancillary"
design-overlap: false
date-added: 2026-11-08
source: "pubmed-verified"
tags: [ai-safety-failure-modes, emergency-triage-ai, benchmark-methodology, ancillary]
---
# Large language models are unstable as autonomous medical evaluators across clinical tasks

**Carvalho E Silva M, Carvalho E Silva F, de Paula Gomes Nunes de Castro R, Gonçalves A, Figueiredo Delgado A** — *Journal of the American Medical Informatics Association* (2026)

> [!note] Clinical relevance
> LLM-as-judge stability benchmark (JAMIA 2026) evaluating 10 LLMs (Claude, GPT, DeepSeek; 3 local open-source + 7 API) as autonomous evaluators across three tasks with human reference labels -- LiveQA-Med answer quality, PubMedQA appraisal, and Emergency Severity Index (ESI) triage on MIMIC-IV-Ext (n=256; 25,680 judgments). Evaluator performance was unstable across tasks (no model top-3 on all three; every model shifted >=3 rank positions between some task pair). Most relevant here: in the highest-stakes task, ESI level 1 (Resuscitation) cases were UNDER-TRIAGED in 89.1% of evaluations across ALL 10 models (range 70.2%-96.9%), with best triage agreement only reaching the human inter-rater range (Claude Opus quadratic-weighted kappa=0.60); the authors conclude emergency triage demands human oversight at the highest-acuity tier. Clinician/specialist-facing ESI benchmark (not lay patient-facing), included via the over/undertriage failure-mode branch; ancillary, design_overlap false. PubMed-verified (PMID 42995166); Scite editorialNotices unavailable this run (monthly limit) but the PubMed record carries no retraction/correction.

**Link:** https://doi.org/10.1093/jamia/ocag190
**DOI:** `10.1093/jamia/ocag190`
**PMID:** `42995166`

Topics: AI safety failure modes · Emergency triage AI · Benchmark methodology

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
