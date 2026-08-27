# CONTEXT MEMORY — Cedars-Sinai LLM Safety Protocol

> **Resume phrase:** the PI resumes this work by saying **"LLM SAFETY PROTOCOL"** or
> **"CEDARS SINAI LLM SAFETY PROTOCOL"**. On either phrase, read this file end to end
> before doing anything else, then confirm state with `git log` and the open items in §9.
>
> **Last updated:** 21 August 2026 · **Maintainer:** update this file whenever a
> decision closes, a document version changes, or a standing rule is set.

---

## 1. What this project is

**Study title:** LLM Safety and Medical Reasoning Assessment
**Scientific title:** Physician-Authored Evaluation of Patient-Facing Artificial
Intelligence in Emergency Triage

**The core question.** When a patient describes symptoms in ordinary everyday language to a
large language model, does the model reliably recognize the presentations that require
emergency care? Not "does it pass a medical exam" — the question is whether it fails safely
at the point of first contact, where a person with no clinical training is the one typing.

**Why it is not already answered.** Three failures of transfer:
1. **Format.** Benchmarks are multiple-choice; patients are not.
2. **Contamination.** Public benchmarks are in the training data; performance on them is
   not evidence about novel presentations.
3. **Register.** Benchmarks are written in expert clinical prose; patients speak in lay
   narrative. The register shift is itself a distribution shift, and it is untested.

**Why triage specifically.** Triage has a defensible asymmetric loss function that most
clinical AI tasks lack. In acute coronary syndrome the accepted operating point is
**under 5% undertriage against as much as 35% overtriage** — the field has already decided
that missing is far worse than over-calling. That asymmetry is what makes a safety endpoint
constructible rather than arbitrary.

**Status:** in preparation for Cedars-Sinai IRB submission. Not yet filed. Filing is
blocked on §9.

---

## 2. People

| Role | Person | Contact / note |
|---|---|---|
| Principal Investigator | **S. Sanjay Srivatsa, MD**, FACC, FSCAI, MRCP (London), DABVLM | drsanjaysrivatsa@gmail.com · Director, HAV Center of Fresno, Fresno CA |
| Co-Investigator | **Keyur Pawaskar, MSc** (Computer Science) | pawaskarkeyur96@gmail.com |
| Additional investigator | CSU Fresno investigator | Named in the April 2026 packet; **name and role still to be confirmed** |
| Institutional sponsor / routing | **Michael E. Farkouh, MD** | Vice Dean, Research & Clinical Trials, Cedars-Sinai. See INPUT 2 — Amendment 1 called him "IRB chair" and is likely wrong |
| Collaborator | **Brennan Spiegel, MD, MSHS** | Cedars-Sinai |
| Reviewing IRB | Cedars-Sinai Medical Center | Pathway undetermined: exemption vs expedited |

**Email routing rules in force (PI-set):**
- Weekly-review *proposals* go to the PI only.
- When the PI *approves* changes, the record of what was approved goes to **Keyur
  (cc PI)** — with the literature justification, the approval wording and date, the commit
  SHA, document versions, **and the live dashboard link**. Approval emails, never proposals.

---

## 3. Where everything lives

**Repository:** `sanjaysrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-`
Local path `/home/user/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-`
**Working branch: `claude/cedars-sinai-safety-protocol-0gb0wg`** — never push elsewhere
without explicit permission. Open **draft PR #2**.

Note: this repository is primarily the **AMIS (AI Medical Information Standards)** project —
`README.md`, `SPECIFICATION.md`, `standards/*.yaml`, `implementation/python/`. The Cedars
protocol is a sub-package under `docs/`. Do not assume the whole repo is the protocol.

### Protocol documents (the deliverables)

| File | What it is |
|---|---|
| `docs/protocol/PROTOCOL_v3_CONSOLIDATED.md` | **The protocol of record.** v3.1, 21 Aug 2026, 22 pp. §0–§14 plus Appendix A (tables) and Appendix B (scenario authoring spec) |
| `docs/protocol/Protocol_v3_Consolidated.docx` / `.pdf` | Built deliverables |
| `docs/protocol_scientific_introduction_v3.md` | Scientific Introduction v3, 20 pp / ~7,555 words (April version was 10 pp / 3,698 words) |
| `docs/Protocol_Scientific_Introduction_v3.docx` / `.pdf` | Built deliverables |
| `docs/protocol/PHYSICIAN_ONBOARDING_BRIEFING.md` | "Why This Study, and Why Now" — 8 pp, ~2,359 words, for general physicians reviewing the protocol. Nine sections, ends with the clinical bottom line |
| `docs/protocol/Physician_Onboarding_Briefing.docx` / `.pdf` | Built deliverables |
| `docs/irb_letter_farkouh_v2.md` + `.docx`/`.pdf` | Cover letter to Farkouh. Enclosure list is written as a **complete replacement package** because Cedars holds only April |
| `docs/cedars_ramaswamy_nm2026_redraft_plan.md` | Redraft plan; §2.11 = Sheng verification record, §3.6 = traced edits |
| `docs/protocol/weekly_reviews/` | Weekly agent: `README.md` (method), `state.json` (watermark), dated review files, `proposed_edits_*.patch` |
| `reference-library/library.json` | 172 references. **Strict 14-key schema** — see §7 |

### Documents that do NOT exist (searched for, not found — do not wait on them)
`Protocol_v2_Amendment1.docx` and `Protocol_Tables_All.docx`. The PI confirmed on
21 Aug 2026: *"i searched — i dont have these."* Amendment 1 (11 changes, 23 July 2026) and
Addendum A (methods hardening, 1 Aug 2026) survive only as their change lists, which are
incorporated into the consolidated protocol. Appendix A tables were therefore **constructed**
from the protocol body, not reproduced — this is disclosed in a provenance note at the head
of the appendix. Tables numbered 5 and 6 in the record remain unaccounted for.

### What Cedars-Sinai actually holds
**Only the April 2026 package**, established with certainty via MD5, embedded PDF
timestamps, and the Gmail chronology:
- Research Submission Packet (9 April 2026)
- Scenario Author Briefing (14 April 2026)
- Scientific Introduction, first version (14 April 2026, 10 pp)

**Amendment 1, Addendum A, and the entire 2026 evidence revision were never transmitted.**
Consequence: the consolidated protocol conflicts with nothing in the Cedars file. It is the
first full protocol they will receive and it supersedes the April condensed version outright.
(An earlier warning in this project about a lineage conflict was overstated and has been
retracted.)

---

## 4. The study design

### Endpoints
- **Primary: Critical Miss Rate** — failure to recommend ED or EMS evaluation when the
  physician-defined gold standard requires urgent escalation.
- **Secondary:** Failure Severity Index · Anchoring Failure Rate · Time-to-Escalation ·
  Human–LLM Degradation Gap.

### Design
Cross-sectional, physician-authored, **dual-register** benchmark with a three-arm
comparative architecture. **50 final scenarios** (60–70 drafted), each written in both a
**lay narrative** and an **expert vignette** register — the register contrast is the
distribution-shift probe, not decoration. Duration **22 weeks** (Amendment 1 added 2).

### Arms
| Arm | What it measures |
|---|---|
| **A** | Model alone |
| **B** | Physician benchmark (the comparator that makes model numbers interpretable) |
| **C** | Human–LLM interaction |
| **C1** | Exploratory longitudinal interaction, counterbalanced sub-arm — **in/out of scope is DECISION 4** |

### Four non-overlapping physician panels
Authoring · gold-standard (Delphi) · answering · scoring. The separation is a hard
independence rule, not a convenience — §5.4.

### Scenario methodology
**Key Features Question** methodology (Medical Council of Canada; Page & Bordage), including
**killer items** and severity weights **SW 1–3**. Disposition scale: EMS NOW / ED NOW /
Urgent Care / PCP Follow-up / Reassurance. Appendix B carries the seven components, the
syndrome coverage map, and a worked example (atypical ACS in an elderly diabetic).

### Scoring architecture — three layers with explicit authority
| Layer | Weight | Authority |
|---|---|---|
| Deterministic escalation phrase-inventory rule set | ~40% | Mechanical |
| **LLM jury** — ≥3 cross-vendor, version-pinned, majority verdict | ~30% | **Subordinate and provisional** |
| Physician scoring | ~30% | **Sovereign** |
Three-tier adjudication in §7.5.

### The two falsifiable jury acceptance gates
1. **Jury–physician agreement ≥ inter-physician agreement** (NOHARM logic).
2. **Gwet AC1 ≥ 0.75** — DECISION 2.

**Known crux (worked out in-session, unresolved):** Gate 1 does catch correlated judge error,
*provided* the error runs in a direction physicians reject. Two real residual gaps remain:
(a) the gates pass **on average** over a validation sample, while correlated error would
concentrate in the atypical-catastrophe / benign-anchor tail — exactly where the study's
value lies; and (b) "majority verdict" does not distinguish 3–0 from 2–1. (The "Afrasyab
inter-judge Fleiss κ = 0.65" figure formerly cited here is STRUCK — arXiv 2607.18828 is
content-denied, absent from PubMed, and unreachable; the figure is unverifiable, not merely
secondary-source. The verifiable bounding case is Byun et al., *J Med Syst* 2026, PMID
42481841: three frontier verifiers on clinical reasoning coherence, Fleiss κ 0.087–0.223 —
different generators and task, cite as bounding only, never as a planning parameter.) **Proposed inversion, not yet adopted:** high jury agreement is
not self-evidently good — pre-register an agreement *band* benchmarked against
inter-physician disagreement, rather than a floor. §7.3 carries `[PENDING — jury robustness
amendment]`.

### Statistics
Mixed-effects logistic regression · McNemar / conditional logistic · Benjamini–Hochberg FDR ·
TRIPOD-LLM reporting.
**§8.4 is BLOCKING and says so plainly: "No power figures may be stated at this revision."**
DECISION 1 invalidates the existing power calculation if adopted, and the sample-size
justification cannot be written until pilot data exist.

### Human subjects
**No patients. No PHI.** Physicians across four panels, plus lay adult participants in the
interaction arm. Minimal risk. De-identified physician-authored composite scenarios only.

### Regulatory frame
EU AI Act Art. 72 · FDA PCCP guidance (Aug 2025) · IMDRF N81/N88 · NIST AI RMF 1.0 ·
WHO LMM guidance. Sheng et al.'s **S1–S4** deployment safety classification is used to
position the work: this is an **S2-grade instrument aimed at an S3-tailed hazard**.

---

## 5. Evidence base — the load-bearing citations

**Verified, peer-reviewed:**
- **Omar et al., *Rheumatology* 2026 (PMID 42587430)** — a dismissive referral-note anchor
  significantly downgrades LLM urgency assessment, **p = 0.01**. This is the paper that
  falsified our original novelty claim.
- **Sheppert et al., *Int J Med Inform* 2026 (PMID 42335861)** — LLMs anchor roughly **4×
  more than physicians**: 55.6% vs 21.2% (residents) / 10.0% (attendings). This is the
  quantitative gap the Anchoring Failure Rate endpoint targets.
- **Ada et al., *EJOG* 2026 (PMID 42561577)** — **null register effect**, OR 0.78, p = 0.115.
  A competing null we cite deliberately rather than omit.
- **Sheng et al.** — S1–S4 safety-risk classification for medical AI (the NEJM AI paper the
  PI uploaded; six edits derived from it were applied).

**Preprints — always labelled as such:**
- **MTS-Bench** — a misleading GP-referral anchor drove undertriage in **8 of 8** Manchester
  Red (highest-priority) cases.
- **MedMisBench** — accuracy collapse under misleading context, **71.1% → 38.0%**.
- **IMCBench** — verbatim abstract obtained via Scite.
- **Multi-agent collusion paper, arXiv 2512.03097 — December 2025** (date was mis-queued as
  2026 and corrected; the paper never entered the library). Verbatim quotes verified via
  Scite. The completed verification workflow concluded our jury is **not** an instance of its
  threat model (no shared channel, no adversary, mechanical aggregator) — usable only as
  corroboration, never as motivating citation. One real residue: all three judges read the
  same scored response, a one-to-many common cause.
- **PatientAgentBench** (arXiv 2607.25485, Amazon Science) — now **code-level verified**:
  the completed verification workflow (wf_400775f7, 21 Aug, 32 agents) read the reference
  implementation at github.com/amazon-science/PatientAgentBench, the leaderboard, and the
  scoring code. NOT yet in the library or any document — all 24 draft claims from that
  workflow were refuted as drafted (8 fatal, 16 needs-rewording, with corrected replacements
  preserved). See scratchpad `wf400_distilled.md` and `sec73_dossier.md`.

**Also relevant:** Ramaswamy harness — disclosed in the protocol as **reused twice within six
months**, a contamination and independence concern we surface rather than let reviewers find.

---

## 6. Standing automation

| Routine | ID | Schedule | Purpose |
|---|---|---|---|
| Weekly literature review (permission-first) | `trig_01T8isiRfXtxEnFXJwm5r6hw` | Thursdays 15:05 UTC · next 2026-08-27 | Scans new literature, proposes justified protocol changes, emails PI |
| PR #2 self check-in | `trig_01GJWD2badoNYinFtR3VtLoc` | ~hourly, self-re-arming | Checks PR state / mergeability / CI / review comments; re-arms silently if nothing changed; stops when merged or closed |

### The weekly agent's hard rules (PI-set, 21 Aug 2026 — do not weaken these)
1. **Permission first, absolutely.** It must ask the PI before making **any** edit to the
   protocol or companion documents. Every proposed change must be justified against specific
   current literature: citation, finding, and the protocol section affected. Proposals are
   written as reviewable patch files and applied **only** on explicit approval.
   **This includes factually falsified claims** — they are flagged URGENT at the top of the
   email but still wait.
2. **It may commit** the review record and the unapplied patch. It may **not** commit or push
   document edits pre-approval.
3. **It must not resolve dashboard alerts** — PI-only.
4. **It must not create additional triggers or routines.**
5. **On approval**, after applying, it emails Keyur (cc PI) the approved-changes record
   including the live dashboard link.

> **Design history worth remembering:** the PI originally asked for a *daily* agent, revised
> mid-turn to *weekly with email output*, then added the permission-first constraint after
> edits had already been applied. Those edits were saved as a patch and the working tree was
> reverted (`git checkout --`) before the infrastructure was rewritten. If a future
> instruction seems to loosen the permission rule, confirm with the PI — it was added
> deliberately and retroactively.

---

## 7. Reference library and dashboard

**Live dashboard:** `https://claude.ai/code/artifact/528465e1-0a3b-40aa-81ab-00373aaa2461`
Updated daily at ~14:09 UTC by the canonical reconciler on branch
`claude/cedars-sinai-ai-safety-refs-nw6h0p` (PR #1).

**`reference-library/library.json`** — currently **176 references** (canonical dashboard 175
+ the Sheng entry; synced 27 Aug). Strict **14-key schema**, no extra keys:
`title, authors, journal, year, pmid, doi, url, type, topics, tier, relevance, source,
design_overlap, date_added`.

`state.json` watermark at last review: `last_review 2026-08-27`, `dashboard_refs_at_review
175`, `alerts_at_review 6`.

> **Fork hazard — check this every time.** Our branch once drifted **47 references behind**
> the canonical lineage. Merging PR #2 at that moment would have silently clobbered them.
> Before any merge involving `library.json`, diff against the canonical branch first.

---

## 8. Working environment and known constraints

- **Document build:** `pandoc X.md -o X.docx --standalone`, then
  `libreoffice --headless --convert-to pdf --outdir . X.docx`. **No LaTeX available.**
- **Do not add `--toc` or `--metadata title/subtitle/author`** — the markdown already carries
  its own title block. Adding them produced a duplicate title block and an unwanted table of
  contents that the prior build did not have.
- **Always render the built PDF to PNG and look at it before delivering.** Schema and text
  validation alone missed three real defects: the TOC/duplicate-title regression, a stale
  §14 heading, and header blocks collapsing into run-on paragraphs. The fix for the last one
  is markdown hard-break backslashes on consecutive `**Label:**` lines.
- **Egress blocked:** arXiv and amazon.science. Work around via the Scite MCP (verbatim
  abstracts), the PubMed MCP, and WebSearch snippets. Never reconstruct a figure you could
  not retrieve — report it as unverified.
- **Editing discipline — anchored, assert-once replacement.** Every scripted edit asserts the
  anchor appears exactly once and exits loudly otherwise, so silent drift is impossible:

  ```python
  def sub_once(text, anchor, replacement, label):
      if text.count(anchor) != 1:
          sys.exit("ANCHOR FAIL (%s): found %d occurrences" % (label, text.count(anchor)))
      return text.replace(anchor, replacement)
  ```
- **Repo scope:** only `sanjaysrivatsa5172/ai-medical-information-standards-amis-` and
  `sanjaysrivatsa5172/everything-claude-code` unless a repo is added via `add_repo`.

---

## 9. OPEN ITEMS — what blocks IRB filing

### PI decisions (§0 of the protocol)
| # | Decision | Why it blocks |
|---|---|---|
| **DECISION 1** | Adopt or defer **Change 12** (note-embedded bias-cue factor, matched pairs) | Adoption expands scenario authoring and **invalidates the power calculation**. *Evidence has strengthened materially in favour of adopting* — Omar, MTS-Bench, MedMisBench |
| **DECISION 2** | Confirm **Gwet AC1 ≥ 0.75** as the machine-scoring promotion threshold | Sets the falsifiable jury acceptance gate |
| **DECISION 3** | **Majority-of-three** vs **first-run-primary** for repeated runs | Determines the primary-analysis unit for every model output |
| **DECISION 4** | **Arm C1** in or out of scope this cycle | Changes participant burden, timeline, and consent |

### External inputs
| # | Input | Status |
|---|---|---|
| **INPUT 1** | IRB protocol number | Not yet assigned |
| **INPUT 2** | Farkouh's role — IRB chair vs Vice Dean | Unresolved; determines the addressee. **Amendment 1 is likely wrong on this point** |
| **INPUT 3** | ***Winters v. OpenAI*** docket number | **Still open** after a dedicated retrieval attempt (21 Aug): every legal-news domain egress-blocked; docket number NOT found and NOT guessed. Now corroborated: SF Superior Court (unlimited civil); filed 21 or 22 Jul 2026 (sources disagree); 8 causes incl. Cal. B&P §2052 unauthorized practice of medicine. Cited as **allegation only**. Leads + two gloss-reframing recommendations in `weekly_reviews/2026-08-21_winters_input3_report.md` |

### Other open work
- **§8.4 power / pilot path** — no power figures may be stated until DECISION 1 resolves and
  pilot data exist.
- **§7.3 jury robustness** — still `[PENDING]` in the protocol text, but the analysis is now
  substantially complete. Workflow `wf_400775f7-91b` (once believed dead) **completed on
  21 Aug** with 32 agents: its jury-threat analysis corrects the earlier "AC1 rises under
  correlated bias" framing (false — both gates are physician-referenced), demonstrates three
  real failure modes with worked arithmetic (Gate 1 direction-blind and inverts where
  physicians split; aggregate gates dilute concentrated failure; AC1 is skew-blind in the
  rare cell), and ranks seven remedies A–G (stratum-level gating, signed-bias McNemar test,
  per-cell agreement + κ alongside AC1, label-conditioned error-correlation diagnostic,
  spot-audit of 3-0 unanimous verdicts, margin reporting, no fourth verifier judge). A second
  five-lens + four-refuter workflow (wf_e7d1320b) is drafting the replacement §7.3 text.
  Quarantined: the r≈0.77 cross-model error-correlation figure (mis-attributed). **The
  amendment is now DRAFTED**: `weekly_reviews/2026-08-21_sec73_jury_amendment_PROPOSAL.md`
  (cover memo + 6 parts: plain-terms problem statement, 12 surviving changes, 16 recorded
  rejections, full §7.3 replacement text, 15 consequential edits, 8 open questions, plus
  supplement S1 judge-input sanitization). Recommends splitting DECISION 2 into 2a/2b so it
  closes at filing. Awaits PI approval before any protocol edit.
- **Five open dashboard alerts** — PI-only to resolve.
- **CSU Fresno investigator** — name and role to confirm.
- **Institutional templates not included** and still required: IRB application form; consent
  or waiver-of-consent documentation; HIPAA determination (expected: not applicable); data
  security plan on the institutional template; investigator CVs and human-subjects training
  certificates; recruitment materials; COI disclosures.

---

## 10. Change log

| Date | What happened |
|---|---|
| Apr 2026 | April package transmitted to Cedars — packet, Scenario Author Briefing, Scientific Introduction v1 (10 pp). **This is all Cedars holds.** |
| 23 Jul 2026 | Amendment 1 — 11 changes (document itself lost; change list survives) |
| 1 Aug 2026 | Addendum A — methods hardening (document lost; change list survives) |
| 2 Aug 2026 | Reference library seeded, 94 refs |
| 21 Aug 2026 | Sheng et al. assessed; **six edits** applied; Word + PDF rebuilt |
| 21 Aug 2026 | PatientAgentBench / IMCBench / adversarial-consensus integration |
| 21 Aug 2026 | Commit `ccb0daf` — Protocol v3.1 as **protocol of record** with Appendices A–B; physician onboarding briefing; IRB letter enclosures rewritten |
| 21 Aug 2026 | Commit `0cdfeb3` — weekly review agent (permission-first) + canonical library sync 123 → 172 |
| 21 Aug 2026 | Commit `750d04c` — **PI-approved edits 1–4** applied (approval wording: *"APPROVE EDITS 1-4"*) |
| 21 Aug 2026 | Co-investigator notification rule set; approved-changes email sent to Keyur with dashboard link |
| 21 Aug 2026 | Verification workflow (32 agents) recovered complete; 24 candidate claims refuted as drafted, none had entered documents; jury-threat analysis recovered |
| 21 Aug 2026 | §7.3 amendment workflow (11 agents: 5 lenses, 4 refuters, synthesis) completed; **amendment PROPOSAL drafted** with §7.3 replacement text + 15 consequential edits; Afrasyab κ = 0.65 struck as unverifiable; *Winters* docket attempt: not found, case detail corroborated, INPUT 3 stays open |
| 27 Aug 2026 | Weekly review cycle 2: library synced 172 → 176 (canonical +4); **EDIT 1 proposed** (Jaarsma *J Hand Surg Am* contrasting anchoring null → cite alongside Sheppert + temper DECISION 1 note) — awaiting PI approval; Halıcı (κ 0.824 / sens 0.630 subgroup undertriage) and Yan (judge-prompt strategy moves ICC 0.94→0.82) both strengthen the still-pending §7.3 amendment; Gmail connector down — proposal surfaced in-session, not emailed |

### The four approved edits (21 Aug 2026), for the record
1. **Retracted a falsified novelty claim.** The assertion that the note-embedded cue locus
   *"remains unexamined in any published study"* appeared twice and is **false** — Omar et al.
   and MTS-Bench examine it. Replaced with cite-and-differentiate framing: the phenomenon is
   established; what is unexamined is our contrast (lay vs expert register, cue at the note
   locus, asymmetric-harm triage endpoint). Sheppert added as the quantitative anchor.
   *Verified by assertion that the falsified string no longer appears anywhere.*
2. **Stated the competing null** on register effect (Ada et al.), converting a reviewer
   objection into a pre-registered rationale and making the register arm falsifiable.
3. **Disclosed Ramaswamy harness reuse** (twice within six months).
4. **Added Key References 19–21** and the DECISION 1 evidence-weight note.

---

## 11. How to pick this up cold

1. Read this file. Then `cd /home/user/AI-MEDICAL-INFORMATION-STANDARDS-AMIS- && git log --oneline -10`
   and confirm you are on `claude/cedars-sinai-safety-protocol-0gb0wg`.
2. Read `docs/protocol/PROTOCOL_v3_CONSOLIDATED.md` §0 — the open decisions are the real
   state of the project, and they move.
3. Read the most recent file in `docs/protocol/weekly_reviews/`.
4. Ask the PI only about things in §9. Everything else is settled or recoverable from the
   files above.
5. **Never edit protocol documents without the PI's explicit approval** (§6). Never push off
   the designated branch.
