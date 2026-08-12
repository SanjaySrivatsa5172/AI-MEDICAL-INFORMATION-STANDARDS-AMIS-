; ============================================================================
; Medical Procedure Shortcuts - Gmail + Microsoft Word (Windows)
; ----------------------------------------------------------------------------
; Pressing Ctrl+R / Ctrl+L / Ctrl+P / Ctrl+V / Ctrl+S while working in
; Microsoft Word or in a Gmail browser tab types the matching procedure
; phrase at the cursor. Everywhere else these keys keep their normal meaning.
;
; Requires AutoHotkey v2 (free, https://www.autohotkey.com). Double-click
; this file to run it; a green "H" tray icon appears while it is active.
;
; NOTE: while Word or Gmail is the active window, these shortcuts REPLACE
; the standard actions (Ctrl+V paste, Ctrl+S save, Ctrl+P print,
; Ctrl+R refresh, Ctrl+L address bar). Press Ctrl+Shift+F12 to pause or
; resume the shortcuts, or change MODS below to "^!" to use Ctrl+Alt
; combinations instead and keep the standard keys.
; ============================================================================
#Requires AutoHotkey v2.0
#SingleInstance Force

; =========================== EDIT SNIPPETS HERE =============================
MODS := "^"  ; "^" = Ctrl (as requested). Change to "^!" for Ctrl+Alt.

Snippets := Map(
    "r", "RIGHT GSV (AK) AND RIGHT GSV (BK) VARITHENA AND RIGHT LEG SCLEROTHERAPY",
    "l", "LEFT GSV (AK) RFA AND LEFT GSV (BK) VARITHENA AND LEFT LEG SCLEROTHERAPY",
    "p", "RIGHT/LEFT CALF PERFORATOR EVLT",
    "v", "VARITHENA OF LARGE VARICES RIGHT/LEFT LEG",
    "s", "SCLEROTHERAPY OF BILATERAL LEGS"
)
; ============================================================================

; Browsers checked for an active Gmail tab (window title must contain "Gmail").
Browsers := ["chrome.exe", "msedge.exe", "firefox.exe", "brave.exe", "opera.exe", "vivaldi.exe"]

InGmailOrWord(*) {
    if WinActive("ahk_exe WINWORD.EXE")
        return true
    ; if WinActive("ahk_exe OUTLOOK.EXE")  ; uncomment to enable in Outlook too
    ;     return true
    for exe in Browsers {
        if WinActive("ahk_exe " exe) && InStr(WinGetTitle("A"), "Gmail")
            return true
    }
    return false
}

InsertSnippet(text, *) {
    SendText(text)  ; types the phrase; does not touch the clipboard
}

HotIf InGmailOrWord
for key, text in Snippets
    Hotkey(MODS . key, InsertSnippet.Bind(text))
HotIf

; Ctrl+Shift+F12 pauses/resumes all shortcuts (e.g. to get normal Ctrl+V back).
#SuspendExempt
^+F12:: {
    Suspend(-1)
    if A_IsSuspended
        TrayTip("Shortcuts PAUSED - press Ctrl+Shift+F12 to resume", "Medical Shortcuts")
    else
        TrayTip("Shortcuts ACTIVE", "Medical Shortcuts")
}
#SuspendExempt False

TrayTip("Loaded - active only in Word and Gmail browser tabs", "Medical Shortcuts")
