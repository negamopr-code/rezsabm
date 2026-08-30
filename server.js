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
  '.pdf': 'application/pdf',
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
  const ext = path.extname(target).toLowerCase();
  const head = { 'Content-Type': MIME[ext] || 'application/octet-stream' };
  if (ext === '.html' || ext === '.js' || ext === '.json') head['Cache-Control'] = 'no-store';
  res.writeHead(200, head);
  fs.createReadStream(target).pipe(res);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);

  if (url.pathname === '/api/health') return send(res, 200, { ok: true, tool: 'REZSABM' });

  // ── Exit advisor: picture → rolling PDF → SABM notebook (the brain) → exit verdict ──
  if (url.pathname === '/api/advisor/status') {
    const sabm = require('./lib/sabm');
    const claude = require('./lib/claude');
    return send(res, 200, {
      notebook: sabm.NOTEBOOK, quota: sabm.quotaState(), busy: sabm.lockHeld(),
      claude: claude.credsStatus(), model: claude.model(),
      consults: require('./lib/advisor').history().length,
    });
  }

  if (url.pathname === '/api/advisor/history') {
    return send(res, 200, require('./lib/advisor').history().slice(-40).reverse());
  }

  if (url.pathname === '/api/advisor/consult' && req.method === 'POST') {
    const chunks = [];
    let size = 0;
    req.on('data', c => {
      size += c.length;
      if (size > 12e6) { req.destroy(); return; }              // the page downscales before sending
      chunks.push(c);
    });
    req.on('end', async () => {
      let body;
      try { body = JSON.parse(Buffer.concat(chunks).toString('utf8')); }
      catch { return send(res, 400, { error: 'bad JSON body' }); }
      if (!body.imageBase64) return send(res, 400, { error: 'no picture' });
      try {
        return send(res, 200, await require('./lib/advisor').consult(body));
      } catch (e) {
        const quota = e.constructor && e.constructor.name === 'QuotaError';
        console.error(`[advisor] ${new Date().toISOString()} ${quota ? 'QUOTA' : 'ERROR'}: ${e.message}`);
        return send(res, quota ? 429 : 502, { error: e.message, quota: quota || undefined });
      }
    });
    return;
  }

  if (url.pathname === '/api/advisor/chat' && req.method === 'POST') {
    const chunks = [];
    req.on('data', c => chunks.push(c));
    req.on('end', async () => {
      let body;
      try { body = JSON.parse(Buffer.concat(chunks).toString('utf8')); }
      catch { return send(res, 400, { error: 'bad JSON body' }); }
      if (!body.id || !body.message) return send(res, 400, { error: 'id and message required' });
      try {
        return send(res, 200, await require('./lib/advisor').chat(body.id, body.message));
      } catch (e) {
        const quota = e.constructor && e.constructor.name === 'QuotaError';
        console.error(`[advisor] ${new Date().toISOString()} ${quota ? 'QUOTA' : 'ERROR'}: ${e.message}`);
        return send(res, quota ? 429 : 502, { error: e.message, quota: quota || undefined });
      }
    });
    return;
  }

  if (url.pathname === '/api/advisor/add-image' && req.method === 'POST') {
    const chunks = [];
    let size = 0;
    req.on('data', c => { size += c.length; if (size > 12e6) { req.destroy(); return; } chunks.push(c); });
    req.on('end', async () => {
      let body;
      try { body = JSON.parse(Buffer.concat(chunks).toString('utf8')); }
      catch { return send(res, 400, { error: 'bad JSON body' }); }
      if (!body.id || !body.imageBase64) return send(res, 400, { error: 'id and picture required' });
      try {
        return send(res, 200, await require('./lib/advisor').addImage(body.id, body));
      } catch (e) {
        const quota = e.constructor && e.constructor.name === 'QuotaError';
        console.error(`[advisor] ${new Date().toISOString()} ${quota ? 'QUOTA' : 'ERROR'}: ${e.message}`);
        return send(res, quota ? 429 : 502, { error: e.message, quota: quota || undefined });
      }
    });
    return;
  }

  if (url.pathname === '/api/advisor/erase' && req.method === 'POST') {
    const id = url.searchParams.get('id');
    if (!id) return send(res, 400, { error: 'id required' });
    require('./lib/advisor').erase(id)
      .then(r => send(res, 200, r))
      .catch(e => send(res, 502, { error: e.message }));
    return;
  }

  // The PDF the notebook reads, always freshly rebuilt from consults.json first, so what you
  // download is exactly what the notebook sees — including an exchange whose background
  // republish has not finished yet.
  if (url.pathname === '/api/advisor/pdf') {
    const advisor = require('./lib/advisor');
    require('child_process').execFile('python3', ['scripts/chart_pdf.py', 'sync'], { cwd: ROOT }, () => {
      const pdf = path.join(advisor.DIR, 'charts.pdf');
      if (!fs.existsSync(pdf)) return send(res, 404, { error: 'no consults yet — nothing to download' });
      const name = `rezsabm-charts-${new Date().toISOString().slice(0, 16).replace(/[-:]/g, '').replace('T', '-')}.pdf`;
      res.writeHead(200, { 'Content-Type': 'application/pdf', 'Cache-Control': 'no-store',
                           'Content-Disposition': `attachment; filename="${name}"` });
      fs.createReadStream(pdf).pipe(res);
    });
    return;
  }

  if (url.pathname.startsWith('/advisor/')) {
    const advisor = require('./lib/advisor');
    const rel = path.normalize(url.pathname.replace('/advisor/', '')).replace(/^(\.\.[\\/])+/, '');
    const target = path.join(advisor.DIR, rel);
    if (!target.startsWith(advisor.DIR)) return send(res, 403, 'forbidden', 'text/plain');
    return serveFile(res, target);
  }

  if (url.pathname === '/api/run-open' && req.method === 'POST') {
    const sl = parseFloat(url.searchParams.get('sl') || '0.2');
    if (!(sl >= 0.05 && sl <= 5)) return send(res, 400, { error: 'sl must be 0.05..5 (%)' });
    const mode = url.searchParams.get('exit') || 'e2';   // e2 | R1 | R2 | R3 | disc | transform
    const trig = parseFloat(url.searchParams.get('trigger') || '2');
    const { execFile } = require('child_process');
    const lock = path.join(ROOT, 'data', 'run_open.lock');
    if (fs.existsSync(lock) && Date.now() - fs.statSync(lock).mtimeMs < 3600e3) {
      return send(res, 409, { error: 'a run is already in progress' });
    }
    const args = ['scripts/sabm_r1_spy.py', '--entry', 'open', '--open-sl-pct', String(sl), '--videos'];
    let variant;
    if (mode === 'e2') {
      args.push('--exit', 'e2');
      variant = `SPY_open${sl === 0.2 ? '' : '_sl' + sl}`;
    } else if (mode === 'disc') {
      args.push('--exit', 'disc');
      variant = `SPY_opendisc${sl === 0.25 ? '' : '_sl' + sl}`;
    } else if (mode === 'transform') {
      // trigger: 'afford' (dynamic affordability, engine default) or a fixed % (always _t-tagged)
      const trigRaw = url.searchParams.get('trigger') || 'afford';
      const dte = url.searchParams.get('dte') === '21' ? 21 : 5;
      const texit = url.searchParams.get('texit') === 'prevlow' ? 'prevlow' : 'trail';
      args.push('--exit', 'transform', '--opt-days', String(dte));
      let ttag = '';
      if (trigRaw !== 'afford') {
        const tp = parseFloat(trigRaw);
        if (!(tp >= 0.3 && tp <= 20)) return send(res, 400, { error: 'trigger must be "afford" or 0.3..20 (%)' });
        args.push('--transform-trigger', 'pct', '--transform-trigger-pct', String(tp));
        ttag = '_t' + tp;
      }
      if (texit === 'prevlow') args.push('--transform-exit', 'prevlow');
      variant = `SPY_0dtew${ttag}${sl === 0.25 ? '' : '_sl' + sl}${dte === 21 ? '_21d' : ''}${texit === 'prevlow' ? '_prevlow' : ''}`;
    } else {
      const rk = mode.replace('R', '');
      args.push('--exit', 'target', '--rk', rk);
      variant = `SPY_openR${rk}${sl === 0.25 ? '' : '_sl' + sl}`;
    }
    fs.writeFileSync(lock, `${sl} ${mode}`);
    const log = fs.openSync(path.join(ROOT, 'data', 'run_open.log'), 'w');
    const child = execFile('python3', args, { cwd: ROOT });
    child.stdout.pipe(fs.createWriteStream(null, { fd: log }));
    child.on('exit', () => { try { fs.unlinkSync(lock); } catch {} });
    return send(res, 200, { started: true, sl, mode, variant });
  }

  if (url.pathname === '/api/run-open-status' && req.method === 'GET') {
    const lock = path.join(ROOT, 'data', 'run_open.lock');
    let log = '';
    try { const t = fs.readFileSync(path.join(ROOT, 'data', 'run_open.log'), 'utf8'); log = t.slice(-200); } catch {}
    return send(res, 200, { running: fs.existsSync(lock), tail: log.trim().split('\n').pop() || '' });
  }

  if (url.pathname === '/api/ticker-search' && req.method === 'GET') {
    const q = (url.searchParams.get('q') || '').trim();
    if (!q) return send(res, 400, { error: 'q required' });
    const local = [];
    try {
      const u = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'universe.json')));
      const Q = q.toUpperCase();
      for (const x of u.symbols || []) {
        if (x.s.startsWith(Q) || x.n.toUpperCase().includes(Q)) {
          local.push({ symbol: x.s, name: x.n, exch: 'US', type: 'local' });
          if (local.length >= 8) break;
        }
      }
    } catch {}
    fetch(`https://query1.finance.yahoo.com/v1/finance/search?q=${encodeURIComponent(q)}&quotesCount=10&newsCount=0`,
      { headers: { 'User-Agent': 'Mozilla/5.0' } })
      .then(r => r.json())
      .then(j => send(res, 200, { results: local.concat((j.quotes || []).filter(x => x.symbol)
        .map(x => ({ symbol: x.symbol, name: x.shortname || x.longname || '', exch: x.exchDisp || '', type: x.typeDisp || '' }))) }))
      .catch(() => send(res, 200, { results: local }));
    return;
  }

  if (url.pathname === '/api/fetch-ohlc' && req.method === 'POST') {
    const sym = (url.searchParams.get('symbol') || '').trim();
    if (!sym) return send(res, 400, { error: 'symbol required' });
    fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(sym)}?period1=0&period2=9999999999&interval=1d`,
      { headers: { 'User-Agent': 'Mozilla/5.0' } })
      .then(r => r.json())
      .then(j => {
        const result = j.chart && j.chart.result && j.chart.result[0];
        if (!result || !result.timestamp) throw new Error((j.chart && j.chart.error && j.chart.error.description) || 'no data for ' + sym);
        const q = result.indicators.quote[0];
        const lines = ['Date,Open,High,Low,Close'];
        result.timestamp.forEach((t, i) => {
          const o = q.open[i], h = q.high[i], l = q.low[i], c = q.close[i];
          if (o == null || h == null || l == null || c == null) return;
          lines.push(`${new Date(t * 1000).toISOString().slice(0, 10)},${o.toFixed(4)},${h.toFixed(4)},${l.toFixed(4)},${c.toFixed(4)}`);
        });
        if (lines.length < 100) throw new Error('too few rows for ' + sym);
        const name = sym.toUpperCase().replace(/[^A-Z0-9^.\-]/g, '') + '_daily_OHLC_yahoo.csv';
        fs.writeFileSync(path.join(ROOT, 'uploads', name), lines.join('\n') + '\n');
        send(res, 200, { ok: true, symbol: sym.toUpperCase(), rows: lines.length - 1,
          from: lines[1].slice(0, 10), to: lines[lines.length - 1].slice(0, 10) });
      })
      .catch(e => send(res, 502, { error: e.message }));
    return;
  }

  if (url.pathname === '/api/run-suite' && req.method === 'POST') {
    const sym = (url.searchParams.get('symbol') || '').trim().toUpperCase();
    if (!sym) return send(res, 400, { error: 'symbol required' });
    if (!fs.existsSync(path.join(ROOT, 'uploads', `${sym}_daily_OHLC_yahoo.csv`))) {
      return send(res, 400, { error: `no history for ${sym} — fetch it first` });
    }
    const { exec } = require('child_process');
    const lock = path.join(ROOT, 'data', 'run_suite.lock');
    if (fs.existsSync(lock) && Date.now() - fs.statSync(lock).mtimeMs < 7200e3) {
      return send(res, 409, { error: 'a suite run is already in progress' });
    }
    fs.writeFileSync(lock, sym);
    const P = `python3 scripts/sabm_r1_spy.py --symbol ${sym}`;
    const cmd = `{ ${P} --videos && ${P} --rk 2 --videos && ${P} --rk 3 --videos && ` +
      `${P} --exit disc --videos && ${P} --entry open --videos && ${P} --options --videos; } ` +
      `> data/run_suite.log 2>&1; rm -f data/run_suite.lock`;
    exec(cmd, { cwd: ROOT });
    return send(res, 200, { started: true, symbol: sym,
      lines: [`${sym}_R1`, `${sym}_R2`, `${sym}_R3`, `${sym}_disc`, `${sym}_open`, `${sym}_R1_optbs`] });
  }

  if (url.pathname === '/api/run-suite-status' && req.method === 'GET') {
    const lock = path.join(ROOT, 'data', 'run_suite.lock');
    let tail = '';
    try { tail = fs.readFileSync(path.join(ROOT, 'data', 'run_suite.log'), 'utf8').trim().split('\n').pop() || ''; } catch {}
    return send(res, 200, { running: fs.existsSync(lock), symbol: fs.existsSync(lock) ? fs.readFileSync(lock, 'utf8') : '', tail });
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
