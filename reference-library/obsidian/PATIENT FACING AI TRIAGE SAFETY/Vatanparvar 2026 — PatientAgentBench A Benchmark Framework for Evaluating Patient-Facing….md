---
title: "PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents"
authors: "Vatanparvar K, Joshi A, Xenochristou M, et al."
journal: "arXiv"
year: 2026
doi: "10.48550/arxiv.2607.25485"
pmid: ""
url: "https://arxiv.org/abs/2607.25485"
type: "preprint"
tier: "ancillary"
design-overlap: false
date-added: 2026-10-03
source: "scite-verified"
tags: [patient-facing-ai, benchmark-methodology, emergency-triage-ai, ancillary]
---
# PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents

**Vatanparvar K, Joshi A, Xenochristou M, et al.** — *arXiv* (2026)

> [!note] Clinical relevance
> Benchmark framework for PATIENT-FACING health AI agents: a foundation model wrapped in an agent with a sandbox of healthcare tools (scheduling, prescriptions, telehealth, escalation) holds multi-turn conversations with a simulated patient and is scored by an LLM-as-a-Jury across six dimensions using 100+ conversation-agnostic, clinician-grounded criteria; licensed clinicians annotated shared conversations for validation (79-93% adjacent jury-vs-expert agreement, on par with or exceeding clinician inter-rater agreement). 10 models over 1,200 scenarios. TRIAGE QUALITY is the single most discriminating dimension (pass rates 32% weakest -> 88% strongest), with care-level recommendations spanning a five-tier hierarchy from EMERGENCY (911/ER) through urgent care, primary care, telehealth, to self-care; a named frontier failure mode is 'omitted crisis resources in an emergency.' Relevant to physician-grounded rubric design and escalation/triage behaviour in patient-facing AI (the protocol's digital-front-door anchor). CAVEAT / why ancillary and design_overlap FALSE: primary-care-general (not emergency-specific), SYNTHETIC patients, and LLM-as-Jury scoring rather than physician adjudication -- it complements, and does not overlap, the protocol's physician-authored harm-weighted emergency design; same posture as the library's other patient-facing benchmark entries (CARE-Bench, MedTriage). RECOVERED from the 2026-10-03 fresh-session scan (which tagged source 'websearch' with doi/pmid null and authors 'Amazon Science et al.'); INDEPENDENTLY VERIFIED via Scite (DOI 10.48550/arXiv.2607.25485 confirmed; OA green with byte-matching abstract; authors CORRECTED to Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou; NO editorialNotices) and PubMed convert_article_ids returned NO record (arXiv not PubMed-indexed, pmid null). Corrected the scan's invalid topic tag 'physician-authored-evaluation' (dropped -- scoring is LLM-as-Jury; clinicians only ground/validate the rubric, they do not adjudicate) and its vague author field; source upgraded websearch -> scite-verified; no identifier invented.

**Link:** https://arxiv.org/abs/2607.25485
**DOI:** `10.48550/arxiv.2607.25485`

Topics: Patient-facing AI · Benchmark methodology · Emergency triage AI

Index: [[00 INDEX — Patient-Facing AI Triage Safety]]
