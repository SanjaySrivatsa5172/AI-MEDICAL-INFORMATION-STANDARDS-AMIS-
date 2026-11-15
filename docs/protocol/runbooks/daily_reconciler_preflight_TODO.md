# TODO — add Step 0 preflight to the daily reconciler routine

**Status: NOT APPLIED. Requires action outside this session.**
Raised 4 September 2026, PI-directed ("add the same check to the daily routines").

## What was done and what was not

| Routine | Trigger ID | Status |
|---|---|---|
| Weekly Cedars protocol literature review | `trig_01T8isiRfXtxEnFXJwm5r6hw` | ✅ **Step 0 added** (PDF-toolchain variant) |
| Daily AI-triage-safety reference scan | `trig_017Ae5N9nuLofnMaiRc1TTNr` | ✅ **Step 0 added** (node/dashboard variant) |
| Daily scan reconciler | `trig_01VkgTjn9QapNNosjrWmVvem` | ❌ **BLOCKED — see below** |

The reconciler fires into a **different persistent session**
(`session_01EYtS2J8Au3WFQ5FziPV937`). Editing the prompt of a routine bound to another session
is not permitted from this one:

> `update_trigger: editing the prompt of a routine whose fires deliver into a session that is
> not your own is not available via this tool.`

That session was not running, so it could not be messaged either. **Its name, schedule and
enabled state can still be changed from here — only the prompt is locked.**

## Two ways to apply it

1. **From the owning session** (`session_01EYtS2J8Au3WFQ5FziPV937`): resume it and ask it to
   update its own routine `trig_01VkgTjn9QapNNosjrWmVvem` with the Step 0 block below.
2. **Manually**: open the routine in the Routines list and paste the Step 0 block in
   immediately after the `ENVIRONMENT FACTS` paragraph, before `1) SYNC CHECK`.

Do **not** delete and recreate the routine — that loses its run history, and the PI-set rule for
this project forbids creating additional triggers.

## Why the reconciler needs it

It runs `node reference-library/build.js` and then **republishes the dashboard artifact**. If the
build does not actually run, `dashboard.html` keeps its previous contents and the reconciler
republishes a **stale dashboard** while every step reports success. It is the same class of
failure that hit the weekly review on 3 September — where `libreoffice-core` was installed but
`libreoffice-writer` was not, so `soffice --convert-to pdf` printed an error, **exited 0**, and
left the old PDF in place, making page counts look correct while measuring a stale file.

The reconciler builds no PDFs, so the *check* differs — but the lesson is identical: **never
trust an exit code; verify the artifact actually changed.**

---

## Step 0 block to insert verbatim

```
STEP 0 — ENVIRONMENT PREFLIGHT (do this FIRST; added 4 Sep 2026, PI-directed)
The container is ephemeral and may be freshly provisioned. Two silent failures have actually occurred on this project:

(a) BRANCH. The working tree may come up on `main` with none of the work present. Nothing has been lost — it is all on the remote. Do the checkout in step 1 before concluding anything is missing, and confirm reference-library/library.json, dashboard-template.html and build.js all exist.

(b) NODE. build.js needs node (stdlib only, no npm install), and node may not be on PATH in a fresh container — it has been found at /opt/node22/bin/node. Check `which node || ls /opt/node*/bin/node`; if needed use the absolute path or export PATH=/opt/node22/bin:$PATH. Confirm `node --version` prints before relying on it.

(c) THE SILENT FAILURE THAT MATTERS HERE — republishing a stale dashboard. If build.js does not actually run, dashboard.html retains its PREVIOUS contents, and republishing to the artifact URL then pushes a stale dashboard while every step appears to succeed. build.js exits 1 if the template marker is missing, but a build you never ran cannot fail. After running `node reference-library/build.js` and BEFORE publishing, verify BOTH:
    - dashboard.html's mtime is NEWER than library.json's;
    - the reference count is what you intend to publish:
      node -e 'const fs=require("fs");console.log("library references:",JSON.parse(fs.readFileSync("reference-library/library.json","utf8")).references.length)'
  If the mtime is older or the counts disagree, the build did not take — fix and re-run rather than publishing.
Note the analogous trap in the sibling weekly-review routine: `libreoffice-core` can be installed while `libreoffice-writer` is not, in which case `soffice --convert-to pdf` prints an error, EXITS 0, and leaves the old PDF in place. You do not build PDFs, but the lesson is the same — never trust an exit code, verify the artifact changed.
Report any Step 0 problem explicitly in your final status line.
```

Two small companion edits to the same prompt, if convenient:

- In step 1, change the checkout to `git checkout -B claude/cedars-sinai-ai-safety-refs-nw6h0p origin/claude/cedars-sinai-ai-safety-refs-nw6h0p` so a container that came up on `main` self-heals.
- In steps 4 and 6, add "Do not publish unless the Step 0(c) checks passed."
- In step 8, add `PREFLIGHT clean` to the healthy single-line status.
