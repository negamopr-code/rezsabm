#!/usr/bin/env python3
"""Sync FULL raw transcripts into the SMB Options notebook as archive volumes.

"SMB transcripts archive vol. N" — verbatim transcripts, most-viewed order,
rolled at ~2.4M chars (~400k words, under NLM's ~500k-word/source ceiling),
replace-by-title per changed volume (NLM sources are immutable).
Runs inside awf-monitor-runner (nlm CLI + work4 profile). Idempotent.
"""
import json
import os
import subprocess
import tempfile
import time

WORK = os.path.dirname(os.path.abspath(__file__))
NB = 'e2e327c6-18bd-4a2a-bc8c-90ae2337f91c'
PROFILE = 'work4'
TDIR = os.path.join(WORK, 'transcripts')
ROLL = 2_400_000  # chars per volume
GAP = 1.6
_last = [0.0]


def nlm(*args, timeout=900):
    wait = GAP - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    r = subprocess.run(['nlm', *args, '-p', PROFILE], capture_output=True, text=True, timeout=timeout)
    _last[0] = time.time()
    return r


def sources():
    r = nlm('source', 'list', NB)
    try:
        return json.loads(r.stdout)
    except Exception:
        return []


def main():
    videos = json.load(open(os.path.join(WORK, 'videos.json')))['videos']
    order = [v['id'] for v in videos]
    have = {f[:-4] for f in os.listdir(TDIR) if f.endswith('.txt')}
    ids = [i for i in order if i in have]
    vols, cur, size = [], [], 0
    for vid in ids:
        text = open(os.path.join(TDIR, vid + '.txt')).read()
        if size + len(text) > ROLL and cur:
            vols.append(cur)
            cur, size = [], 0
        cur.append((vid, text))
        size += len(text)
    if cur:
        vols.append(cur)
    existing = {s.get('title'): s['id'] for s in sources()}
    state_p = os.path.join(WORK, 'archive_state.json')
    state = json.load(open(state_p)) if os.path.exists(state_p) else {}
    for n, vol in enumerate(vols, 1):
        title = f'SMB transcripts archive vol. {n}'
        vids_in = [v for v, _ in vol]
        if state.get(title) == vids_in and title in existing:
            print(f'{title}: unchanged ({len(vids_in)} videos)')
            continue
        body = (f'{title} — FULL VERBATIM transcripts of SMB Capital options videos '
                f'({len(vids_in)} videos, most-viewed order). Companion of the distilled '
                f'"SMB Options vol." documents.\n\n' + '\n\n'.join(t for _, t in vol))
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f:
            f.write(body)
            tmp = f.name
        if title in existing:
            nlm('source', 'delete', existing[title], '--confirm')
        r = nlm('source', 'add', NB, '--file', tmp, '--title', title, '--wait', '--wait-timeout', '900')
        os.unlink(tmp)
        ok = 'ready' in (r.stdout + r.stderr).lower() or 'Added source' in r.stdout
        print(f'{title}: {"synced" if ok else "FAILED"} ({len(vids_in)} videos, {len(body)} chars)')
        if ok:
            state[title] = vids_in
            json.dump(state, open(state_p, 'w'))
    print('done:', len(vols), 'volume(s)')


if __name__ == '__main__':
    main()
