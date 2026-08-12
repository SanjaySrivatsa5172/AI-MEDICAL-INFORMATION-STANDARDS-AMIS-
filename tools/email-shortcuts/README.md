# Email & Word Keyboard Shortcuts — Vein Procedure Phrases

Press **Ctrl + a letter** while typing in a Gmail message or a Word document and the
matching procedure phrase is typed at the cursor.

| Shortcut | Text inserted |
|----------|---------------|
| **Ctrl+R** | `RIGHT GSV (AK) AND RIGHT GSV (BK) VARITHENA AND RIGHT LEG SCLEROTHERAPY` |
| **Ctrl+L** | `LEFT GSV (AK) RFA AND LEFT GSV (BK) VARITHENA AND LEFT LEG SCLEROTHERAPY` |
| **Ctrl+P** | `RIGHT/LEFT CALF PERFORATOR EVLT` |
| **Ctrl+V** | `VARITHENA OF LARGE VARICES RIGHT/LEFT LEG` |
| **Ctrl+S** | `SCLEROTHERAPY OF BILATERAL LEGS` |

## ⚠️ Verify the wording before relying on it

Two spots in the original request looked like typos, so please confirm:

1. **Ctrl+R** — the request read `RIGHT GSV (AK) AND RIGHT GSV (BK) VARITHEN`.
   It is stored here as `…GSV (AK) AND RIGHT GSV (BK) VARITHENA…` (spelling fixed).
   If the right leg should mirror the left leg — i.e. `RIGHT GSV (AK) RFA AND …` —
   add **RFA** after `(AK)` in each file's *EDIT SNIPPETS HERE* block.
2. **Varithena** spelling was normalized everywhere (`VARITHEN` → `VARITHENA`).

Ctrl+P and Ctrl+V insert `RIGHT/LEFT` literally — delete the side that does not
apply after inserting.

## ⚠️ These combos replace standard shortcuts

While you are in Gmail or Word, **Ctrl+V no longer pastes, Ctrl+S no longer
saves, Ctrl+P no longer prints, Ctrl+R no longer refreshes/right-aligns**.
Everywhere else they behave normally. If that gets in the way:

- Each file has a one-line switch to use **Ctrl+Alt+letter** instead
  (`MODS := "^!"` in the AutoHotkey script, `REQUIRE_ALT = true` in the
  userscript; for Word macros, rebind via `Tools → Customize Keyboard`).
- The AutoHotkey script can be paused/resumed anytime with **Ctrl+Shift+F12**.
- You can still save in Word with **F12**/AutoSave, paste with
  **Shift+Insert**/right-click, and print from **File → Print**.

## Pick your setup

| You use… | Install |
|----------|---------|
| **Windows** (Gmail in any browser + Word) | `windows/medical-shortcuts.ahk` — one script covers both |
| **Word only** (Windows) | `word/MedicalShortcuts.bas` macros |
| **Gmail on any OS** (Mac, ChromeOS, Linux, Windows) | `gmail/medical-shortcuts.user.js` browser userscript |

Use **one** solution per app (don't run the AutoHotkey script *and* the
userscript on the same PC — AutoHotkey already covers Gmail there).

### 1. AutoHotkey (Windows — recommended, covers Gmail and Word)

1. Install **AutoHotkey v2** (free): <https://www.autohotkey.com>
2. Double-click `windows/medical-shortcuts.ahk`. A green tray icon appears.
3. Optional — start it with Windows: press `Win+R`, type `shell:startup`,
   and put a shortcut to the `.ahk` file in that folder.

The script only fires inside Word or a browser tab whose title contains
"Gmail"; everywhere else all keys stay normal.

### 2. Word macros (Windows Word; Mac Word see note)

1. In Word press `Alt+F11` → **File → Import File…** → choose
   `word/MedicalShortcuts.bas` (into the **Normal** project).
2. Press `Alt+F8`, run **InstallMedicalShortcuts** once. Done — the bindings
   persist in Normal.dotm across restarts.
3. To remove: `Alt+F8` → **UninstallMedicalShortcuts** (restores standard keys).

*Word for Mac:* import the module the same way, then bind the five
`MedShortcut_…` macros to keys via **Tools → Customize Keyboard** (the
automatic key-binding API is Windows-only).

### 3. Gmail userscript (any OS / browser)

1. Install the **Tampermonkey** (or Violentmonkey) browser extension.
2. Extension menu → **Create a new script** → paste the contents of
   `gmail/medical-shortcuts.user.js` → save.
3. Open Gmail, click into a compose window, try `Ctrl+S`.

Only runs on `mail.google.com`, and only while the cursor is in an editable
field, so shortcuts elsewhere in the browser are untouched. If your browser
still grabs a combo (some reserve `Ctrl+L` for the address bar), use the
AutoHotkey script instead — it intercepts keys at the OS level.

## Editing the phrases

Each of the three files has a clearly marked **`EDIT SNIPPETS HERE`** block at
the top — change the text there (keep it identical across files you use), then
restart the script / re-run `InstallMedicalShortcuts` / save the userscript.

## No-install alternatives

- **Gmail Templates**: Settings → See all settings → Advanced → enable
  Templates. Save each phrase once, insert via ⋮ → Templates while composing.
- **Word AutoText**: select a phrase → `Alt+F3` to save it; later type its
  name and press `F3` to expand. No macros required.

## A note on content

These snippets are procedure names only. Keep auto-inserted text free of
patient identifiers or other PHI — anything typed by a shortcut can land in
the wrong window.
