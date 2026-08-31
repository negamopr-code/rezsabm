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
const tree = require('./tree');

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
const syncPdf = () => run('python3', ['scripts/chart_pdf.py', 'sync']).catch(() => {});

/** Snapshot of the walk so far, so the PDF (and a download) always shows the live path —
 *  chart_pdf.py renders consult.walk and knows nothing about the tree. */
function snapshotWalk(entry) {
  const st = tree.walk(entry.answers || []);
  entry.walk = { ...(entry.walk || {}), path: st.path, inProgress: !st.done,
                 rule: st.done ? st.rule : null, exit: st.done ? st.exit : null,
                 quote: st.done ? st.quote : null };
  return st;
}

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

// ── what the notebook must establish before it may name a rule ─────────────────────────
// The first ETHUSD verdict (2026-08-30) applied the generic post-R2 trendline rule and got
// the exit wrong: price had reached R3 in ONE session, which the course treats as a violent
// arrival demanding an intraday exit. The knowledge was in the corpus — the question simply
// never required it to look. So every opening question now carries the qualifying checklist.
// FALLBACK is used until refreshCriteria() has asked the course for its own list.
const CRITERIA_FILE = path.join(DIR, 'criteria.md');
const CORRECTIONS_FILE = path.join(DIR, 'corrections.json');

const FALLBACK_CRITERIA = `- how many sessions passed from the breakout to R1, to R2 and to R3?
- was any level reached in ONE session (violent arrival) or gradually?
- was each level reached intraday, or on the close?
- which phase is the trade in now: before R1, between R1 and R2, after R2, after R3?
- is a trendline validly drawable yet, and on which two lows?
- has the tempo of the move changed since entry?`;

const criteria = () => {
  try { return fs.readFileSync(CRITERIA_FILE, 'utf8').trim() || FALLBACK_CRITERIA; }
  catch { return FALLBACK_CRITERIA; }
};

function corrections() {
  try { return JSON.parse(fs.readFileSync(CORRECTIONS_FILE, 'utf8')); } catch { return []; }
}

function saveCorrections(list) {
  fs.mkdirSync(DIR, { recursive: true });
  fs.writeFileSync(CORRECTIONS_FILE, JSON.stringify(list, null, 1));
}

/** The trader pushed back and the notebook conceded — keep the lesson and put it in front of
 *  every future verdict, so the same class of miss does not recur on the next chart. */
function addCorrection(consultId, turnIndex) {
  const c = history().find(x => x.id === consultId);
  if (!c) throw new Error('no such consult');
  const answer = c.turns[turnIndex];
  const trigger = [...c.turns.slice(0, turnIndex)].reverse().find(t => t.role === 'user');
  if (!answer || answer.role !== 'nlm' || !trigger) throw new Error('pin a notebook answer that follows a message of yours');
  const list = corrections();
  list.push({ at: answer.at, consult: consultId,
              trader: (trigger.text || '').slice(0, 400),
              conceded: (answer.text || '').replace(/\s+/g, ' ').slice(0, 400) });
  saveCorrections(list);
  return list;
}

function removeCorrection(i) {
  const list = corrections();
  if (i < 0 || i >= list.length) throw new Error('no such correction');
  list.splice(i, 1);
  saveCorrections(list);
  return list;
}

const correctionsBlock = () => {
  const list = corrections();
  if (!list.length) return '';
  return `\nSTANDING CORRECTIONS — past consults where the trader was right and you changed your answer. ` +
    `Check every one of these BEFORE you commit to a rule:\n` +
    list.map((c, i) => `${i + 1}. [${c.at}] the trader objected: "${c.trader}" — you then concluded: "${c.conceded}"`).join('\n') + '\n';
};

/** One query, run rarely: let the course define its own qualifying checklist. */
async function refreshCriteria() {
  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');
  sabm.takeLock();
  try {
    const r = await sabm.ask(
      `Using ONLY the SABM course, list the questions that MUST be answered about a chart before one can decide ` +
      `which exit rule applies — the qualifying criteria the method itself requires (tempo and speed of arrival at ` +
      `each R level, intraday versus close, the phase of the trade, whether a trendline may yet be drawn, and any ` +
      `others the course insists on). Output ONLY a flat markdown list of short questions, no preamble, no commentary.`,
      null);
    const list = r.answer.split('\n').filter(l => /^\s*[-*]/.test(l)).join('\n').trim();
    if (!list) throw new Error('the notebook did not return a list');
    fs.mkdirSync(DIR, { recursive: true });
    fs.writeFileSync(CRITERIA_FILE, list + '\n');
    return { criteria: list };
  } finally {
    sabm.releaseLock();
  }
}

// ── the question the notebook is asked ─────────────────────────────────────────────────
function openingQuestion(id, when, notes, facts) {
  return [
    `Use the source "${sabm.SOURCE_TITLE}" (a PDF where each page is an uploaded chart followed by the conversation about it) together with the SABM course.`,
    `Judge the page headed "CHART UPLOAD ${id}", uploaded ${when} UTC — the LAST chart in that PDF. Earlier pages are history you may refer to.`,
    notes ? `\nWhat the trader says about this position: ${notes}` : '\nThe trader gave no extra notes.',
    facts ? `\nA vision model transcribed the chart as follows (observed data, not advice):\n${facts}` : '',
    correctionsBlock(),
    `\nDecide, using ONLY the SABM method as the course states it, where this position should be exited.`,
    `Answer in English, in this structure:`,
    `1. WHAT YOU SEE — instrument, timeframe and the price structure you read from the page (say plainly if the image is unreadable).`,
    `2. QUALIFYING FACTS — before naming any rule, answer each of these from the chart, and say "not visible" rather than guessing:\n${criteria()}`,
    `3. WHICH SABM RULE APPLIES — the rule the course prescribes FOR THAT CASE (not the general one), named as the course names it, and why the qualifying facts above select it.`,
    `4. THE EXIT — a concrete level or a precise condition ("close below the last structural low at X"). If the chart does not show enough to fix a level, say exactly what is missing instead of guessing.`,
    `5. WHAT WOULD CHANGE IT — what invalidates this exit, or when to move it.`,
    `Quote the course where it decides the matter.`,
  ].filter(Boolean).join('\n');
}

const followUp = (id, message) =>
  `Still about the chart on the page headed "CHART UPLOAD ${id}" in the source "${sabm.SOURCE_TITLE}" ` +
  `(that page also carries everything we have already said about it).\n\n${message}\n\n` +
  `Answer from the SABM course, quoting it where it decides the matter. If the chart does not show what you need, say what is missing.`;

// ── operations ─────────────────────────────────────────────────────────────────────────

// ── guided walk ────────────────────────────────────────────────────────────────────────
// The trader answers the course's questions (he can see his platform; the picture cannot show
// everything), the notebook answers the SAME questions from the picture alone, and the two are
// compared before any verdict. His answers are the facts of record — a disagreement is a flag
// for him to resolve, never a silent override.

/** Start a guided consult: store the picture, publish it, return the first question. */
async function start({ imageBase64, mime, notes = '', precise = false }) {
  const ext = EXT[mime] || 'png';
  const id = new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14);
  const when = stamp();
  const image = `${id}-1.${ext}`;
  fs.mkdirSync(path.join(DIR, 'raw'), { recursive: true });
  fs.writeFileSync(path.join(DIR, 'raw', image), Buffer.from(imageBase64, 'base64'));

  const entry = put({ id, when, notes, precise, facts: '', image, guided: true, answers: [],
                      turns: [{ role: 'user', at: when, image,
                                text: notes || 'Guided SABM exit walk — starting.' }] });
  snapshotWalk(entry); put(entry);
  syncPdf();          // the PDF file is kept current locally; the upload happens at conclude
  return { ...entry, step: tree.walk([]) };
}

/** Record one answer and hand back the next question — no NLM query until the walk ends. */
function answer(id, choice) {
  const entry = history().find(c => c.id === id);
  if (!entry) throw new Error('no such consult');
  const next = tree.walk([...(entry.answers || []), choice]);
  if (next.error) throw new Error(next.error);
  entry.answers = [...(entry.answers || []), choice];
  snapshotWalk(entry);
  put(entry);
  syncPdf();          // every answer lands in the PDF immediately, no NLM call
  return { ...entry, step: next };
}

function undo(id) {
  const entry = history().find(c => c.id === id);
  if (!entry) throw new Error('no such consult');
  entry.answers = (entry.answers || []).slice(0, -1);
  snapshotWalk(entry);
  put(entry);
  syncPdf();
  return { ...entry, step: tree.walk(entry.answers) };
}

const readingPrompt = (id, qs) =>
  `Look ONLY at the picture(s) on the page headed "CHART UPLOAD ${id}" in the source "${sabm.SOURCE_TITLE}". ` +
  `Answer each question below FROM THE PICTURE ALONE — no course reasoning, no advice, and never guess: ` +
  `write "not visible" whenever the chart does not show it.\n\n` +
  qs.map((q, i) => `${i + 1}. ${q.q}\n   choose one of: ${q.options.join(' | ')} | not visible`).join('\n') +
  `\n\nOutput one line per question, exactly "<number>. <chosen option> — <what you saw that decides it>".`;

/** The walk is finished: ask the notebook to read the chart itself, compare, then rule. */
async function conclude(id) {
  const entry = history().find(c => c.id === id);
  if (!entry) throw new Error('no such consult');
  const step = tree.walk(entry.answers || []);
  if (!step.done) throw new Error('the walk is not finished');
  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');

  const asked = step.path.map(p => ({ q: p.q, options: [] }));
  const qs = tree.allQuestions().filter(q => step.path.some(p => p.node === q.id));

  sabm.takeLock();
  try {
    await publish();                                // the picture must be in the source first
    // 1. the notebook's own reading of the same questions
    const reading = await sabm.ask(readingPrompt(id, qs.length ? qs : asked), null,
                                   { conversationId: entry.conversationId });
    entry.conversationId = reading.conversationId || entry.conversationId;

    // 2. optional third opinion from Claude's eyes (costs Claude tokens)
    let claudeReading = '';
    if (entry.precise) {
      const img = fs.readFileSync(path.join(DIR, 'raw', entry.image)).toString('base64');
      claudeReading = await claude.messages([
        claude.imageBlock(img, EXT[entry.image.split('.').pop()] ? `image/${entry.image.split('.').pop()}` : 'image/png'),
        { type: 'text', text: `${VISION_PROMPT}\n\nThen answer, from the picture only, one line each:\n` +
            qs.map((q, i) => `${i + 1}. ${q.q}`).join('\n') }], { maxTokens: 2000 });
    }

    // 3. the verdict, with both readings on the table
    const walkText = step.path.map((p, i) =>
      `${i + 1}. ${p.q}\n   TRADER: ${p.answer}${p.kind === 'number' && p.unit ? ' ' + p.unit : ''}`).join('\n');
    const q = [
      `Still the position on the page headed "CHART UPLOAD ${id}" in the source "${sabm.SOURCE_TITLE}".`,
      correctionsBlock(),
      `\nThe trader walked the course's own exit decision tree and answered:\n${walkText}`,
      `\nA local spine walked those answers to: ${step.rule} — ${step.exit}. Treat that as PROVISIONAL: it branches only on categorical answers and deliberately does NOT interpret the numbers above, because how the course classifies a given tempo is yours to say, not ours.`,
      `\nYou read the same questions from the picture as:\n${reading.answer}`,
      claudeReading ? `\nA vision model read the picture as (observed data, not advice):\n${claudeReading.slice(0, 2500)}` : '',
      `\nNow answer, in English:`,
      `1. DISAGREEMENTS — every question where your reading of the picture differs from the trader's answer, and what you saw. If none, say "none".`,
      `2. WHAT THE TEMPO MEANS — take the raw numbers the trader gave (sessions to each R level) and say which scenario the COURSE puts them in, in its own words and with its own threshold if it states one. Do not round them into categories we invented.`,
      `3. IS THE PROVISIONAL RULE RIGHT — does "${step.rule}" hold once that tempo is taken into account, or does the course prescribe something else for this exact combination? Quote the course.`,
      `4. THE EXIT — the concrete level or condition. The trader's answers are the facts of record; where you disagree, give the exit under HIS answers first, then say how it would change under yours.`,
      `5. WHAT WOULD CHANGE IT.`,
    ].filter(Boolean).join('\n');

    const r = await sabm.ask(q, null, { conversationId: entry.conversationId });
    entry.turns.push({ role: 'user', at: stamp(), text: `Guided walk completed:\n${walkText}\n\nTree rule: ${step.rule}` });
    entry.turns.push({ role: 'nlm', at: stamp(), text: `**Notebook's own reading of the chart**\n\n${reading.answer}\n\n---\n\n${r.answer}` });
    if (r.conversationId) entry.conversationId = r.conversationId;
    entry.walk = { path: step.path, inProgress: false, rule: step.rule, exit: step.exit,
                   quote: step.quote, reading: reading.answer };
    put(entry);
    publish();
    return entry;
  } finally {
    sabm.releaseLock();
  }
}

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
      `${message || 'What he is asking is drawn on the picture.'}\n` + correctionsBlock() +
      `\nBefore committing to a rule, re-answer the qualifying facts from this new picture:\n${criteria()}\n\n` +
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

module.exports = { consult, chat, addImage, erase, history, publish, criteria, corrections,
                   start, answer, undo, conclude, tree,
                   addCorrection, removeCorrection, refreshCriteria, DIR, VISION_PROMPT };
