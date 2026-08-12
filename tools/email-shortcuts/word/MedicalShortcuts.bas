Attribute VB_Name = "MedicalShortcuts"
Option Explicit

' ============================================================================
' Medical Procedure Shortcuts for Microsoft Word
' ----------------------------------------------------------------------------
' After installation, Ctrl+R / Ctrl+L / Ctrl+P / Ctrl+V / Ctrl+S insert the
' procedure phrases below at the cursor in any Word document.
'
' INSTALL:   Alt+F11 -> File > Import File... -> pick this .bas file (into the
'            "Normal" project) -> Alt+F8 -> run InstallMedicalShortcuts.
' UNINSTALL: Alt+F8 -> run UninstallMedicalShortcuts (restores the standard
'            Word meanings of these keys: paste, save, print, etc.).
'
' NOTE: while installed, these bindings REPLACE Word's standard Ctrl+V paste,
' Ctrl+S save, Ctrl+P print, Ctrl+R right-align and Ctrl+L left-align.
' You can still save with F12 / the Save button / AutoSave, paste with
' Shift+Insert or right-click, and print from File > Print.
' ============================================================================

' =========================== EDIT SNIPPETS HERE =============================
Private Const SNIP_R As String = "RIGHT GSV (AK) AND RIGHT GSV (BK) VARITHENA AND RIGHT LEG SCLEROTHERAPY"
Private Const SNIP_L As String = "LEFT GSV (AK) RFA AND LEFT GSV (BK) VARITHENA AND LEFT LEG SCLEROTHERAPY"
Private Const SNIP_P As String = "RIGHT/LEFT CALF PERFORATOR EVLT"
Private Const SNIP_V As String = "VARITHENA OF LARGE VARICES RIGHT/LEFT LEG"
Private Const SNIP_S As String = "SCLEROTHERAPY OF BILATERAL LEGS"
' ============================================================================

Public Sub InstallMedicalShortcuts()
    CustomizationContext = NormalTemplate
    AddBinding "MedShortcut_RightLeg", wdKeyR
    AddBinding "MedShortcut_LeftLeg", wdKeyL
    AddBinding "MedShortcut_Perforator", wdKeyP
    AddBinding "MedShortcut_Varithena", wdKeyV
    AddBinding "MedShortcut_Sclerotherapy", wdKeyS
    NormalTemplate.Save
    MsgBox "Medical shortcuts installed:" & vbCrLf & vbCrLf & _
           "Ctrl+R  right leg plan" & vbCrLf & _
           "Ctrl+L  left leg plan" & vbCrLf & _
           "Ctrl+P  calf perforator EVLT" & vbCrLf & _
           "Ctrl+V  Varithena of large varices" & vbCrLf & _
           "Ctrl+S  sclerotherapy of bilateral legs" & vbCrLf & vbCrLf & _
           "Run UninstallMedicalShortcuts to restore the standard keys.", _
           vbInformation, "Medical Shortcuts"
End Sub

Public Sub UninstallMedicalShortcuts()
    CustomizationContext = NormalTemplate
    ClearBinding wdKeyR
    ClearBinding wdKeyL
    ClearBinding wdKeyP
    ClearBinding wdKeyV
    ClearBinding wdKeyS
    NormalTemplate.Save
    MsgBox "Medical shortcuts removed. Standard Ctrl+R/L/P/V/S restored.", _
           vbInformation, "Medical Shortcuts"
End Sub

Private Sub AddBinding(macroName As String, letterKey As Long)
    ClearBinding letterKey
    KeyBindings.Add KeyCategory:=wdKeyCategoryMacro, Command:=macroName, _
        KeyCode:=BuildKeyCode(wdKeyControl, letterKey)
End Sub

Private Sub ClearBinding(letterKey As Long)
    On Error Resume Next  ' FindKey errors if no custom binding exists
    FindKey(BuildKeyCode(wdKeyControl, letterKey)).Clear
    On Error GoTo 0
End Sub

Public Sub MedShortcut_RightLeg()
    Selection.TypeText SNIP_R
End Sub

Public Sub MedShortcut_LeftLeg()
    Selection.TypeText SNIP_L
End Sub

Public Sub MedShortcut_Perforator()
    Selection.TypeText SNIP_P
End Sub

Public Sub MedShortcut_Varithena()
    Selection.TypeText SNIP_V
End Sub

Public Sub MedShortcut_Sclerotherapy()
    Selection.TypeText SNIP_S
End Sub
