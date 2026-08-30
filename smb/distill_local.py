#!/usr/bin/env python3
"""Container-side hybrid distillation EXTRACTION (zero Claude tokens).
For each transcribed video that is neither distilled (present in volume-1.md) nor already
extracted, ask NotebookLM one source-scoped question over the transcripts archive volume that
actually contains it, and store the answer in distill/<id>.md. A Claude tick later merges those
answers into volume-1.md through the figure gate. Stops immediately on RESOURCE_EXHAUSTED.
Usage: distill_local.py [N]"""
import json, os, subprocess, sys, time

W = '/app/state/smb-options'
OUT = os.path.join(W, 'distill')
ROLL = 2_400_000
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
sys.path.insert(0, W)
import comments_sync as cs


def journal(line):
    with open(os.path.join(W, 'daemon-journal.md'), 'a') as f:
        f.write(line + '\n')


def volume_map():
    """sync_archives' split: videos.json order, real file sizes, ROLL chars per volume."""
    order = [v['id'] for v in json.load(open(os.path.join(W, 'videos.json')))['videos']]
    tdir = os.path.join(W, 'transcripts')
    have = {f[:-4]: os.path.getsize(os.path.join(tdir, f)) for f in os.listdir(tdir) if f.endswith('.txt')}
    vol_of, size, n, cur = {}, 0, 1, 0
    for vid in order:
        if vid not in have: continue
        c = have[vid]
        if size + c > ROLL and cur:
            n += 1; size = 0; cur = 0
        vol_of[vid] = n; size += c; cur += 1
    return vol_of


def main():
    os.makedirs(OUT, exist_ok=True)
    led = json.load(open(os.path.join(W, 'ledger.json')))
    v = led.get('videos', led)
    if isinstance(v, dict):
        for k, it in v.items(): it.setdefault('id', k)
        items = list(v.values())
    else:
        items = v
    volp = os.path.join(W, 'volume-1.md')
    vol_txt = open(volp).read() if os.path.exists(volp) else ''
    done = {f[:-3] for f in os.listdir(OUT) if f.endswith('.md') and os.path.getsize(os.path.join(OUT, f)) > 200}
    tr = sorted([x for x in items if x.get('status') == 'transcribed'], key=lambda x: -(x.get('views') or 0))
    todo = [x for x in tr if x['id'] not in vol_txt and x['id'] not in done][:N]
    if not todo:
        print(json.dumps({'extracted': 0, 'reason': 'nothing to do'})); return
    vmap = volume_map()
    src = {s.get('title'): s['id'] for s in cs.sources()}
    got = 0
    for x in todo:
        # yield to an interactive work4 job (the REZSABM exit advisor takes this lock while a
        # user waits on a chart verdict) — the daemon only checked it once per cycle, which is
        # too coarse for a 10-video batch that runs for half an hour
        lk = os.path.join(W, 'nlm_external.lock')
        if os.path.exists(lk) and time.time() - os.path.getmtime(lk) < 7200:
            journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DISTILL: paused, external NLM job holds the lock')
            break
        vol = vmap.get(x['id'])
        title = f'SMB transcripts archive vol. {vol}'
        sid = src.get(title)
        if not sid:
            journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DISTILL: no source "{title}" for {x["id"]}')
            continue
        q = (f'Use ONLY the source "{title}", and within it ONLY the transcript of the video with id '
             f'[{x["id"]}] titled "{x.get("title","")}". Ignore every other transcript in the source.\n\n'
             'Produce two parts about THAT ONE video, no preamble:\n\n'
             'PART A — handbook chapter content: the setup (instrument, structure, strikes/deltas, DTE, entry '
             'trigger), the management and exit rules, the stated edge or statistics, and the caveats the presenter '
             'gives.\n\nPART B — a markdown table of every CONCRETE NUMBER spoken, columns: | theme | trade '
             '(instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, '
             'P&L, win rate, percentages) |. One row per distinct trade or statistic.\n\n'
             'Rules: never invent, round or reconcile a figure that is not spoken; quote each exactly as said; if a '
             'number is garbled write it as spoken and add "(garbled)"; omit anything the video does not state.')
        qp = os.path.join(W, 'distill_q.txt'); open(qp, 'w').write(q)
        r = subprocess.run([sys.executable, os.path.join(W, 'comments_sync.py'), 'query', sid, qp, '420'],
                           capture_output=True, text=True, cwd=W)
        try:
            d = json.loads(r.stdout); a = (d.get('answer') or '').strip(); err = d.get('err') or ''
        except Exception:
            a, err = '', (r.stdout + r.stderr)
        if not a and 'RESOURCE_EXHAUSTED' in err:
            open(os.path.join(W, 'quota_exhausted'), 'w').write(str(int(time.time())))
            journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DISTILL: work4 RESOURCE_EXHAUSTED after '
                    f'{got} extraction(s) — backing off')
            print(json.dumps({'extracted': got, 'quota': 'exhausted'})); sys.exit(76)
        if not a:
            journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DISTILL: empty answer for {x["id"]} '
                    f'({err[:120]}) — will retry next cycle')
            continue
        open(os.path.join(OUT, f'{x["id"]}.md'), 'w').write(a)
        got += 1
        journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DISTILL: extracted [{x["id"]}] '
                f'{x.get("title","")[:60]} ({len(a)} chars, archive vol. {vol})')
        time.sleep(20)
    print(json.dumps({'extracted': got, 'remaining_estimate': len([x for x in tr if x['id'] not in vol_txt]) - got}))


if __name__ == '__main__':
    main()
