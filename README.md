# REZSABM

Backtest lab: **Rezvyakov-style breakout entry** (daily candle closes above the previous
day's high → long at that close) × **SABM R-target exits** (stop at the signal candle's
body bottom; profit target at entry + k·R for R1/R2/R3; resting orders, gaps fill at the
open; a day touching both stop and target counts pessimistically as a stop).

Serving: **http://localhost:8112/** — container `rezsabm-serve` (`--restart unless-stopped`),
rebuild with `scripts/serve.sh`. Code is bind-mounted; server/front-end changes need only a
container restart (server) or a page reload (front-end).

## Layout

- `server.js` — zero-dependency node server: static `public/`, results at `/results/...`,
  `/api/variants`.
- `public/index.html` — viewer: stats, SABM-style portfolio graph, R-distribution,
  filterable trade table, per-entry animated webp videos.
- `scripts/sabm_r1_spy.py` — backtest + Pillow renderer.
  `python3 scripts/sabm_r1_spy.py --symbol SPY --rk 1 [--minr-pct 0.1] [--videos]`
  → writes `data/results/<SYMBOL>_R<k>[_minR..]/` (stats.json, trades.json, graphs, videos/).
- `uploads/<SYM>_daily_OHLC_yahoo.csv` — daily OHLC per instrument (Yahoo chart API);
  fetch with `scripts/fetch-ohlc.sh <SYM>`.
- Knowledge basis: SABM course in NotebookLM notebook `b57ecd77-292a-434b-90c4-6956723634d3`
  (account work4). Quote history can be mirrored there as a document (multi-instrument).

## Doctrine

Working mode (user 2026-08-23): tasks are split across agents — a **SABM-auditor** checks
every change against the original course PDF; a **video agent** owns the entry videos;
mass renders are gated on the user's approval of a corrected sample.

## Exit advisor (tab 2)

Upload a screenshot of an open position; the **NotebookLM notebook "SABM — Sortir au Bon
Moment"** (work4) says where to exit. The brain is the notebook — this app only carries the
picture there and renders the answer.

How the picture reaches a text-only notebook, **without spending Claude tokens**:

1. `scripts/chart_pdf.py` folds the picture into ONE rolling PDF (`data/advisor/charts.pdf`),
   newest page last, each page stamped with consult id, UTC date/time and the trader's note.
2. That PDF replaces the single source titled **"REZSABM chart uploads"** in the notebook —
   replace-by-title, so no matter how many charts are analysed the notebook keeps 3 sources
   and the 50-source cap never moves.
3. NotebookLM reads the image itself and answers from the SABM course, quoting it.

Optional **precise mode** adds a Claude vision pass that transcribes the chart into neutral
facts (no advice) before asking — for charts whose levels are not printed on the axes. That
one costs Claude tokens; the default path costs none.

Measured limits (first real consults, 2026-08-30): printed text, axis labels and dates are
read exactly; levels the model must *infer from pixels* (an unlabelled swing low, a gridline
step) can be invented. Put your real entry/stop/current price in the notes field.

Serialisation: work4 runs one job at a time. A consult takes
`state/smb-options/nlm_external.lock`; the SMB pipeline daemon idles while it exists, and
`distill_local.py` now checks it between videos, so an interactive question never waits for a
10-video extraction batch.

Extra mounts this needs (see `scripts/serve.sh`): the Docker socket (to run the `nlm` CLI
inside `awf-monitor-runner`, where the work4 cookies live), `/nlmwork` (shared dir — the PDF
crosses the container boundary through it) and `/seed:ro` (Claude OAuth, precise mode only).
