#!/usr/bin/env bash
# Write the SMB pipeline heartbeat shown on the NLM Slot Manager (http://localhost:8110/,
# "Background jobs"). Usage: heartbeat.sh <state> "<summary>" ["<needsUser>"]
# state: running | paused | blocked | done | error. Counts are read live from the ledger.
set -u
STATE="${1:-running}"; SUMMARY="${2:-}"; NEEDS="${3:-}"
HB="${HB_DIR:-/home/node/.notebooklm-mcp-cli/heartbeats}"; mkdir -p "$HB"
C=$(docker exec awf-monitor-runner sh -c 'cd /app/state/smb-options && python3 harvest.py status 2>/dev/null' | python3 -c 'import sys,json
try: d=json.load(sys.stdin)["counts"]
except Exception: d={}
print(json.dumps({k:d.get(k,0) for k in ("transcribed","pending","failed","unavailable") if k in d or k=="transcribed"}))')
DIST=$(grep -o '^\*\*Ledger' -c /workspace/smb/volume-1.md 2>/dev/null || true)
python3 - "$STATE" "$SUMMARY" "$NEEDS" "$C" "$HB" <<'PY'
import sys,json,datetime,re
state,summary,needs,counts,hb=sys.argv[1:6]
c=json.loads(counts)
try:
    v=open('/workspace/smb/volume-1.md').read(); c['distilled']=len(set(re.findall(r'\[([A-Za-z0-9_-]{11})\]',v)))
except Exception: pass
c['total']=364
j={"job":"SMB Capital → NLM harvest/distill","account":"work4","state":state,"summary":summary,
   "counts":c,"updatedAt":datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
if needs: j["needsUser"]=needs
json.dump(j,open(f"{hb}/smb-pipeline.json","w"),indent=1)
print(json.dumps(j))
PY
