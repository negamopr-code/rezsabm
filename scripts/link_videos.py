#!/usr/bin/env python3
"""Incrementally link already-rendered videos into each line's trades.json so the
viewer shows animations while a mass render is still running. Idempotent; the
renderer's own final rewrite (with the complete link set) remains authoritative —
any interleaving converges on the next pass. Exits 0 when everything is linked."""
import glob
import json
import os

pending = 0
for tj in sorted(glob.glob('data/results/*/trades.json')):
    d = os.path.dirname(tj)
    vd = os.path.join(d, 'videos')
    if not os.path.isdir(vd):
        pending += 1
        continue
    try:
        ts = json.load(open(tj))
    except (json.JSONDecodeError, OSError):   # mid-write by the renderer; next pass
        pending += 1
        continue
    changed = linked = 0
    for t in ts:
        if t.get('video'):
            linked += 1
            continue
        name = f"{t['n']:04d}_{t['entry_date']}_{'win' if t['r'] > 0 else 'loss'}.webp"
        p = os.path.join(vd, name)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            t['video'] = 'videos/' + name
            changed += 1
            linked += 1
    if changed:
        with open(tj, 'w') as f:
            json.dump(ts, f)
        print(f'{d}: +{changed} -> {linked}/{len(ts)}', flush=True)
    if linked < len(ts):
        pending += 1
raise SystemExit(0 if pending == 0 else 1)
