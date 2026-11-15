# Co-investigator notifications — sent record

## 2026-11-15 — consolidated send, five approvals

Gmail was unauthorized from late August 2026 until 12 November 2026, so the co-investigator
notifications required by the standing PI-set rule of 21 August queued in
`../pending_notifications/` rather than going out.

On 15 November 2026 the PI chose, from four offered options, to send **one consolidated note**
rather than four separate stale messages. Sent to pawaskarkeyur96@gmail.com, cc
drsanjaysrivatsa@gmail.com, subject *"Cedars protocol — PI-approved changes 29 Aug – 3 Sep 2026
(consolidated record)"*, Gmail message id `1a1e05337af16060`.

The four files in this directory are the originals as drafted at the time, moved here unchanged.
They are the source for the consolidated note and are kept for the record.

### What the consolidated note covered

| # | Approval wording | Date | Commit | Protocol after |
|---|---|---|---|---|
| 1 | `APPROVE EDIT 1` | 29 Aug 2026 | `4c343e3` | v3.1, 22 pp |
| 2 | `APPROVE THE 7.3 AMENDMENT` | 29 Aug 2026 | `8aebcfc` | v3.1, 29 pp |
| 3 | `APPROVE PART 5 ITEMS 2 AND 3` | 30 Aug 2026 | `f6e1aa9` | v3.1, 31 pp |
| 4 | `APPROVE PART 5 ITEMS 4 AND 5` | 30 Aug 2026 | `ebb651e` | v3.1, 32 pp |
| 5 | `APPROVE EDITS 1-3` | 3 Sep 2026 | `8b72f46` | v3.1, 33 pp |

### Two defects in the queue, found while reconciling it — both now closed

1. **Approval 4 had no notification at all.** `ebb651e` ("APPROVE PART 5 ITEMS 4 AND 5",
   30 August — item 4 removed the ~40/30/30 scoring weights, item 5 added §7.6, the
   non-load-bearing declaration) was approved and applied, but no notification file was ever
   drafted for it. The standing rule requires one per approval. Found by diffing the queued
   files against `git log` for protocol-touching commits in the window, not by reading the
   queue — the queue cannot reveal its own omissions. Written up in full in the consolidated
   note from the commit record.

2. **Approval 3's file carried no commit SHA**, reading "Applied in commit (see repository
   log...)". The rule requires the SHA. Recovered as `f6e1aa9` and included.

**Standing recommendation:** reconcile the notification queue against `git log` on the protocol
file, not against the queue's own contents, whenever the queue is next worked. One approval in
five was missing, and the only way to see that was from the commit side.
