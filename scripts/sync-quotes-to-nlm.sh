#!/usr/bin/env bash
# Sync the instrument quote database (all uploads/*_daily_OHLC_yahoo.csv) into the
# work4 SABM NotebookLM notebook, SHARDED at 5 instruments per source document
# (user decision 2026-08-23: measured capacity is ~10 full 33y histories / ~100k OHLC
# rows per source; 5 leaves margin for decades of future daily rows).
# NLM sources are immutable -> the daily "append" = replace-by-title per volume.
#
# Run from the claude session container (needs the nlm CLI + docker):
#   bash scripts/sync-quotes-to-nlm.sh
set -euo pipefail

NOTEBOOK="b57ecd77-292a-434b-90c4-6956723634d3"   # "SABM — Sortir au Bon Moment", account work4
PROFILE="work4"
NLM="/home/node/patent-wiki-analyzer/.venv/bin/nlm"
CT="rezsabm-serve"
PER_VOL=5
GUARD_ROWS=95000   # measured 2026-08-23: one source tops out ~100k OHLC rows (500k words, 5/row)

# work4 cookies rotate quickly; the keeper holds the live session - refresh first
docker exec nlm-keeper cat /home/app/.notebooklm-mcp-cli/profiles/work4/cookies.json  > ~/.notebooklm-mcp-cli/profiles/work4/cookies.json
docker exec nlm-keeper cat /home/app/.notebooklm-mcp-cli/profiles/work4/metadata.json > ~/.notebooklm-mcp-cli/profiles/work4/metadata.json

SYMS=$(docker exec "$CT" sh -c 'ls /app/uploads/*_daily_OHLC_yahoo.csv' \
  | sed 's|.*/||; s/_daily_OHLC_yahoo.csv//' | sort)
[ -n "$SYMS" ] || { echo "no instrument CSVs in uploads/"; exit 1; }

SOURCES_JSON="$($NLM source list "$NOTEBOOK" -p "$PROFILE" 2>/dev/null)"

vol=0; chunk=""; want_titles=""
sync_chunk() {
  vol=$((vol + 1))
  local title="Quotes database vol. $vol (daily OHLC)"
  want_titles="$want_titles|$title"
  local tmp; tmp="$(mktemp --suffix=.txt)"
  {
    echo "QUOTES DATABASE volume $vol — daily OHLC per instrument (Date,Open,High,Low,Close)."
    echo "Instruments in this volume:$chunk. Auto-synced from the REZSABM tool (http://localhost:8112/)."
    echo
    for sym in $chunk; do
      echo "=== INSTRUMENT: $sym ==="
      docker exec "$CT" cat "/app/uploads/${sym}_daily_OHLC_yahoo.csv"
      echo
    done
  } > "$tmp"
  local lines; lines=$(wc -l < "$tmp")
  echo "vol. $vol [$chunk ]: $lines lines, $(du -h "$tmp" | cut -f1)"
  if [ "$lines" -gt "$GUARD_ROWS" ]; then
    echo "⚠ vol. $vol exceeds the ${GUARD_ROWS}-row safety margin — lower PER_VOL" >&2
    rm -f "$tmp"; exit 1
  fi
  local old_id
  old_id="$(printf '%s' "$SOURCES_JSON" | python3 -c "import json,sys; ss=json.load(sys.stdin); print(next((s['id'] for s in ss if s.get('title')=='$title'), ''))")"
  if [ -n "$old_id" ]; then
    echo y | $NLM source delete "$old_id" -p "$PROFILE" >/dev/null 2>&1 || true
    echo "  replaced old source $old_id"
  fi
  $NLM source add "$NOTEBOOK" --file "$tmp" --title "$title" --wait -p "$PROFILE" | tail -1
  rm -f "$tmp"
}

n=0
for sym in $SYMS; do
  chunk="$chunk $sym"; n=$((n + 1))
  if [ "$n" -eq "$PER_VOL" ]; then sync_chunk; chunk=""; n=0; fi
done
[ -n "$chunk" ] && sync_chunk

# drop stale quote sources (old volumes beyond the current count, or the pre-shard single doc)
printf '%s' "$SOURCES_JSON" | python3 -c "
import json, sys
want = set('$want_titles'.strip('|').split('|'))
for s in json.load(sys.stdin):
    t = s.get('title') or ''
    if t.startswith('Quotes database') and t not in want:
        print(s['id'])" | while read -r sid; do
  [ -n "$sid" ] || continue
  echo y | $NLM source delete "$sid" -p "$PROFILE" >/dev/null 2>&1 || true
  echo "deleted stale quotes source $sid"
done

echo "synced $vol volume(s) -> notebook $NOTEBOOK ($PROFILE)"
