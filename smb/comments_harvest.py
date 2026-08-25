#!/usr/bin/env python3
"""SMB Capital options-video COMMENTS harvester (second SMB pipeline, user 2026-08-25).

Runs inside awf-monitor-runner (yt-dlp present, no API key needed — same mechanism as
yt2nlm/youtube.py fetch_video). Ledger-driven over videos.json (364 options videos,
most-viewed first); fetches ALL top-level comments + ALL replies (likes, dates) and
stores comments/<videoId>.jsonl. Own state only: comments/, comments_ledger.json,
comments.log, comments_harvest.lock. NEVER touches ledger.json / harvest.lock /
transcripts/ of the transcript pipeline. Touches NotebookLM never (see comments_sync.py).

Usage:
  python3 comments_harvest.py harvest [N]   # next N pending (default all)
  python3 comments_harvest.py status
  python3 comments_harvest.py retry         # failed -> pending (attempts kept)
"""
import json
import os
import random
import sys
import time

WORK = os.path.dirname(os.path.abspath(__file__))
VIDEOS = os.path.join(WORK, 'videos.json')
LEDGER = os.path.join(WORK, 'comments_ledger.json')
CDIR = os.path.join(WORK, 'comments')
LOCK = os.path.join(WORK, 'comments_harvest.lock')
GAP = (3.0, 7.0)          # polite random pause between videos (seconds)
MAX_ATTEMPTS = 3


def log(msg):
    print(time.strftime('%Y-%m-%d %H:%M:%S'), msg, flush=True)


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


def videos():
    return json.load(open(VIDEOS))['videos']


def ledger():
    led = load(LEDGER, {})
    for v in videos():
        led.setdefault(v['id'], {'status': 'pending', 'title': v['title'], 'views': v['views'], 'attempts': 0})
    return led


def fetch(video_id):
    """All comments (top-level + replies) via yt-dlp, no cap. Returns (info, comments)."""
    from yt_dlp import YoutubeDL
    opts = {
        'quiet': True, 'no_warnings': True, 'skip_download': True, 'getcomments': True,
        'extractor_args': {'youtube': {'comment_sort': ['top'],
                                       'max_comments': ['all', 'all', 'all', 'all']}},
    }
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
    out = []
    for c in info.get('comments') or []:
        out.append({
            'id': c.get('id', ''), 'parent': c.get('parent', 'root'),
            'author': c.get('author') or 'anonymous', 'text': (c.get('text') or '').strip(),
            'likes': c.get('like_count') or 0, 'ts': c.get('timestamp'),
            'uploader': bool(c.get('author_is_uploader')), 'pinned': bool(c.get('is_pinned')),
        })
    meta = {'id': video_id, 'title': info.get('title'), 'url': info.get('webpage_url'),
            'views': info.get('view_count'), 'upload_date': info.get('upload_date'),
            'comment_count': info.get('comment_count'), 'fetched': len(out),
            'fetched_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    return meta, out


def harvest_one(vid, led):
    row = led[vid]
    row['attempts'] = row.get('attempts', 0) + 1
    try:
        meta, comments = fetch(vid)
    except Exception as e:  # network / extractor / rate-limit
        why = str(e).splitlines()[0][:200]
        row['status'] = 'failed' if row['attempts'] >= MAX_ATTEMPTS else 'pending'
        row['why'] = why
        log(f'  FAIL {vid} attempt {row["attempts"]}: {why}')
        if 'Sign in' in why or '429' in why or 'Too Many' in why:
            return 'ratelimit'
        return 'fail'
    os.makedirs(CDIR, exist_ok=True)
    path = os.path.join(CDIR, vid + '.jsonl')
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        f.write(json.dumps({'_meta': meta}, ensure_ascii=False) + '\n')
        for c in comments:
            f.write(json.dumps(c, ensure_ascii=False) + '\n')
    os.replace(tmp, path)
    roots = sum(1 for c in comments if c['parent'] == 'root')
    row.update({'status': 'done', 'comments': len(comments), 'roots': roots,
                'replies': len(comments) - roots, 'yt_count': meta['comment_count'],
                'fetched_at': meta['fetched_at']})
    row.pop('why', None)
    log(f'  ok {vid}: {len(comments)} comments ({roots} top-level) / yt says {meta["comment_count"]}')
    return 'ok'


def cmd_harvest(n):
    if os.path.exists(LOCK):
        pid = open(LOCK).read().strip()
        if pid and os.path.isdir(f'/proc/{pid}'):
            log(f'another comments harvester alive (pid {pid}) - exit')
            sys.exit(2)
        os.unlink(LOCK)
    open(LOCK, 'w').write(str(os.getpid()))
    try:
        led = ledger()
        order = [v['id'] for v in videos()]
        todo = [i for i in order if led[i]['status'] == 'pending'][:n]
        log(f'harvest: {len(todo)} pending to process')
        strikes = 0
        for k, vid in enumerate(todo, 1):
            log(f'[{k}/{len(todo)}] {vid} {led[vid]["title"][:70]} ({led[vid]["views"]} views)')
            res = harvest_one(vid, led)
            save(LEDGER, led)
            if res == 'ratelimit':
                strikes += 1
                cool = min(1800, 300 * strikes)
                log(f'  rate-limited/blocked -> cooling {cool}s')
                time.sleep(cool)
            else:
                strikes = 0 if res == 'ok' else strikes
                time.sleep(random.uniform(*GAP))
        save(LEDGER, led)
        log('harvest done: ' + json.dumps(counts(led)))
    finally:
        if os.path.exists(LOCK):
            os.unlink(LOCK)


def counts(led):
    c = {}
    for r in led.values():
        c[r['status']] = c.get(r['status'], 0) + 1
    c['comments'] = sum(r.get('comments', 0) for r in led.values())
    c['videos_done'] = c.get('done', 0)
    return c


def cmd_status():
    led = ledger()
    print(json.dumps({'counts': counts(led), 'total': len(led)}))


def cmd_retry():
    led = ledger()
    n = 0
    for r in led.values():
        if r['status'] == 'failed':
            r['status'] = 'pending'
            n += 1
    save(LEDGER, led)
    print(f'{n} failed -> pending')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'harvest':
        cmd_harvest(int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 6)
    elif cmd == 'retry':
        cmd_retry()
    else:
        cmd_status()
