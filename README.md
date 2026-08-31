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

1. `scripts/chart_pdf.py` rebuilds ONE rolling PDF (`data/advisor/charts.pdf`) from
   `data/advisor/consults.json`. One consult = one section, headed by its id and UTC time,
   holding **everything about that position in order**: the picture, the verdict, any
   follow-up picture, and every message either side sent.
2. That PDF replaces the single source titled **"REZSABM chart uploads"** in the notebook —
   replace-by-title, so no matter how many charts are analysed the notebook keeps 3 sources
   and the 50-source cap never moves.
3. NotebookLM reads the image itself and answers from the SABM course, quoting it.

**Chat.** Every consult is a live NotebookLM conversation (`conversation_id`), so follow-ups
keep the context: *"and if it closes below 623.58 tomorrow?"*. Each exchange is written back
under its picture in the PDF, so the notebook re-reads its own earlier verdicts as a source.

**Follow-up pictures.** Disagree with a verdict? Draw your objection on the chart and upload
it again — it joins the **same** section, same id, same conversation, as PICTURE 2, 3, … The
tool never files a picture silently: after every upload it asks *where does this picture
belong* — a new chart, or a follow-up to one of the existing consults.

**Erase.** 🗑 removes the consult, its pictures and its whole conversation; the PDF is rebuilt
without that section and re-published, so the notebook stops seeing it too.

Optional **precise mode** adds a Claude vision pass that transcribes the chart into neutral
facts (no advice) before asking — for charts whose levels are not printed on the axes. That
one costs Claude tokens; the default path costs none.

**Why the first verdict used to be wrong.** The opening ETHUSD consult (2026-08-30) applied the
generic *"après R2 → trendline break → trail to the first creux"* rule and named the wrong exit.
The moment the trader pointed at the **speed** of the move, the notebook produced the right
rule with a course quote it had had all along: price reached R3 on the first session after the
breakout, which the course treats as a violent arrival demanding *"la sortie ... en intraday"*.
The knowledge was in the corpus; the question never made it look. So now:

- **Qualifying facts gate** — before it may name a rule, the notebook must answer the course's
  own preconditions (sessions to R1/R2/R3, violent vs gradual, intraday vs close, phase,
  whether a trendline may be drawn yet) and say *"not visible"* rather than guess. Section 2 of
  every answer. `POST /api/advisor/refresh-criteria` spends ONE query to let the course
  restate that checklist in its own words (`data/advisor/criteria.md`); until then a
  built-in fallback list is used.
- **Standing corrections** — 📌 on any answer where you pushed back and it conceded stores the
  lesson (`data/advisor/corrections.json`) and prepends it to every future verdict, so the
  same class of miss does not recur on the next chart. Listed in the tab, removable with ✕.

**Guided walk (default for a new chart).** Instead of hoping the notebook checks the right
things, the tool walks the course's own exit decision tree with you: one question at a time,
each next question determined by your last answer, starting with the tempo of arrival at the R
levels because the course makes that decisive. You answer what only you can see (your
platform, the sessions, the intraday fill); the notebook is asked nothing until the walk ends,
so a guided consult still costs **two** work4 queries however long the tree is:

1. it answers the same questions **from the picture alone** — no course reasoning, "not
   visible" allowed, guessing not;
2. it then rules, with your answers, its own reading and any standing corrections in front of
   it, and must list every **disagreement** first. Your answers are the facts of record; a
   disagreement is a flag for you to resolve, never a silent override.

`lib/tree_fallback.json` is a hand-written spine so the walker is never dead;
`POST /api/advisor/tree/refresh` spends one query to have the course emit its own tree, which
is validated (no dangling branch, every terminal quotes the course) before it is installed.
The whole walk — every question, your answer, the rule it lands on, the course quote and the
notebook's independent reading — is drawn into that chart's section of the PDF, so the
decisions accumulate as a database the notebook reads on later consults.

Optional `precise` adds Claude as a third reader answering the same tree questions.

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
