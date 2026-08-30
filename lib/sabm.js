// The SABM brain: NotebookLM notebook "SABM — Sortir au Bon Moment" (work4 account).
//
// This app has no nlm CLI and no work4 cookies of its own — both live in the
// awf-monitor-runner container. So every NLM call is run *there*, over the Docker socket
// (the docker CLI isn't installed either; /containers/.../exec is spoken directly).
// The chart PDF crosses the container boundary through a shared host directory:
// /nlmwork here == /app in awf-monitor-runner.
//
// Serialisation: work4 runs ONE job at a time. The SMB pipeline daemon idles while
// state/smb-options/nlm_external.lock exists, so every consult takes that lock first —
// the user's question never queues behind a 10-video extraction batch.
const fs = require('fs');
const http = require('http');
const path = require('path');

const SOCK = '/var/run/docker.sock';
const CT = process.env.REZ_NLM_CONTAINER || 'awf-monitor-runner';
const NOTEBOOK = process.env.REZ_SABM_NOTEBOOK || 'b57ecd77-292a-434b-90c4-6956723634d3';
const PROFILE = process.env.REZ_NLM_PROFILE || 'work4';
const SOURCE_TITLE = 'REZSABM chart uploads';

const NLMWORK = '/nlmwork';                                   // = /app inside awf-monitor-runner
const STATE_HOST = path.join(NLMWORK, 'state', 'smb-options');
const STATE_CT = '/app/state/smb-options';
const LOCK = path.join(STATE_HOST, 'nlm_external.lock');
const QUOTA = path.join(STATE_HOST, 'quota_exhausted');
const PDF_HOST = path.join(STATE_HOST, 'advisor', 'charts.pdf');
const PDF_CT = `${STATE_CT}/advisor/charts.pdf`;
const QUOTA_BACKOFF_S = 25200;                                // 7 h — same window the daemon uses

class NlmError extends Error {}
class QuotaError extends NlmError {}

function dockerApi(method, urlPath, body) {
  return new Promise((resolve, reject) => {
    const payload = body === undefined ? null : Buffer.from(JSON.stringify(body));
    const req = http.request(
      { socketPath: SOCK, method, path: urlPath, headers: payload
          ? { 'content-type': 'application/json', 'content-length': payload.length } : {} },
      res => {
        const chunks = [];
        res.on('data', c => chunks.push(c));
        res.on('end', () => resolve({ status: res.statusCode, buf: Buffer.concat(chunks) }));
      });
    req.on('error', e => reject(new NlmError(`docker socket: ${e.message}`)));
    if (payload) req.write(payload);
    req.end();
  });
}

/** Docker's non-TTY attach stream is 8-byte-framed: [stream, 0,0,0, len32be]. */
function demux(buf) {
  let out = '', err = '', i = 0;
  while (i + 8 <= buf.length) {
    const stream = buf[i];
    const len = buf.readUInt32BE(i + 4);
    const chunk = buf.slice(i + 8, i + 8 + len).toString('utf8');
    if (stream === 2) err += chunk; else out += chunk;
    i += 8 + len;
  }
  if (!out && !err) out = buf.toString('utf8');               // unframed (older API / TTY)
  return { out, err };
}

async function exec(cmd, { timeoutMs = 420000 } = {}) {
  const created = await dockerApi('POST', `/containers/${CT}/exec`, {
    AttachStdout: true, AttachStderr: true, Tty: false,
    Env: [`NLM_PROFILE=${PROFILE}`], Cmd: cmd,
  });
  if (created.status !== 201) {
    throw new NlmError(`docker exec create failed (${created.status}): ${created.buf.toString().slice(0, 200)}`);
  }
  const id = JSON.parse(created.buf).Id;
  const run = await Promise.race([
    dockerApi('POST', `/exec/${id}/start`, { Detach: false, Tty: false }),
    new Promise((_, rej) => setTimeout(() => rej(new NlmError('NLM call timed out')), timeoutMs)),
  ]);
  const { out, err } = demux(run.buf);
  const info = await dockerApi('GET', `/exec/${id}/json`);
  const code = info.status === 200 ? JSON.parse(info.buf).ExitCode : null;
  return { out, err, code };
}

// ── work4 serialisation + quota bookkeeping ────────────────────────────────────────────
const lockHeld = () => {
  try { return Date.now() - fs.statSync(LOCK).mtimeMs < 120 * 60e3; } catch { return false; }
};
const takeLock = () => { fs.mkdirSync(STATE_HOST, { recursive: true }); fs.writeFileSync(LOCK, 'rezsabm exit advisor\n'); };
const releaseLock = () => { try { fs.unlinkSync(LOCK); } catch {} };

function quotaState() {
  let stamp = 0;
  try { stamp = parseInt(fs.readFileSync(QUOTA, 'utf8').trim(), 10) || 0; } catch {}
  const age = Math.floor(Date.now() / 1000) - stamp;
  const blocked = stamp > 0 && age < QUOTA_BACKOFF_S;
  return { blocked, retry_at: blocked ? new Date((stamp + QUOTA_BACKOFF_S) * 1000).toISOString() : null };
}

/** Record exhaustion the way analyze_local.py does, so the daemon backs off too. */
function markExhausted() {
  try { fs.writeFileSync(QUOTA, String(Math.floor(Date.now() / 1000))); } catch {}
}

// ── the two NLM operations ─────────────────────────────────────────────────────────────

/** Replace-by-title: the notebook always holds exactly ONE chart-upload source. */
async function publishCharts(localPdf) {
  fs.mkdirSync(path.dirname(PDF_HOST), { recursive: true });
  fs.copyFileSync(localPdf, PDF_HOST);

  const listed = await exec(['nlm', 'source', 'list', NOTEBOOK, '-p', PROFILE], { timeoutMs: 120000 });
  let old = null;
  try {
    old = (JSON.parse(listed.out).find(s => s.title === SOURCE_TITLE) || {}).id || null;
  } catch { /* an unparseable list just means "no old source known" */ }

  const added = await exec(['nlm', 'source', 'add', NOTEBOOK, '--file', PDF_CT,
    '--title', SOURCE_TITLE, '--wait', '--wait-timeout', '300', '-p', PROFILE], { timeoutMs: 360000 });
  const m = (added.out + added.err).match(/Source ID:\s*([0-9a-f-]{36})/i);
  if (!m) {
    if (/RESOURCE_EXHAUSTED|quota/i.test(added.out + added.err)) { markExhausted(); throw new QuotaError('work4 NLM quota exhausted'); }
    throw new NlmError(`upload failed: ${(added.err || added.out).slice(-300)}`);
  }
  const id = m[1];
  if (old && old !== id) await exec(['nlm', 'source', 'delete', old, '--confirm', '-p', PROFILE], { timeoutMs: 120000 });
  return id;
}

/** One scoped question against the chart source + the SABM course. */
async function ask(question, sourceIds, { timeoutS = 300 } = {}) {
  const args = ['nlm', 'notebook', 'query', '--json', '-t', String(timeoutS)];
  if (sourceIds && sourceIds.length) args.push('-s', sourceIds.join(','));
  args.push(NOTEBOOK, question, '-p', PROFILE);
  const r = await exec(args, { timeoutMs: (timeoutS + 60) * 1000 });

  let answer = '', err = '';
  try {
    const j = JSON.parse(r.out);
    const v = j.value || j;
    answer = v.answer || '';
    err = v.error || '';
  } catch {
    err = (r.err || r.out).slice(-400);
  }
  if (!answer) {
    if (/RESOURCE_EXHAUSTED|quota/i.test(err + r.err + r.out)) {
      markExhausted();
      throw new QuotaError('work4 NLM quota exhausted — the daily cap is spent');
    }
    throw new NlmError(err || 'NotebookLM returned an empty answer');
  }
  return answer;
}

module.exports = { publishCharts, ask, quotaState, takeLock, releaseLock, lockHeld,
                   NOTEBOOK, SOURCE_TITLE, NlmError, QuotaError };
