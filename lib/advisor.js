// Exit advisor — the tab is only a viewport; the brain is the SABM notebook.
//
// One consult = one chart + the whole conversation about it. Both live in ONE rolling PDF
// (scripts/chart_pdf.py): page = stamp + picture + transcript. That PDF replaces the single
// "REZSABM chart uploads" source after every exchange, so the notebook re-reads its own
// earlier verdicts as a source, the source count never grows, and erasing a consult here
// erases it from what the notebook can see.
//
// Default path costs ZERO Claude tokens. "Precise mode" adds one Claude vision pass that
// transcribes the chart into neutral facts (no advice) for charts without printed levels.
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
const stamp = () => new Date().toISOString().slice(0, 16).replace('T', ' ');

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

// ── store ──────────────────────────────────────────────────────────────────────────────
function history() {
  let all;
  try { all = JSON.parse(fs.readFileSync(LOG, 'utf8')); } catch { return []; }
  // Consults written before the conversation model existed carry a single {answer} field.
  // Lift them into turns[] on read so an early verdict is never lost from the PDF or the UI.
  const migrated = all.map(c => c.turns ? c : ({
    ...c,
    turns: [{ role: 'user', at: c.when, image: c.image,
              text: c.notes || 'Where should this position be exited?' },
            ...(c.answer ? [{ role: 'nlm', at: c.when, text: c.answer }] : [])],
  }));
  // Persist the lift once: chart_pdf.py reads this file directly and only understands turns[].
  if (migrated.some((c, i) => c !== all[i])) save(migrated);
  return migrated;
}

function save(all) {
  fs.mkdirSync(DIR, { recursive: true });
  fs.writeFileSync(LOG, JSON.stringify(all, null, 1));
}

function put(entry) {
  const all = history().filter(c => c.id !== entry.id);
  all.push(entry);
  save(all);
  return entry;
}

/** Rebuild the PDF from consults.json and hand it to the notebook (replace-by-title).
 *  Serialised: two exchanges can never upload at once. */
let publishing = Promise.resolve();
function publish() {
  publishing = publishing.catch(() => {}).then(async () => {
    const info = JSON.parse(await run('python3', ['scripts/chart_pdf.py', 'sync']));
    if (!info.pdf) return info;                      // nothing left to publish (all erased)
    await sabm.publishCharts(PDF);
    return info;
  });
  return publishing;
}

// ── the question the notebook is asked ─────────────────────────────────────────────────
function openingQuestion(id, when, notes, facts) {
  return [
    `Use the source "${sabm.SOURCE_TITLE}" (a PDF where each page is an uploaded chart followed by the conversation about it) together with the SABM course.`,
    `Judge the page headed "CHART UPLOAD ${id}", uploaded ${when} UTC — the LAST chart in that PDF. Earlier pages are history you may refer to.`,
    notes ? `\nWhat the trader says about this position: ${notes}` : '\nThe trader gave no extra notes.',
    facts ? `\nA vision model transcribed the chart as follows (observed data, not advice):\n${facts}` : '',
    `\nDecide, using ONLY the SABM method as the course states it, where this position should be exited.`,
    `Answer in English, in this structure:`,
    `1. WHAT YOU SEE — instrument, timeframe and the price structure you read from the page (say plainly if the image is unreadable).`,
    `2. WHICH SABM RULE APPLIES — name it as the course names it (R1/R2/R3 target, Dow structure trailing, trendline break, deep trailing…) and why this chart matches it.`,
    `3. THE EXIT — a concrete level or a precise condition ("close below the last structural low at X"). If the chart does not show enough to fix a level, say exactly what is missing instead of guessing.`,
    `4. WHAT WOULD CHANGE IT — what invalidates this exit, or when to move it.`,
    `Quote the course where it decides the matter.`,
  ].filter(Boolean).join('\n');
}

const followUp = (id, message) =>
  `Still about the chart on the page headed "CHART UPLOAD ${id}" in the source "${sabm.SOURCE_TITLE}" ` +
  `(that page also carries everything we have already said about it).\n\n${message}\n\n` +
  `Answer from the SABM course, quoting it where it decides the matter. If the chart does not show what you need, say what is missing.`;

// ── operations ─────────────────────────────────────────────────────────────────────────

/** New chart → first verdict. */
async function consult({ imageBase64, mime, notes = '', precise = false }) {
  const ext = EXT[mime] || 'png';
  const id = new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14);
  const when = stamp();
  const image = `${id}-1.${ext}`;
  fs.mkdirSync(path.join(DIR, 'raw'), { recursive: true });
  fs.writeFileSync(path.join(DIR, 'raw', image), Buffer.from(imageBase64, 'base64'));

  let facts = '';
  if (precise) {
    const text = await claude.messages(
      [claude.imageBlock(imageBase64, mime || 'image/png'), { type: 'text', text: VISION_PROMPT }],
      { maxTokens: 2000 });
    const j = claude.extractJson(text);
    facts = j ? JSON.stringify(j, null, 1) : text.slice(0, 4000);
  }

  const entry = put({ id, when, notes, precise, facts, image,
    turns: [{ role: 'user', at: when, image,
              text: notes || 'Where should this position be exited?' }] });

  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');
  sabm.takeLock();
  try {
    await publish();                                  // the picture must be a source before we ask
    const q = openingQuestion(id, when, notes, facts);
    const r = await sabm.ask(q, null);
    entry.turns.push({ role: 'nlm', at: stamp(), text: r.answer });
    entry.conversationId = r.conversationId;
    put(entry);
    publish();                                        // fold the verdict into the PDF, in background
    return entry;
  } finally {
    sabm.releaseLock();
  }
}

/** A follow-up PICTURE — the trader draws his objections on the chart and re-uploads.
 *  It joins the SAME consult (same id, same section of the PDF, same NLM conversation), so
 *  the notebook sees it as another view of one position rather than a new trade. */
async function addImage(id, { imageBase64, mime, message = '' }) {
  const entry = history().find(c => c.id === id);
  if (!entry) throw new Error('no such consult');
  const ext = EXT[mime] || 'png';
  const n = entry.turns.filter(t => t.image).length + 1;
  const image = `${id}-${n}.${ext}`;
  fs.writeFileSync(path.join(DIR, 'raw', image), Buffer.from(imageBase64, 'base64'));
  const at = stamp();
  entry.turns.push({ role: 'user', at, image, text: message || 'Another view of the same position — see the annotations on the picture.' });
  put(entry);

  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');
  sabm.takeLock();
  try {
    await publish();                                  // the new picture must be IN the source first
    const q = `Still the position on the page headed "CHART UPLOAD ${id}" in the source "${sabm.SOURCE_TITLE}". ` +
      `The trader has added PICTURE ${n} (uploaded ${at} UTC) to that same section — read it, including anything drawn or written on it.\n\n` +
      `${message || 'What he is asking is drawn on the picture.'}\n\n` +
      `Answer from the SABM course, quoting it where it decides the matter. Say plainly if the annotation is unreadable.`;
    const r = await sabm.ask(q, null, { conversationId: entry.conversationId });
    entry.turns.push({ role: 'nlm', at: stamp(), text: r.answer });
    if (r.conversationId) entry.conversationId = r.conversationId;
    put(entry);
    publish();
    return entry;
  } finally {
    sabm.releaseLock();
  }
}

/** Follow-up turn in the same NLM conversation, about the same chart. */
async function chat(id, message) {
  const entry = history().find(c => c.id === id);
  if (!entry) throw new Error('no such consult');
  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');
  sabm.takeLock();
  try {
    const r = await sabm.ask(followUp(id, message), null, { conversationId: entry.conversationId });
    entry.turns.push({ role: 'user', at: stamp(), text: message });
    entry.turns.push({ role: 'nlm', at: stamp(), text: r.answer });
    if (r.conversationId) entry.conversationId = r.conversationId;
    put(entry);
    publish();                                        // the exchange lands under its picture
    return entry;
  } finally {
    sabm.releaseLock();
  }
}

/** Erase a consult here → its page leaves the PDF → the notebook stops seeing it. */
async function erase(id) {
  const all = history();
  const gone = all.find(c => c.id === id);
  if (!gone) throw new Error('no such consult');
  save(all.filter(c => c.id !== id));
  for (const t of gone.turns || []) {                 // every picture of the thread, not just the first
    if (t.image) { try { fs.unlinkSync(path.join(DIR, 'raw', t.image)); } catch {} }
  }
  const info = await publish();
  return { erased: id, remaining: history().length, pdf: info };
}

module.exports = { consult, chat, addImage, erase, history, publish, DIR, VISION_PROMPT };
