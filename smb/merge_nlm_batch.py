#!/usr/bin/env python3
"""Merge already-extracted NotebookLM per-video answers into volume-1.md (hybrid pipeline).
Zero NLM quota (extraction is already paid for), zero Claude tokens: every figure is checked
against the raw transcript by trial_verify_figures' rules and flagged inline when unverified.
Sections land in a clearly-labelled NLM chapter; the video index gets one row per video.
Usage: merge_nlm_batch.py [--dry]"""
import json, os, re, subprocess, sys

SMB = '/workspace/smb'; TRIAL = f'{SMB}/trial'; CACHE = '/tmp/tx'
VOL = f'{SMB}/volume-1.md'
FIG = re.compile(r'\$ ?[0-9][0-9,\.]*|\b[0-9]+(?:\.[0-9]+)?%')
ONES = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
        12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
        19:'nineteen',20:'twenty',25:'twenty five',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
        75:'seventy five',80:'eighty',90:'ninety',100:'one hundred'}
HEAD = '\n## CHAPTER: NLM-extracted videos (hybrid pipeline — NotebookLM extraction, figure-gated)\n\n' \
       '> Extracted by NotebookLM from the verbatim transcript archives, then gated by ' \
       '`trial_verify_figures.py`: every figure below appears in the raw transcript unless marked ' \
       '**⚠unverified** (not found as digits or spoken words — treat as suspect until a human or Claude pass ' \
       'adjudicates it). Claude did not read these transcripts.\n'


def norm(s): return re.sub(r'[,\s$%]', '', s).rstrip('.')


def spoken(fig):
    d = norm(fig)
    try: n = int(float(d))
    except ValueError: return set()
    out = set()
    for unit, name in ((1_000_000, 'million'), (1_000, 'thousand')):
        if n % unit == 0 and n // unit in ONES: out.add(f'{ONES[n//unit]} {name}')
    if n in ONES: out |= {ONES[n], f'{ONES[n]} percent'}
    return out


def transcript(vid):
    p = f'{CACHE}/{vid}.txt'
    if not os.path.exists(p):
        subprocess.run(['docker','cp',f'awf-monitor-runner:/app/state/smb-options/transcripts/{vid}.txt',p],
                       capture_output=True)
    return open(p).read() if os.path.exists(p) else ''


def ledger():
    r = subprocess.run(['docker','exec','awf-monitor-runner','sh','-c',
                        'cd /app/state/smb-options && cat ledger.json'], capture_output=True, text=True)
    d = json.loads(r.stdout); v = d.get('videos', d)
    if isinstance(v, dict):
        for k, it in v.items(): it.setdefault('id', k)
        return list(v.values())
    return v


def main():
    dry = '--dry' in sys.argv
    vol = open(VOL).read()
    meta = {x['id']: x for x in ledger()}
    todo = sorted([f[7:-3] for f in os.listdir(TRIAL) if f.startswith('nlm-b9-') and f.endswith('.md')],
                  key=lambda i: -(meta.get(i, {}).get('views') or 0))
    todo = [i for i in todo if i not in vol]
    if not todo:
        print(json.dumps({'merged': 0, 'reason': 'nothing new'})); return
    secs, index, stats = [], [], []
    for vid in todo:
        ans = open(f'{TRIAL}/nlm-b9-{vid}.md').read().strip()
        tx = transcript(vid); txn, txl = norm(tx), tx.lower()
        figs = sorted(set(FIG.findall(ans)), key=len, reverse=True)
        bad = [f for f in figs if norm(f) not in txn and not any(w in txl for w in spoken(f))]
        for f in bad:                                    # flag in place, longest first (no double-tagging)
            ans = ans.replace(f, f'{f} **⚠unverified**')
        m = meta.get(vid, {})
        secs.append(f'\n### [{vid}] {m.get("title","")} ({(m.get("views") or 0):,} views)\n\n{ans}\n')
        theme = 'NLM-extracted (hybrid); Real numbers' + (f'; {len(bad)} unverified figure(s)' if bad else '')
        index.append(f'| {vid} | {m.get("title","")} | {(m.get("views") or 0):,} | {theme} |')
        stats.append({'id': vid, 'figures': len(figs), 'unverified': bad})
    if dry:
        print(json.dumps({'would_merge': len(todo), 'stats': stats}, indent=1)); return
    # append the chapter before the ledger section, and the index rows at the very end
    marker = '## LEDGER OF DISTILLED VIDEOS'
    body = HEAD + ''.join(secs)
    vol = vol.replace(marker, body + '\n' + marker, 1) if marker in vol else vol + body
    vol = vol.rstrip('\n') + '\n' + '\n'.join(index) + '\n'
    open(VOL, 'w').write(vol)
    tot = sum(s['figures'] for s in stats); unv = sum(len(s['unverified']) for s in stats)
    print(json.dumps({'merged': len(todo), 'figures': tot, 'unverified': unv,
                      'per_video': stats}, indent=1))


if __name__ == '__main__':
    main()
