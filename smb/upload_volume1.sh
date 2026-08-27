#!/usr/bin/env bash
# Replace-by-title upload of the distilled volume ("SMB Options vol. 1") into the SMB Options
# notebook. Waits for the current NLM analysis round to finish first (one work4 job at a time).
set -u
cd /workspace/smb
until [ -f digests/vol-06.md ]; do sleep 20; done      # round 6 finished
sleep 30
OLD=$(docker exec -e NLM_PROFILE=work4 awf-monitor-runner sh -c \
  'nlm source list e2e327c6-18bd-4a2a-bc8c-90ae2337f91c -p work4 2>/dev/null' \
  | python3 -c 'import json,sys;print(next((s["id"] for s in json.load(sys.stdin) if s["title"]=="SMB Options vol. 1"),""))')
echo "old source: $OLD"
docker cp volume-1.md awf-monitor-runner:/app/state/smb-options/volume-1.md
docker exec -e NLM_PROFILE=work4 awf-monitor-runner sh -c 'cd /app/state/smb-options && python3 -c "
import comments_sync as cs
nid = cs.add_source(\"/app/state/smb-options/volume-1.md\", \"SMB Options vol. 1\")
print(\"new:\", nid)
"' | tee /tmp/vol1-upload.txt
NEW=$(grep -o 'new: [0-9a-f-]\{36\}' /tmp/vol1-upload.txt | awk '{print $2}')
if [ -n "$NEW" ] && [ -n "$OLD" ] && [ "$NEW" != "$OLD" ]; then
  docker exec -e NLM_PROFILE=work4 awf-monitor-runner sh -c "cd /app/state/smb-options && python3 -c \"
import comments_sync as cs
print('deleted old:', cs.delete_verified('$OLD'))
\""
fi
bash heartbeat.sh done "$(date -u +%H:%M) UTC volume 'SMB Options vol. 1' refreshed: 161 videos distilled (new $NEW)" >/dev/null 2>&1
echo "upload done new=$NEW old=$OLD"
