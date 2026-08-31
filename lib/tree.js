// The SABM exit decision tree — the course's own branching, walked question by question.
//
// Why a tree at all: the first ETHUSD verdict skipped the tempo of the move and named the
// wrong rule. A checklist asks the notebook to look; a tree cannot advance until the fact
// exists. The trader answers each question (he is the one who can see his platform), the
// notebook answers the same questions from the picture, and disagreements surface before any
// verdict is written.
//
// The tree is extracted FROM the course (refresh()); lib/tree_fallback.json is the hand-written
// spine used until that runs, so the walker is never dead.
const fs = require('fs');
const path = require('path');

const sabm = require('./sabm');

const DIR = path.join(path.dirname(__dirname), 'data', 'advisor');
const FILE = path.join(DIR, 'tree.json');
const FALLBACK = path.join(__dirname, 'tree_fallback.json');

function load() {
  for (const p of [FILE, FALLBACK]) {
    try {
      const t = JSON.parse(fs.readFileSync(p, 'utf8'));
      if (t && t.nodes && t.root && t.nodes[t.root]) return { ...t, derived: p === FILE };
    } catch { /* fall through to the packaged spine */ }
  }
  throw new Error('no usable decision tree');
}

const node = (t, id) => t.nodes[id];

/** Every question on the path so far, with what the trader answered.
 *  A `number` (or `text`) node NEVER branches on its value: bucketing "R3 in 2 sessions" into
 *  violent-or-gradual is the course's call, not a threshold invented here, so the raw answer is
 *  simply carried to the notebook at the end. Only genuinely categorical facts branch locally. */
function walk(answers = []) {
  const t = load();
  const path_ = [];
  let id = t.root;
  for (const a of answers) {
    const n = node(t, id);
    if (!n || n.terminal) break;
    const kind = n.type || 'choice';
    if (kind === 'choice') {
      const opt = (n.options || []).find(o => o.a === a);
      path_.push({ node: id, q: n.q, answer: a, kind });
      if (!opt) return { path: path_, error: `"${a}" is not an option of "${n.q}"` };
      id = opt.next;
    } else {
      path_.push({ node: id, q: n.q, answer: a, kind, unit: n.unit || '' });
      if (!n.next || !t.nodes[n.next]) return { path: path_, error: `"${id}" has no valid next node` };
      id = n.next;
    }
  }
  const cur = node(t, id);
  if (!cur) return { path: path_, error: `the tree points at a missing node "${id}"` };
  if (cur.terminal) {
    return { path: path_, done: true, node: id, rule: cur.rule, exit: cur.exit, quote: cur.quote,
             derived: t.derived };
  }
  return { path: path_, done: false, node: id, q: cur.q, why: cur.why,
           kind: cur.type || 'choice', unit: cur.unit || '',
           options: (cur.options || []).map(o => o.a), derived: t.derived };
}

/** Every question in the tree — what the notebook is asked to answer from the picture. */
function allQuestions() {
  const t = load();
  return Object.entries(t.nodes)
    .filter(([, n]) => !n.terminal)
    .map(([id, n]) => ({ id, q: n.q, kind: n.type || 'choice',
                         options: (n.options || []).map(o => o.a) }));
}

const EXTRACT = `Using ONLY the SABM course, write the EXIT decision tree the method actually follows for an OPEN position: the questions that must be answered, in the order the course requires, and which rule each combination of answers leads to. Start with the tempo/speed of arrival at the R levels, because the course makes that decisive before anything else.

A question whose honest answer is a QUANTITY (how many sessions, how many R, a price) must be asked as a quantity — never as pre-baked ranges. Deciding what "R3 in 2 sessions" means is the course's judgement, made later with the real number in hand; do not invent thresholds.

Output STRICT JSON and nothing else, in exactly this shape:
{"root":"<node id>","nodes":{
  "<id>":{"type":"number","q":"<question>","why":"<one line: why the course asks it here>",
          "unit":"<sessions | R | price>","next":"<node id>"},
  "<id>":{"type":"choice","q":"<question>","why":"<one line>",
          "options":[{"a":"<answer the trader can pick>","next":"<node id>"}]},
  "<id>":{"terminal":true,"rule":"<the rule as the course names it>",
          "exit":"<what to do concretely>","quote":"<verbatim quote from the course, in French>"}
}}

Rules: 12 nodes maximum; every "next" must name a node that exists; every path must end at a terminal node; every terminal must carry a verbatim course quote; use "choice" ONLY where the course itself is categorical; include an option for "not visible on this chart" wherever the trader may be unable to tell.`;

/** One query: let the course define its own tree. */
async function refresh() {
  if (sabm.lockHeld()) throw new Error('another NLM job is running on work4 — try again in a minute');
  sabm.takeLock();
  try {
    const r = await sabm.ask(EXTRACT, null, { timeoutS: 420 });
    const start = r.answer.indexOf('{');
    const end = r.answer.lastIndexOf('}');
    if (start < 0 || end < start) throw new Error('the notebook did not return JSON');
    let t;
    try { t = JSON.parse(r.answer.slice(start, end + 1)); }
    catch (e) { throw new Error(`unparseable tree JSON: ${e.message}`); }

    // Never install a tree that cannot be walked — a dangling "next" would strand the trader.
    if (!t.root || !t.nodes || !t.nodes[t.root]) throw new Error('tree has no usable root');
    const bad = [];
    for (const [id, n] of Object.entries(t.nodes)) {
      if (n.terminal) { if (!n.rule) bad.push(`${id}: terminal without a rule`); continue; }
      if (!n.q) bad.push(`${id}: node without a question`);
      if ((n.type || 'choice') === 'choice') {
        for (const o of n.options || []) if (!t.nodes[o.next]) bad.push(`${id}: option "${o.a}" points at missing "${o.next}"`);
        if (!(n.options || []).length) bad.push(`${id}: choice node with no options`);
      } else if (!t.nodes[n.next]) {
        bad.push(`${id}: ${n.type} node points at missing "${n.next}"`);
      }
    }
    if (bad.length) throw new Error(`tree rejected: ${bad.slice(0, 4).join('; ')}`);

    fs.mkdirSync(DIR, { recursive: true });
    fs.writeFileSync(FILE, JSON.stringify({ ...t, source: 'derived from the SABM course', at: new Date().toISOString() }, null, 1));
    return { nodes: Object.keys(t.nodes).length, root: t.root };
  } finally {
    sabm.releaseLock();
  }
}

module.exports = { load, walk, allQuestions, refresh, FILE };
