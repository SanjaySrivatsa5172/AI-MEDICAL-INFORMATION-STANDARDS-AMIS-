# Reference Library — Search Strategy

Living search specification for the daily-updated reference library supporting the
Cedars-Sinai research protocol **"Physician-Authored Evaluation of Patient-Facing
Artificial Intelligence in Emergency Triage"** (PI: S. Sanjay Srivatsa, MD;
Co-I: Keyur Pawaskar, MSc).

The library seeds from the references cited in the protocol packet and grows daily
with ancillary literature, past and present.

## Core Question Anchor

Every collected reference must bear on, or contextualize, the study's core question:

> **Can AI systems safely recognize when symptoms described in everyday language
> require emergency care?**

References that address the *lay-language / everyday-language* dimension — register
effects, health-literacy effects, free-text vs structured presentation, conversational
symptom description — are priority captures and must not be missed.

## Topics

1. **Emergency Triage AI Safety** — LLM/AI performance and safety in emergency
   triage: ESI level assignment, disposition prediction, undertriage/overtriage,
   critical-miss behavior, false reassurance, anchoring on benign explanations,
   escalation timing, symptom-checker urgency advice.
2. **Physician-Authored Evaluation of Patient-Facing AI** — evaluation frameworks
   where physicians author, grade, or adjudicate patient-facing AI outputs:
   physician-graded rubrics, expert panels, blinded scoring, adjudication ladders,
   human-comparator benchmarks, physician red-teaming.
3. **Combined study topic** — physician-authored evaluation of patient-facing AI
   *in emergency triage* (the intersection is the highest-value capture).

Supporting strands (tagged, lower priority): benchmark methodology and
contamination; triage ground-truth standards (ESI reliability, ACS
undertriage/overtriage norms); key-features assessment methodology; consumer
health-AI policy and regulation in clinical journals.

## Journal Coverage (priority order)

Scan all major medical journals **and their AI subsidiary journals**, including:

- **NEJM AI** and The New England Journal of Medicine
- **JAMA** and the JAMA Network AI channel (JAMA+ AI), JAMA Internal Medicine,
  JAMA Network Open, JAMA Pediatrics
- **The Lancet Digital Health** (the Lancet's AI/digital subsection) and The Lancet
- Nature Medicine, **npj Digital Medicine**, Nature, Communications Medicine
- BMJ, BMJ Digital Health & AI
- Annals of Emergency Medicine, Academic Emergency Medicine, American Journal of
  Emergency Medicine, JACEP Open, Western Journal of Emergency Medicine
- JAMIA, JAMIA Open, JMIR, PLOS Digital Health, Scientific Reports
- Preprint servers for early signal: medRxiv, arXiv (clinical relevance required)

## Inclusion Filter

- **Clinical bias**: studies must be clinical in orientation. Exclude highly
  technical ML/programming papers **unless there is clear clinical relevance**
  (e.g., benchmark contamination that invalidates published triage accuracy).
- Peer-reviewed articles, reviews, editorials/policy pieces in major clinical
  journals, guidelines, and clinically consequential preprints/conference papers.
- Emphasis on 2023–present; seminal older foundations (ESI handbook, key-features
  methodology, symptom-checker audits) retained as context.
- Check retraction/editorial notices before inclusion; never add retracted work
  without flagging.

## Daily Query Bank (rotate and vary phrasing)

- large language model AND (emergency triage OR emergency department disposition)
- ChatGPT/Claude/Gemini AND triage AND (safety OR accuracy OR undertriage)
- AI symptom checker AND (urgency OR triage) AND (accuracy OR safety)
- patient-facing AI / consumer health chatbot AND physician evaluation
- physician-graded rubric AND large language model
- LLM AND (false reassurance OR anchoring OR sycophancy) AND health advice
- lay language OR health literacy OR patient phrasing AND LLM medical advice
- benchmark contamination AND medical LLM evaluation
- Emergency Severity Index AND (reliability OR validity OR mistriage)
- conversational AI diagnosis AND physician comparison

## Dedupe & Provenance Rules

- Identity key: DOI (preferred) → PMID → normalized title.
- Never overwrite `date_added`; new finds get the run date.
- `tier: core` = cited in the protocol packet; `tier: ancillary` = collected.
- Every entry records `source` (protocol / pubmed / scite / manual).

## Cadence

- One automated scan per day (morning US Pacific). Each run: execute query bank
  variants for anything new since the last scan, verify metadata, dedupe against
  `library.json`, append, regenerate `dashboard.html`, republish the dashboard
  artifact, commit and push.
