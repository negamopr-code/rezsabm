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
