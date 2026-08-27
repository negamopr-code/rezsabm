#!/usr/bin/env python3
"""TRIAL: distil the next N undistilled SMB transcripts using NotebookLM instead of a Claude
subagent. Zero Claude tokens: the questions are source-scoped over the "SMB transcripts archive
vol. N" sources; the answers are written verbatim to smb/trial/ and assembled mechanically.
Usage: trial_distill_nlm.py [N]
"""
import json, os, re, subprocess, sys, time

CT, NB, PROF = 'awf-monitor-runner', 'e2e327c6-18bd-4a2a-bc8c-90ae2337f91c', 'work4'
SMB = '/workspace/smb'
TRIAL = os.path.join(SMB, 'trial')
ROLL = 2_400_000
N = int(sys.argv[1]) if len(sys.argv) > 1 else 15


def dexec(cmd, timeout=600):
    return subprocess.run(['docker', 'exec', '-e', f'NLM_PROFILE={PROF}', CT, 'sh', '-c', cmd],
                          capture_output=True, text=True, timeout=timeout)


def ledger():
    r = dexec('cd /app/state/smb-options && cat ledger.json')
    d = json.loads(r.stdout)
    v = d.get('videos', d)
    items = list(v.values()) if isinstance(v, dict) else v
    for it, key in zip(items, (v.keys() if isinstance(v, dict) else [x.get('id') for x in items])):
        it.setdefault('id', key)
    return items


def sources():
    r = dexec(f'nlm source list {NB} -p {PROF}')
    return json.loads(r.stdout)


def query(sid, q, timeout=420):
    """One source-scoped NotebookLM query. Answer is written to a file BEFORE any peek."""
    qp = os.path.join(TRIAL, 'q.txt')
    open(qp, 'w').write(q)
    subprocess.run(['docker', 'cp', qp, f'{CT}:/tmp/trial_q.txt'], check=True)
    r = dexec(f'cd /app/state/smb-options && python3 comments_sync.py query {sid} /tmp/trial_q.txt {timeout}',
              timeout=timeout + 120)
    try:
        return (json.loads(r.stdout).get('answer') or '').strip()
    except Exception:
        return ''


def journal(line):
    with open(os.path.join(SMB, 'nlm-mirror', 'pipeline-journal.md'), 'a') as f:
        f.write(line + '\n')


def main():
    os.makedirs(TRIAL, exist_ok=True)
    done_ids = set(re.findall(r'\b([A-Za-z0-9_-]{11})\b', open(os.path.join(SMB, 'volume-1.md')).read()))
    tr = [x for x in ledger() if x.get('status') == 'transcribed']
    tr.sort(key=lambda x: -(x.get('views') or 0))
    # reproduce sync_archives' split EXACTLY: videos.json order, real file sizes, ROLL chars/volume
    r = dexec('cd /app/state/smb-options && python3 -c "'
              "import json,os;"
              "order=[v['id'] for v in json.load(open('videos.json'))['videos']];"
              "have={f[:-4]:os.path.getsize('transcripts/'+f) for f in os.listdir('transcripts') if f.endswith('.txt')};"
              "print(json.dumps([(i,have[i]) for i in order if i in have]))"
              '"')
    seq = json.loads(r.stdout)
    vol_of, size, n, cur = {}, 0, 1, 0
    for vid, c in seq:
        if size + c > ROLL and cur:
            n += 1; size = 0; cur = 0
        vol_of[vid] = n; size += c; cur += 1
    todo = [x for x in tr if x['id'] not in done_ids][:N]
    if not todo:
        print('nothing undistilled'); return
    src = {s['title']: s['id'] for s in sources()}
    groups = {}
    for x in todo:
        groups.setdefault(vol_of[x['id']], []).append(x)
    print(json.dumps({'batch': [(x['id'], x['title'], x.get('views')) for x in todo],
                      'groups': {k: len(v) for k, v in groups.items()}}, indent=1)[:1500])

    out, qn, empty = [], 0, []
    for vol, vids in sorted(groups.items()):
        title = f'SMB transcripts archive vol. {vol}'
        sid = src.get(title)
        if not sid:
            print('missing source', title); continue
        for x in vids:
            p_out = os.path.join(TRIAL, f'nlm-b9-{x["id"]}.md')
            if os.path.exists(p_out) and os.path.getsize(p_out) > 200 \
                    and 'not available' not in open(p_out).read()[:400]:   # resume: never re-pay
                out.append((vol, x, p_out, os.path.getsize(p_out))); continue
            q = (f'Use ONLY the source "{title}", and within it ONLY the transcript of the video with id '
                 f'[{x["id"]}] titled "{x["title"]}". Ignore every other transcript in the source.\n\n'
                 'Produce two parts about THAT ONE video, no preamble:\n\n'
                 'PART A — handbook chapter content: the setup (instrument, structure, strikes/deltas, DTE, entry '
                 'trigger), the management and exit rules, the stated edge or statistics, and the caveats the '
                 'presenter gives. Dense prose or tight bullets.\n\n'
                 'PART B — a markdown table of every CONCRETE NUMBER spoken, columns: | theme | trade (instrument, '
                 'structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win '
                 'rate, percentages) |. One row per distinct trade or statistic.\n\n'
                 'Rules: never invent, round or reconcile a figure that is not spoken; quote each exactly as said; '
                 'if a number is garbled in the transcript write it as spoken and add "(garbled)"; if the video does '
                 'not state something, omit it rather than guessing.')
            t0 = time.time()
            a = query(sid, q)
            if not a:
                time.sleep(45); a = query(sid, q)
            dt = round(time.time() - t0)
            open(p_out, 'w').write(a)
            qn += 1
            if not a: empty.append(x['id'])
            journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} NLM query `trial-distill` over '
                    f'"{title}" scoped to [{x["id"]}] (source {sid[:8]}, purpose: TRIAL NLM distillation batch 9): '
                    + (f'answered in {dt}s, {len(a)} chars' if a else f'NO ANSWER after {dt}s'))
            out.append((vol, x, p_out, len(a)))
            time.sleep(20)

    asm = os.path.join(TRIAL, 'volume-nlm-batch9.md')
    with open(asm, 'w') as f:
        f.write('# TRIAL — batch 9 distilled by NotebookLM (zero Claude tokens)\n\n'
                f'Generated {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} · {len(todo)} videos · '
                f'{qn} work4 queries · source-scoped over the transcripts archive volumes.\n\n'
                '## Batch\n\n' + '\n'.join(f'- [{x["id"]}] {x["title"]} ({x.get("views")} views)' for x in todo) + '\n')
        for vol, x, p, _ in out:
            f.write(f'\n\n## [{x["id"]}] {x["title"]} ({x.get("views")} views, archive vol. {vol})\n\n'
                    + (open(p).read().strip() or '_NO ANSWER FROM NOTEBOOKLM_') + '\n')
    print(json.dumps({'videos': len(todo), 'queries_paid': qn, 'assembled': asm, 'empty': empty,
                      'chars': {x['id']: c for _, x, _, c in out}}))


if __name__ == '__main__':
    main()
