#!/usr/bin/env bash
# Progressive NLM pacer for the SMB comments pipeline.
# Runs one analysis round (4 NotebookLM questions) per archive volume, spaced ~36 min,
# pushing both Slot Manager heartbeats every 12 min so a quota-pacing gap never reads as STALE.
# Usage: pacer.sh <vol> [<vol> ...]
set -u
cd /workspace/smb
hb() {  # $1 = harvest-job summary, $2 = comments state, $3 = comments summary
  bash heartbeat.sh done "$1" >/dev/null 2>&1
  bash heartbeat-comments.sh "$2" "$3" >/dev/null 2>&1
}
HARV="harvest COMPLETE 361/364 (3 unavailable); archives v1-3 + comments v1-12 final"
first=1
for V in "$@"; do
  if [ $first -eq 0 ]; then                      # pace between rounds (not before the first)
    NEXT=$(date -u -d '+36 minutes' +%H:%M)
    for i in 1 2 3; do
      hb "$(date -u +%H:%M) UTC $HARV" paused \
         "$(date -u +%H:%M) UTC quota pacing — next NLM round vol. $V at ~$NEXT UTC (4 queries/volume, progressive)"
      sleep 720
    done
  fi
  first=0
  hb "$(date -u +%H:%M) UTC $HARV" running "$(date -u +%H:%M) UTC NLM round vol. $V running (4 queries)"
  python3 ~/.claude/skills/smb-audience/scripts/analyze.py "$V" > "logs/analyze-vol$(printf %02d "$V").log" 2>&1
  RC=$?
  python3 ~/.claude/skills/smb-audience/scripts/report.py > /dev/null 2>&1
  N=$(ls digests/vol-*.md 2>/dev/null | wc -l)
  hb "$(date -u +%H:%M) UTC $HARV" running \
     "$(date -u +%H:%M) UTC NLM round vol. $V rc=$RC; digests $N; $((N*4)) queries consumed"
  git -C /workspace add -A >/dev/null 2>&1
  git -C /workspace commit -qm "SMB comments: NLM digest vol. $V (rc=$RC), audience-needs regenerated

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>" >/dev/null 2>&1
  echo "$(date -u +%H:%M) round vol.$V rc=$RC digests=$N"
done
hb "$(date -u +%H:%M) UTC $HARV" paused "$(date -u +%H:%M) UTC today's rounds done ($(ls digests/vol-*.md | wc -l) digests); vols 6-12 tomorrow"
echo done
