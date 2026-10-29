#!/bin/bash
# sync-obsidian-vault.sh — pull the latest generated reference notes from the
# AMIS repo into the local Obsidian vault folder "PATIENT FACING AI TRIAGE SAFETY".
#
# Usage (macOS Terminal):
#   bash sync-obsidian-vault.sh            # sync once, right now
#   bash sync-obsidian-vault.sh install    # sync now + automatically every day at 6:20 AM
#   bash sync-obsidian-vault.sh uninstall  # remove the daily schedule
#
# Personal notes inside the vault folder are never deleted — the script only
# adds/overwrites the generated reference notes and the index.
set -euo pipefail

REPO_URL="https://github.com/SanjaySrivatsa5172/AI-MEDICAL-INFORMATION-STANDARDS-AMIS-.git"
BRANCH="claude/cedars-sinai-ai-safety-refs-nw6h0p" # change to "main" once PR #1 is merged
CACHE_DIR="$HOME/.amis-reflib"
VAULT_DIR="$HOME/Documents/Obsidian Vault/PATIENT FACING AI TRIAGE SAFETY"
SRC_SUBDIR="reference-library/obsidian/PATIENT FACING AI TRIAGE SAFETY"
PLIST="$HOME/Library/LaunchAgents/com.amis.reflib-sync.plist"

sync_now() {
  if [ ! -d "$CACHE_DIR/.git" ]; then
    git clone --quiet --depth 1 --branch "$BRANCH" "$REPO_URL" "$CACHE_DIR"
  else
    git -C "$CACHE_DIR" fetch --quiet --depth 1 origin "$BRANCH"
    git -C "$CACHE_DIR" reset --quiet --hard FETCH_HEAD
  fi
  mkdir -p "$VAULT_DIR"
  rsync -a "$CACHE_DIR/$SRC_SUBDIR/" "$VAULT_DIR/"
  echo "$(date '+%Y-%m-%d %H:%M') — synced $(find "$VAULT_DIR" -name '*.md' | wc -l | tr -d ' ') notes into: $VAULT_DIR"
}

case "${1:-sync}" in
  install)
    SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
    mkdir -p "$HOME/Library/LaunchAgents"
    cat > "$PLIST" <<PLIST_EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.amis.reflib-sync</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${SCRIPT_PATH}</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>6</integer><key>Minute</key><integer>20</integer></dict>
  <key>StandardOutPath</key><string>/tmp/amis-reflib-sync.log</string>
  <key>StandardErrorPath</key><string>/tmp/amis-reflib-sync.log</string>
</dict>
</plist>
PLIST_EOF
    launchctl unload "$PLIST" 2>/dev/null || true
    launchctl load "$PLIST"
    echo "Daily vault sync installed: every day at 6:20 AM (or next wake). Running first sync now…"
    sync_now
    ;;
  uninstall)
    launchctl unload "$PLIST" 2>/dev/null || true
    rm -f "$PLIST"
    echo "Daily vault sync removed."
    ;;
  sync|*)
    sync_now
    ;;
esac
