#!/usr/bin/env bash
# Sync the instrument quote database (all uploads/*_daily_OHLC_yahoo.csv) into the
# work4 SABM NotebookLM notebook as ONE document, replace-by-title (NLM sources are
# immutable, so the daily "append" = re-upload of the whole compact document).
#
# Run from the claude session container (needs the nlm CLI + docker):
#   bash scripts/sync-quotes-to-nlm.sh
set -euo pipefail

NOTEBOOK="b57ecd77-292a-434b-90c4-6956723634d3"   # "SABM — Sortir au Bon Moment", account work4
PROFILE="work4"
TITLE="Quotes database (daily OHLC, all instruments)"
NLM="/home/node/patent-wiki-analyzer/.venv/bin/nlm"
CT="rezsabm-serve"

# work4 cookies rotate quickly; the keeper holds the live session - refresh first
docker exec nlm-keeper cat /home/app/.notebooklm-mcp-cli/profiles/work4/cookies.json  > ~/.notebooklm-mcp-cli/profiles/work4/cookies.json
docker exec nlm-keeper cat /home/app/.notebooklm-mcp-cli/profiles/work4/metadata.json > ~/.notebooklm-mcp-cli/profiles/work4/metadata.json

TMP="$(mktemp --suffix=.txt)"
{
  echo "QUOTES DATABASE — daily OHLC per instrument (Date,Open,High,Low,Close)."
  echo "Auto-synced from the REZSABM tool (http://localhost:8112/). One section per instrument."
  echo
  for f in $(docker exec "$CT" sh -c 'ls /app/uploads/*_daily_OHLC_yahoo.csv'); do
    sym="$(basename "$f" | sed 's/_daily_OHLC_yahoo.csv//')"
    echo "=== INSTRUMENT: $sym ==="
    docker exec "$CT" cat "$f"
    echo
  done
} > "$TMP"

LINES=$(wc -l < "$TMP")
echo "document: $LINES lines, $(du -h "$TMP" | cut -f1)"
# measured 2026-08-23: one NLM source tops out at ~100k OHLC rows (500k words, 5 words/row);
# 10 full 33y histories fit, 12 do not. Beyond that -> shard into "vol. N" sources.
if [ "$LINES" -gt 95000 ]; then
  echo "⚠ $LINES lines exceeds the ~95k-row safety margin for ONE NLM source — split instruments into volume documents" >&2
  exit 1
fi

OLD_ID="$($NLM source list "$NOTEBOOK" -p "$PROFILE" 2>/dev/null \
  | python3 -c "import json,sys; ss=json.load(sys.stdin); print(next((s['id'] for s in ss if s.get('title')=='$TITLE'), ''))")"
if [ -n "$OLD_ID" ]; then
  echo y | $NLM source delete "$OLD_ID" -p "$PROFILE" >/dev/null 2>&1 || true
  echo "replaced old source $OLD_ID"
fi
$NLM source add "$NOTEBOOK" --file "$TMP" --title "$TITLE" --wait -p "$PROFILE"
rm -f "$TMP"
echo "synced -> notebook $NOTEBOOK ($PROFILE)"
