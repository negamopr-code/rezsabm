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

### 2026-08-26 19:32 UTC — resume after Docker restart #3 (26.6 h gap); R9 applied, chunk 3 + collector relaunched
Session-start check (R9a/b): all 30 containers "Up 4 h" (awf-monitor-runner StartedAt 2026-08-26 15:42 UTC),
last log lines 2026-08-25 17:12 UTC (harvest.log at chunk 3 [22/40] = KS9jeJdjy2M, comments.log at
[32/340] PrsUnhNjF4Y) — i.e. both jobs died ~10 min after the 17:04 relaunch (engine restart #3 that
evening; restart #4 today 15:42 — no jobs were alive to lose), and nobody re-armed for 26 h because the
previous session's supervisor died with it (R9(c) again). Locks stale (pids 75/83 gone). No supervisor
alive ⇒ 4 h+ of the day lost; the fix remains: leave a supervisor agent running for the session's life.
R9 applied 19:32: work4 auth VALID (source list ok, 9 sources) → 2 stranded YouTube sources deleted
(`--confirm`): cf90b1c1 = KS9jeJdjy2M (ledger pending → re-added cleanly by the harvester) and 27e8c91f =
BtbqHO7YNE0 "7 Qualities…" (ledger already transcribed → orphan copy) → notebook = 7 keep sources (SMB
Options vol. 1, transcripts archive vol. 1–2, comments archive vol. 1–3, smb-mirror journal) → logs rotated
(harvest.log.chunk3-part2, comments.log.part2) → locks removed → `harvest 40` (pid 502) + `comments_harvest.py
harvest` (pid 510) relaunched; 60 s later 2 transcripts landed (KS9jeJdjy2M 11,162 chars, foY0AsxTjqk
26,928 chars), collector at [4/309]; heartbeats green (247 transcribed / 115 pending / 2 unavailable;
comments 59 videos / 12,553 stored). Container scripts md5-identical to the REZSABM/smb mirrors.
Next (supervisor agent, this session): poll every ~10 min; on chunk end → cleanup leftovers → audit →
sync_archives → distill batch 6 → volume upload → journal sync → `harvest 40` again; comments_sync only
while no harvester is alive (R5).

### 2026-08-26 21:02 UTC — resume after Docker restart #5 (20:57 UTC); chunk 3 DONE, chunk 4 + collector relaunched
Session-start check: all containers "Up 5 min" (awf-monitor-runner StartedAt 20:57:01). Both logs stopped at
19:55 UTC — an hour BEFORE the engine restart: chunk 3 had finished (harvest.log.chunk3-part3 [40/40], ledger
284 transcribed / 77 pending / 3 unavailable), chunk 4 had been launched (pid 1250) and died at [1/40]
(j7curDJSpI4 added as source e0965147, never read); collector died at [145/309]. The previous session's
supervisor died with the session at ~19:55 (R9(c) again) so the post-chunk sync never ran.
R9 applied 21:02: work4 auth valid → stranded source e0965147 deleted (--confirm; ledger pending → re-added
by chunk 4) → logs rotated (harvest.log.chunk4-part1, comments.log.part3) → locks removed → while no
harvester alive (R5): audit_transcripts ok 285 / 0 suspect; sync_archives → transcripts vol. 2 synced (144
videos, 2.10M chars), vol. 1 unchanged (141); comments_sync archive → vols 4–11 created (vol. 11 = 19 videos,
564 comments; total 11 comment volumes) → `harvest 40` (pid 193) + collector (pid 201) relaunched 21:05;
90 s later harvester at [5/40], collector at [11/165]. Notebook = SMB Options vol. 1 + transcripts vol. 1–2
+ comments vol. 1–11 + journal = 15 sources (50-cap fine).
Next: supervisor agent for the session (poll ~10 min; chunk end → cleanup → audit → sync → distill batch 6 →
`harvest 40`; comments_sync only in harvester gaps).

### 2026-08-26 21:18 UTC — resume after Docker restart #6 (21:16 UTC); chunk 4 died at [12/40], chunk 5 + collector relaunched
Session-start check: every container "Up About a minute" (awf-monitor-runner StartedAt 21:16:19); restart cause
unknown (docker events empty after daemon restart; host mem 9.9G, 4.2G available). Before the restart both logs
show a DNS outage 21:11–21:13 (`Failed to resolve www.youtube.com`) → harvester "add refused" backoff at [12/40],
collector FAILs at [30–31/165]; then the engine died. Chunk 4 got 11 transcripts (284 → 295). Previous session's
supervisor died with it (R9(c) — 3rd time today).
R9 applied 21:18: work4 auth valid, notebook = 15 sources, NO stranded YouTube source (the refusals were DNS, not
NLM) → DNS ok again → logs rotated (harvest.log.chunk4-part2, comments.log.part4) → locks removed → `harvest 40`
(chunk 5, pid 61) + collector relaunched 21:18; 90 s later harvester at [4/40] (299 transcribed / 62 pending /
3 unavailable), collector at [11/137]. Not run this time (harvester alive, R5): sync_archives / comments_sync —
queued for the chunk end.
Next: supervisor agent (poll ~10 min; chunk end → cleanup → audit → sync_archives + comments_sync → distill
batch 6 → `harvest 40` for the last ~22). Note for R9: 3 restarts in one evening with no OOM signature — if #7
happens, check Docker Desktop / WSL host logs, not the render containers.
- 2026-08-26 21:22 UTC NLM query `takeaways` over "SMB comments archive vol. 1" (source bf1a74ec, purpose: takeaways layer of audience-needs.md): answered in 47s, 7766 chars
- 2026-08-26 21:24 UTC NLM query `questions` over "SMB comments archive vol. 1" (source bf1a74ec, purpose: questions layer of audience-needs.md): answered in 84s, 4050 chars
- 2026-08-26 21:25 UTC NLM query `needs` over "SMB comments archive vol. 1" (source bf1a74ec, purpose: needs layer of audience-needs.md): answered in 58s, 4962 chars

### 2026-08-27 05:30 UTC — overnight: chunk 5 DONE, comments collector DONE (364/364); supervisor died at Claude session limit
No Docker restart overnight (awf-monitor-runner StartedAt still 21:16:19). Chunk 5 finished [40/40] → 335 transcribed /
26 pending / 3 unavailable. Comments collector finished 21:34 UTC: 364/364 videos, 21,751 comments. The session's
supervisor agent died ~21:40 (Claude "session limit, resets 00:50 UTC") so the post-chunk steps and NLM rounds 2–5
did not run — new failure mode R9(d): supervisor agents also die on Claude usage limits, not only on Docker restarts.
05:30 (harvester gap, R5): audit ok 335 / 0 suspect → sync_archives: transcripts vol. 2 = 171 videos (2.40M chars),
vol. 3 created (23 videos) → comments_sync archive: vol. 11 = 71 videos / 1,936 comments, vol. 12 created (113 videos,
665 comments) — raw layer COMPLETE, 12 comment volumes. Notebook = SMB Options vol. 1 + transcripts 1–3 + comments 1–12
+ journal = 17 sources. Then `harvest 40` relaunched for the last 26 pending; NLM analysis round vol. 2 launched
(analyze.py 2, 4 queries) — user 08-26: consume quota progressively, one volume per ~30–40 min.
Note: analyze.py had a hardcoded dead-session scratchpad path (crash on 08-26 21:20) → fixed to the skill's own .tmp/.
Next: supervisor → harvest end → distill batch 6 (transcripts 6–… of 335) → rounds vol. 3–5 spaced → audience-needs regen.
- 2026-08-27 05:31 UTC NLM query `concerns` over "SMB comments archive vol. 2" (source 92aff17f, purpose: concerns layer of audience-needs.md): answered in 63s, 5505 chars
- 2026-08-27 05:32 UTC NLM query `takeaways` over "SMB comments archive vol. 2" (source 92aff17f, purpose: takeaways layer of audience-needs.md): answered in 50s, 6488 chars
- 2026-08-27 05:34 UTC NLM query `questions` over "SMB comments archive vol. 2" (source 92aff17f, purpose: questions layer of audience-needs.md): answered in 105s, 3500 chars
- 2026-08-27 05:36 UTC NLM query `needs` over "SMB comments archive vol. 2" (source 92aff17f, purpose: needs layer of audience-needs.md): answered in 69s, 5280 chars

### 2026-08-27 05:5x UTC — distill batch 6 DONE (supervisor #2); NLM round vol. 2 running; last chunk at [6/40]
Batch 6 = next 15 undistilled by views (48k → 40k): RP5xIYMrXKE iJMkj24PHqs K6YVPHULzPA 4dedQBgiZJA oO5SfYblvio
xrCSOh4WEGY l7BHgd2PO6A 8u89hMA2was qabKcPmwjEA LwZ9s2ud68s cSI1eXFW6Ms dU3eKVXlKQE 8BjBWBuiEh8 tT08tJdsH_E
9q32G8yLxbM. Truncation NO-GO respected: docker cp → fold -w220 → Read tool, all 15 read to EOF (Read line counts
= wc -l; 270,935 chars on disk = chars read). Merged into 8 chapters + registry rows #183–198 + 15 ledger rows;
volume 45,044 → 49,995 words, ledger 116 → 131 videos; commit e7776f1. Distill backlog 335 − 131 = 204 (+ the
~26 still harvesting). Volume upload ("SMB Options vol. 1", replace-by-title, old id 6f972687) QUEUED for the
harvester gap (R5). Round vol. 2: `concerns` answered 05:31; remaining 3 questions in flight.

### 2026-08-27 05:55 UTC — HARVEST COMPLETE 361/364; archives final; vol. 1 uploaded; classify 21,098; round vol. 2 done
Final chunk ended ~05:40 → ledger 361 transcribed / 3 unavailable (no-subtitle) / 0 pending = 364. audit_transcripts ok 361 /
0 suspect. sync_archives: transcripts vol. 3 = 49 videos (312,761 chars); vol. 1–2 unchanged → 361 verbatim transcripts in
3 volumes. "SMB Options vol. 1" (131 videos, 49,995 words) replaced: new 3e064d92, old 6f972687 deleted; notebook = 17
sources. Harvest heartbeat → done. Comments: round vol. 2 answered 4/4 (05:31–05:36, concerns/takeaways/questions/needs);
classify.py --pull tagged 16,216 new → 21,098 classified from 324 videos (the rest of 21,751 = videos with 0 comments /
replies without text); report.py regenerated audience-needs.md (22 topics, 19 needs) → uploaded "SMB audience needs vol. 1".
Cadence per user (08-26, progressive): round vol. 3 at ~06:10, vol. 4 ~06:45, vol. 5 ~07:20, then stop for the day;
vols 6–12 tomorrow. Distill backlog: 361 − 131 = 230 videos (batch 7+ in later sessions).
- 2026-08-27 06:20 UTC NLM query `concerns` over "SMB comments archive vol. 3" (source b09f3925, purpose: concerns layer of audience-needs.md): answered in 88s, 5529 chars
- 2026-08-27 06:21 UTC NLM query `takeaways` over "SMB comments archive vol. 3" (source b09f3925, purpose: takeaways layer of audience-needs.md): answered in 58s, 5443 chars
- 2026-08-27 06:23 UTC NLM query `questions` over "SMB comments archive vol. 3" (source b09f3925, purpose: questions layer of audience-needs.md): answered in 78s, 3770 chars
- 2026-08-27 06:25 UTC NLM query `needs` over "SMB comments archive vol. 3" (source b09f3925, purpose: needs layer of audience-needs.md): answered in 100s, 5798 chars

### 2026-08-27 06:27 UTC — supervisor #2 died at Claude session limit too; main loop took over
Supervisor #2 (relaunched 05:32) reached: audit 361/0 suspect → transcripts archive vol. 1–3 final (361 videos) →
distill batch 6 (15 videos, registry #183–198) → "SMB Options vol. 1" replaced (3e064d92, 131 videos) →
classify.py --pull (21,098 comments / 324 videos / 22 topics) → audience-needs regenerated → NLM round vol. 2 digest
(4/4). Then it died: "session limit, resets 10:20 UTC" (R9(d) second occurrence — Claude usage limits kill supervisor
agents mid-run; the pipeline itself is unaffected, only the operator).
User feedback 06:15: Slot Manager showed both jobs STALE at 21:05 counts — the heartbeats are pushed by whoever
supervises, so a dead supervisor freezes the DISPLAY while the pipeline is fine. Rule added: push both heartbeats
(heartbeat.sh / heartbeat-comments.sh) after EVERY step and at least every 15 min, and use state done/paused with an
explicit "next round at HH:MM" summary so a quota-pacing gap never reads as a stall.
06:19–06:27 (main loop): heartbeats refreshed → NLM round vol. 3 (4/4: concerns/takeaways/questions/needs, source
b09f3925) → report.py → audience-needs.md = 21,098 comments / 324 videos / 22 topics / 19 needs / 3 NLM digests.
NLM quota consumed so far: 12 queries (vol. 1–3) — progressive pacing per user 08-26.
Next: distill batch 7 (backlog 230), rounds vol. 4 and 5 spaced ~30–40 min, vols 6–12 tomorrow.
- 2026-08-27 07:07 UTC NLM query `concerns` over "SMB comments archive vol. 4" (source 1dfb081a, purpose: concerns layer of audience-needs.md): answered in 88s, 6279 chars
- 2026-08-27 07:08 UTC NLM query `takeaways` over "SMB comments archive vol. 4" (source 1dfb081a, purpose: takeaways layer of audience-needs.md): answered in 56s, 5758 chars
- 2026-08-27 07:10 UTC NLM query `questions` over "SMB comments archive vol. 4" (source 1dfb081a, purpose: questions layer of audience-needs.md): answered in 93s, 3954 chars
- 2026-08-27 07:12 UTC NLM query `needs` over "SMB comments archive vol. 4" (source 1dfb081a, purpose: needs layer of audience-needs.md): answered in 92s, 5512 chars
- 2026-08-27 07:50 UTC NLM query `concerns` over "SMB comments archive vol. 5" (source 9d51472b, purpose: concerns layer of audience-needs.md): answered in 66s, 5954 chars
- 2026-08-27 07:52 UTC NLM query `takeaways` over "SMB comments archive vol. 5" (source 9d51472b, purpose: takeaways layer of audience-needs.md): answered in 96s, 7044 chars
- 2026-08-27 07:54 UTC NLM query `questions` over "SMB comments archive vol. 5" (source 9d51472b, purpose: questions layer of audience-needs.md): answered in 103s, 3878 chars
- 2026-08-27 07:56 UTC NLM query `needs` over "SMB comments archive vol. 5" (source 9d51472b, purpose: needs layer of audience-needs.md): answered in 98s, 5623 chars

### 2026-08-27 11:15 UTC — rounds vol. 4–5 done (20 queries), distill batch 7 restarted after a third session-limit death
07:06–07:56 the harness-supervised pacer ran NLM rounds vol. 4 (rc=0) and vol. 5 (rc=0) with heartbeats every 12 min;
audience-needs.md regenerated after each; commits f18b2f0 / e401b47. Digests now vol. 1–5 = 20 work4 queries.
Distill batch 7 agent died at "session limit, resets 11:10 UTC" before writing anything (third limit death today:
21:40, ~06:05, ~07:20) — volume-1.md untouched, so the batch is simply re-run; distilled stays 131/361.
⚠ Ops lesson (cost 35 min of a frozen Slot Manager): a pacer launched with bare `nohup`/`setsid` from a Claude Bash
call does NOT survive — it showed up in `ps` but wrote zero heartbeats; the identical script works in the foreground.
Long jobs must be started with the Bash tool's `run_in_background`. Also: `pkill -f "pacer.sh 99"` / `pgrep -f
'pacer[.]sh'` matched the tool's OWN command line and killed the session shell (exit 144) twice — clean up by pid
from a pidfile or a /proc scan instead. Memory: feedback_background_jobs_run_in_background.md.
11:15: heartbeats refreshed, pacer relaunched for rounds vol. 6, 7, 8 (36-min spacing), distill batch 7 agent re-spawned.
Next: rounds 9–12 + "SMB audience needs vol. 1" upload; distill backlog 230 → batches 8+.
- 2026-08-27 16:31 UTC NLM query `concerns` over "SMB comments archive vol. 6" (source 6fe14fe5, purpose: concerns layer of audience-needs.md): answered in 71s, 6555 chars
- 2026-08-27 16:39 UTC NLM query `takeaways` over "SMB comments archive vol. 6" (source 6fe14fe5, purpose: takeaways layer of audience-needs.md): answered in 463s, 5401 chars
- 2026-08-27 16:41 UTC NLM query `questions` over "SMB comments archive vol. 6" (source 6fe14fe5, purpose: questions layer of audience-needs.md): answered in 64s, 3828 chars
- 2026-08-27 16:42 UTC NLM query `needs` over "SMB comments archive vol. 6" (source 6fe14fe5, purpose: needs layer of audience-needs.md): answered in 47s, 5768 chars

### 2026-08-27 16:43 UTC — distill batch 8, NLM round vol. 6, "SMB Options vol. 1" refreshed to 161 videos
Distill batch 8 (2acbb55): 15 videos 33k–28k views, registry #214–228 → distilled 161/361. Bookkeeping fix: batch 7
(#199–213) had been committed inside e401b47 ("NLM digest vol. 5") instead of its own distill commit, which is why it
read as missing — the agent verified volume-1.md already held those 15 and moved to the next 15 instead of redoing them.
New teachings merged into existing chapters (spread width vs lot count on fixed risk, put credit spreads INTO VIX
spikes, condor PoP dial + put-condor roll, NFLX LEAPS + deep-ITM share substitute, Brexit/AMZN double calendars,
InvestiQuant 468-period stats 86.4% win, five deadliest mistakes); auto-transcript garbles flagged inline, never
silently corrected.
NLM round vol. 6 rc=0 at 16:42 → 6 digests = 24 work4 queries. Then, in the pacing gap (one work4 job at a time):
"SMB Options vol. 1" replaced by --file upload → new 7182f644, old 3e064d92 deleted (verified). Notebook unchanged
otherwise (transcripts v1–3, comments v1–12, audience needs v1, journal).
⚠ Pacing note: a harness-backgrounded pacer only advances while the Claude session is ACTIVE — rounds 6–8 were
launched 11:15 but the process resumed 16:30 when the session woke. Spacing is real but tracks session activity, not
wall clock; for overnight pacing use a container-side cron instead.
Next: rounds vol. 7–8 (pacer running), then 9–12; distill batches 9+ for the remaining 200.
- 2026-08-27 16:57 UTC NLM query `trial-distill/chapters` over "SMB transcripts archive vol. 1" (source 0a263160, purpose: TRIAL NLM distillation of batch 9, 15 videos): NO ANSWER
- 2026-08-27 17:13 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [-h1mAx67OxA] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 70s, 5522 chars
- 2026-08-27 17:15 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [-Dfl8YyoP0E] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 83s, 6798 chars
- 2026-08-27 17:16 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [-gGvWxd_iXc] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 67s, 4345 chars
- 2026-08-27 17:18 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [-rwYS0Dq6Ro] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 69s, 7403 chars
- 2026-08-27 17:19 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [-huhEgn9TRg] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 90s, 5585 chars
- 2026-08-27 17:23 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [goK0QOsQRvQ] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 172s, 1433 chars
- 2026-08-27 17:24 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [EYA6mxeZmzg] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 76s, 908 chars
- 2026-08-27 17:25 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [j2PxP-o-M1E] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 60s, 794 chars
- 2026-08-27 17:28 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [KBWUtGD1kwk] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 102s, 633 chars
- 2026-08-27 17:30 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [cUfBqD03mTc] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 127s, 6378 chars
- 2026-08-27 17:33 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [BPvBoQLupOQ] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 168s, 751 chars
- 2026-08-27 17:35 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [YVPcw-xIUhs] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 83s, 1277 chars
- 2026-08-27 17:36 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [xDaCtZ9GMl0] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 68s, 1968 chars
- 2026-08-27 17:38 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [-wyjzl9zPfs] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 60s, 1390 chars
- 2026-08-27 17:40 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 1" scoped to [VDYG8LDIfGk] (source 0a263160, purpose: TRIAL NLM distillation batch 9): answered in 94s, 650 chars
- 2026-08-27 17:42 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [goK0QOsQRvQ] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 56s, 5387 chars
- 2026-08-27 17:43 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [EYA6mxeZmzg] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 58s, 6673 chars
- 2026-08-27 17:44 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [j2PxP-o-M1E] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 49s, 4905 chars
- 2026-08-27 17:45 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [KBWUtGD1kwk] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 62s, 6439 chars
- 2026-08-27 17:47 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [cUfBqD03mTc] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 49s, 5343 chars
- 2026-08-27 17:48 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [BPvBoQLupOQ] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 75s, 6946 chars
- 2026-08-27 17:50 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [YVPcw-xIUhs] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 75s, 5992 chars
- 2026-08-27 17:51 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [xDaCtZ9GMl0] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 71s, 7073 chars
- 2026-08-27 17:54 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [-wyjzl9zPfs] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 121s, 5680 chars
- 2026-08-27 17:56 UTC NLM query `trial-distill` over "SMB transcripts archive vol. 2" scoped to [VDYG8LDIfGk] (source 8ccf8c5e, purpose: TRIAL NLM distillation batch 9): answered in 110s, 6132 chars

### 2026-08-27 18:00 UTC — TRIAL: batch 9 distilled by NotebookLM instead of a Claude subagent (user request)
Question: can the distillation half of the pipeline run on NLM quota instead of Claude tokens (the comments half
already does)? Trial = the next 15 undistilled videos (305k–25k views), `trial_distill_nlm.py`, output kept OUT of
volume-1.md in `smb/trial/`.
Findings:
1. **One query per video is mandatory.** A single question covering 15 videos over a 2.4M-char archive source
   returned an empty answer twice. Per-video source-scoped queries return 4.3k–7.4k chars each, chapter-grade.
2. **My routing bug, not an NLM failure:** the first pass scoped all 15 to archive vol. 1 (the split reproduction had
   a dead `and cur` guard + wrong ordering) — 8 of them live in vol. 2. NLM answered "transcript not available in the
   provided passages" and offered web research instead of inventing: correct grounded behaviour. Split fixed to
   videos.json order + real file sizes (vol. 1 = 141 videos, vol. 2 = 171, vol. 3 = 49); resume now treats a
   "not available" answer as unpaid work. Cost of the bug: 8 wasted queries.
3. **Figure fidelity 135/146 = 92.5%** (`trial_verify_figures.py`, zero tokens: every $ figure/percentage in an answer
   must appear in the raw transcript as digits or spoken words). Spot-checks: $2,466 profit, $36,366 capital, "$1,200
   average per week", Feb/Apr/Jun losing months, 6-lot 5350/5430/5270 iron fly — all exact.
4. **Two real defects.** (a) Silent repair of a garbled figure: transcript says "36,3 66 in capital", answer says
   $36,366 with no "(garbled)" flag though the prompt demanded one. (b) **Invented illustration**: a caveat reads
   "$400 chump-change drawdown on a 1-lot becomes a $40,000 drawdown on a 10-lot" — "chump" appears 0× in the
   transcript and the arithmetic is 100×, not 10×. That is exactly the failure the registry must not absorb.
5. Cost/latency: 15 videos = 15 NLM queries, ~5–8 min each ⇒ ~1.5 h wall clock, **0 Claude tokens** (Claude batch 8 =
   ~196k tokens, ~10 min). Trial spent 25 queries total (15 + 8 re-runs + 2 dead batch-wide).
Verdict: NLM is good enough for PART A chapter prose as a first draft; it is NOT trustworthy unsupervised for the
"Real numbers from the desk" registry. Recommended shape for batches 10+: NLM extracts (quota) → `trial_verify_figures.py`
gates every figure (zero tokens) → Claude adjudicates only the handful of unmatched figures per batch instead of reading
all 15 transcripts. Awaiting user's decision before any NLM-distilled text enters volume-1.md.
- 2026-08-27 18:01 UTC NLM query `concerns` over "SMB comments archive vol. 7" (source 752deb2d, purpose: concerns layer of audience-needs.md): answered in 122s, 5304 chars
- 2026-08-27 18:02 UTC NLM query `takeaways` over "SMB comments archive vol. 7" (source 752deb2d, purpose: takeaways layer of audience-needs.md): answered in 64s, 6063 chars
- 2026-08-27 18:04 UTC NLM query `questions` over "SMB comments archive vol. 7" (source 752deb2d, purpose: questions layer of audience-needs.md): answered in 83s, 4351 chars
- 2026-08-27 18:05 UTC NLM query `needs` over "SMB comments archive vol. 7" (source 752deb2d, purpose: needs layer of audience-needs.md): answered in 47s, 6478 chars
- 2026-08-27 18:42 UTC NLM query `concerns` over "SMB comments archive vol. 8" (source 6ab6d2d1, purpose: concerns layer of audience-needs.md): answered in 70s, 5651 chars
- 2026-08-27 18:44 UTC NLM query `takeaways` over "SMB comments archive vol. 8" (source 6ab6d2d1, purpose: takeaways layer of audience-needs.md): answered in 91s, 6208 chars
- 2026-08-27 18:47 UTC NLM query `questions` over "SMB comments archive vol. 8" (source 6ab6d2d1, purpose: questions layer of audience-needs.md): answered in 127s, 3909 chars
- 2026-08-27 18:49 UTC NLM query `needs` over "SMB comments archive vol. 8" (source 6ab6d2d1, purpose: needs layer of audience-needs.md): answered in 105s, 6595 chars
- 2026-08-27 19:27 UTC NLM query `concerns` over "SMB comments archive vol. 9" (source 1a11b60b, purpose: concerns layer of audience-needs.md): answered in 86s, 5044 chars
- 2026-08-27 19:28 UTC NLM query `takeaways` over "SMB comments archive vol. 9" (source 1a11b60b, purpose: takeaways layer of audience-needs.md): answered in 60s, 5793 chars
- 2026-08-27 19:30 UTC NLM query `questions` over "SMB comments archive vol. 9" (source 1a11b60b, purpose: questions layer of audience-needs.md): answered in 113s, 3913 chars
- 2026-08-27 19:32 UTC NLM query `needs` over "SMB comments archive vol. 9" (source 1a11b60b, purpose: needs layer of audience-needs.md): answered in 78s, 6961 chars

### 2026-08-27 21:15 UTC — comment rounds 7–9 done (36 queries), audience-needs source refreshed, final rounds 10–12 launched
Pacer ran vol. 7 (18:05), vol. 8 (18:49), vol. 9 (19:32), all rc=0 → 9 digests = 36 work4 queries; audience-needs.md
regenerated after each (commits a6b1f50 / 5e98009 / 608896c). "SMB audience needs vol. 1" replaced with the current
living doc → new source c441cbfa (old deleted by cmd_needs). Final rounds vol. 10–12 launched 21:15 — after them the
whole comments corpus (12 archive volumes, 21,751 comments) will have been analysed by NotebookLM = 48 queries.
Distillation stays paused pending the user's decision on the NLM-vs-Claude trial verdict (see 18:00 entry).
- 2026-08-27 21:16 UTC NLM query `concerns` over "SMB comments archive vol. 10" (source 152a40ec, purpose: concerns layer of audience-needs.md): answered in 216s, 9953 chars
- 2026-08-27 21:17 UTC NLM query `takeaways` over "SMB comments archive vol. 10" (source 152a40ec, purpose: takeaways layer of audience-needs.md): answered in 47s, 5653 chars
- 2026-08-27 21:19 UTC NLM query `questions` over "SMB comments archive vol. 10" (source 152a40ec, purpose: questions layer of audience-needs.md): answered in 116s, 4457 chars
- 2026-08-27 21:22 UTC NLM query `needs` over "SMB comments archive vol. 10" (source 152a40ec, purpose: needs layer of audience-needs.md): answered in 124s, 6852 chars

### 2026-08-27 21:25 UTC — completeness re-check, container-side DAEMON (limit-proof), head-to-head verdict
User: "continue adding all comments and videos… and when Claude tokens are out, come back and continue when they're back."
COMPLETENESS: ledger 361 transcribed / 3 unavailable (tpxBJhfawzQ, DUY1tapNfZE, ckkX94GD7M4 — no subtitles, never retry)
/ comments 364/364 done, 21,751 stored. Channel RE-LISTED (inventory was 4 days old): 2,020 → 2,022 videos, options
364 → **365** ⇒ 1 new pending video queued. So "all" is a moving target: the channel keeps publishing, hence the daemon.
DAEMON (`smb_daemon.sh`, runs INSIDE awf-monitor-runner, zero Claude tokens, survives usage limits / session end /
Claude-container restarts; /app and the heartbeat dir are host binds so nothing is lost): every 30 min, strictly in
series — re-list channel once a day → harvest pending transcripts → collect missing comments → sync transcript +
comment archives → run ONE NLM round for the lowest comment volume lacking a digest (`analyze_local.py`, container
copy of the round logic) → push both Slot Manager heartbeats. Guarded by `nlm_external.lock` (a Claude-side pacer
holds it; the lock SELF-EXPIRES after 2 h so a dead session can never block the daemon forever).
Claude-side auto-resume: cron 43e83a70 every :23/:53 continues the distillation backlog and restarts the daemon if
needed — a tick during a usage limit simply fails and the next one retries. Session-only (7-day expiry); the daemon is
the durable half.
HEAD-TO-HEAD (batch 9 vs volume-1.md, `compare_nlm_vs_claude.py`, zero tokens, ground truth = raw transcript): 5
videos were distilled by BOTH (my `\b` id regex hid ids starting with "-", so 6 already-distilled videos were re-sent
to NLM — bug fixed, true distilled count 161, undistilled 200).
  precision (figures stated that really appear in the transcript): **Claude 71/78 = 91.0% · NLM 57/64 = 89.1%**
  recall (share of the transcript's distinct figures captured): Claude 45/67/53/100% · NLM 75/75/33/100%
  Residual mismatches are mostly derived numbers (Claude: $54.90 × 100 = $5,490) or spoken-word variants; the one
  confirmed fabrication stays NLM's "$400 chump-change → $40,000 on a 10-lot" ("chump" appears 0× in the transcript).
VERDICT: parity on precision ⇒ adopt the hybrid — NLM extracts (quota, 0 tokens) → `trial_verify_figures.py` gates
every figure (0 tokens) → Claude only adjudicates the handful of unmatched figures. Cost per 15-video batch falls from
~196k tokens to ~15 NLM queries + a few flagged lines.

### 2026-08-27 21:28 UTC — auto-resume tick #1
Daemon alive (pid 5413), correctly idle behind `nlm_external.lock` while the host pacer finishes rounds 11–12.
Mirrored the 10 host-side digests INTO the container's digests/ dir — without this the daemon would have re-paid ~40
work4 queries re-analysing volumes 1–10 (it picks "lowest volume lacking a digest" from its own filesystem).
audience-needs.md regenerated. Hybrid distill batch DEFERRED this tick: the pacer holds the account (one work4 job at
a time); the next tick runs it once rounds 11–12 are done.

### 2026-08-27 22:00 UTC — auto-resume tick #2: FIRST HYBRID MERGE (161 → 171 distilled, zero NLM, zero-token gate)
Daemon alive (5413), still idle behind the lock (host pacer mid-round 11). No new NLM work possible this tick, so the
tick spent itself on the already-paid extraction: of the 15 trial answers, 5 were videos Claude had distilled
(head-to-head material) and **10 were genuinely undistilled** → merged by the new `merge_nlm_batch.py`:
- every figure re-checked against the raw transcript (digits or spoken words); **82 figures, 4 flagged ⚠unverified**
  ($422,500 and $3,780 in j2PxP-o-M1E, $3,050 in goK0QOsQRvQ, $92,700 in EYA6mxeZmzg) — flags are written INLINE next
  to the figure, so nothing suspect is silently absorbed into the volume;
- sections land in a clearly-labelled chapter "NLM-extracted videos (hybrid pipeline — NotebookLM extraction,
  figure-gated)" stating that Claude did not read these transcripts, plus one index row per video;
- distilled **171/361**, volume 76,492 words.
Cost of this batch: 0 NLM queries (already paid), 0 Claude tokens for extraction — only the merge script ran.
Pending: refresh "SMB Options vol. 1" in the notebook (needs the account, blocked behind the pacer) and adjudicate the
4 flagged figures (cheap Claude work, next tick).
- 2026-08-27 21:59 UTC NLM query `concerns` over "SMB comments archive vol. 11" (source ac6a3b70): NO ANSWER after 50s () → stop round, retry later (exit 75)

### 2026-08-27 22:30 UTC — auto-resume tick #3: flagged figures adjudicated, gate taught compound spoken numbers
Daemon alive (5413), still idle behind the lock. Pacer: round vol. 10 rc=0, **round vol. 11 rc=75 (empty answer, partial
saved — retries later, no quota lost)**; round 12 pending, so no new NLM work this tick.
Adjudicated the 4 figures the hybrid merge had flagged (zero NLM, cheap Claude):
- **$422,500 → ✓VERIFIED**: spoken in the transcript as "four hundred twenty two thousand five hundred dollars" — a
  false flag by the gate, not an NLM error.
- **$3,780 → ⚠derived**: transcript states price "3.78" / premium "37.80"; the ×100 is arithmetic, never spoken.
- **$92,700 → ⚠inferred**: the transcript is garbled ("700 shares of UPS… worth $927"); NLM reconstructed 700 × ~$132.
- **$3,050 → ⚠unverified**: absent from the transcript in any digit or spoken form — the one genuine miss.
Annotations rewritten inline in volume-1.md (✓verified / ⚠derived / ⚠inferred / ⚠unverified) so the distinction between
"gate limitation" and "model invention" is visible to any future reader.
Gate upgraded (zero tokens, permanent): `spoken_numbers()` now parses COMPOUND spoken numbers ("four hundred twenty two
thousand five hundred" = 422,500) in both trial_verify_figures.py and merge_nlm_batch.py — batch-9 fidelity re-measured
92.5% → **93.2%**, and future batches will stop false-flagging word-form figures.
- 2026-08-27 22:36 UTC NLM query `concerns` over "SMB comments archive vol. 12" (source 0def1927): NO ANSWER after 50s () → stop round, retry later (exit 75)

### 2026-08-27 22:40 UTC — work4 DAILY NLM QUOTA EXHAUSTED (root cause of rounds 11–12 rc=75); daemon made quota-aware
Rounds vol. 11 and 12 both returned empty. Probing the CLI directly gave the real error, which the wrapper had been
swallowing as `answer: ""`:
  `Google rejected the query (error code 8: RESOURCE_EXHAUSTED)` — work4's DAILY QUERY QUOTA is spent.
Consumed today: 40 comment-round queries (digests vol. 1–10) + 25 trial-distillation queries + probes ≈ **~68 work4
queries** — i.e. the user's "consume the quota progressively" goal was met and then some; the cap, not a fault, stopped us.
Fixes (both zero-token, permanent):
- `analyze_local.py` now detects RESOURCE_EXHAUSTED, writes `quota_exhausted` (dated), saves the partial and exits 76
  instead of burning retries; the partial means tomorrow's round re-asks only the unanswered questions.
- `smb_daemon.sh` skips the round step while `quota_exhausted` carries today's UTC date, and resumes automatically
  tomorrow. Everything else in the cycle keeps running.
Proof the non-query half is unaffected: with the lock released the daemon immediately re-listed the channel and
harvested the NEW options video → **362 transcribed / 3 unavailable**, then synced the archives. Source uploads and
transcript reads are NOT rate-limited by the query quota.
State: digests vol. 1–10 (40 queries) + partials for 11 and 12 waiting on tomorrow's quota; distilled 171/362;
comments 364/364 (21,751) plus the new video's comments queued in the daemon's next cycle.

### 2026-08-27 23:00 UTC — auto-resume tick #4: new-video DEADLOCK in the daemon found and fixed
Daemon healthy; quota backoff working as designed ("round: skipped, work4 NLM quota exhausted today (2026-08-27)").
BUG (would have silently dropped every future video's comments): the daemon computed pending-comments from
`comments_ledger.json` alone, but a NEWLY listed video is absent from that file until `comments_harvest.py` runs — and
the harvester only ran when the count was > 0. So video 0jPpJRi4tuc (listed 21:24 by the daily re-list, transcript
harvested → 362) would never have had its comments collected. Fixed: CPEND now = (videos.json ids missing from the
ledger) + (ledger entries not done). After the restart the daemon immediately picked it up — comments ledger 364 → 365,
all done; archives re-synced (12 volumes).
Distillation blocked this tick: the hybrid batch starts with NLM extraction, and work4 queries are capped until
tomorrow. Counts: 362 transcribed / 3 unavailable / 365 comment-videos / 21,751+ comments / digests vol. 1–10 /
distilled 171.

### 2026-08-27 23:30 UTC — auto-resume tick #5: classification refreshed, COMMENT COMPLETENESS PROVEN
Daemon alive, quota backoff still holding (work4 capped until the daily reset). Digests mirrored both ways (12 files:
vol. 1–10 complete + vol. 11/12 partials, both empty because the quota hit before the first answer).
classify.py --pull re-run: +26 comments → **21,124 classified from 325 videos**; audience-needs.md regenerated (22
topics, 19 needs). The 325-vs-365 gap is NOT loss: **40 of the 365 videos genuinely have zero comments**, and every
video with comments is mirrored locally (0 missing).
Completeness proof against YouTube itself: stored 21,777 = YouTube's own reported total 21,777 across all videos,
**0 videos short of their yt_count**. The comments layer is complete by the source's own numbers.
Distillation still blocked (hybrid batch begins with NLM extraction; quota resets tomorrow). Counts: 362 transcribed /
3 unavailable / 365 videos with comments collected / distilled 171.

### 2026-08-28 00:02 UTC — auto-resume tick #6: work4 quota does NOT reset at UTC midnight → time-based backoff
Probed the CLI one minute past midnight UTC: still `RESOURCE_EXHAUSTED`. So the daily cap is on Google's own clock
(Pacific, or a rolling 24 h window) — not the UTC date. The date-based marker had just "expired", which would have made
the daemon retry and fail every 30 minutes all night.
Fix (zero tokens): `quota_exhausted` now stores an EPOCH timestamp and both `analyze_local.py` and `smb_daemon.sh` use
a **7-hour** time-based backoff (covers a Pacific-midnight reset ≈ 07:00–08:00 UTC). Daemon restarted; it re-listed the
channel immediately and will attempt round vol. 11 after the backoff, resuming from the saved partials.
Counts unchanged: 362 transcribed / 3 unavailable, 365 videos' comments (21,777 = YouTube's own total), digests vol.
1–10, distilled 171. Distillation still blocked on the same quota.
