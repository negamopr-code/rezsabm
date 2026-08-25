#!/usr/bin/env python3
"""SMB Capital options-video transcript harvester (REZSABM / SMB-OPTIONS corpus).

Runs inside awf-monitor-runner (yt-dlp + nlm CLI + work4 profile present).
Transcripts come THROUGH NotebookLM (yt2nlm method): add video as source ->
poll raw content (zero AI quota) -> save text -> delete source. Ledger-driven,
idempotent, sequential with polite gaps.

Usage:
  python3 harvest.py list           # channel inventory -> videos.json (+ledger seed)
  python3 harvest.py harvest N      # process next N pending (most-viewed first)
  python3 harvest.py status
"""
import json
import os
import re
import subprocess
import sys
import time

WORK = os.path.dirname(os.path.abspath(__file__))
NB = 'e2e327c6-18bd-4a2a-bc8c-90ae2337f91c'   # "SMB Options" notebook, work4
PROFILE = 'work4'
CHANNEL = 'https://www.youtube.com/@smbcapital/videos'
VIDEOS = os.path.join(WORK, 'videos.json')
LEDGER = os.path.join(WORK, 'ledger.json')
TDIR = os.path.join(WORK, 'transcripts')
GAP = 1.6
_last = [0.0]

KEYS = ['option', 'spread', 'condor', 'straddle', 'strangle', 'butterfly', 'premium',
        'theta', 'delta', 'gamma', 'vega', '0dte', '0 dte', 'covered call', 'credit',
        'debit', 'leaps', 'wheel', 'iron ', 'volatility', 'vix', 'hedg']
WORD_KEYS = re.compile(r'\b(calls?|puts?)\b', re.I)


def nlm(*args, timeout=700):
    wait = GAP - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    r = subprocess.run(['nlm', *args, '-p', PROFILE], capture_output=True, text=True, timeout=timeout)
    _last[0] = time.time()
    return r


def source_ids():
    r = nlm('source', 'list', NB)
    try:
        return {s['id']: s.get('title', '') for s in json.loads(r.stdout)}
    except Exception:
        return {}


def source_content(sid):
    for cmd in (('source', 'content', sid), ('source', 'get', sid)):
        r = nlm(*cmd)
        if r.returncode == 0 and r.stdout.strip():
            try:
                j = json.loads(r.stdout)
                return (j.get('value') or {}).get('content') or j.get('content') or ''
            except Exception:
                if len(r.stdout) > 200:
                    return r.stdout
    return ''


def load(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)


def is_options(title):
    t = title.lower()
    return any(k in t for k in KEYS) or bool(WORD_KEYS.search(title))


def cmd_list():
    import yt_dlp
    opts = {'quiet': True, 'extract_flat': 'in_playlist', 'skip_download': True}
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(CHANNEL, download=False)
    entries = info.get('entries') or []
    vids = []
    for e in entries:
        if not e or not e.get('id'):
            continue
        vids.append({'id': e['id'], 'title': e.get('title') or '',
                     'views': e.get('view_count') or 0,
                     'duration': e.get('duration') or 0,
                     'url': f"https://www.youtube.com/watch?v={e['id']}"})
    opt = [v for v in vids if is_options(v['title'])]
    opt.sort(key=lambda v: -v['views'])
    save(VIDEOS, {'channel': CHANNEL, 'listed_at': time.strftime('%Y-%m-%d'),
                  'total_channel_videos': len(vids), 'options_videos': len(opt), 'videos': opt})
    led = load(LEDGER, {})
    for v in opt:
        led.setdefault(v['id'], {'status': 'pending', 'title': v['title'], 'views': v['views']})
    save(LEDGER, led)
    print(f"channel videos: {len(vids)}; options-related: {len(opt)}; "
          f"pending: {sum(1 for x in led.values() if x['status'] == 'pending')}")


REFUSED_STREAK = [0]


def harvest_one(v, led):
    vid = v['id']
    before = set(source_ids())
    r = None
    for attempt, backoff in enumerate((0, 60, 300, 900)):
        if backoff:
            print(f'  add refused, retry in {backoff}s', flush=True)
            time.sleep(backoff)
        r = nlm('source', 'add', NB, '--youtube', v['url'], '--wait', '--wait-timeout', '600')
        if 'could not add' not in (r.stdout + r.stderr).lower():
            REFUSED_STREAK[0] = 0
            break
        # 2026-08-25 incident: "could not add" masked an EXPIRED work4 session for 34 h.
        # Probe auth once; if expired, backoff is pointless -> exit loudly for the supervisor.
        pr = nlm('notebook', 'list', timeout=120)
        if 'authentication expired' in (pr.stdout + pr.stderr).lower() or 'authentication error' in (pr.stdout + pr.stderr).lower():
            save(LEDGER, led)
            print('AUTH EXPIRED for profile ' + PROFILE + ' - sync keeper cookies -> bind store and restart (see smb/nlm-mirror/pipeline-journal.md)', flush=True)
            sys.exit(3)
    else:
        # add-refusal is a RATE LIMIT symptom, NOT missing captions -> retryable 'failed'
        led[vid] = {**led[vid], 'status': 'failed', 'why': 'add refused after retries'}
        REFUSED_STREAK[0] += 1
        if REFUSED_STREAK[0] >= 3:
            print('  3 consecutive refusals despite backoff - cooling down 30 min', flush=True)
            time.sleep(1800)
            REFUSED_STREAK[0] = 0
        return False
    sid = None
    for _ in range(6):
        now = source_ids()
        new = {k: t for k, t in now.items() if k not in before}
        if new:
            # 2026-08-25 incident: a concurrently uploaded volume/journal source was grabbed
            # as "the video" and then deleted. Prefer the source whose title matches the video;
            # never touch sources that look like our own documents.
            def ours(t):
                t = (t or '').lower()
                return t.startswith('smb options') or t.startswith('smb transcripts') or t.startswith('smb-mirror')
            want = re.sub(r'\W+', ' ', v['title'].lower()).strip()
            cand = [k for k, t in new.items() if want and re.sub(r'\W+', ' ', (t or '').lower()).strip()[:40] == want[:40]]
            if not cand:
                cand = [k for k, t in new.items() if not ours(t)]
            if len(cand) == 1:
                sid = cand[0]
                break
            if len(cand) > 1:
                print(f'  ambiguous new sources {cand} - waiting', flush=True)
        time.sleep(10)
    if sid is None:
        led[vid] = {**led[vid], 'status': 'failed', 'why': 'no new source appeared'}
        return False
    text = ''
    for _ in range(15):
        text = source_content(sid)
        if text and len(text) > 300:
            break
        time.sleep(20)
    if text and text.lstrip()[:80].upper().startswith('# SMB OPTIONS'):
        print('  captured a foreign source (distilled volume) - NOT deleting it, marking pending', flush=True)
        led[vid] = {**led[vid], 'status': 'pending'}
        return False
    if text and len(text) > 300:
        os.makedirs(TDIR, exist_ok=True)
        with open(os.path.join(TDIR, vid + '.txt'), 'w') as f:
            f.write(f"## {v['title']} | {v['views']} views | {v['url']}\n\n{text}\n")
        led[vid] = {**led[vid], 'status': 'transcribed', 'chars': len(text)}
        ok = True
    else:
        led[vid] = {**led[vid], 'status': 'unavailable', 'why': 'empty content'}
        ok = False
    nlm('source', 'delete', sid, '--confirm')
    if sid in source_ids():
        nlm('source', 'delete', sid, '--confirm')
    return ok


def cmd_harvest(n):
    # single-process lock (2026-08-23 incident: two racing harvesters clobbered the ledger)
    lock = os.path.join(WORK, 'harvest.lock')
    if os.path.exists(lock):
        pid = open(lock).read().strip()
        if os.path.isdir(f'/proc/{pid}'):
            sys.exit(f'another harvester is running (pid {pid}) - refusing to start')
    open(lock, 'w').write(str(os.getpid()))
    data = load(VIDEOS, None)
    led = load(LEDGER, {})
    if not data:
        sys.exit('run list first')
    done = 0
    for v in data['videos']:
        if done >= n:
            break
        st = led.get(v['id'], {}).get('status')
        if st not in (None, 'pending', 'failed'):
            continue
        print(f"[{done + 1}/{n}] {v['id']} {v['title'][:70]} ({v['views']} views)", flush=True)
        try:
            harvest_one(v, led)
        except Exception as e:  # noqa: BLE001
            led[v['id']] = {**led.get(v['id'], {}), 'status': 'failed', 'why': str(e)[:200]}
        save(LEDGER, led)
        done += 1
        time.sleep(5)
    c = {}
    for x in led.values():
        c[x['status']] = c.get(x['status'], 0) + 1
    print('ledger:', c)


def cmd_status():
    led = load(LEDGER, {})
    c = {}
    for x in led.values():
        c[x['status']] = c.get(x['status'], 0) + 1
    total_chars = sum(x.get('chars', 0) for x in led.values())
    print(json.dumps({'counts': c, 'transcribed_chars': total_chars}, indent=1))


if __name__ == '__main__':
    a = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if a == 'list':
        cmd_list()
    elif a == 'harvest':
        cmd_harvest(int(sys.argv[2]) if len(sys.argv) > 2 else 10)
    else:
        cmd_status()
