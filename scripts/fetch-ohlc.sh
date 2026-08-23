#!/usr/bin/env bash
# Fetch daily OHLC history from Yahoo Finance's chart API into uploads/.
# Usage: scripts/fetch-ohlc.sh [SYMBOL] (default FILA.MI)
# Note: stooq.com is behind a JS challenge, so Yahoo is the fetch source; be gentle (single request).
set -euo pipefail
SYM="${1:-FILA.MI}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$DIR/uploads/${SYM}_daily_OHLC_yahoo.csv"
TMP="$(mktemp)"
curl -s --max-time 30 -H 'User-Agent: Mozilla/5.0' \
  "https://query1.finance.yahoo.com/v8/finance/chart/${SYM}?period1=0&period2=9999999999&interval=1d" -o "$TMP"
python3 - "$TMP" "$OUT" << 'EOF'
import json, sys, csv, datetime
tmp, out = sys.argv[1], sys.argv[2]
j = json.load(open(tmp))
r = (j.get('chart') or {}).get('result')
if not r:
    sys.exit('Yahoo returned no result: ' + json.dumps(j)[:200])
res = r[0]; ts = res['timestamp']; q = res['indicators']['quote'][0]
rows = []
for i, t in enumerate(ts):
    o, h, l, c = q['open'][i], q['high'][i], q['low'][i], q['close'][i]
    if None in (o, h, l, c):
        continue
    rows.append((datetime.datetime.utcfromtimestamp(t).date().isoformat(),
                 round(o, 4), round(h, 4), round(l, 4), round(c, 4)))
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['Date', 'Open', 'High', 'Low', 'Close']); w.writerows(rows)
print(f'{out}: {len(rows)} rows, {rows[0][0]} -> {rows[-1][0]}')
EOF
rm -f "$TMP"
