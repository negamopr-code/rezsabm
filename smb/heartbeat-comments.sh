#!/usr/bin/env bash
# Heartbeat of the SMB COMMENTS pipeline for the NLM Slot Manager (http://localhost:8110/,
# "Background jobs"). Usage: heartbeat-comments.sh <state> "<summary>" ["<needsUser>"]
# state: running | paused | blocked | done | error. Counts read live from the comments ledger
# (container) + the local classification store.
set -u
STATE="${1:-running}"; SUMMARY="${2:-}"; NEEDS="${3:-}"
HB="${HB_DIR:-/home/node/.notebooklm-mcp-cli/heartbeats}"; mkdir -p "$HB"
C=$(docker exec awf-monitor-runner sh -c 'cd /app/state/smb-options && python3 comments_harvest.py status 2>/dev/null' | python3 -c 'import sys,json
try: d=json.load(sys.stdin)["counts"]
except Exception: d={}
print(json.dumps(d))')
python3 - "$STATE" "$SUMMARY" "$NEEDS" "$C" "$HB" <<'PY'
import sys,json,datetime,os
state,summary,needs,counts,hb=sys.argv[1:6]
d=json.loads(counts)
c={"videos_fetched":d.get("videos_done",0),"videos_pending":d.get("pending",0),"videos_failed":d.get("failed",0),
   "comments_stored":d.get("comments",0),"comments_classified":0,"topics":0,"total_videos":364}
try:
    cl='/workspace/smb/comments_classified.jsonl'
    if os.path.exists(cl):
        topics=set(); n=0
        for line in open(cl):
            try: r=json.loads(line)
            except Exception: continue
            n+=1; topics.update(r.get("topics") or [])
        c["comments_classified"]=n; c["topics"]=len(topics)
except Exception: pass
j={"job":"SMB Capital comments → NLM + classify","account":"work4","state":state,"summary":summary,
   "counts":c,"updatedAt":datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
if needs: j["needsUser"]=needs
json.dump(j,open(f"{hb}/smb-comments.json","w"),indent=1)
print(json.dumps(j))
PY
