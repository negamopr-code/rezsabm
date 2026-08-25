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

### 2026-08-25 — distill batch 3: transcript zs4pK__ncCo is NOT a transcript (wrong NLM source captured)
Symptom: `transcripts/zs4pK__ncCo.txt` ("Top 3 Options Trading Mistakes You Must Avoid", 94k views)
is 164,752 chars — ~8× a normal transcript — and after the harvester's `## title | views | url`
header its body is a verbatim copy of **SMB Options vol. 1** (the distilled volume), not the
video. ledger.json still says `status: transcribed, chars: 161450`. The youtube source for that
video (id ecefa0da-…) is also still present in the notebook, i.e. the harvester's delete step did
not run for it. Likely cause: the raw-content poll read a different source (the volume upload
that was happening concurrently) instead of the freshly added video source — harvest.py polls
by position/latest rather than by the source id it just created (to verify).
Distiller action: excluded from batch 3, substituted W5Gl_E2Sq-A; ledger row in volume-1.md
marks it "NOT DISTILLED — re-harvest required". Note for backlog computation: the volume now
CITES [zs4pK__ncCo] (header + ledger), so a set-difference "harvested − cited" will hide it —
treat it as pending until re-harvested.
Fix TODO (supervisor/harvester owner): (1) delete/rename `transcripts/zs4pK__ncCo.txt`;
(2) set ledger.json[zs4pK__ncCo].status → pending (only while no harvester holds harvest.lock);
(3) delete stale youtube source ecefa0da-c890-43fb-abed-50382daaa347 after re-listing;
(4) make harvest.py poll the source id returned by `source add` and add a content sanity
check (reject bodies that start with "SMB OPTIONS — distilled" or exceed ~6× expected chars/min);
(5) audit_transcripts.py should flag size outliers, not only short/garbled tails.
Also noted: no "SMB Options vol. 1" source existed in the notebook before batch 3's upload
(7 sources listed) — the batch-2 copy had disappeared; batch 3 re-added it as
a6701d05-2a2b-4c5f-915f-039fa5e0e3a7 (ready).

### 2026-08-25 — ROOT CAUSE of the zs4pK__ncCo contamination + vanished vol. 1: source-identification race
Confirmed by reading harvest.py: after `source add` it took `new = source_ids(now) − before` and used
`new.pop()` as the video source. Any CONCURRENT `source add` on the notebook (distiller uploading
"SMB Options vol. 1", journal sync, sync_archives.py) lands in that set → the harvester reads the
foreign document as the "transcript" and then DELETES it. That is how the batch-2 vol. 1 source
disappeared and why zs4pK__ncCo.txt contains the volume. Only 1 of 131 transcripts affected (scan
08-25 09:30 UTC: header check + size outliers).
Fix (harvest.py patched 09:35 UTC, effective on next restart; mirrored in REZSABM/smb/smb_harvest.py):
(1) new source chosen by TITLE MATCH with the video, never a source titled "SMB Options*/SMB
transcripts*/smb-mirror*"; ambiguous → wait; (2) content starting with "# SMB OPTIONS" → mark
pending, do NOT delete the source; (3) on the first "could not add", probe `nlm notebook list` →
"Authentication expired" ⇒ print AUTH EXPIRED and exit 3 (no backoff).
RULES (standing): R5 — NEVER `source add` to the SMB notebook while a harvester process is alive:
no sync_archives, no volume upload, no journal sync. Order at end of a harvest run: cleanup
(remove bad transcript, ledger → pending, delete leftover YouTube sources after re-listing) →
audit_transcripts → sync_archives → volume upload → journal sync → restart harvester.
R6 — ledger.json is held in memory by a running harvester and re-saved after every video: never
edit it while the harvester is alive (edits get overwritten).
Pending cleanup (supervisor at end of run): rm transcripts/zs4pK__ncCo.txt; ledger zs4pK__ncCo →
pending; delete 6 leftover YouTube sources incl. ecefa0da-c890-43fb-abed-50382daaa347.

### 2026-08-25 09:20 UTC — user directives: visible heartbeat + progressive NLM usage
User: "you should just output this heartbeat shortly to nlm slot manager, where I can see what is
going on" and "it is better to use quota of nlm progressively and not at one time at the end of
the day".
Implemented: R7 — every supervisor writes `smb/heartbeat.sh <state> "<summary>" ["<needs user>"]`
at least every 10 min → `persistent/nlm-profile/heartbeats/smb-pipeline.json` → shown on the
NLM Slot Manager (http://localhost:8110/, section "Background jobs"; >20 min without heartbeat =
STALE in red). R8 — chunked cycle instead of one 400-run: harvest 40 → (harvester exits) →
cleanup leftovers → audit → sync_archives → distill batch (agent) → volume upload → journal sync
→ heartbeat → next chunk. NLM work is spread across the day and R5 (no concurrent adds) holds
because every add happens between chunks. Slot-manager patch (collectors.scanHeartbeats +
"Background jobs" UI) applied via docker cp into `workspaces/nlm slot manager` — NOT yet
git-committed there (no git in that container; commit from a session with that mount).

## 2026-08-25 09:19–09:30 UTC — cycle 1 (supervisor, progressive-chunk mode)
Harvester 400-run (started 08:5x, old source-diff code) stopped cleanly at [64/400] after
BY2qOpNoDdI began (ledger confirmed pending); 94 → 157 transcribed at ~3 vid/min, 0 refusals,
auth valid throughout. Cleanup: rm transcripts/zs4pK__ncCo.txt + ledger → pending; deleted 5
leftover YouTube sources (627beeb9, 2a1a49fd, 19119e29, 97aa8831, ecefa0da) → notebook = 3 keep
sources. Source count stayed 9 during the whole run (no concurrent adders observed).
audit_transcripts: 156 ok / 0 suspect. sync_archives 41 s: archive vol.1 = 142 videos
(2,389,200 chars), NEW archive vol.2 = 14 videos (210,126 chars). Distill batch 4 (agent): 15
videos, volume 32,304 → 39,216 words, all 15 files read to EOF (no truncation), new
"SMB Options vol. 1" = f357475f-7e7b-457a-8b34-a1d9327e6284, old a6701d05 deleted, commit
9e1be2c; distill backlog 56. Next: harvester chunk of 40 (patched harvest.py, title-match).

### 2026-08-25 11:59–12:05 UTC — STALE heartbeat (2h20m) root-caused: Docker restart killed the harvester
User: "smb is without heartbeat more than 20 min". Last heartbeat 09:37, last harvest.log line 09:39
([28/40] tpxBJhfawzQ, cycle-2 chunk). `docker inspect awf-monitor-runner` StartedAt = 09:54:21 UTC —
every container shows "Up 2 hours" ⇒ Docker/WSL restarted at 09:54 and the `docker exec -d` harvester
(pid 3200) died with it; the previous session's supervisor agent was gone too, so nobody re-armed.
Auth on work4 was VALID (notebook list ok) — this was not the 08-25 cookie incident. One stranded
YouTube source c9432390 ("A Really Interesting One Day Options Strategy") left in the notebook.
Fix 12:00 UTC: harvest.log → harvest.log.cycle2-part1, stale lock removed, `harvest 40` restarted
(pid 322; ledger-driven, so it continues from the 12 remaining + next pending), heartbeat written.
`nlm source delete` without `--confirm` prompts and aborts — the stranded c9432390 stays until the
harvester exits (R5), then delete with `--confirm`. harvest_one's `before` snapshot excludes it, so
the re-added copy is selected unambiguously.
LESSON / R9: a `docker exec -d` job does not survive a Docker restart, and neither does the
supervising agent of a finished session. Every session touching SMB must (a) read the heartbeat
age first, (b) if container StartedAt > last log line ⇒ restart the chunk, no diagnosis needed,
(c) leave a supervisor agent running for as long as the session lives.

### 2026-08-25 12:40 → 16:47 UTC — supervisor killed by session limit; post-chunk steps did not run (4 h gap)
Symptom: heartbeat stale 12:39→16:47. The cycle-2 chunk (`harvest 40`, pid 322, restarted 12:00) finished
on its own (ledger 221 transcribed) but the supervisor agent died with the Claude session at ~12:40, so
cleanup/audit/sync/distill/next-chunk never ran (R9(c) again — the supervisor's life is the session's).
Resume 16:5x: harvester dead (lock pid gone, /proc grep clean, container StartedAt 09:54 unchanged),
auth valid. Cleanup: stale lock removed; 5 leftover YouTube sources deleted after re-list (stranded
c9432390 + 4× DUY1tapNfZE) → notebook = 4 keep sources. audit 221 ok / 0 suspect. sync_archives:
archive vol.1 = 141 videos (2,392,834 chars), vol.2 = 80 videos (1,187,496 chars). Distill batch 5
agent launched (backlog 120 → 15 taken: vFTpvP8kwzY WDbHqMeSCHA lRj741LUAFo 1HXDto7qXaU RbWA61gJSa4
KPcDNIqd4OI Stfx1brjj0k 4iCQciAzjJY pW2ZZAAPVMI DQ6nTpng7MM ic24mZL9Fdk qm5ENAPUCEA toMmfKHzQXU
weUoHkMBL4A ipzry05eP00).
FINDING — "add refused" is not always rate-limit OR auth: DUY1tapNfZE ("Options Tribe Sam Parikh…",
12k views) got 4× "Could not add url source" (60/300/900 s backoff, ~21 min wasted) while NLM in fact
CREATED a youtube source each time, titled with the raw URL — the video is not fetchable by NLM (likely
a livestream/restricted). Ledger set to `unavailable` (not pending) so it is never retried.
TODO harvest.py: after a refusal, re-list; if a new youtube source titled with the video URL appeared →
delete it and mark `unavailable` immediately (no backoff). Decision: `failed`+"refused" entries are reset
to pending only when auth was the cause; per-video refusals with URL-titled sources = unavailable.
UPDATE 17:1x UTC: the harvest.py TODO above is DONE (patched while no harvester was alive; mirrored in
REZSABM/smb/smb_harvest.py): on a "could not add", re-list; a new source titled with the video URL ⇒
delete the stub, ledger `unavailable`, return without backoff. Auth probe unchanged (runs after).

## COMMENTS PIPELINE (second SMB pipeline — YouTube comments → raw archive + audience analysis)

### 2026-08-25 16:45 UTC — pipeline born (user directive 12:15 UTC; a first agent died before doing anything)
Mechanism REUSED, not invented: yt-dlp `getcomments` exactly as yt2nlm/youtube.py fetch_video (no API key),
cap lifted to `max_comments=all,all,all,all` (yt2nlm caps at 1000 — see market-monitor sharp edge);
verified: the 1.1M-view video returns 1002 comments = YouTube's own comment_count, ~90 s; small videos ~5 s.
Files (container awf-monitor-runner:/app/state/smb-options/, mirrored in REZSABM/smb/): `comments_harvest.py`
(ledger-driven over videos.json most-viewed first; own state only: comments/<id>.jsonl, comments_ledger.json,
comments.log, comments_harvest.lock — NEVER touches the transcript pipeline's ledger/lock/transcripts),
`comments_sync.py` (archive volumes "SMB comments archive vol. N" ~400k chars, temporary "SMB comments batch
<tag>" sources for source-scoped analysis queries, "SMB audience needs vol. 1"; every add is R5-guarded:
exits 75 if harvest.lock pid is alive), `heartbeat-comments.sh` → heartbeats/smb-comments.json (Slot Manager
"Background jobs"). Full collector launched 16:52 UTC (`docker exec -d … comments_harvest.py harvest`), 3-video
e2e test passed first (1,953 comments).
DESIGN DECISION (user, relayed 16:52 UTC — overrides the initial "Haiku, zero NLM quota" plan): the ANALYSIS is
done by NotebookLM itself on work4 quota, market-monitor style: batch source uploaded → fixed question set asked
source-scoped (`nlm notebook query -s <sid>`) → answers parsed → batch source deleted → comments merged into the
archive. Per-comment coverage is verified by numbering every comment in the rendered source (`[#n 👍likes date]`,
replies `#n.k`) and checking every number comes back; if NLM's per-comment coverage proves unreliable, NLM keeps
the digest/takeaways/needs role and the per-comment topic count is done locally (stated in audience-needs.md).
Haiku-via-OAuth path (cigna pattern) was verified working (0.9 s) but is NOT used for the analysis by user decision.
Commenter display names stay in the raw archive (NLM) only — never in audience-needs.md, digests, memory, commits;
the local mirror /workspace/smb/comments/ is gitignored.

### 2026-08-25 16:55 UTC — user refinement: spend NLM quota WISELY (relayed by coordinator)
No per-video / small-batch queries. Batch unit = one COMPLETED "SMB comments archive vol. N" (~400k chars ≈
1.5–2k comments; volumes are stable once the next one starts because videos arrive in fixed most-viewed order).
Round = 4 fixed questions over that volume's source (concerns+new topics / takeaways / unanswered questions /
needs), a handful of rounds per day (R8), every query logged below with purpose + size. Per-comment counting =
local rule-based classifier (`~/.claude/skills/smb-audience/scripts/classify.py`, zero quota; coarse — ~40% of
comments fall into offtopic/praise sinks in v0, NLM's concern ranking is used to refine rules). Temporary batch
sources dropped from the design (test source cd25b3c0 deleted, no AI quota spent on it). Local layer first run:
4,882 comments / 10 videos classified 16:56 UTC.
#### NLM query log (comments pipeline)
- 2026-08-25 16:59 UTC NLM query `concerns` over "SMB comments archive vol. 1" (source bf1a74ec, purpose: concerns layer of audience-needs.md): answered in 68s, 5099 chars
- 2026-08-25 16:59 UTC NLM query `takeaways` over "SMB comments archive vol. 1" (source bf1a74ec): NO ANSWER after 1s () → stop round, retry later (exit 75)
Batch 5 DONE 17:2x UTC: 15/15 read to EOF, volume 39,216 → 45,044 words, new "SMB Options vol. 1" =
6f972687-1d57-4379-86ec-11dcb98c26d8 (old f357475f deleted), commit 5f6b7f5; distill backlog 105.
Comments pipeline (parallel agent) uploaded "SMB comments archive vol. 1–3" while no harvester was
alive (R5 respected). Next: journal sync → chunk 3 (harvest 40, patched harvest.py).

### 2026-08-25 17:00 UTC — resume: chunk 2 done (221/364), chunk 3 launched; openday :8114 wedged forward restarted
Heartbeat check first (R9): container StartedAt 09:54 unchanged, harvest.log ended at [40/40] of chunk 2,
harvest.lock left EMPTY (stale — note: `test -d /proc/$(cat lock)` with an empty lock is a FALSE "alive",
check the pid string is non-empty). Ledger 221 transcribed / 141 pending / 2 unavailable. Comments collector
alive (pid 1754, 20/364 videos). work4 auth valid. Patched smb_harvest.py (URL-titled stub ⇒ unavailable)
verified identical to the container copy; committed. Chunk 3 = `harvest 40` launched 17:0x UTC.
Side incident: http://localhost:8114/ (openday-serve) dead for the user although container Up + app
listening ⇒ wedged port forward after the 09:54 Docker restart; `docker restart openday-serve` → 200.
- 2026-08-25 17:02 UTC INCIDENT: `takeaways` query returned empty after 1 s (transient; identical query answered fine 2 min later). Manual reproduction printed only the first 800 chars of the answer → that answer was NOT stored = one wasted work4 query. Fixes: analyze.py resumes from `vol-N.md.partial` (never re-asks an answered question) + one retry after 45 s on an empty answer; rule: every NLM answer goes to a file BEFORE any peek.

### 2026-08-25 17:02 UTC — DOCKER ENGINE RESTART #2 (root cause found: openday video render OOMs the WSL VM)
All 30 containers restarted 17:02:36; claude session died ("it crashed again"). Harvester (chunk 3, pid 2162,
at [1/40]) and comments collector (pid 1754, 21/361) killed, locks stale, one stranded YouTube source
2371d404 ("A Lucrative Options Strategy for AMZN" — its ledger entry was already `transcribed`, so only the
notebook copy was orphaned). R9 applied 17:04: auth valid → stranded source deleted (--confirm) → logs rotated
(harvest.log.chunk3-part1, comments.log.part1) → both locks removed → `harvest 40` + `comments_harvest.py
harvest` relaunched (pids 75 / 83), heartbeats green (225 transcribed / 137 pending; comments 25/364, 8,418 stored).
ROOT CAUSE (both restarts today, 09:54 and 17:02): openday-serve `render_full.py` = min(cpu-1,12) = 12 parallel
PIL+ffmpeg libx264 1080p chunks, auto-threaded, no container memory limit → WSL VM (10 GB, ~5 GB in use)
OOM → Docker Desktop restarts the engine. GAZP render finished 09:51 → restart 09:54; SPY tps2 render started
17:01 → restart 17:02. Fix (host workspaces/openday via docker exec -i): OPENDAY_RENDER_WORKERS default 3 +
`-threads 2` per encoder (measured 862 MiB, 753 frames/min); `docker update --memory 3g --memory-swap 3g
openday-serve` live + same flags in scripts/serve.sh. Verified: the unpatched 12-chunk run under the cap pinned
at 3.0 GiB but Docker SURVIVED (cap contains the blast radius). Lesson: `docker exec` without `-i` swallows a
heredoc silently — the first patch attempt was a no-op; always grep-verify.
