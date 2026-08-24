#!/bin/sh
# Resume/finish the mass video render for every strategy line (2026-08-24).
# Idempotent: sabm_r1_spy.py --videos skips already-rendered .webp files and
# rewrites trades.json with the video links at the end of each line.
cd /app || exit 1
LOG=data/render_all4.log
run() {
    echo "=== $(date -u '+%Y-%m-%d %H:%M:%S') START $*" >> "$LOG"
    python3 scripts/sabm_r1_spy.py "$@" --videos >> "$LOG" 2>&1
    echo "=== $(date -u '+%Y-%m-%d %H:%M:%S') DONE  $* (exit $?)" >> "$LOG"
}
# 1) finish the interrupted openR2 line (5570/7508 already on disk)
run --entry open --exit target --rk 2
# 2) the 7 SMB structures (small, completes the SMB tab quickly)
for s in cc csp pcs ic ib cds leap; do run --smb "$s"; done
# 3) the remaining big open-entry lines
run --entry open --exit target --rk 3
run --entry open --exit disc
run --entry open --exit transform
echo "=== $(date -u '+%Y-%m-%d %H:%M:%S') ALL RENDERS DONE ===" >> "$LOG"
