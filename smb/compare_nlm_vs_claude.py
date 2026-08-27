#!/usr/bin/env python3
"""Head-to-head on videos distilled by BOTH Claude (volume-1.md) and NotebookLM (trial/).
Ground truth = the raw transcript. Reports, per source:
  precision = figures it states that DO appear in the transcript (1 - invention rate)
  recall    = share of the transcript's distinct figures it captured
Zero Claude tokens, zero NLM quota: pure text comparison."""
import os, re, subprocess, json

SMB = '/workspace/smb'; TRIAL = f'{SMB}/trial'; CACHE = '/tmp/tx'
FIG = re.compile(r'\$ ?[0-9][0-9,\.]*|\b[0-9]+(?:\.[0-9]+)?%')
ONES = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
        12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
        19:'nineteen',20:'twenty',25:'twenty five',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
        75:'seventy five',80:'eighty',90:'ninety',100:'one hundred'}


def norm(s): return re.sub(r'[,\s$%]', '', s).rstrip('.')


def spoken(fig):
    d = norm(fig)
    try: n = int(float(d))
    except ValueError: return set()
    out = set()
    for unit, name in ((1_000_000, 'million'), (1_000, 'thousand')):
        if n % unit == 0 and n // unit in ONES: out.add(f'{ONES[n//unit]} {name}')
    if n in ONES: out.add(ONES[n]); out.add(f'{ONES[n]} percent')
    return out


def in_text(fig, txn, txl):
    return norm(fig) in txn or any(w in txl for w in spoken(fig))


def transcript(vid):
    p = f'{CACHE}/{vid}.txt'
    if not os.path.exists(p):
        subprocess.run(['docker','cp',f'awf-monitor-runner:/app/state/smb-options/transcripts/{vid}.txt',p],
                       capture_output=True)
    return open(p).read() if os.path.exists(p) else ''


def main():
    vol = open(f'{SMB}/volume-1.md').read()
    rows = []
    for f in sorted(os.listdir(TRIAL)):
        if not (f.startswith('nlm-b9-') and f.endswith('.md')): continue
        vid = f[7:-3]
        if vid not in vol: continue                      # not distilled by Claude -> no head-to-head
        tx = transcript(vid)
        if not tx: continue
        txn, txl = norm(tx), tx.lower()
        truth = {x for x in FIG.findall(tx)}
        claude = set()
        idpat = re.compile(r'\[([A-Za-z0-9_-]{11})\]')
        for line in vol.split('\n'):
            if vid not in line: continue
            cited = set(idpat.findall(line))
            if cited - {vid}: continue          # multi-cited line: figures may belong to another video
            claude |= set(FIG.findall(line))
        nlm = set(FIG.findall(open(f'{TRIAL}/{f}').read()))
        def score(s):
            ok = {x for x in s if in_text(x, txn, txl)}
            return len(s), len(ok), (round(100*len(ok)/len(s),1) if s else None), \
                   round(100*len({norm(x) for x in ok} & {norm(t) for t in truth})/max(len({norm(t) for t in truth}),1),1)
        rows.append({'video': vid, 'transcript_figures': len({norm(t) for t in truth}),
                     'claude': score(claude), 'nlm': score(nlm),
                     'nlm_not_in_transcript': sorted(x for x in nlm if not in_text(x, txn, txl)),
                     'claude_not_in_transcript': sorted(x for x in claude if not in_text(x, txn, txl))})
    print(f"{'video':14} {'truth':>6} | {'Claude n/ok/prec/recall':>26} | {'NLM n/ok/prec/recall':>26}")
    for r in rows:
        c, n = r['claude'], r['nlm']
        print(f"{r['video']:14} {r['transcript_figures']:6} | {c[0]:4}/{c[1]:<4}{str(c[2]):>6}% {str(c[3]):>6}%   | "
              f"{n[0]:4}/{n[1]:<4}{str(n[2]):>6}% {str(n[3]):>6}%")
    agg = lambda k, i: sum(r[k][i] for r in rows)
    print(f"\nTOTAL  Claude: {agg('claude',1)}/{agg('claude',0)} figures verified "
          f"({100*agg('claude',1)/max(agg('claude',0),1):.1f}% precision)")
    print(f"TOTAL  NLM   : {agg('nlm',1)}/{agg('nlm',0)} figures verified "
          f"({100*agg('nlm',1)/max(agg('nlm',0),1):.1f}% precision)")
    json.dump(rows, open(f'{TRIAL}/head-to-head.json','w'), indent=1)
    for r in rows:
        if r['nlm_not_in_transcript'] or r['claude_not_in_transcript']:
            print(f"  {r['video']}: NLM invented {r['nlm_not_in_transcript']} | Claude invented {r['claude_not_in_transcript']}")


if __name__ == '__main__':
    main()
