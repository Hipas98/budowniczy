#!/bin/bash
cd /Users/damianmanski/Documents/ClaudeCode/Fenix

# Sprawdź czy są jakiekolwiek zmiany (unstaged, staged, untracked)
HAS_CHANGES=0
if ! git diff --quiet 2>/dev/null; then HAS_CHANGES=1; fi
if ! git diff --staged --quiet 2>/dev/null; then HAS_CHANGES=1; fi
if [ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then HAS_CHANGES=1; fi

if [ "$HAS_CHANGES" -eq 0 ]; then exit 0; fi

# Sprawdź czy od ostatniego commita minęło ponad 10 minut (600 sekund)
LAST_COMMIT=$(git log -1 --format="%ct" 2>/dev/null || echo "0")
NOW=$(date +%s)
DIFF=$((NOW - LAST_COMMIT))

if [ "$DIFF" -lt 600 ]; then exit 0; fi

# Commit i push
git add -A
git commit -m "auto: zapis sesji $(date '+%Y-%m-%d %H:%M')" --no-verify 2>/dev/null
git push origin main 2>/dev/null
