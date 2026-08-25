#!/usr/bin/env python3
"""SMB comments -> NotebookLM ("SMB Options" notebook, work4). Runs INSIDE awf-monitor-runner.

Layers it maintains (all replace-by-title, never touching other sources):
  "SMB comments archive vol. N"  rolling raw archive (~400k chars/vol) of ALL comments
  "SMB comments batch <tag>"     TEMPORARY source = the comments of a few videos, queried
                                 source-scoped by the smb-audience skill, then deleted
  "SMB audience needs vol. 1"    the living analysis doc (smb/audience-needs.md)

R5: NEVER `source add` while the TRANSCRIPT harvester is alive (harvest.lock pid in /proc):
every add re-checks the lock right before the call and exits 75 if busy (caller retries later).

Usage (cd /app/state/smb-options):
  python3 comments_sync.py archive                 # rebuild+upload changed archive volumes
  python3 comments_sync.py batch-add <tag> <vid>...  # -> prints source id (JSON)
  python3 comments_sync.py query <sid> <question-file> [timeout]   # -> prints answer JSON
  python3 comments_sync.py delete <sid>            # verified delete (re-list)
  python3 comments_sync.py needs <file.md>         # upload "SMB audience needs vol. 1"
  python3 comments_sync.py render <vid>            # print one video's rendered block
  python3 comments_sync.py sources                 # list our sources
"""
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

WORK = os.path.dirname(os.path.abspath(__file__))
NB = 'e2e327c6-18bd-4a2a-bc8c-90ae2337f91c'
PROFILE = 'work4'
CDIR = os.path.join(WORK, 'comments')
STATE = os.path.join(WORK, 'comments_archive_state.json')
HLOCK = os.path.join(WORK, 'harvest.lock')          # transcript harvester (read-only for us)
ROLL = 400_000
ARCHIVE_T = 'SMB comments archive vol. {n}'
BATCH_T = 'SMB comments batch {tag}'
NEEDS_T = 'SMB audience needs vol. 1'
GAP = 1.6
_last = [0.0]


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, file=sys.stderr, flush=True)


def nlm(*args, timeout=900):
    wait = GAP - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    r = subprocess.run(['nlm', *args, '-p', PROFILE], capture_output=True, text=True, timeout=timeout)
    _last[0] = time.time()
    return r


def transcript_harvester_alive():
    try:
        pid = open(HLOCK).read().strip()
    except OSError:
        return False
    return bool(pid) and os.path.isdir(f'/proc/{pid}')


def sources():
    r = nlm('source', 'list', NB)
    try:
        d = json.loads(r.stdout)
        if isinstance(d, dict):
            d = d.get('sources') or d.get('value') or []
        return [s for s in d if isinstance(s, dict)]
    except Exception:
        return []


def ours(title_prefix='SMB comments'):
    return [s for s in sources() if (s.get('title') or '').startswith(title_prefix)]


def add_source(path, title):
    """R5-guarded add via --file; returns the new source id (title-matched after re-list) or None."""
    if transcript_harvester_alive():
        log('R5: transcript harvester alive -> no add; exit 75')
        sys.exit(75)
    before = {s['id'] for s in sources()}
    if transcript_harvester_alive():
        log('R5: transcript harvester alive (re-check) -> exit 75')
        sys.exit(75)
    r = nlm('source', 'add', NB, '--file', path, '--title', title, '--wait', '--wait-timeout', '900')
    out = (r.stdout + r.stderr)
    for _ in range(6):
        cand = [s for s in sources() if s['id'] not in before and (s.get('title') or '') == title]
        if cand:
            return cand[0]['id']
        time.sleep(5)
    log('add: no new source titled', title, '| nlm said:', out[:300])
    return None


def delete_verified(sid):
    nlm('source', 'delete', sid, '--confirm')
    for _ in range(3):
        if sid not in {s['id'] for s in sources()}:
            return True
        time.sleep(3)
    return False


# ---------- rendering ----------
def load_video(vid):
    rows = [json.loads(l) for l in open(os.path.join(CDIR, vid + '.jsonl')) if l.strip()]
    meta = rows[0]['_meta']
    return meta, rows[1:]


def fmt_ts(ts):
    if not ts:
        return '?'
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%Y-%m-%d')


def number(comments):
    """Stable per-video numbering: roots #1..#R in file order, replies #n.k. Returns list of
    (num, comment, is_reply)."""
    out, children = [], {}
    roots = [c for c in comments if c['parent'] == 'root' or not c['parent']]
    for c in comments:
        if c['parent'] != 'root' and c['parent']:
            children.setdefault(c['parent'], []).append(c)
    seen = set()
    for i, r in enumerate(roots, 1):
        out.append((f'{i}', r, False))
        for k, ch in enumerate(children.get(r['id'], []), 1):
            out.append((f'{i}.{k}', ch, True))
            seen.add(ch['id'])
    # replies whose parent is gone (deleted comment): keep them, numbered after the roots
    i = len(roots)
    for c in comments:
        if c['parent'] != 'root' and c['parent'] and c['id'] not in seen:
            i += 1
            out.append((f'{i}', c, False))
    return out


def render_video(vid, with_names=True):
    meta, comments = load_video(vid)
    head = (f"## VIDEO {vid} — {meta.get('title')}\n"
            f"url: {meta.get('url')} | views: {meta.get('views')} | uploaded: {meta.get('upload_date')} "
            f"| comments: {len(comments)} ({sum(1 for c in comments if c['parent']=='root')} top-level)\n")
    lines = [head]
    for num, c, is_reply in number(comments):
        who = (c['author'] + (' [SMB]' if c.get('uploader') else '')) if with_names else ('[SMB]' if c.get('uploader') else '')
        text = c['text'].replace('\n', ' ').strip()
        tag = f"[#{num} 👍{c['likes']} {fmt_ts(c.get('ts'))}]"
        if is_reply:
            lines.append(f"    ↳ {tag} {who}: {text}")
        else:
            lines.append(f"{tag} {who}: {text}")
    return '\n'.join(lines) + '\n'


# ---------- commands ----------
def cmd_archive():
    order = [v['id'] for v in json.load(open(os.path.join(WORK, 'videos.json')))['videos']]
    have = {f[:-6] for f in os.listdir(CDIR) if f.endswith('.jsonl')} if os.path.isdir(CDIR) else set()
    ids = [i for i in order if i in have]
    vols, cur, size = [], [], 0
    for vid in ids:
        text = render_video(vid)
        if size + len(text) > ROLL and cur:
            vols.append(cur)
            cur, size = [], 0
        cur.append((vid, text))
        size += len(text)
    if cur:
        vols.append(cur)
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    existing = {s.get('title'): s['id'] for s in sources()}
    for n, vol in enumerate(vols, 1):
        title = ARCHIVE_T.format(n=n)
        vids_in = [v for v, _ in vol]
        if state.get(title) == vids_in and title in existing:
            print(f'{title}: unchanged ({len(vids_in)} videos)')
            continue
        ncom = sum(t.count('[#') for _, t in vol)
        body = (f'{title} — RAW archive of ALL YouTube comments (with replies, like counts, dates) under '
                f'SMB Capital options videos: {len(vids_in)} videos, {ncom} comments, most-viewed order. '
                f'Companion of "SMB transcripts archive" / "SMB Options" / "SMB audience needs".\n\n'
                + '\n'.join(t for _, t in vol))
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f:
            f.write(body)
            tmp = f.name
        sid = add_source(tmp, title)        # add new first
        os.unlink(tmp)
        if sid:
            state[title] = vids_in
            json.dump(state, open(STATE, 'w'))
            if title in existing and existing[title] != sid:
                delete_verified(existing[title])   # then drop the superseded copy
            print(f'{title}: synced {sid} ({len(vids_in)} videos, {ncom} comments, {len(body)} chars)')
        else:
            print(f'{title}: FAILED')
    print('done:', len(vols), 'volume(s)')


def cmd_batch_add(tag, vids):
    body = f'SMB comments batch {tag} — temporary analysis source ({len(vids)} videos).\n\n' + \
           '\n'.join(render_video(v) for v in vids)
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f:
        f.write(body)
        tmp = f.name
    sid = add_source(tmp, BATCH_T.format(tag=tag))
    os.unlink(tmp)
    print(json.dumps({'sid': sid, 'chars': len(body), 'comments': body.count('[#')}))


def cmd_query(sid, qfile, timeout=240):
    q = open(qfile).read()
    r = nlm('notebook', 'query', '--json', '-t', str(timeout), '-s', sid, NB, q, timeout=timeout + 60)
    try:
        d = json.loads(r.stdout)
        v = d.get('value', {})
        print(json.dumps({'answer': v.get('answer') or '', 'sources_used': v.get('sources_used'),
                          'rc': r.returncode}))
    except Exception:
        print(json.dumps({'answer': '', 'rc': r.returncode, 'err': (r.stdout + r.stderr)[-600:]}))


def cmd_needs(path):
    existing = {s.get('title'): s['id'] for s in sources()}
    sid = add_source(path, NEEDS_T)
    if sid and NEEDS_T in existing and existing[NEEDS_T] != sid:
        delete_verified(existing[NEEDS_T])
    print(json.dumps({'sid': sid}))


if __name__ == '__main__':
    a = sys.argv[1:]
    cmd = a[0] if a else 'sources'
    if cmd == 'archive':
        cmd_archive()
    elif cmd == 'batch-add':
        cmd_batch_add(a[1], a[2:])
    elif cmd == 'query':
        cmd_query(a[1], a[2], int(a[3]) if len(a) > 3 else 240)
    elif cmd == 'delete':
        print(json.dumps({'deleted': delete_verified(a[1])}))
    elif cmd == 'needs':
        cmd_needs(a[1])
    elif cmd == 'render':
        print(render_video(a[1]))
    else:
        print(json.dumps([{'id': s['id'], 'title': s.get('title')} for s in sources()], indent=1))
