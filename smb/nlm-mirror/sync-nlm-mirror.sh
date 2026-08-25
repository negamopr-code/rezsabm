#!/usr/bin/env bash
# Sync smb/nlm-mirror/*.md into the "SMB Options" NotebookLM notebook (profile work4) as
# sources titled "smb-mirror: <basename>". Replace-by-title (delete old, add new via --file —
# argv-embedded text truncates/hangs). Runs nlm INSIDE awf-monitor-runner, which has the CLI
# and the work4 bind profile. Pattern: patent-workbench / resim mirrors.
# Auth expired? see pipeline-journal.md incident 2026-08-25 (copy keeper cookies → bind).
set -euo pipefail
NB="${NOTEBOOK_ID:-e2e327c6-18bd-4a2a-bc8c-90ae2337f91c}"
CT="${RUNNER:-awf-monitor-runner}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for f in "$HERE"/*.md; do
  base="$(basename "$f" .md)"; title="smb-mirror: $base"
  docker cp "$f" "$CT:/tmp/$base.md"
  docker exec "$CT" sh -c "
    old=\$(nlm source list '$NB' -p work4 --json 2>/dev/null | python3 -c '
import sys,json
t=sys.argv[1]
try: d=json.loads(sys.stdin.read() or \"[]\")
except Exception: d=[]
if isinstance(d,dict): d=d.get(\"sources\") or d.get(\"value\") or []
print(\" \".join(s.get(\"id\") or s.get(\"source_id\") or \"\" for s in d if isinstance(s,dict) and s.get(\"title\")==t))' '$title')
    sleep 1.6
    nlm source add '$NB' --file /tmp/$base.md --title '$title' -p work4 >/dev/null
    sleep 1.6
    for sid in \$old; do nlm source delete \$sid --confirm -p work4 >/dev/null 2>&1 || true; sleep 1.6; done
    nlm source list '$NB' -p work4 --json 2>/dev/null | grep -c '$title' | sed 's/^/  copies now: /'
  "
  echo "✓ synced $title"
done
echo "done → notebook $NB (work4)"
