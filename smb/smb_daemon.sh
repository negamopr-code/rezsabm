#!/bin/sh
# SMB pipeline daemon — runs INSIDE awf-monitor-runner, so it survives Claude usage limits,
# session ends and Docker restarts of the Claude container. Zero Claude tokens.
# Each cycle, strictly in series (one work4 job at a time):
#   1. refresh the channel inventory once a day (new SMB uploads)
#   2. harvest pending transcripts
#   3. collect comments for pending videos
#   4. sync transcript + comment archives
#   5. run ONE NotebookLM analysis round for the lowest archive volume lacking a digest
#   6. push both Slot Manager heartbeats
W=/app/state/smb-options
HB=/home/app/.notebooklm-mcp-cli/heartbeats
export NLM_PROFILE=work4
cd $W || exit 1
mkdir -p $HB digests
LOG=$W/daemon.log
say() { echo "$(date -u '+%F %H:%M') $*" >> $LOG; }

hb() {  # $1 job-file, $2 job name, $3 state, $4 summary, $5 counts-json
  python3 - "$1" "$2" "$3" "$4" "$5" "$HB" <<'PY'
import sys, json, datetime
f, job, state, summary, counts, hb = sys.argv[1:7]
try: c = json.loads(counts)
except Exception: c = {}
json.dump({"job": job, "account": "work4", "state": state, "summary": summary, "counts": c,
           "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')},
          open(f"{hb}/{f}", "w"), indent=1)
PY
}

counts_harvest() { python3 -c "
import json,re
d=json.load(open('$W/ledger.json')); v=d.get('videos',d)
# ledger.json is keyed by video id and the values carry no 'id' field, so the id has to be
# injected from the key — without this the 'distilled' count was structurally always 0
items=[dict(x, id=k) for k, x in v.items()] if isinstance(v,dict) else v
from collections import Counter; c=Counter(x.get('status') for x in items)
try: vol=open('/app/state/smb-options/volume-1.md').read()
except Exception: vol=''
print(json.dumps({'transcribed':c.get('transcribed',0),'pending':c.get('pending',0),
                  'unavailable':c.get('unavailable',0),'total':len(items),
                  'distilled':len({x for x in re.findall(r'[A-Za-z0-9_-]{11}',vol)} & {(x.get('id') or '') for x in items})}))"; }

counts_comments() { python3 -c "
import json
d=json.load(open('$W/comments_ledger.json')); v=d.get('videos',d)
items=list(v.values()) if isinstance(v,dict) else v
from collections import Counter; c=Counter(x.get('status') for x in items)
import os
dig=len([f for f in os.listdir('$W/digests') if f.startswith('vol-') and f.endswith('.md')])
print(json.dumps({'videos_fetched':c.get('done',0),'videos_pending':c.get('pending',0),
                  'comments_stored':sum(x.get('comments',0) or 0 for x in items),
                  'total_videos':len(items),'nlm_digests':dig,'nlm_queries':dig*4}))"; }

LAST_LIST=0
while true; do
  NOW=$(date -u +%s)
  # external NLM job (a Claude-side pacer) holds this lock: stay idle, one work4 job at a time
  if [ -f $W/nlm_external.lock ] && [ -n "$(find $W/nlm_external.lock -mmin -120 2>/dev/null)" ]; then
    say "idle: external NLM job holds the lock"
    hb smb-comments.json "SMB Capital comments → NLM + classify" running "$(date -u +%H:%M) UTC daemon idle — external NLM round in progress" "$(counts_comments)"
    sleep 600; continue
  fi
  rm -f $W/nlm_external.lock 2>/dev/null   # stale lock (>2 h): the Claude-side job is gone, take over
  # 1. refresh channel inventory once every 24 h
  if [ $((NOW - LAST_LIST)) -gt 86400 ]; then
    say "list: refreshing channel inventory"
    timeout 900 python3 harvest.py list >> $LOG 2>&1 && LAST_LIST=$NOW
  fi
  # 2. transcripts
  PEND=$(python3 -c "import json;d=json.load(open('$W/ledger.json'));v=d.get('videos',d);i=list(v.values()) if isinstance(v,dict) else v;print(sum(1 for x in i if x.get('status')=='pending'))")
  if [ "$PEND" -gt 0 ]; then
    hb smb-pipeline.json "SMB Capital → NLM harvest/distill" running "$(date -u +%H:%M) UTC daemon: harvesting $PEND new transcript(s)" "$(counts_harvest)"
    say "harvest: $PEND pending"
    timeout 3600 python3 harvest.py harvest 20 >> $LOG 2>&1
  fi
  # 3. comments for any video without them
  CPEND=$(python3 -c "
import json
vj={v['id'] for v in json.load(open('$W/videos.json'))['videos']}
d=json.load(open('$W/comments_ledger.json')); v=d.get('videos',d)
ids=set(v.keys()) if isinstance(v,dict) else {x.get('id') for x in v}
items=list(v.values()) if isinstance(v,dict) else v
# a video absent from the ledger is pending too — otherwise a NEW video never triggers the harvester
print(len(vj-ids) + sum(1 for x in items if x.get('status')!='done'))")
  if [ "$CPEND" -gt 0 ]; then
    hb smb-comments.json "SMB Capital comments → NLM + classify" running "$(date -u +%H:%M) UTC daemon: collecting comments for $CPEND video(s)" "$(counts_comments)"
    say "comments: $CPEND pending"
    timeout 3600 python3 comments_harvest.py harvest >> $LOG 2>&1
  fi
  # 4. archives (only when no harvester is running — this loop is serial, so it is safe here)
  if [ "$PEND" -gt 0 ] || [ "$CPEND" -gt 0 ]; then
    say "sync: archives"
    timeout 1800 python3 sync_archives.py >> $LOG 2>&1
    timeout 1800 python3 comments_sync.py archive >> $LOG 2>&1
  fi
  # 5. one NLM analysis round for the lowest comment-archive volume without a digest
  NEXT=$(python3 -c "
import json,os,subprocess
have={int(f[4:6]) for f in os.listdir('$W/digests') if f.startswith('vol-') and f.endswith('.md')}
out=subprocess.run(['python3','$W/comments_sync.py','sources'],capture_output=True,text=True,cwd='$W').stdout
try: src=json.loads(out)
except Exception: src=[]
vols=sorted(int(s['title'].rsplit(' ',1)[1]) for s in src if s.get('title','').startswith('SMB comments archive vol.'))
todo=[v for v in vols if v not in have]
print(todo[0] if todo else 0)")
  QTS=$(cat $W/quota_exhausted 2>/dev/null)
  case "$QTS" in ''|*[!0-9]*) QTS=0 ;; esac
  AGE=$(( $(date -u +%s) - QTS ))
  if [ "$QTS" -gt 0 ] && [ "$AGE" -lt 25200 ]; then   # 7 h: the daily cap does NOT reset at UTC midnight
    say "round: skipped, work4 quota exhausted ${AGE}s ago (retry after 7 h)"
    NEXT=0
  fi
  if [ "$NEXT" != "0" ] && [ -n "$NEXT" ]; then
    say "round: analysing comments archive vol. $NEXT"
    hb smb-comments.json "SMB Capital comments → NLM + classify" running "$(date -u +%H:%M) UTC daemon: NLM round vol. $NEXT (4 queries)" "$(counts_comments)"
    timeout 3600 python3 analyze_local.py "$NEXT" >> $LOG 2>&1
    say "round vol. $NEXT rc=$?"
  fi
  # 5b. hybrid distillation EXTRACTION (zero Claude tokens) — only while quota is healthy
  QTS2=$(cat $W/quota_exhausted 2>/dev/null); case "$QTS2" in ''|*[!0-9]*) QTS2=0 ;; esac
  if [ $(( $(date -u +%s) - QTS2 )) -ge 25200 ]; then
    say "distill: extracting up to 10 videos"
    timeout 5400 python3 distill_local.py 10 >> $LOG 2>&1
    say "distill rc=$?"
  fi

  # 6. heartbeats
  hb smb-pipeline.json "SMB Capital → NLM harvest/distill" done "$(date -u +%H:%M) UTC daemon alive; transcripts complete, distillation runs in-daemon (step 5b), Claude only gates+merges" "$(counts_harvest)"
  DIGN=$(ls $W/digests/vol-*.md 2>/dev/null | wc -l)
  hb smb-comments.json "SMB Capital comments → NLM + classify" running "$(date -u +%H:%M) UTC daemon alive; $DIGN digests = $((DIGN*4)) NLM queries; next round when a volume lacks one" "$(counts_comments)"
  sleep 1800
done
