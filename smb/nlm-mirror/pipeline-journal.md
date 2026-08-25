# SMB Options pipeline — operations journal (incidents, root causes, fixes, decisions)

Purpose: crash-proof, agent-readable memory of how the SMB Capital → NotebookLM ingestion
pipeline breaks and how it was fixed, so no session or agent re-diagnoses a known problem.
Consult this FIRST (file: `workspaces/REZSABM/smb/nlm-mirror/pipeline-journal.md`, or ask the
"SMB Options" notebook e2e327c6 on work4 — source "smb-mirror: pipeline-journal") whenever
harvest/distill/sync misbehaves. Append-only; never rewrite history.

## Pipeline map (what runs where)
- State: container `awf-monitor-runner`, dir `/app/state/smb-options/` (host: workspaces
  "need collecting from customers comments"/state/smb-options/): harvest.py (list/harvest/
  status), audit_transcripts.py, sync_archives.py, videos.json, ledger.json, transcripts/,
  harvest.log.
- Harvest run: `docker exec -d -e NLM_PROFILE=work4 awf-monitor-runner sh -c 'cd /app/state/smb-options && python3 harvest.py harvest 400 > harvest.log 2>&1'`
- Notebook: "SMB Options" `e2e327c6-18bd-4a2a-bc8c-90ae2337f91c`, profile **work4**
  (mickaelsh951). Layers: "SMB transcripts archive vol. N" (verbatim) + "SMB Options vol. N"
  (distilled) + "smb-mirror: pipeline-journal" (this file).
- Distilled volume canonical mirror: `workspaces/REZSABM/smb/volume-1.md` (git).
- Skill: `~/.claude/skills/smb-options/` (doctrine + consult.sh + lessons.md).
- Cookie stores for work4 (they DIVERGE by design): keeper named volume `nlm-profile`
  (`nlm-keeper:/home/app/.notebooklm-mcp-cli/profiles/work4/`, refreshed by the keeper) vs
  bind store `persistent/nlm-profile/profiles/work4/` (= what awf-monitor-runner and the
  claude container use).

## Standing rules
- R1 (user 2026-08-25): any long background job gets a SUPERVISOR agent that polls, diagnoses
  root causes, fixes, restarts and reports proactively. Never leave a stalled job waiting.
- R2: every incident/root cause/fix/decision is appended here AND synced to NLM
  (`bash smb/nlm-mirror/sync-nlm-mirror.sh`) in the same session — patent-workbench pattern.
- R3 (truncation no-go): distillers never `cat` transcripts through docker exec; docker cp +
  Read with paging; verify end-of-file; volume uploads via `--file`.
- R4: no-subtitle videos = `unavailable`, never retried; source delete trusted only after
  re-list; ≥1.5 s between nlm calls; fill vol. 1 before vol. 2.

## Incident log

### 2026-08-23 — two racing harvesters clobbered ledger.json
Symptom: ledger inconsistencies. Cause: two `harvest.py` processes launched in parallel.
Fix: single-process lock in harvest.py. Lesson: check /proc for a live harvester before
starting another (no `ps` in the runner image — grep /proc/*/cmdline).

### 2026-08-23 23:19 → 2026-08-25 08:53 UTC — 34 h silent stall, misdiagnosed as rate limit
Symptom: harvest.log ends with repeated `add refused, retry in 60/300/900s`, "3 consecutive
refusals despite backoff - cooling down 30 min", then the process died at 29/400; ledger 94
transcribed / 4 failed(refused) / 266 pending. Nobody noticed until the user saw NLM idle.
Root cause: NLM `source add` error "Could not add url source" was NOT a rate limit — it
masked **expired work4 auth in the BIND cookie store** (bind cookies.json 08-23 23:06, keeper
volume cookies 08-24 01:28). The keeper probes the VOLUME store (`cli_probe` → notebook list)
and kept logging "[work4] quarantined: CLI session ALIVE … running login-free", so its
dashboard looked green while the runner's copy was dead. harvest.py's retry logic only
matches the string "could not add" and cannot tell auth from rate limit.
Diagnosis that works: `docker exec awf-monitor-runner sh -c 'timeout 60 nlm notebook list -p work4'`
→ "Authentication expired" = auth problem (no amount of backoff helps).
Fix applied 08-25 08:57 UTC: backup bind cookies.json (`.bak-2026-08-25`); `docker cp
nlm-keeper:/home/app/.notebooklm-mcp-cli/profiles/work4/{cookies.json,metadata.json}` →
bind store; re-test notebook list (OK); ledger entries `failed` with why containing
"refused" → `pending` (4 reset); rotate harvest.log → harvest.log.1; restart harvester.
Result: 5 videos harvested in the first 90 s, no refusals. Supervisor agent + distill batch 3
agent launched 09:00 UTC.
Decisions: (a) auth expiry ⇒ sync volume→bind, NOT retry; (b) if the keeper's own cookies
also fail → human login via noVNC http://localhost:8106 is required, stop and report;
(c) harvest.py should probe auth (`notebook list`) on the first refusal and exit with a clear
"AUTH EXPIRED" message instead of backing off — TODO, not yet implemented.
