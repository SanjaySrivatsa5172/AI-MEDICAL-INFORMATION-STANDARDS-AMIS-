# Weekly Literature Review — Method

A recurring weekly agent reviews the live reference-library dashboard
(https://claude.ai/code/artifact/528465e1-0a3b-40aa-81ab-00373aaa2461 — updated daily by the canonical
reconciler at ~14:09 UTC on branch `claude/cedars-sinai-ai-safety-refs-nw6h0p`), assesses the week's
additions and alerts against the protocol's design features, and **emails the PI a prioritized,
literature-justified list of suggested changes**.

**Permission rule (PI-set, 21 Aug 2026): the agent must ask the PI's permission — with each change
justified against the current literature — before making ANY edit to the protocol or its companion
documents.** Proposed edits are prepared as reviewable patch files in this directory and applied only
on the PI's explicit approval. This includes factually falsified claims: they are flagged URGENT at the
top of the email, but still wait for approval.

Each run: (1) fetch the dashboard and diff against `state.json`; (2) verify load-bearing items via
PubMed/Scite before citing them; (3) write a dated review and a `proposed_edits_*.patch`; (4) commit
and push the review materials (never the edits themselves); (5) email the PI the justified suggestion
list and the permission request. Cadence: Thursdays 15:05 UTC. Preprints always labelled; unverifiable
figures reported as unverified, never reconstructed.

## Co-investigator notification (PI-set, 21 Aug 2026)

**Whenever the PI approves protocol changes, the agent must — after applying them — email
Keyur Pawaskar, co-investigator, at `pawaskarkeyur96@gmail.com` (cc the PI at
`drsanjaysrivatsa@gmail.com`).**

The notification must carry:

1. the exact edits approved;
2. the literature justification for each — citation, finding, and the protocol section
   affected;
3. the date and wording of the PI's approval;
4. the resulting commit SHA and document versions;
5. **the live reference dashboard link**
   (https://claude.ai/code/artifact/528465e1-0a3b-40aa-81ab-00373aaa2461).

Subject line: `Cedars protocol — PI-approved changes [date]`.

**This fires on approval, not on proposal.** Keyur receives the record of what was approved
and applied — never the proposal email. Proposals go to the PI alone.

## Project context

Full project state — people, design, endpoints, evidence base, open decisions, working
constraints — is maintained in [`../CONTEXT_MEMORY.md`](../CONTEXT_MEMORY.md). Read it before
each review; update it when a decision closes or a document version changes.
