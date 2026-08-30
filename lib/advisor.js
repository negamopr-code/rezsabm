// Exit advisor — the tab is only a viewport; the brain is the SABM notebook.
//
// Flow of one consult (default path costs ZERO Claude tokens):
//   picture → one rolling PDF (scripts/chart_pdf.py, newest page last, each page stamped)
//           → replaces the single "REZSABM chart uploads" source in the SABM notebook
//           → NotebookLM reads the picture itself and answers from the course
// "Precise mode" additionally has Claude transcribe the chart into neutral facts (no advice)
// and pastes them into the question — for charts whose levels are not printed on the axes.
const { execFile } = require('child_process');
const fs = require('fs');
const path = require('path');

const claude = require('./claude');
const sabm = require('./sabm');

const ROOT = path.dirname(__dirname);
const DIR = path.join(ROOT, 'data', 'advisor');
const PDF = path.join(DIR, 'charts.pdf');
const LOG = path.join(DIR, 'consults.json');

const EXT = { 'image/png': 'png', 'image/jpeg': 'jpg', 'image/webp': 'webp' };

const run = (cmd, args, opts = {}) => new Promise((resolve, reject) =>
  execFile(cmd, args, { cwd: ROOT, maxBuffer: 8e6, ...opts },
    (e, stdout, stderr) => (e ? reject(new Error((stderr || e.message).slice(-400))) : resolve(stdout))));

const VISION_PROMPT = `You are the EYES of a trading assistant, not its brain. Read this chart screenshot and report only what is visually present.

Hard rules:
- Never give trading advice. Do not suggest an exit, a target, a stop or a direction — another system decides that from its own methodology.
- Never invent a number. If the price axis is unreadable, say so instead of estimating.

Reply with JSON only:
{"instrument": "", "timeframe": "", "price_axis": {"readable": true, "labels": []},
 "current_price": "", "structure": {"trend": "", "last_swing_high": "", "last_swing_low": "",
 "recent_bars": ""}, "drawn_objects": [], "position_markers": {"entry": "", "stop": "", "target": ""},
 "unreadable": []}`;

function question(id, when, notes, facts) {
  return [
    `Use the source "${sabm.SOURCE_TITLE}" (a PDF of uploaded chart screenshots) together with the SABM course.`,
    `The chart to judge is the page headed "CHART UPLOAD ${id}", uploaded ${when} UTC — the LAST page of that PDF. Ignore the earlier pages except as history.`,
    notes ? `\nWhat the trader says about this position: ${notes}` : '\nThe trader gave no extra notes.',
    facts ? `\nA vision model transcribed the chart as follows (observed data, not advice):\n${facts}` : '',
    `\nDecide, using ONLY the SABM method as the course states it, where this position should be exited.`,
    `Answer in English, in this structure:`,
    `1. WHAT YOU SEE — instrument, timeframe and the price structure you are reading from the page (say plainly if the image is unreadable).`,
    `2. WHICH SABM RULE APPLIES — name it as the course names it (R1/R2/R3 target, Dow structure trailing, trendline break, deep trailing…) and why this chart matches it.`,
    `3. THE EXIT — a concrete level or a precise condition ("close below the last structural low at X"). If the chart does not show enough to fix a level, say exactly what is missing instead of guessing.`,
    `4. WHAT WOULD CHANGE IT — what invalidates this exit, or when to move it.`,
    `Quote the course where it decides the matter.`,
  ].filter(Boolean).join('\n');
}

function history() {
  try { return JSON.parse(fs.readFileSync(LOG, 'utf8')); } catch { return []; }
}

function record(entry) {
  const all = history().filter(c => c.id !== entry.id);
  all.push(entry);
  fs.writeFileSync(LOG, JSON.stringify(all.slice(-200), null, 1));
}

async function consult({ imageBase64, mime, notes = '', precise = false }) {
  const ext = EXT[mime] || 'png';
  const now = new Date();
  const id = now.toISOString().replace(/[-:T]/g, '').slice(0, 14);      // 20260830T164500 → 20260830164500
  const when = now.toISOString().slice(0, 16).replace('T', ' ');
  fs.mkdirSync(path.join(DIR, 'raw'), { recursive: true });
  const raw = path.join(DIR, 'raw', `${id}.${ext}`);
  fs.writeFileSync(raw, Buffer.from(imageBase64, 'base64'));

  // 1. rolling PDF — one page per upload, stamped, newest last
  const pdfInfo = JSON.parse(await run('python3', ['scripts/chart_pdf.py', 'add', raw, id, when, notes || 'no notes']));

  // 2. optional Claude eyes (precise mode)
  let facts = '';
  if (precise) {
    const text = await claude.messages(
      [claude.imageBlock(imageBase64, mime || 'image/png'), { type: 'text', text: VISION_PROMPT }],
      { maxTokens: 2000 });
    const j = claude.extractJson(text);
    facts = j ? JSON.stringify(j, null, 1) : text.slice(0, 4000);
  }

  // 3. one work4 job at a time — the SMB daemon idles while this lock exists
  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');
  sabm.takeLock();
  try {
    const chartSource = await sabm.publishCharts(PDF);
    const answer = await sabm.ask(question(id, when, notes, facts), null);
    const entry = { id, when, notes, precise, answer, facts, pages: pdfInfo.pages,
                    image: `${id}.${ext}`, source: chartSource };
    record(entry);
    return entry;
  } finally {
    sabm.releaseLock();
  }
}

module.exports = { consult, history, DIR, VISION_PROMPT };
