#!/usr/bin/env python3
"""Container-side NLM analysis round: 4 fixed questions over one "SMB comments archive vol. N"
source. No docker, no Claude — runs inside awf-monitor-runner so it survives Claude usage limits.
Usage: analyze_local.py <volume-number> [--force]"""
import json, os, re, sys, time
sys.path.insert(0, '/app/state/smb-options')
import comments_sync as cs

W = '/app/state/smb-options'
DIG = os.path.join(W, 'digests')
JOURNAL = os.path.join(W, 'daemon-journal.md')


def journal(line):
    with open(JOURNAL, 'a') as f:
        f.write(line + '\n')


def taxonomy_ids():
    p = os.path.join(W, 'taxonomy_ids.txt')
    return open(p).read().strip() if os.path.exists(p) else ''


def main():
    n = int(sys.argv[1]); force = '--force' in sys.argv
    os.makedirs(DIG, exist_ok=True)
    out = os.path.join(DIG, f'vol-{n:02d}.md')
    if os.path.exists(out) and not force:
        print(json.dumps({'volume': n, 'skipped': 'digest exists'})); return
    title = f'SMB comments archive vol. {n}'
    sid = next((s['id'] for s in cs.sources() if s.get('title') == title), None)
    if not sid:
        print(json.dumps({'volume': n, 'error': 'no source'})); sys.exit(1)
    tax = taxonomy_ids()
    common = (f'Use ONLY the source "{title}" (raw YouTube comments under SMB Capital options videos; each comment is '
              f'labelled [#n likes date], replies #n.k). Never mention commenter usernames. Be concrete and dense; '
              f'no preamble.\n')
    QS = [
        ('concerns', common + (f'Taxonomy of concerns: {tax}.\n' if tax else '') +
         'Task: list the concrete concerns/topics this audience raises in this volume, ranked by how many comments '
         'raise them. For each: taxonomy id (or NEW:<slug> if none fits), estimated comment count in this volume, a '
         'one-line description, and the single most-liked example comment paraphrased in <=20 words. Then a section '
         '"NEW TOPICS NOT IN TAXONOMY" with any recurring concern (>=5 comments) the taxonomy misses.'),
        ('takeaways', common +
         'Task: give 8-12 dated TAKEAWAYS about this audience from this volume — what they misunderstand, struggle '
         'with, push back on, ask SMB for, and which video topics trigger which reactions. Each takeaway: one bold '
         'sentence + evidence (approx. how many comments, likes, which video).'),
        ('questions', common +
         'Task: list the 15 most important QUESTIONS asked in the comments that did NOT get a substantive reply. Rank '
         'by likes, give the [#n] label, the video title (short), likes, and the question paraphrased in <=25 words. '
         'Then 5 questions that SMB itself DID answer in replies (label + one-line answer).'),
        ('needs', common +
         'Task: "WHAT THIS PUBLIC NEEDS" — rank the 10 needs of this audience (content, tools, explanations, proof, '
         'products) by strength of evidence (comment count x likes). For each: the need in one sentence, the evidence '
         '(counts, likes), and 2 short anonymous quotes (<=20 words, no usernames). Finally 3 concrete recommendations '
         'for what a product/course/tool for this public must contain.'),
    ]
    parts, done = [f'### NotebookLM digest — {title} ({time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())})\n'], set()
    if os.path.exists(out + '.partial'):                     # resume: never re-pay for an answer
        prev = open(out + '.partial').read()
        for key, _ in QS:
            m = re.search(rf'#### {key}\n\n(.*?)(?=\n#### |\Z)', prev, re.S)
            if m and m.group(1).strip():
                parts.append(f'#### {key}\n\n{m.group(1).strip()}\n'); done.add(key)
    ok = len(done)
    for key, q in QS:
        if key in done: continue
        qp = os.path.join(W, 'daemon_q.txt'); open(qp, 'w').write(q)
        t0 = time.time()
        a = cs.query_source(sid, q) if hasattr(cs, 'query_source') else None
        if a is None:                                        # fall back to the CLI path used by cmd_query
            import subprocess
            r = subprocess.run([sys.executable, os.path.join(W, 'comments_sync.py'), 'query', sid, qp, '420'],
                               capture_output=True, text=True, cwd=W)
            try: a = (json.loads(r.stdout).get('answer') or '').strip()
            except Exception: a = ''
        if not a:
            time.sleep(45)
            import subprocess
            r = subprocess.run([sys.executable, os.path.join(W, 'comments_sync.py'), 'query', sid, qp, '420'],
                               capture_output=True, text=True, cwd=W)
            try: a = (json.loads(r.stdout).get('answer') or '').strip()
            except Exception: a = ''
        raw = ''
        try: raw = r.stdout + r.stderr
        except Exception: pass
        if not a and 'RESOURCE_EXHAUSTED' in raw:
            open(os.path.join(W, 'quota_exhausted'), 'w').write(str(int(time.time())))  # epoch: backoff is time-based, the cap does NOT reset at UTC midnight
            journal('- ' + time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()) +
                    ' DAEMON: work4 RESOURCE_EXHAUSTED - daily NLM quota spent, backing off until tomorrow')
            open(out + '.partial', 'w').write('\n'.join(parts))
            print(json.dumps({'volume': n, 'answered': ok, 'quota': 'exhausted'})); sys.exit(76)
        dt = round(time.time() - t0)
        if not a:
            journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DAEMON NLM query `{key}` over "{title}" '
                    f'(source {sid[:8]}): NO ANSWER after {dt}s -> stop round, retry next cycle')
            open(out + '.partial', 'w').write('\n'.join(parts))
            print(json.dumps({'volume': n, 'answered': ok, 'failed': key})); sys.exit(75)
        ok += 1; parts.append(f'#### {key}\n\n{a}\n')
        journal(f'- {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())} DAEMON NLM query `{key}` over "{title}" '
                f'(source {sid[:8]}, purpose: {key} layer of audience-needs.md): answered in {dt}s, {len(a)} chars')
        time.sleep(20)
    open(out, 'w').write('\n'.join(parts))
    if os.path.exists(out + '.partial'): os.unlink(out + '.partial')
    print(json.dumps({'volume': n, 'answered': ok, 'digest': out}))


if __name__ == '__main__':
    main()
