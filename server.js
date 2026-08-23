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
