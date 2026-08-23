// REZSABM — Rezvyakov breakout entry × SABM R-target exits. Zero-dependency server.
// Static: public/ at /, results at /results/<variant>/... (data/results on disk).
// API: /api/variants — list result variants; /api/health.
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const PORT = process.env.PORT || 8112;
const RESULTS = path.join(ROOT, 'data', 'results');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
};

function send(res, code, body, type = 'application/json; charset=utf-8') {
  res.writeHead(code, { 'Content-Type': type });
  res.end(typeof body === 'string' ? body : JSON.stringify(body));
}

function serveFile(res, target) {
  if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
    return send(res, 404, 'not found', 'text/plain');
  }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(target).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(target).pipe(res);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);

  if (url.pathname === '/api/health') return send(res, 200, { ok: true, tool: 'REZSABM' });

  if (url.pathname === '/api/run-open' && req.method === 'POST') {
    const sl = parseFloat(url.searchParams.get('sl') || '0.2');
    if (!(sl >= 0.05 && sl <= 5)) return send(res, 400, { error: 'sl must be 0.05..5 (%)' });
    const { execFile } = require('child_process');
    const lock = path.join(ROOT, 'data', 'run_open.lock');
    if (fs.existsSync(lock) && Date.now() - fs.statSync(lock).mtimeMs < 3600e3) {
      return send(res, 409, { error: 'a run is already in progress' });
    }
    fs.writeFileSync(lock, String(sl));
    const log = fs.openSync(path.join(ROOT, 'data', 'run_open.log'), 'w');
    const child = execFile('python3', ['scripts/sabm_r1_spy.py', '--entry', 'open',
      '--open-sl-pct', String(sl), '--videos'], { cwd: ROOT });
    child.stdout.pipe(fs.createWriteStream(null, { fd: log }));
    child.on('exit', () => { try { fs.unlinkSync(lock); } catch {} });
    const variant = `SPY_open${sl === 0.2 ? '' : '_sl' + sl}`;
    return send(res, 200, { started: true, sl, variant });
  }

  if (url.pathname === '/api/run-open-status' && req.method === 'GET') {
    const lock = path.join(ROOT, 'data', 'run_open.lock');
    let log = '';
    try { const t = fs.readFileSync(path.join(ROOT, 'data', 'run_open.log'), 'utf8'); log = t.slice(-200); } catch {}
    return send(res, 200, { running: fs.existsSync(lock), tail: log.trim().split('\n').pop() || '' });
  }

  if (url.pathname === '/api/variants') {
    let dirs = [];
    try {
      dirs = fs.readdirSync(RESULTS).filter(d => fs.existsSync(path.join(RESULTS, d, 'stats.json')));
    } catch {}
    return send(res, 200, dirs.sort());
  }

  const clean = path.normalize(url.pathname).replace(/^(\.\.[\\/])+/, '');
  if (clean.startsWith('/results/') || clean.startsWith('results/')) {
    const rel = clean.replace(/^\/?results\//, '');
    const target = path.join(RESULTS, rel);
    if (!target.startsWith(RESULTS)) return send(res, 403, 'forbidden', 'text/plain');
    return serveFile(res, target);
  }

  const file = clean === '/' || clean === '.' ? '/index.html' : clean;
  const target = path.join(ROOT, 'public', file);
  if (!target.startsWith(path.join(ROOT, 'public'))) return send(res, 403, 'forbidden', 'text/plain');
  return serveFile(res, target);
});

server.listen(PORT, () => console.log(`REZSABM listening on :${PORT}`));
