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

Scan all major medical journals **and their AI subsidiary journals**. The curated
**digital.health/journals** index (28 titles — full snapshot in
`journal-directory.json`, as of 2026-08-11) is the authoritative source set; the
emergency-medicine journals are additional (not on that index but essential for this
triage study).

**Marquee clinical + AI (highest yield):**

- **NEJM AI** and The New England Journal of Medicine; **NEJM Catalyst** Innovations in Care Delivery
- **JAMA** + JAMA Network AI (JAMA+ AI), JAMA Internal Medicine, **JAMA Network Open**, JAMA Pediatrics
- **The Lancet Digital Health** and The Lancet
- **Nature Medicine**, **npj Digital Medicine**, Nature, Communications Medicine, **Cell Reports Medicine**
- **The BMJ**, **BMJ Health & Care Informatics**
- **JAMIA**, JAMIA Open, **Journal of Biomedical Informatics**, **International Journal of Medical Informatics**, **Applied Clinical Informatics**, **IEEE JBHI**, **Artificial Intelligence in Medicine**
- **JMIR**, **JMIR AI**, **JMIR mHealth and uHealth**, **PLOS Digital Health**, **Digital Health (SAGE)**, **Frontiers in Digital Health**
- **Telemedicine and e-Health**, **Digital Biomarkers**, **Digital Medicine** (Wolters Kluwer / ISDM), **International Journal of Digital Healthcare**, **Health Affairs**, **Learning Health Systems**, **Mayo Clinic Proceedings: Digital Health**
- Scientific Reports

**Emergency medicine (this study's core clinical venues — not on the digital.health index):**

- Annals of Emergency Medicine, Academic Emergency Medicine, American Journal of
  Emergency Medicine, JACEP Open, Western Journal of Emergency Medicine

**Databases (digital.health `#databases`):** PubMed (NIH/NLM — verification + recency
sweeps, already in use); **ClinicalTrials.gov** (NIH — new angle: sweep for
active/completed trials or benchmarks matching the protocol design, an Urgent-Alert
trigger).

**Preprint servers for early signal:** medRxiv, arXiv (cs.LG / q-bio) — clinical
relevance required.

### External coverage source — digital.health/journals (PI directive, 2026-08-14)

The curated directory at <https://digital.health/journals> (Daniel Kraft, MD;
~27 peer-reviewed digital-health / AI-in-medicine / telehealth / informatics
journals) is an authoritative source for expanding the coverage list above. It is a
*journal directory*, not an article feed, so it changes rarely — the daily value is
ensuring the article scan covers every journal on it, not re-reading the directory.

**Access note:** `digital.health` is blocked by this environment's network egress
allowlist; direct fetch fails until the domain is allowlisted (PI action in
progress, 2026-08-14). Do **not** route around the egress policy — if the fetch is
still blocked, skip this step for the run and note it.

**Initial snapshot captured 2026-08-14** from a PI-uploaded PDF of the page (28
journals + the PubMed / ClinicalTrials.gov databases + medRxiv / arXiv), stored in
`journal-directory.json`; the Journal Coverage list above already reflects it. The
fetch procedure below therefore now serves **auto-refresh**: the index is
editorially reviewed ~twice yearly, so re-fetch once `digital.health` is allowlisted
and act only when the snapshot diff is non-empty.

**Procedure — attempt once per reconciler run; execute only when reachable:**

1. Fetch `digital.health/journals`; extract each journal (name + homepage link).
2. Snapshot to `reference-library/journal-directory.json` (record the fetch date).
3. Diff against the Journal Coverage list above; add any journal not already
   covered, then do a one-time backfill sweep of each newly-added journal's recent
   clinically-relevant articles (verified via PubMed/Scite, deduped by
   DOI → PMID → normalized title).
4. Re-check daily but **act only when the directory diff is non-empty** — no churn
   on identical days. Commit any coverage or library change with its own note.

The directory widens the *source set*, not the relevance bar: articles are still
filtered by the Core Question Anchor and the Inclusion Filter below. Only the
`/journals` slice feeds this library; the sibling `/resources`, `/books`,
`/podcasts`, and `/programs` pages are not article sources.

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
- named consumer health AI products AND (triage OR safety OR evaluation) —
  e.g. "ChatGPT Health", Gemini/Med-Gemini health features, AMIE, Claude health
  uses, Grok (xAI), Meta AI health queries (the Ramaswamy Nature Medicine
  ChatGPT Health stress test was found via product-name search, not generic
  LLM-triage terms — always include this angle; patients use whatever consumer
  chatbot is at hand, not only health-branded ones)

## Dedupe & Provenance Rules

- Identity key: DOI (preferred) → PMID → normalized title.
- Never overwrite `date_added`; new finds get the run date.
- `tier: core` = cited in the protocol packet; `tier: ancillary` = collected.
- Every entry records `source` (protocol / pubmed / scite / manual).

## Single-Writer Policy (PI directive, 2026-08-15)

To end multi-session write conflicts (dashboard 409s / forked `library.json`),
exactly **one** session is the canonical writer of this reference library.

- **Canonical writer:** the reference-library reconciler main session (persistent;
  reconciler trigger `trig_01VkgTjn9QapNNosjrWmVvem`). It ALONE may commit
  `reference-library/library.json` and publish / republish the dashboard artifact
  `528465e1-0a3b-40aa-81ab-00373aaa2461`.
- **Every other session** — the fresh-session daily scan, `session_019fsE75`
  (PR #2 Cedars redraft), and any future session — must treat `library.json` and
  the dashboard artifact as **READ-ONLY**. They may *propose* candidate references
  (in a scan report or PR comment) but must **NOT** write `library.json` or publish
  the artifact.
- The canonical writer performs the whole pipeline atomically: scan → verify
  (PubMed/Scite, else WebSearch) → dedupe → write → build → commit/push → republish.

Rationale: git push and Artifact publish both succeed only from the persistent
reconciler session; fresh-session scans cannot push (403) and their artifact
publishes are the sole source of the forks. One writer removes the conflict.
Mechanical enforcement (switching off the separate daily-scan trigger and folding
the scan into the canonical writer) is tracked separately with the PI.

## Urgent Alert Protocol

A newly found reference is **major** when it would plausibly require addition to or
alteration of this trial, or has specific bearing on its results. Triggers include:

- Publication of a benchmark or trial closely matching this protocol's design
  (physician-authored triage scenarios, dual-register presentation, harm-weighted
  scoring, or a Critical-Miss-Rate-style primary endpoint).
- New evidence directly affecting the primary endpoint's interpretation (e.g.,
  contamination findings invalidating ESI-based LLM triage results, or major lay-
  vs-expert register performance findings in frontier models).
- Regulatory or policy action governing patient-facing AI triage.
- Retraction or correction of any reference cited in the protocol.

When a major reference is found, the daily scan must, in addition to normal
library entry (with `design_overlap` as applicable):

1. Append an entry to `meta.alerts` in `library.json`
   (`{date, headline, detail, doi, url, resolved: false}`) — this renders an
   urgent red banner at the top of the dashboard until marked `resolved`.
2. Create a Gmail draft addressed to **drsanjaysrivatsa@gmail.com** with subject
   `[URGENT — AI Triage Study] <headline>` summarizing the finding, its bearing
   on the trial, and the recommended action (drafts require a manual send).
3. Send a push notification summarizing the alert.

## Cadence

- One automated scan per day (morning US Pacific). Each run: execute query bank
  variants for anything new since the last scan, verify metadata, dedupe against
  `library.json`, append, regenerate `dashboard.html`, republish the dashboard
  artifact, commit and push.
