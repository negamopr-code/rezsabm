#!/usr/bin/env python3
"""Zero-token fidelity gate for NLM-distilled batches: every $ figure / percentage in an answer
must appear verbatim in that video's raw transcript (digits or spoken words). Unmatched figures
are reported so they can be flagged in the volume instead of trusted.
Usage: trial_verify_figures.py [answer-dir]"""
import os, re, subprocess, sys, json

TR = sys.argv[1] if len(sys.argv) > 1 else '/workspace/smb/trial'
CACHE = '/tmp/tx'
ONES = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
        11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
        18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
        80:'eighty',90:'ninety'}


def words(n):
    """Spoken forms a transcript may use for a round number (20000000 -> 'twenty million')."""
    out = set()
    for unit, name in ((1_000_000, 'million'), (1_000, 'thousand')):
        if n % unit == 0 and n // unit in ONES:
            out.add(f'{ONES[n // unit]} {name}')
    if n in ONES:
        out.add(ONES[n])
    return out


WORD = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
        'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
        'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,
        'eighty':80,'ninety':90}
SCALE = {'hundred':100,'thousand':1000,'million':1000000,'billion':1000000000}


def spoken_numbers(text):
    """Every number a transcript states in words, as integers (handles 'four hundred twenty two
    thousand five hundred')."""
    out, cur, tot = set(), 0, 0
    for tok in re.findall(r"[a-z]+", text.lower()):
        if tok in WORD:
            cur += WORD[tok]
        elif tok == 'hundred':
            cur = (cur or 1) * 100
        elif tok in SCALE:
            tot += (cur or 1) * SCALE[tok]; cur = 0
        else:
            if tot or cur: out.add(tot + cur)
            cur = tot = 0
    if tot or cur: out.add(tot + cur)
    return out


def norm(s):
    return re.sub(r'[,\s$]', '', s)


def main():
    ids = [f[7:-3] for f in os.listdir(TR) if f.startswith('nlm-b9-') and f.endswith('.md')]
    os.makedirs(CACHE, exist_ok=True)
    rows, tot, hits = [], 0, 0
    for i in sorted(ids):
        p = f'{CACHE}/{i}.txt'
        if not os.path.exists(p):
            subprocess.run(['docker', 'cp', f'awf-monitor-runner:/app/state/smb-options/transcripts/{i}.txt', p],
                           capture_output=True)
        if not os.path.exists(p):
            continue
        tx = open(p).read(); txn = norm(tx); txl = tx.lower()
        ans = open(f'{TR}/nlm-b9-{i}.md').read()
        figs = set(re.findall(r'\$ ?[0-9][0-9,\.]*|\b[0-9]+(?:\.[0-9]+)?%', ans))
        sp = spoken_numbers(txl)
        miss = []
        for f in figs:
            digits = norm(f).rstrip('%')
            if digits in txn:
                continue
            try:
                spoken = words(int(float(digits)))
            except ValueError:
                spoken = set()
            if any(w in txl for w in spoken):
                continue
            if f.endswith('%') and any(w in txl for w in {f'{d} percent' for d in words(int(float(digits)))} |
                                       {f'{digits} percent'}):
                continue
            try:
                if int(float(digits)) in sp:      # spoken compound, e.g. "four hundred twenty two thousand five hundred"
                    continue
            except ValueError:
                pass
            miss.append(f)
        tot += len(figs); hits += len(figs) - len(miss)
        rows.append({'id': i, 'figures': len(figs), 'unmatched': sorted(miss)})
    print(json.dumps({'figure_fidelity': f'{hits}/{tot}',
                      'pct': round(100 * hits / tot, 1) if tot else None,
                      'videos': rows}, indent=1))


if __name__ == '__main__':
    main()
