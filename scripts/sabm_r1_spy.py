#!/usr/bin/env python3
"""SABM R-target backtest (default SPY) + SABM-style graphs + per-entry webp videos.

Rules (user 2026-08-23, audited against the SABM course):
- Entry: daily candle CLOSES above the previous day's HIGH, and we are flat -> long at that close.
- Stop:  bottom of the signal candle's BODY (min(open, close)); R = close - body_bottom.
  Signals with non-positive body or R < --minr-pct of price (default 0.3, SABM p.6 floor)
  are skipped; --minr-pct 0 = literal raw mode (micro-body artifacts, "_raw" output dir).
- Target: entry + RK*R (--rk 1/2/3 -> R1/R2/R3). Resting orders; gaps fill at the open
  (gap through target = "accident positif" beyond the objective; gap through stop = worse than -1R).
- Day that touches BOTH stop and target: intraday order unknowable from OHLC -> pessimistic stop.
- No other exit; data ending mid-trade -> closed at last close, labeled "open".
  NO TPG cut/trailing layer -> results not comparable to the SABM 2013 track record.
- Portfolio curves: risk min(1%, R% of price) per trade (no leverage), fixed-T0 vs compounded;
  --sig-r = "trades significatifs" threshold proxy for the win-rate convention (p.12).

Outputs into <out-root>/<SYM>_R<k>[suffix]/: trades.json, stats.json, curves.json,
graph_portfolio.png, graph_distribution.png, (--videos) videos/*.webp per entry;
--compare additionally draws the p.27 compounded R1/R2/R3 overlay from curves.json.
"""
from __future__ import annotations

import csv
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


SYM = arg('--symbol', 'SPY')
RK = float(arg('--rk', '1'))  # target = entry + RK * R  (1 -> R1, 2 -> R2, 3 -> R3)
# SABM p.6: a meaningful R spans "0.3% comme de 30%" of price — 0.3% is the course's own
# floor, so it is the default. --minr-pct 0 = literal raw mode (micro-body dojis included,
# which produce +-100R denominator artifacts; see the audit).
MINR = float(arg('--minr-pct', '0.3'))
SIGR = float(arg('--sig-r', '0.2'))  # |r| below this = "trade non significatif" (SABM p.12/p.16 proxy)
# --- rough weekly-call OPTION overlay (user 2026-08-23: "it is not like this in reality",
# deliberately simplified to test for edge vs the linear market; all knobs editable) ---
EXIT_MODE = arg('--exit', 'target')  # 'target' = SABM part I (R objective) | 'disc' = part II cocktail proxy
ENTRY = arg('--entry', 'breakout')   # 'breakout' = close > prev high | 'open' = resim daily-open strategy
OPEN_SL = float(arg('--open-sl-pct', '0.2'))  # resim: resting SL X% below the entry-day open (editable)
OPT = '--options' in sys.argv
OPT_DELTA = float(arg('--opt-delta', '0.5'))        # static delta: collect delta*move (R1 -> 0.5R)
OPT_PREM = float(arg('--opt-premium-pct', '1.0'))   # premium as % of underlying price per option
OPT_DAYS = int(arg('--opt-days', '5'))              # trading days to expiry ("weekly")
PRICING = arg('--pricing', 'bsm')                   # 'bsm' = Black-Scholes from quote history | 'rough' = static delta + flat premium
IV_MARKUP = float(arg('--iv-markup', '1.2'))        # sigma = RV(window) * markup (resim doctrine: never raw RV)
RV_WIN = int(arg('--rv-window', '20'))              # realized-vol lookback (trading days, no lookahead)
IV_SRC = arg('--iv-source', 'rv')                   # 'rv' = RV*markup | 'vix' = real VIX history (uploads/VIX_...csv)
IV_FLOOR = float(arg('--iv-floor', '0.10'))         # sigma floor (annualized) - dead-calm RV underprices real options
OPT_RATE = float(arg('--opt-rate', '0.04'))         # risk-free rate for BSM
HAIRCUT = float(arg('--opt-haircut-pct', '3'))      # % lost to spread/fees on each buy AND sell
# part-II exit knobs (exit-conformance audit 2026-08-23)
DEEP_BODY_K = float(arg('--deep-body-k', '1.5'))    # wick must be "fortement superieure" to body (p.55)
DEEP_MIN_R = float(arg('--deep-min-r', '0.5'))      # wick depth vs the trade's R ("gros creux profond", p.52)
DEEP_MIN_RANGE = float(arg('--deep-min-range', '0.5'))  # wick vs day range
HUG_TOL = float(arg('--hug-tol', '1.0'))            # >=3R hug only within this many R of the trendline (p.57/p.66)
STOP_BUF = float(arg('--stop-buf', '0.05'))         # stop sits UNDER the low by this many R (pp.45/52/57)
CSV = os.path.join(ROOT, 'uploads', f'{SYM}_daily_OHLC_yahoo.csv')
_SUFFIX = '' if MINR == 0.3 else ('_raw' if MINR == 0 else f'_minR{MINR:g}')
if ENTRY == 'open':
    _BASE = f"{SYM}_open" + (f"_sl{OPEN_SL:g}" if OPEN_SL != 0.2 else '')
elif EXIT_MODE == 'disc':
    _BASE = f"{SYM}_disc"
else:
    _BASE = f"{SYM}_R{RK:g}"
_DTE_TAG = '' if OPT_DAYS == 5 else f'{OPT_DAYS}d'
_OPT_SUFFIX = '' if not OPT else (('_optbs' if PRICING == 'bsm' else '_opt') + _DTE_TAG + ('_vix' if IV_SRC == 'vix' else ''))


def _dte_label():
    return {5: 'weekly', 21: 'monthly', 63: 'quarterly'}.get(OPT_DAYS, f'{OPT_DAYS}-day')
OUT = os.path.join(ROOT, 'data', 'results', f"{_BASE}{_SUFFIX}{_OPT_SUFFIX}")
VID = os.path.join(OUT, 'videos')

# --- palette (same family as the dashboard sim_chart renderer) ---
BG = (11, 15, 21)
GRID = (26, 37, 53)
UP = (0, 217, 126)
DN = (240, 54, 74)
TXT = (112, 144, 160)
MARK = (0, 200, 240)
HEAD = (221, 238, 246)
TGT = (255, 176, 32)


def load_bars(path: str) -> list[dict]:
    out = []
    with open(path) as f:
        for r in csv.DictReader(f):
            out.append({'date': r['Date'], 'open': float(r['Open']), 'high': float(r['High']),
                        'low': float(r['Low']), 'close': float(r['Close'])})
    return out


def backtest(bars: list[dict]) -> tuple[list[dict], dict]:
    trades: list[dict] = []
    pos = None
    skipped_body = 0
    for i in range(1, len(bars)):
        b = bars[i]
        if pos is not None:
            e, stop, tgt = pos['entry_price'], pos['stop'], pos['target']
            R = e - stop
            exit_price = None
            reason = None
            if b['open'] <= stop:
                exit_price, reason = b['open'], 'gap-stop'
            elif b['open'] >= tgt:
                exit_price, reason = b['open'], 'gap-target'
            elif b['low'] <= stop and b['high'] >= tgt:
                exit_price, reason = stop, 'ambiguous-stop'
            elif b['low'] <= stop:
                exit_price, reason = stop, 'stop'
            elif b['high'] >= tgt:
                exit_price, reason = tgt, 'target'
            if exit_price is not None:
                pos.update(exit_i=i, exit_date=b['date'], exit_price=round(exit_price, 4),
                           reason=reason, r=round((exit_price - e) / R, 4), days=i - pos['entry_i'])
                trades.append(pos)
                pos = None
        if pos is None:
            prev = bars[i - 1]
            if b['close'] > prev['high']:
                body_bottom = min(b['open'], b['close'])
                R = b['close'] - body_bottom
                if R <= 0 or R < b['close'] * MINR / 100:
                    skipped_body += 1
                    continue
                pos = {'n': len(trades) + 1, 'entry_i': i, 'entry_date': b['date'],
                       'entry_price': round(b['close'], 4), 'stop': round(body_bottom, 4),
                       'target': round(b['close'] + RK * R, 4), 'R_abs': round(R, 4)}
    if pos is not None:
        last = bars[-1]
        e, R = pos['entry_price'], pos['entry_price'] - pos['stop']
        pos.update(exit_i=len(bars) - 1, exit_date=last['date'], exit_price=round(last['close'], 4),
                   reason='open', r=round((last['close'] - e) / R, 4), days=len(bars) - 1 - pos['entry_i'])
        trades.append(pos)

    rs = [t['r'] for t in trades]
    wins = [r for r in rs if r > 0]
    losses = [r for r in rs if r < 0]  # r == 0 is flat, not a loss
    flats = sum(1 for r in rs if r == 0)
    gross_w = sum(wins)
    gross_l = -sum(losses)
    # SABM p.12/16/19/23 reports win rate on "trades significatifs" only (81->71/69);
    # the course never defines the threshold numerically -> SIGR is our proxy.
    sig = [r for r in rs if abs(r) >= SIGR]
    wins_sig = [r for r in sig if r > 0]
    losses_sig = [r for r in sig if r < 0]
    # portfolio curves at 1% risk per trade (SABM: fixed on T0 capital vs compounded),
    # position capped at 100% equity (no leverage): a tiny R cannot be levered to 1% risk.
    fixed, comp = [0.0], [100.0]
    capped = 0
    for t in trades:
        f_i = min(0.01, t['R_abs'] / t['entry_price'])  # actual risk fraction, cap = fundable
        if f_i < 0.01:
            capped += 1
        fixed.append(fixed[-1] + t['r'] * f_i * 100)
        comp.append(comp[-1] * (1 + t['r'] * f_i))
    comp_pct = [c - 100.0 for c in comp]
    def maxdd(curve):
        peak, dd = -1e18, 0.0
        for v in curve:
            peak = max(peak, v)
            dd = min(dd, v - peak)
        return dd

    def maxdd_rel(curve):  # relative % drawdown on a multiplicative equity curve
        peak, dd = 1e-18, 0.0
        for v in curve:
            peak = max(peak, v)
            dd = min(dd, (v / peak - 1) * 100)
        return dd
    bh = (bars[-1]['close'] / bars[0]['close'] - 1) * 100
    stats = {
        'symbol': SYM, 'target': f'R{RK:g}', 'bars': len(bars), 'from': bars[0]['date'], 'to': bars[-1]['date'],
        'rule': f"long at close when close > previous day's high; stop = body bottom (min(open,close)); target = entry + {RK:g}*R; both-touched day = pessimistic stop",
        'min_R_filter_pct_of_price': MINR,
        'trades': len(trades), 'skipped_signals': skipped_body,
        'micro_body_trades_R_lt_0.1pct_of_price': sum(1 for t in trades if t['R_abs'] < 0.001 * t['entry_price']),
        'win_rate_pct_all_trades': round(100 * len(wins) / len(trades), 2),
        'significant_trades': len(sig), 'non_significant_trades': len(trades) - len(sig),
        'significance_threshold_R': SIGR, 'flat_trades_r_eq_0': flats,
        'win_rate_pct_significant': round(100 * len(wins_sig) / len(sig), 2) if sig else None,
        'profit_factor': round(gross_w / gross_l, 3) if gross_l else None,
        'profit_factor_significant': round(sum(wins_sig) / -sum(losses_sig), 3) if losses_sig else None,
        'avg_r': round(sum(rs) / len(rs), 4), 'sum_r': round(sum(rs), 2),
        'sum_r_excl_micro': round(sum(t['r'] for t in trades if t['R_abs'] >= 0.001 * t['entry_price']), 2),
        'top10_trades_sum_r': round(sum(sorted(rs, reverse=True)[:10]), 2),
        'positive_accidents_beyond_target': sum(1 for r in rs if r > RK + 0.0001),
        'gap_losses_worse_than_minus1R': sum(1 for r in rs if r < -1.0001),
        'ambiguous_days_pessimistic': sum(1 for t in trades if t['reason'] == 'ambiguous-stop'),
        'sum_r_optimistic_ambiguous': round(sum(rs) + (RK + 1) * sum(1 for t in trades if t['reason'] == 'ambiguous-stop'), 2),
        'still_open': sum(1 for t in trades if t['reason'] == 'open'),
        'median_hold_days': sorted(t['days'] for t in trades)[len(trades) // 2],
        'max_hold_days': max(t['days'] for t in trades),
        'leverage_capped_curve': True, 'trades_hitting_notional_cap': capped,
        'final_fixed_pct_sabm_literal': round(sum(rs), 2),  # p.12 "1R = 1%": uncapped cumulative R
        'avg_risk_fraction_pct': round(100 * sum(min(0.01, t['R_abs'] / t['entry_price']) for t in trades) / len(trades), 3),
        'final_fixed_pct': round(fixed[-1], 2), 'final_compounded_pct': round(comp_pct[-1], 2),
        'maxdd_fixed_pct_of_T0': round(maxdd(fixed), 2),
        'maxdd_compounded_pct_points_SABM': round(maxdd(comp_pct), 2),
        'maxdd_compounded_pct_relative': round(maxdd_rel(comp), 2),
        'buy_hold_pct': round(bh, 2),
        'description': (f"Linear breakout with the SABM Part-I R-target exit: enter long at the daily "
                        f"close when the candle closes above the previous day's high (stop = bottom of the "
                        f"signal candle's body, defining R); a resting limit sells at entry + {RK:g}R; the "
                        f"resting stop exits at -1R; gaps fill at the open (accidents beyond the target, "
                        f"losses beyond -1R); a day touching both counts pessimistically as a stop."),
        'note': ('gross of commissions/slippage; risk 1% per trade like the SABM study, position capped at '
                 '100% equity (no leverage). NO TPG breakeven/cut layer: unlike the SABM track record '
                 '(p.11, p.15) losers are not neutralised, so the -1R bucket is the mode rather than the '
                 'exception - win rate and profit factor are NOT comparable to SABM 62% / 2.74. '
                 'SABM-style maxDD = percentage-point spread on the compounded curve (p.20).'),
    }
    return trades, {'stats': stats, 'fixed': fixed, 'comp_pct': comp_pct}


def backtest_options(bars: list[dict]) -> tuple[list[dict], dict]:
    """Rough long weekly call on the SAME breakout signals: premium is the whole risk
    (no stop, Korovin/`resim` locked doctrine), static delta capture, settle at expiry.
    Deliberate simplifications (user-acknowledged): delta does not grow ITM (understates
    wins), theta path ignored (premium is a flat cost), IV regime constant."""
    trades: list[dict] = []
    pos = None
    skipped_body = 0
    for i in range(1, len(bars)):
        b = bars[i]
        if pos is not None:
            e, tgt = pos['entry_price'], pos['target']
            R = pos['R_abs']
            move = None
            reason = None
            if b['open'] >= tgt:
                move, reason = b['open'] - e, 'gap-target'
            elif b['high'] >= tgt:
                move, reason = tgt - e, 'target'
            elif i >= pos['expiry_i']:
                move, reason = b['close'] - e, 'expiry'
            if reason is not None:
                payoff = OPT_DELTA * max(0.0, move)
                prem = pos['premium']
                pos.update(exit_i=i, exit_date=b['date'],
                           exit_price=round(e + move, 4), reason=reason,
                           r_gross=round(payoff / R, 4), premium_R=round(prem / R, 4),
                           r=round((payoff - prem) / R, 4),
                           opt_multiple=round(payoff / prem - 1, 4),
                           days=i - pos['entry_i'])
                trades.append(pos)
                pos = None
        if pos is None:
            prev = bars[i - 1]
            if b['close'] > prev['high']:
                body_bottom = min(b['open'], b['close'])
                R = b['close'] - body_bottom
                if R <= 0 or R < b['close'] * MINR / 100:
                    skipped_body += 1
                    continue
                pos = {'n': len(trades) + 1, 'entry_i': i, 'entry_date': b['date'],
                       'entry_price': round(b['close'], 4), 'stop': round(body_bottom, 4),
                       'target': round(b['close'] + RK * R, 4), 'R_abs': round(R, 4),
                       'opt': True, 'premium': round(b['close'] * OPT_PREM / 100, 4),
                       'delta': OPT_DELTA, 'expiry_i': i + OPT_DAYS,
                       'be': round(b['close'] + b['close'] * OPT_PREM / 100 / OPT_DELTA, 4)}
    if pos is not None:
        last = bars[-1]
        e, R = pos['entry_price'], pos['R_abs']
        move = last['close'] - e
        payoff = OPT_DELTA * max(0.0, move)
        pos.update(exit_i=len(bars) - 1, exit_date=last['date'], exit_price=round(last['close'], 4),
                   reason='open', r_gross=round(payoff / R, 4), premium_R=round(pos['premium'] / R, 4),
                   r=round((payoff - pos['premium']) / R, 4),
                   opt_multiple=round(payoff / pos['premium'] - 1, 4),
                   days=len(bars) - 1 - pos['entry_i'])
        trades.append(pos)

    rs = [t['r'] for t in trades]
    wins = [r for r in rs if r > 0]
    losses = [r for r in rs if r < 0]
    sig = [r for r in rs if abs(r) >= SIGR]
    wins_sig = [r for r in sig if r > 0]
    losses_sig = [r for r in sig if r < 0]
    gross_w, gross_l = sum(wins), -sum(losses)
    # equity curves: spend 1% of equity on premium per trade (premium IS the whole risk)
    fixed, comp = [0.0], [100.0]
    for t in trades:
        m = t['opt_multiple']
        fixed.append(fixed[-1] + m * 1.0)
        comp.append(comp[-1] * (1 + 0.01 * m))
    comp_pct = [c - 100.0 for c in comp]

    def maxdd(curve):
        peak, dd = -1e18, 0.0
        for v in curve:
            peak = max(peak, v)
            dd = min(dd, v - peak)
        return dd

    def maxdd_rel(curve):
        peak, dd = 1e-18, 0.0
        for v in curve:
            peak = max(peak, v)
            dd = min(dd, (v / peak - 1) * 100)
        return dd

    bh = (bars[-1]['close'] / bars[0]['close'] - 1) * 100
    stats = {
        'symbol': SYM, 'target': f'R{RK:g}', 'mode': 'weekly-call-rough',
        'bars': len(bars), 'from': bars[0]['date'], 'to': bars[-1]['date'],
        'rule': (f"same breakout signals; LONG CALL delta {OPT_DELTA:g}, premium {OPT_PREM:g}% of price, "
                 f"{OPT_DAYS} trading days to expiry; NO stop (premium = whole risk); exit at target touch "
                 f"(collect delta*{RK:g}R, gaps collect delta*gap) or settle delta*max(0,move) at expiry"),
        'min_R_filter_pct_of_price': MINR,
        'trades': len(trades), 'skipped_signals': skipped_body,
        'win_rate_pct_all_trades': round(100 * len(wins) / len(trades), 2),
        'significant_trades': len(sig), 'non_significant_trades': len(trades) - len(sig),
        'significance_threshold_R': SIGR,
        'win_rate_pct_significant': round(100 * len(wins_sig) / len(sig), 2) if sig else None,
        'profit_factor': round(gross_w / gross_l, 3) if gross_l else None,
        'profit_factor_significant': round(sum(wins_sig) / -sum(losses_sig), 3) if losses_sig else None,
        'avg_r': round(sum(rs) / len(rs), 4), 'sum_r': round(sum(rs), 2),
        'avg_premium_R': round(sum(t['premium_R'] for t in trades) / len(trades), 3),
        'positive_accidents_beyond_target': sum(1 for t in trades if t['r_gross'] > OPT_DELTA * RK + 0.0001),
        'expiry_settlements': sum(1 for t in trades if t['reason'] == 'expiry'),
        'target_exits': sum(1 for t in trades if t['reason'] in ('target', 'gap-target')),
        'expired_worthless': sum(1 for t in trades if t['reason'] == 'expiry' and t['r_gross'] == 0),
        'still_open': sum(1 for t in trades if t['reason'] == 'open'),
        'median_hold_days': sorted(t['days'] for t in trades)[len(trades) // 2],
        'final_fixed_pct': round(fixed[-1], 2), 'final_compounded_pct': round(comp_pct[-1], 2),
        'maxdd_fixed_pct_of_T0': round(maxdd(fixed), 2),
        'maxdd_compounded_pct_points_SABM': round(maxdd(comp_pct), 2),
        'maxdd_compounded_pct_relative': round(maxdd_rel(comp), 2),
        'buy_hold_pct': round(bh, 2),
        'description': (f"ROUGH option overlay on the same breakout signals: instead of the linear "
                        f"position, buy a weekly call with static delta {OPT_DELTA:g} for a flat premium of "
                        f"{OPT_PREM:g}% of the price; no stop - the premium is the whole risk; collect "
                        f"delta*move at the R{RK:g} target or settle delta*max(0, move) at expiry."),
        'note': (f"ROUGH option model (user-acknowledged): static delta understates ITM wins, theta path "
                 f"ignored, IV constant; premium {OPT_PREM:g}%/wk is realistic-ish for ATM SPY (0.4*sigma*sqrt(T)); "
                 f"weeklies sit in the FASTEST-theta zone (Korovin rolls a week before expiry to dodge it). "
                 f"1% of equity spent on premium per trade; r values are NET of premium in R units."),
    }
    return trades, {'stats': stats, 'fixed': fixed, 'comp_pct': comp_pct}


def _disc_signals_and_trail(bars):
    """Shared engine for the SABM part-II 'cocktail' exit, mechanized on daily OHLC.

    Mapping (course pp. 44-70, esp. p.57 cocktail + p.64 'logique globale'):
    - Dow (p.45): a pivot low (low[j] < low[j-1] and low[j] < low[j+1], known at close j+1)
      becomes the stop once a NEW HIGH above the peak preceding that pivot prints.
    - Deep (p.52/p.55): a REAL deep only - wick > DEEP_BODY_K*body, >= DEEP_MIN_R*R and
      >= DEEP_MIN_RANGE of the day's range -> stop under the wick, any R zone.
    - Tempo line (p.47): anchored at the entry bar's low + confirmed pivot lows, ascending
      only; descending segments give no line.
    - R zones (p.57, p.64): below 2R 'let it breathe' (only validated Dow + deep);
      from 2R, IF the tempo line is broken (close < line), stop under the last visible
      pivot low even unvalidated; from 3R 'coller le mouvement': hug the previous day's
      low ONLY when it sits within HUG_TOL*R of the tempo line (p.66 counter-example:
      no line/no creux -> no move).
    - All stop moves are effective from the NEXT day (no lookahead); stop only ratchets up.
    - Exit: open <= stop -> at open (gap), else low <= stop -> at stop. No profit target.
    NOT implemented (disclosed): gap-zone stop rules (pp.61-63/77/90), intraday climax exits
    (pp.91-94, daily data only), the ambiguous R1 activation gate (p.57), literal trendlines
    (proxied by the last-two-pivot-lows line). Deep requires a REAL deep (wick > k*body,
    >= minR*R, >= half the range - p.52 "gros creux profond" / p.55 pseudo-deep rejection);
    stops sit STOP_BUF*R UNDER the reference low (pp.45/52/57).
    Yields closed positions as dicts (without option/linear economics)."""
    pos = None
    skipped = 0
    out = []
    for i in range(1, len(bars)):
        b = bars[i]
        if pos is not None:
            stop = pos['trail']
            if b['open'] <= stop:
                pos.update(exit_i=i, exit_date=b['date'], exit_price=round(b['open'], 4), reason='gap-trail')
                out.append(pos); pos = None
            elif b['low'] <= stop:
                pos.update(exit_i=i, exit_date=b['date'], exit_price=round(stop, 4), reason='trail-stop')
                out.append(pos); pos = None
        if pos is not None:
            e, R = pos['entry_price'], pos['R_abs']
            pos['peak'] = max(pos['peak'], b['high'])
            zone = (pos['peak'] - e) / R

            def tl(j):  # tempo line: entry anchor + confirmed pivot lows, ascending only (p.47)
                tp = pos['tl_pts']
                if len(tp) < 2:
                    return None
                (i1, l1), (i2, l2) = tp[-2], tp[-1]
                if l2 <= l1:
                    return None
                return l2 + (l2 - l1) / (i2 - i1) * (j - i2)

            new_stop = pos['trail']
            # deep (p.52/p.55): a REAL deep only - wick strongly > body, deep vs R and vs range
            body = abs(b['close'] - b['open'])
            wick = min(b['open'], b['close']) - b['low']
            rng = b['high'] - b['low']
            if (wick > DEEP_BODY_K * body and wick >= DEEP_MIN_R * R
                    and rng > 0 and wick >= DEEP_MIN_RANGE * rng and b['low'] - STOP_BUF * R > new_stop):
                new_stop = b['low'] - STOP_BUF * R
            # pivot low at i-1 (needs i-2 inside the trade window)
            if i - 2 >= pos['entry_i']:
                pl, pm, pr = bars[i - 2]['low'], bars[i - 1]['low'], b['low']
                if pm < pl and pm < pr:
                    pos['pivot'] = (pm, pos['peak_before'])
                    pos['tl_pts'].append((i - 1, pm))
            # after R2 AND trendline broken: stop under the LAST VISIBLE low, unvalidated
            # (p.50 pt3/p.57), evaluated every bar
            line = tl(i)
            if (zone >= 2 and pos['pivot'] is not None and line is not None and b['close'] < line
                    and pos['pivot'][0] - STOP_BUF * R > new_stop):
                new_stop = pos['pivot'][0] - STOP_BUF * R
            # Dow validation (p.45): new high above the peak that preceded the last pivot
            if pos['pivot'] is not None:
                plow, ppeak = pos['pivot']
                if b['high'] > ppeak and plow - STOP_BUF * R > new_stop:
                    new_stop = plow - STOP_BUF * R
            # >=3R climax hug (p.57/p.64) ONLY for lows that hug the trendline (p.66 counter-example)
            if zone >= 3:
                lo1 = bars[i - 1]['low']
                near = (line is not None) and (lo1 - tl(i - 1)) <= HUG_TOL * R
                if near and lo1 - STOP_BUF * R > new_stop:
                    new_stop = lo1 - STOP_BUF * R
            new_stop = round(new_stop, 4)
            if new_stop > pos['trail']:
                pos['trail'] = new_stop
                pos['stops'].append([i, pos['trail']])
            pos['peak_before'] = pos['peak']
        if pos is None:
            prev = bars[i - 1]
            if b['close'] > prev['high']:
                body_bottom = min(b['open'], b['close'])
                R = b['close'] - body_bottom
                if R <= 0 or R < b['close'] * MINR / 100:
                    skipped += 1
                    continue
                pos = {'n': len(out) + 1, 'entry_i': i, 'entry_date': b['date'],
                       'entry_price': round(b['close'], 4), 'stop': round(body_bottom, 4),
                       'R_abs': round(R, 4), 'trail': round(body_bottom, 4),
                       'stops': [[i, round(body_bottom, 4)]], 'peak': b['high'],
                       'peak_before': b['high'], 'pivot': None, 'tl_pts': [(i, b['low'])], 'disc': True}
    if pos is not None:
        last = bars[-1]
        pos.update(exit_i=len(bars) - 1, exit_date=last['date'], exit_price=round(last['close'], 4), reason='open')
        out.append(pos)
    return out, skipped


def _std_stats(trades, rs, fixed, comp, comp_pct, bars, skipped, rule, extra):
    wins = [r for r in rs if r > 0]
    losses = [r for r in rs if r < 0]
    sig = [r for r in rs if abs(r) >= SIGR]
    wins_sig = [r for r in sig if r > 0]
    losses_sig = [r for r in sig if r < 0]

    def maxdd(curve):
        peak, dd = -1e18, 0.0
        for v in curve:
            peak = max(peak, v); dd = min(dd, v - peak)
        return dd

    def maxdd_rel(curve):
        peak, dd = 1e-18, 0.0
        for v in curve:
            peak = max(peak, v); dd = min(dd, (v / peak - 1) * 100)
        return dd

    st = {
        'symbol': SYM, 'bars': len(bars), 'from': bars[0]['date'], 'to': bars[-1]['date'],
        'rule': rule, 'min_R_filter_pct_of_price': MINR,
        'trades': len(trades), 'skipped_signals': skipped,
        'win_rate_pct_all_trades': round(100 * len(wins) / len(trades), 2),
        'significant_trades': len(sig), 'non_significant_trades': len(trades) - len(sig),
        'significance_threshold_R': SIGR,
        'win_rate_pct_significant': round(100 * len(wins_sig) / len(sig), 2) if sig else None,
        'profit_factor': round(sum(wins) / -sum(losses), 3) if losses else None,
        'profit_factor_significant': round(sum(wins_sig) / -sum(losses_sig), 3) if losses_sig else None,
        'avg_r': round(sum(rs) / len(rs), 4), 'sum_r': round(sum(rs), 2),
        'median_hold_days': sorted(t['days'] for t in trades)[len(trades) // 2],
        'max_hold_days': max(t['days'] for t in trades),
        'still_open': sum(1 for t in trades if t['reason'] == 'open'),
        'final_fixed_pct': round(fixed[-1], 2), 'final_compounded_pct': round(comp_pct[-1], 2),
        'maxdd_fixed_pct_of_T0': round(maxdd(fixed), 2),
        'maxdd_compounded_pct_points_SABM': round(maxdd(comp_pct), 2),
        'maxdd_compounded_pct_relative': round(maxdd_rel(comp), 2),
        'buy_hold_pct': round((bars[-1]['close'] / bars[0]['close'] - 1) * 100, 2),
    }
    st.update(extra)
    return st


def backtest_disc(bars):
    """Linear position, SABM part-II discretionary-proxy trailing exit."""
    raw, skipped = _disc_signals_and_trail(bars)
    trades = []
    for t in raw:
        e, R = t['entry_price'], t['R_abs']
        t['days'] = t['exit_i'] - t['entry_i']
        t['r'] = round((t['exit_price'] - e) / R, 4)
        t['max_r'] = round((t['peak'] - e) / R, 2)
        t['target'] = round(e + RK * R, 4)  # ladder reference only (no target exit)
        for k in ('peak', 'peak_before', 'pivot', 'trail', 'tl_pts'):
            t.pop(k, None)
        trades.append(t)
    rs = [t['r'] for t in trades]
    fixed, comp = [0.0], [100.0]
    capped = 0
    for t in trades:
        f_i = min(0.01, t['R_abs'] / t['entry_price'])
        capped += f_i < 0.01
        fixed.append(fixed[-1] + t['r'] * f_i * 100)
        comp.append(comp[-1] * (1 + t['r'] * f_i))
    comp_pct = [c - 100.0 for c in comp]
    extra = {
        'target': 'disc', 'mode': 'disc-linear',
        'final_fixed_pct_sabm_literal': round(sum(rs), 2),
        'leverage_capped_curve': True, 'trades_hitting_notional_cap': capped,
        'reached_2R_pct': round(100 * sum(1 for t in trades if t['max_r'] >= 2) / len(trades), 1),
        'reached_3R_pct': round(100 * sum(1 for t in trades if t['max_r'] >= 3) / len(trades), 1),
        'best_trade_R': max(rs), 'avg_win_R': round(sum(r for r in rs if r > 0) / max(1, sum(1 for r in rs if r > 0)), 2),
        'description': ("SABM Part-II discretionary exit, mechanized ('the cocktail'): same breakout "
                        "entry, then NO profit target - the stop trails the trend: under validated swing "
                        "lows (Dow), under REAL long-wick 'deep' days, after 2R behind fresh lows once the "
                        "tempo line breaks, and above 3R hugging every low near the trendline (climax "
                        "mode). Exits when the trailed stop is hit. Audited against the course PDF by the "
                        "exit-conformance agent."),
        'note': ('SABM part-II DISCRETIONARY PROXY (exit-conformance audited): real-deep wicks, Dow '
                 'validated pivots, entry-anchored ascending tempo line gating the >=2R unvalidated-low '
                 'rule (on break) and the >=3R hug (proximity); stops buffered under lows; effective '
                 'next day; no profit target. Gross.'),
    }
    rule = ("long at close when close > previous day's high; initial stop = body bottom; EXIT = part-II "
            "cocktail proxy (real-deep/Dow trail, tempo-line-gated >=2R lows and >=3R hug); no target")
    return trades, {'stats': _std_stats(trades, rs, fixed, comp, comp_pct, bars, skipped, rule, extra),
                    'fixed': fixed, 'comp_pct': comp_pct}


def backtest_disc_options(bars):
    """Rough call held under the part-II trailing exit: premium re-paid every OPT_DAYS held
    (weekly roll while the trade lives), payoff = delta * max(0, exit move) - premiums."""
    raw, skipped = _disc_signals_and_trail(bars)
    trades = []
    for t in raw:
        e, R = t['entry_price'], t['R_abs']
        t['days'] = t['exit_i'] - t['entry_i']
        weeks = max(1, -(-t['days'] // OPT_DAYS))
        prem = round(e * OPT_PREM / 100 * weeks, 4)
        move = t['exit_price'] - e
        payoff = OPT_DELTA * max(0.0, move)
        t.update(opt=True, delta=OPT_DELTA, weeks_rolled=weeks, premium=prem,
                 be=round(e + prem / OPT_DELTA, 4),
                 r_gross=round(payoff / R, 4), premium_R=round(prem / R, 4),
                 r=round((payoff - prem) / R, 4),
                 opt_multiple=round(payoff / prem - 1, 4),
                 max_r=round((t['peak'] - e) / R, 2), target=round(e + RK * R, 4))
        for k in ('peak', 'peak_before', 'pivot', 'trail', 'tl_pts'):
            t.pop(k, None)
        trades.append(t)
    rs = [t['r'] for t in trades]
    fixed, comp = [0.0], [100.0]
    for t in trades:
        m = t['opt_multiple']
        fixed.append(fixed[-1] + m * 1.0)
        comp.append(comp[-1] * (1 + 0.01 * m))
    comp_pct = [c - 100.0 for c in comp]
    extra = {
        'target': 'disc', 'mode': 'disc-option-rough',
        'avg_premium_R': round(sum(t['premium_R'] for t in trades) / len(trades), 3),
        'avg_weeks_rolled': round(sum(t['weeks_rolled'] for t in trades) / len(trades), 2),
        'reached_2R_pct': round(100 * sum(1 for t in trades if t['max_r'] >= 2) / len(trades), 1),
        'reached_3R_pct': round(100 * sum(1 for t in trades if t['max_r'] >= 3) / len(trades), 1),
        'best_trade_R': max(rs),
        'note': ('ROUGH option on the part-II trail: same trail exits as linear; the call is ROLLED '
                 'every OPT_DAYS held (premium re-paid), payoff = delta*max(0, exit move) - total '
                 'premiums; static delta, no theta path (user-acknowledged). 1% equity premium budget.'),
    }
    rule = (f"part-II cocktail-proxy trail exits; LONG CALL delta {OPT_DELTA:g}, premium {OPT_PREM:g}%/"
            f"{OPT_DAYS}d rolled while the trade lives; no stop on the option (premium = risk)")
    return trades, {'stats': _std_stats(trades, rs, fixed, comp, comp_pct, bars, skipped, rule, extra),
                    'fixed': fixed, 'comp_pct': comp_pct}


def _norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_call(S, K, T, sigma, r=None):
    """European call (Black-Scholes). Hull 15.6 fixture verified in the resim engine port."""
    r = OPT_RATE if r is None else r
    if T <= 0 or sigma <= 0:
        return max(0.0, S - K)
    sq = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / sq
    d2 = d1 - sq
    return S * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)


def realized_vols(bars, win=None):
    """Annualized close-to-close realized vol per bar index, window ending AT that bar
    (usable same-day at the close; no lookahead). None while history is insufficient."""
    win = RV_WIN if win is None else win
    logs = [None]
    for i in range(1, len(bars)):
        logs.append(math.log(bars[i]['close'] / bars[i - 1]['close']))
    out = [None] * len(bars)
    for i in range(win, len(bars)):
        w = logs[i - win + 1:i + 1]
        mu = sum(w) / len(w)
        var = sum((x - mu) ** 2 for x in w) / (len(w) - 1)
        out[i] = math.sqrt(var * 252)
    return out


def _sigma_base(bars):
    """Per-bar base sigma: real VIX close/100 (date-joined, forward-filled) when
    --iv-source vix, else RV(RV_WIN). Markup and IV_FLOOR applied at the use site."""
    if IV_SRC == 'vix':
        vix = {}
        path = os.path.join(ROOT, 'uploads', 'VIX_daily_OHLC_yahoo.csv')
        with open(path) as f:
            for r in csv.DictReader(f):
                vix[r['Date']] = float(r['Close']) / 100.0
        out, last = [], None
        for b in bars:
            last = vix.get(b['date'], last)
            out.append(last)
        return out
    return realized_vols(bars)


def _t_years(trading_days):
    return trading_days * 7 / 5 / 365.0  # trading days -> calendar fraction (resim: cal/365)


def backtest_options_bsm(bars, markup=None):
    """Model-priced weekly ATM call on the same breakout signals (target exit mode).
    Premium = BS(S, K=S, T, sigma=RV(win)*markup) * (1+haircut); early exit (target/gap)
    sells at BS remaining * (1-haircut) with the leg's entry sigma; expiry settles intrinsic.
    Premium is the whole risk - no stop."""
    markup = IV_MARKUP if markup is None else markup
    rvs = _sigma_base(bars)
    trades = []
    pos = None
    skipped_body = 0
    skipped_rv = 0
    for i in range(1, len(bars)):
        b = bars[i]
        if pos is not None:
            e, tgt, K = pos['entry_price'], pos['target'], pos['strike']
            S_exit = None
            reason = None
            if b['open'] >= tgt:
                S_exit, reason = b['open'], 'gap-target'
            elif b['high'] >= tgt:
                S_exit, reason = tgt, 'target'
            elif i >= pos['expiry_i']:
                S_exit, reason = b['close'], 'expiry'
            if reason is not None:
                t_rem = _t_years(pos['expiry_i'] - i)
                if reason == 'expiry':
                    proceeds = max(0.0, S_exit - K)
                else:
                    proceeds = bs_call(S_exit, K, t_rem, pos['sigma']) * (1 - HAIRCUT / 100)
                prem = pos['premium']
                R = pos['R_abs']
                pos.update(exit_i=i, exit_date=b['date'], exit_price=round(S_exit, 4), reason=reason,
                           s_exit=round(S_exit, 4), t_rem_days=pos['expiry_i'] - i,
                           r_gross=round(proceeds / R, 4), premium_R=round(prem / R, 4),
                           r=round((proceeds - prem) / R, 4),
                           opt_multiple=round(proceeds / prem - 1, 4), days=i - pos['entry_i'])
                trades.append(pos)
                pos = None
        if pos is None:
            prev = bars[i - 1]
            if b['close'] > prev['high']:
                body_bottom = min(b['open'], b['close'])
                R = b['close'] - body_bottom
                if R <= 0 or R < b['close'] * MINR / 100:
                    skipped_body += 1
                    continue
                if rvs[i] is None:
                    skipped_rv += 1
                    continue
                sigma = max(IV_FLOOR, rvs[i] * markup)
                prem = bs_call(b['close'], b['close'], _t_years(OPT_DAYS), sigma) * (1 + HAIRCUT / 100)
                pos = {'n': len(trades) + 1, 'entry_i': i, 'entry_date': b['date'],
                       'entry_price': round(b['close'], 4), 'stop': round(body_bottom, 4),
                       'target': round(b['close'] + RK * R, 4), 'R_abs': round(R, 4),
                       'opt': True, 'bsm': True, 'strike': round(b['close'], 4),
                       'rv': round(rvs[i], 4), 'sigma': round(sigma, 4),
                       'premium': round(prem, 4), 'premium_pct_of_S': round(100 * prem / b['close'], 3),
                       'expiry_i': i + OPT_DAYS,
                       'be': round(b['close'] + prem, 4)}
    if pos is not None:
        last = bars[-1]
        prem, R, K = pos['premium'], pos['R_abs'], pos['strike']
        proceeds = max(0.0, last['close'] - K)
        pos.update(exit_i=len(bars) - 1, exit_date=last['date'], exit_price=round(last['close'], 4),
                   reason='open', r_gross=round(proceeds / R, 4), premium_R=round(prem / R, 4),
                   r=round((proceeds - prem) / R, 4), opt_multiple=round(proceeds / prem - 1, 4),
                   days=len(bars) - 1 - pos['entry_i'])
        trades.append(pos)

    rs = [t['r'] for t in trades]
    fixed, comp = [0.0], [100.0]
    for t in trades:
        m = t['opt_multiple']
        fixed.append(fixed[-1] + m * 1.0)
        comp.append(comp[-1] * (1 + 0.01 * m))
    comp_pct = [c - 100.0 for c in comp]
    extra = {
        'target': f'R{RK:g}', 'mode': 'weekly-call-bsm',
        'pricing': f"BSM sigma={'VIX' if IV_SRC == 'vix' else f'RV({RV_WIN})'}*{markup:g} (floor {IV_FLOOR:g}), r={OPT_RATE:g}, haircut {HAIRCUT:g}%/side, T=cal/365",
        'avg_premium_pct_of_S': round(sum(t['premium_pct_of_S'] for t in trades) / len(trades), 3),
        'avg_premium_R': round(sum(t['premium_R'] for t in trades) / len(trades), 3),
        'skipped_no_rv_history': skipped_rv,
        'target_exits': sum(1 for t in trades if t['reason'] in ('target', 'gap-target')),
        'expiry_settlements': sum(1 for t in trades if t['reason'] == 'expiry'),
        'expired_worthless': sum(1 for t in trades if t['reason'] == 'expiry' and t['r_gross'] == 0),
        'best_trade_R': max(rs),
        'description': (f"MODEL-priced option on the breakout signals: a {_dte_label()} ATM call priced by "
                        f"Black-Scholes from our own quote history (sigma = {RV_WIN}-day realized vol x "
                        f"{markup:g} markup, {HAIRCUT:g}%/side costs); sells at model value on the R{RK:g} "
                        f"target touch, settles intrinsic at expiry; premium = the whole risk."),
        'note': ('MODEL-priced option (user request): premium & early-sale value from Black-Scholes '
                 'with sigma = realized vol of our own quote history * markup (resim doctrine); '
                 'gamma/time value now included in wins; expiry = intrinsic. Still simplified: '
                 'RV-proxy IV (no vol smile/term structure), leg keeps entry sigma. '
                 '1% of equity spent on premium per trade.'),
    }
    rule = (f"same breakout signals; LONG {_dte_label()} ATM CALL priced by BSM (RV({RV_WIN})*{markup:g}), {OPT_DAYS}d expiry; "
            f"target-touch sells at model value, expiry settles intrinsic; premium = whole risk")
    return trades, {'stats': _std_stats(trades, rs, fixed, comp, comp_pct, bars, skipped_body, rule, extra),
                    'fixed': fixed, 'comp_pct': comp_pct}


def backtest_disc_options_bsm(bars, markup=None):
    """Model-priced call chain under the part-II trail: ATM leg bought at entry; at each
    expiry while the trade lives, settle intrinsic and re-buy ATM at the current close with
    CURRENT RV; trail exit sells the live leg at model value."""
    markup = IV_MARKUP if markup is None else markup
    rvs = _sigma_base(bars)
    raw, skipped = _disc_signals_and_trail(bars)
    trades = []
    skipped_rv = 0
    for t in raw:
        i0 = t['entry_i']
        if rvs[i0] is None:
            skipped_rv += 1
            continue
        legs = []
        cost = 0.0
        proceeds = 0.0
        j = i0
        K = t['entry_price']
        sigma = max(IV_FLOOR, rvs[i0] * markup)
        prem = bs_call(t['entry_price'], K, _t_years(OPT_DAYS), sigma) * (1 + HAIRCUT / 100)
        cost += prem
        expiry = i0 + OPT_DAYS
        while True:
            if t['exit_i'] <= expiry:
                t_rem = _t_years(expiry - t['exit_i'])
                S = t['exit_price']
                if expiry == t['exit_i']:
                    proceeds += max(0.0, S - K)
                else:
                    proceeds += bs_call(S, K, t_rem, sigma) * (1 - HAIRCUT / 100)
                legs.append({'K': round(K, 4), 'prem': round(prem, 4), 'settle': 'exit'})
                break
            S_roll = bars[expiry]['close']
            proceeds += max(0.0, S_roll - K)
            legs.append({'K': round(K, 4), 'prem': round(prem, 4), 'settle': 'roll'})
            K = S_roll
            sigma = max(IV_FLOOR, (rvs[expiry] or sigma / markup) * markup)
            prem = bs_call(S_roll, K, _t_years(OPT_DAYS), sigma) * (1 + HAIRCUT / 100)
            cost += prem
            expiry += OPT_DAYS
        e, R = t['entry_price'], t['R_abs']
        t['days'] = t['exit_i'] - t['entry_i']
        t.update(opt=True, bsm=True, legs=legs, weeks_rolled=len(legs), premium=round(cost, 4),
                 be=round(e + cost, 4), rv=round(rvs[i0], 4),
                 r_gross=round(proceeds / R, 4), premium_R=round(cost / R, 4),
                 r=round((proceeds - cost) / R, 4),
                 opt_multiple=round(proceeds / cost - 1, 4),
                 max_r=round((t['peak'] - e) / R, 2), target=round(e + RK * R, 4))
        for k in ('peak', 'peak_before', 'pivot', 'trail'):
            t.pop(k, None)
        trades.append(t)
    rs = [t['r'] for t in trades]
    fixed, comp = [0.0], [100.0]
    for t in trades:
        m = t['opt_multiple']
        fixed.append(fixed[-1] + m * 1.0)
        comp.append(comp[-1] * (1 + 0.01 * m))
    comp_pct = [c - 100.0 for c in comp]
    extra = {
        'target': 'disc', 'mode': 'disc-option-bsm',
        'pricing': f"BSM sigma={'VIX' if IV_SRC == 'vix' else f'RV({RV_WIN})'}*{markup:g} (floor {IV_FLOOR:g}), r={OPT_RATE:g}, haircut {HAIRCUT:g}%/side, ATM re-strike each roll",
        'avg_premium_R': round(sum(t['premium_R'] for t in trades) / len(trades), 3),
        'avg_weeks_rolled': round(sum(t['weeks_rolled'] for t in trades) / len(trades), 2),
        'skipped_no_rv_history': skipped_rv,
        'reached_2R_pct': round(100 * sum(1 for t in trades if t['max_r'] >= 2) / len(trades), 1),
        'reached_3R_pct': round(100 * sum(1 for t in trades if t['max_r'] >= 3) / len(trades), 1),
        'best_trade_R': max(rs),
        'description': ("MODEL-priced option chain riding the Part-II discretionary trail: ATM call "
                        f"priced by Black-Scholes from the quote history, re-struck ATM at every {_dte_label()} "
                        "expiry while the trade lives (intrinsic collected each roll), model value at the "
                        "trail exit; premiums = the whole risk."),
        'note': ('MODEL-priced option chain on the part-II trail: BSM premiums from our quote history '
                 '(RV*markup), intrinsic at each weekly roll (ATM re-strike), model value at trail exit. '
                 '1% equity premium budget per trade-chain.'),
    }
    rule = (f"part-II cocktail-proxy trail exits; ATM CALL chain priced by BSM (RV({RV_WIN})*{markup:g}), "
            f"re-struck ATM every {OPT_DAYS}d while the trade lives")
    return trades, {'stats': _std_stats(trades, rs, fixed, comp, comp_pct, bars, skipped, rule, extra),
                    'fixed': fixed, 'comp_pct': comp_pct}


def backtest_open(bars):
    """The random-entry-simulation daily-open strategy (its living spec, E2 + Day trail):
    enter long at EVERY open when flat; resting SL = OPEN_SL% below the entry-day open,
    active every day until hit (gap-down opens fill at the open), level never moves;
    hold while it survives; exit at the close of the first completed day whose close is
    below the previous day's low (entry bar skipped: first check compares the next day's
    close to the ENTRY day's low). Re-entry at the next day's open."""
    trades = []
    pos = None
    for i in range(1, len(bars)):
        b = bars[i]
        if pos is not None:
            stop = pos['stop']
            exit_price = None
            reason = None
            if b['open'] <= stop:
                exit_price, reason = b['open'], 'gap-stop'
            elif b['low'] <= stop:
                exit_price, reason = stop, 'stop'
            elif b['close'] < bars[i - 1]['low']:
                exit_price, reason = b['close'], 'trail-close'
            if exit_price is not None:
                e, R = pos['entry_price'], pos['R_abs']
                pos.update(exit_i=i, exit_date=b['date'], exit_price=round(exit_price, 4),
                           reason=reason, r=round((exit_price - e) / R, 4), days=i - pos['entry_i'])
                trades.append(pos)
                pos = None
                continue  # re-entry only from the NEXT day's open
        if pos is None:
            stop = b['open'] * (1 - OPEN_SL / 100)
            R = b['open'] - stop
            pos = {'n': len(trades) + 1, 'entry_i': i, 'entry_date': b['date'],
                   'entry_price': round(b['open'], 4), 'stop': round(stop, 4),
                   'R_abs': round(R, 4), 'open_entry': True,
                   'target': round(b['open'] + RK * R, 4)}
            if b['low'] <= pos['stop']:  # entry-day stop touch
                e = pos['entry_price']
                pos.update(exit_i=i, exit_date=b['date'], exit_price=pos['stop'], reason='stop',
                           r=-1.0, days=0)
                trades.append(pos)
                pos = None
    if pos is not None:
        last = bars[-1]
        e, R = pos['entry_price'], pos['R_abs']
        pos.update(exit_i=len(bars) - 1, exit_date=last['date'], exit_price=round(last['close'], 4),
                   reason='open', r=round((last['close'] - e) / R, 4), days=len(bars) - 1 - pos['entry_i'])
        trades.append(pos)
    rs = [t['r'] for t in trades]
    fixed, comp = [0.0], [100.0]
    capped = 0
    for t in trades:
        f_i = min(0.01, t['R_abs'] / t['entry_price'])
        capped += f_i < 0.01
        fixed.append(fixed[-1] + t['r'] * f_i * 100)
        comp.append(comp[-1] * (1 + t['r'] * f_i))
    comp_pct = [c - 100.0 for c in comp]
    extra = {
        'target': f'SL{OPEN_SL:g}%', 'mode': 'daily-open-e2',
        'open_sl_pct': OPEN_SL,
        'final_fixed_pct_sabm_literal': round(sum(rs), 2),
        'leverage_capped_curve': True, 'trades_hitting_notional_cap': capped,
        'best_trade_R': max(rs), 'trail_exits': sum(1 for t in trades if t['reason'] == 'trail-close'),
        'stop_exits': sum(1 for t in trades if t['reason'] in ('stop', 'gap-stop')),
        'description': (f"Daily-open strategy (ported from the random-entry-simulation lab, its E2 'hold "
                        f"after survive' with the Day trail bar): enter long at EVERY market open when flat; "
                        f"a resting stop-loss sits {OPEN_SL:g}% below the entry-day open (editable "
                        f"--open-sl-pct), active every day at its fixed level until hit - gap-down opens "
                        f"fill at the open; while it survives, hold and exit at the close of the first day "
                        f"whose close is below the previous day's low. No profit target."),
        'note': 'resim living-spec port: resting SL never moves; entry bar skipped by the trail; gross.',
    }
    rule = (f"long at EVERY open when flat; resting SL {OPEN_SL:g}% below entry open (fixed level); "
            f"exit at stop or at the first close below the previous day's low")
    return trades, {'stats': _std_stats(trades, rs, fixed, comp, comp_pct, bars, 0, rule, extra),
                    'fixed': fixed, 'comp_pct': comp_pct}


# ---------- rendering ----------
from PIL import Image, ImageDraw, ImageFont  # noqa: E402


def font(size: int):
    try:
        return ImageFont.load_default(size=size)
    except Exception:
        return ImageFont.load_default()


def graph_portfolio(trades, fixed, comp_pct, stats, path, w=1920, h=1080):
    img = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(img)
    f, fs = font(26), font(18)
    pl, pr, pt, pb = 90, 90, 120, 60
    n = len(trades)
    lo = min(min(fixed), min(comp_pct))
    hi = max(max(fixed), max(comp_pct))
    span = max(hi - lo, 1e-9)
    rlo, rhi = max(-5.0, min(t['r'] for t in trades)), min(5.0, max(t['r'] for t in trades))
    rspan = max(rhi - rlo, 1e-9)

    def x(i):
        return pl + i / max(1, n) * (w - pl - pr)

    def y(v):
        return pt + (hi - v) / span * (h - pt - pb)

    def yr(v):
        return pt + (rhi - v) / rspan * (h - pt - pb)

    for g in range(7):
        v = hi - span * g / 6
        yy = int(y(v))
        d.line([(pl, yy), (w - pr, yy)], fill=GRID, width=1)
        d.text((10, yy - 10), f'{v:+.0f}%', fill=TXT, font=fs)
        rv = rhi - rspan * g / 6
        d.text((w - pr + 8, yy - 10), f'{rv:+.1f}R', fill=(150, 80, 90), font=fs)
    # per-trade R bars (right axis), SABM-style red
    y0r = yr(0)
    bw = max(1, int((w - pl - pr) / max(1, n)) - 1)
    for i, t in enumerate(trades):
        xx = int(x(i))
        rv = max(rlo, min(rhi, t['r']))
        d.rectangle([xx, min(y0r, yr(rv)), xx + bw, max(y0r, yr(rv))], fill=(120, 27, 37))
    # curves
    for series, col, label in ((fixed, (80, 140, 255), 'fixed'), (comp_pct, UP, 'compounded')):
        pts = [(x(i), y(v)) for i, v in enumerate(series)]
        d.line(pts, fill=col, width=3)
    opt_mode = stats.get('mode') == 'weekly-call-rough'
    what = ("rough weekly CALL, no stop (premium = risk)" if opt_mode else "SABM " + stats['target'] + " exit, entry: close > prev high, stop: body bottom")
    d.text((pl, 16), f"{stats['symbol']} daily {stats['from']} -> {stats['to']}  |  {what}  |  "
                     f"{stats['trades']} trades, win(sig) {stats['win_rate_pct_significant']}%, PF(sig) {stats['profit_factor_significant']}", fill=HEAD, font=f)
    lit = '' if opt_mode else f"; SABM-literal fixed {stats.get('final_fixed_pct_sabm_literal', 0):+.1f}R"
    basis = "1% of equity spent on premium per trade" if opt_mode else "risk min(1%, R%) of equity (no leverage), gross"
    d.text((pl, 46), f"fixed {stats['final_fixed_pct']:+.1f}% (maxDD {stats['maxdd_fixed_pct_of_T0']}% of T0)   "
                     f"compounded {stats['final_compounded_pct']:+.1f}% (maxDD SABM-style {stats['maxdd_compounded_pct_points_SABM']} pts / rel {stats['maxdd_compounded_pct_relative']}%)   "
                     f"buy&hold {stats['buy_hold_pct']:+.1f}%   {basis}{lit}", fill=TXT, font=fs)
    warn = ("ROUGH option model: static delta, flat premium, no theta path (user-acknowledged) - r values NET of premium"
            if opt_mode else
            "pure R-target system: no TPG cut, no trailing, no trade-plan exit (SABM p.11) - not comparable to the SABM 2013 track record")
    d.text((pl, 66), warn, fill=(200, 150, 60), font=fs)
    d.line([(pl, 112), (pl + 40, 112)], fill=(80, 140, 255), width=3)
    d.text((pl + 48, 104), 'fixed min(1%,R%) (T0)', fill=(80, 140, 255), font=fs)
    d.line([(pl + 260, 112), (pl + 300, 112)], fill=UP, width=3)
    d.text((pl + 308, 104), 'compounded min(1%,R%)', fill=UP, font=fs)
    d.text((pl + 560, 104), 'bars = R per trade (right axis, clipped at +/-5R)', fill=(200, 90, 100), font=fs)
    img.save(path)


def graph_distribution(trades, path, w=1920, h=1080):
    img = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(img)
    f, fs = font(26), font(18)
    rs = [max(-5.25, min(5.25, t['r'])) for t in trades]  # edge bins collect the tails
    lo = math.floor(min(rs) * 4) / 4
    hi = math.ceil(max(rs) * 4) / 4
    nb = int(round((hi - lo) / 0.25))
    bins = [0] * nb
    for r in rs:
        bins[min(nb - 1, int((r - lo) / 0.25))] += 1
    mx = max(bins)
    pl, pr, pt, pb = 90, 40, 90, 80
    bw = (w - pl - pr) / nb
    for i, c in enumerate(bins):
        if not c:
            continue
        x0 = pl + i * bw
        hh = c / mx * (h - pt - pb)
        center = lo + (i + 0.5) * 0.25
        col = UP if center > 0 else DN
        d.rectangle([x0 + 1, h - pb - hh, x0 + bw - 1, h - pb], fill=col)
        if c > mx * 0.02:
            d.text((x0 + bw / 2 - 14, h - pb - hh - 26), str(c), fill=TXT, font=fs)
    for i in range(nb + 1):
        v = lo + i * 0.25
        if abs(v * 4 - round(v * 4)) < 1e-9 and (round(v * 4) % 4 == 0):
            xx = int(pl + i * bw)
            d.line([(xx, pt), (xx, h - pb)], fill=GRID, width=1)
            d.text((xx - 16, h - pb + 10), f'{v:+.0f}R', fill=TXT, font=fs)
    d.text((pl, 16), f"Result distribution (R multiples, 0.25R bins) - {trades and ''}SABM target exit", fill=HEAD, font=f)
    d.text((pl, 52), f'tails beyond +/-5R collected into the edge bins; <-1R = gap-through-stop opens, >+{RK:g}R = gap-through-target accidents (SABM)', fill=TXT, font=fs)
    img.save(path)


# SABM chart color conventions (course p. 58): entry = green, stop = red, target = blue.
LVL_ENTRY = (110, 255, 110)   # bright pure green, distinct from candle UP (0,217,126)
LVL_STOP = DN                 # red (kept)
LVL_TGT = (70, 140, 255)      # clear blue (R1..R3 per p. 58)
LVL_HI = (140, 150, 160)      # grey (R4+ per p. 58)


def render_video(bars, t, path, w=1280, h=720, pad_before=12, pad_after=4, max_frames=48):
    s = w / 640.0
    f = font(round(13 * s))
    fs = font(round(11 * s))
    fl = font(round(9 * s))  # small font for right-edge level labels
    i0, i1 = t['entry_i'], t['exit_i']
    lo_i = max(0, i0 - pad_before)
    hi_i = min(len(bars), i1 + pad_after + 1)
    win = bars[lo_i:hi_i]
    ie, ix = i0 - lo_i, i1 - lo_i
    lo = min(min(b['low'] for b in win), t['stop'])
    hi = max(max(b['high'] for b in win), t['target'])
    hi += (hi - lo) * 0.04  # headroom so the next ladder line can peek in when close
    span = max(hi - lo, 1e-9)
    pl, pr, pt, pb = round(8 * s), round(64 * s), round(34 * s), round(26 * s)

    def y(p):
        return pt + (hi - p) / span * (h - pt - pb)

    n = len(win)
    step = (w - pl - pr) / max(1, n)

    def x(i):
        return pl + step * i + step / 2

    body_w = max(2, int(step * 0.6))
    lw = max(1, round(s / 2))

    # level lines + their right-edge labels, de-overlapped vertically.
    # SABM p.58 ladder: entry green, stop red, R1..R3 blue, R4+ grey; ladder lines are
    # drawn only where they fall inside the visible price range (keeps the candles readable).
    R_abs = t['entry_price'] - t['stop']
    if t.get('opt'):
        levels = [(t['entry_price'], LVL_ENTRY, 'entry'), (t['be'], TGT, 'BE')]
    elif t.get('stops'):
        levels = [(t['entry_price'], LVL_ENTRY, 'entry')]  # trail drawn dynamically
    else:
        levels = [(t['entry_price'], LVL_ENTRY, 'entry'), (t['stop'], LVL_STOP, 'stop')]
    for k in range(1, 7):
        p = t['entry_price'] + k * R_abs
        if p <= hi:
            levels.append((p, LVL_TGT if k <= 3 else LVL_HI, f'R{k}'))
    lab_gap = round(11 * s)
    lab = sorted((int(y(p)), p, col, name) for p, col, name in levels)
    lab_ys, last_y = {}, None
    for yy, p, col, name in lab:
        ly = yy if last_y is None else max(yy, last_y + lab_gap)
        ly = min(ly, h - pb - lab_gap)
        lab_ys[name] = ly
        last_y = ly

    def base_img():
        img = Image.new('RGB', (w, h), BG)
        d = ImageDraw.Draw(img)
        for g in range(5):
            p = hi - span * g / 4
            yy = int(y(p))
            d.line([(pl, yy), (w - pr, yy)], fill=GRID, width=1)
            # drop the price tick label where a level label sits (avoid overlap)
            if all(abs(yy - ly) > lab_gap for ly in lab_ys.values()):
                d.text((w - pr + round(5 * s), yy - round(6 * s)), f'{p:.2f}', fill=TXT, font=fs)
        for i in range(0, n, max(1, n // 6)):
            d.text((max(pl, x(i) - 30 * s / 2), h - pb + round(6 * s)), win[i]['date'], fill=TXT, font=fs)
        return img, d

    def candle(d, i):
        b = win[i]
        col = UP if b['close'] >= b['open'] else DN
        cx = int(x(i))
        d.line([(cx, y(b['high'])), (cx, y(b['low']))], fill=col, width=lw)
        top, bot = y(max(b['open'], b['close'])), y(min(b['open'], b['close']))
        d.rectangle([cx - body_w // 2, top, cx + body_w // 2, max(bot, top + 1)], fill=col)

    def level(d, p, col, name):
        yy = int(y(p))
        for xx in range(pl, w - pr, round(9 * s)):
            d.line([(xx, yy), (xx + round(4 * s), yy)], fill=col, width=lw)
        d.text((w - pr + round(5 * s), lab_ys[name] - round(5 * s)), f'{name} {p:.2f}', fill=col, font=fl)

    def marker(d, i, p, up, col, label, clear_y=None):
        cx = x(i)
        yy = y(p) + round(14 * s) if up else y(p) - round(14 * s)
        if up:
            d.polygon([(cx, yy - round(7 * s)), (cx - round(5 * s), yy), (cx + round(5 * s), yy)], fill=col)
        else:
            d.polygon([(cx, yy + round(7 * s)), (cx - round(5 * s), yy), (cx + round(5 * s), yy)], fill=col)
        # label: to the left of the marker when it sits in the right half of the plot,
        # and vertically pushed clear of the candle (clear_y = candle low/high pixel)
        tw = d.textlength(label, font=fs)
        if cx > (pl + w - pr) / 2:
            tx = cx - round(7 * s) - tw
        else:
            tx = cx + round(7 * s)
        tx = max(pl, min(tx, w - pr - tw - round(2 * s)))
        ty = yy - round(5 * s)
        if clear_y is not None:
            if up:
                ty = max(ty, clear_y + round(3 * s))
            else:
                ty = min(ty, clear_y - round(13 * s))
        ty = max(pt + round(2 * s), min(ty, h - pb - round(12 * s)))
        d.text((tx, ty), label, fill=col, font=fs)

    def header(d, text):
        # full text must stay visible at the right edge: shrink, then split into 2 lines
        avail = w - pl - round(4 * s)
        size = round(13 * s)
        fh = font(size)
        while size > round(9 * s) and d.textlength(text, font=fh) > avail:
            size -= 1
            fh = font(size)
        if d.textlength(text, font=fh) <= avail:
            d.text((pl + 2, round(10 * s)), text, fill=HEAD, font=fh)
            return
        if '  -> ' in text:
            l1, l2 = text.split('  -> ', 1)
            l2 = '-> ' + l2
        else:
            mid = len(text) // 2
            cut = text.rfind(' ', 0, mid)
            cut = cut if cut > 0 else mid
            l1, l2 = text[:cut], text[cut:].lstrip()
        size = round(11 * s)
        fh = font(size)
        while size > round(8 * s) and max(d.textlength(l1, font=fh), d.textlength(l2, font=fh)) > avail:
            size -= 1
            fh = font(size)
        d.text((pl + 2, round(2 * s)), l1, fill=HEAD, font=fh)
        d.text((pl + 2, round(2 * s) + size + round(2 * s)), l2, fill=HEAD, font=fh)

    win_col = UP if t['r'] > 0 else DN
    _dl = f"d{t['delta']:g}" if t.get('delta') is not None else 'BSM'
    if t.get('opt') and t.get('stops'):
        head_live = (f"{SYM} 1d  #{t['n']:04d}  CALL {_dl} SABM-II trail {t['entry_date']} @ {t['entry_price']}  "
                     f"rolls {OPT_PREM:g}%/{OPT_DAYS}d  forming...")
        head_done = (f"{SYM} 1d  #{t['n']:04d}  CALL {_dl} SABM-II trail {t['entry_date']} @ {t['entry_price']}  "
                     f"-> {t['exit_date']}  gross {t['r_gross']:+.2f}R - prem {t['premium_R']:.2f}R ({t['weeks_rolled']}wk) = {t['r']:+.2f}R ({t['reason']}, {t['days']}d)")
    elif t.get('open_entry'):
        head_live = f"{SYM} 1d  #{t['n']:04d}  LONG daily-open {t['entry_date']} @ {t['entry_price']}  SL {t['stop']}  forming..."
        head_done = (f"{SYM} 1d  #{t['n']:04d}  LONG daily-open {t['entry_date']} @ {t['entry_price']}  SL {t['stop']}  "
                     f"-> {t['exit_date']} @ {t['exit_price']}  {t['r']:+.2f}R ({t['reason']}, {t['days']}d)")
    elif t.get('stops'):
        head_live = f"{SYM} 1d  #{t['n']:04d}  LONG SABM-II trail {t['entry_date']} @ {t['entry_price']}  init stop {t['stop']}  forming..."
        head_done = (f"{SYM} 1d  #{t['n']:04d}  LONG SABM-II trail {t['entry_date']} @ {t['entry_price']}  "
                     f"-> {t['exit_date']} @ {t['exit_price']}  {t['r']:+.2f}R (max {t.get('max_r', 0):+.1f}R, {t['reason']}, {t['days']}d)")
    elif t.get('opt'):
        head_live = (f"{SYM} 1d  #{t['n']:04d}  CALL {_dl} prem {t['premium']} {t['entry_date']} @ {t['entry_price']}  "
                     f"tgt {t['target']}  no stop, premium = risk  forming...")
        head_done = (f"{SYM} 1d  #{t['n']:04d}  CALL {_dl} prem {t['premium']} {t['entry_date']} @ {t['entry_price']}  tgt {t['target']}  "
                     f"-> {t['exit_date']}  gross {t['r_gross']:+.2f}R - prem {t['premium_R']:.2f}R = {t['r']:+.2f}R ({t['reason']}, {t['days']}d)")
    else:
        head_live = f"{SYM} 1d  #{t['n']:04d}  LONG {t['entry_date']} @ {t['entry_price']}  stop {t['stop']}  tgt {t['target']}  forming..."
        head_done = (f"{SYM} 1d  #{t['n']:04d}  LONG {t['entry_date']} @ {t['entry_price']}  stop {t['stop']}  tgt {t['target']}  "
                     f"-> {t['exit_date']} @ {t['exit_price']}  {t['r']:+.2f}R ({t['reason']}, {t['days']}d)")

    # frame schedule: context+signal first, then each held day, exit last (interior sampled to cap)
    reveal_idx = list(range(ie, ix + 1))
    if len(reveal_idx) > max_frames - 2:
        interior = reveal_idx[1:-1]
        stepn = (len(interior) + max_frames - 4) // (max_frames - 3)
        reveal_idx = [reveal_idx[0]] + interior[::stepn] + [reveal_idx[-1]]
    tail_idx = list(range(ix + 1, n))

    img, d = base_img()
    frames, durs = [], []
    # pre-entry build-up: reveal the context candle-by-candle (grouped into ~8 steps)
    # so the formation of the setup is VISIBLE before the entry appears
    if ie > 0:
        group = max(1, math.ceil(ie / 8))
        i = 0
        while i < ie:
            for j in range(i, min(i + group, ie)):
                candle(d, j)
            i += group
            fr = img.copy()
            ImageDraw.Draw(fr).text((pl + 2, round(10 * s)),
                                    f"{SYM} 1d  waiting for a signal... ({win[min(i, ie) - 1]['date']})",
                                    fill=TXT, font=f)
            frames.append(fr)
            durs.append(160)
    prev_k = ie - 1
    for k in reveal_idx:
        for i in range(prev_k + 1, k + 1):
            candle(d, i)
        prev_k = k
        fr = img.copy()
        dd = ImageDraw.Draw(fr)
        for p, col, name in levels:
            level(dd, p, col, name)
        if t.get('stops'):
            # trailing stop as a stepped red line, revealed with the candles
            steps = [(bi - lo_i, lvl) for bi, lvl in t['stops'] if bi - lo_i <= k]
            for si, (ri, lvl) in enumerate(steps):
                x1 = x(steps[si + 1][0]) if si + 1 < len(steps) else min(x(k) + step, w - pr)
                yy = int(y(lvl))
                for xx in range(int(x(ri)), int(x1), round(7 * s)):
                    dd.line([(xx, yy), (xx + round(3 * s), yy)], fill=LVL_STOP, width=lw)
                if si + 1 < len(steps):
                    dd.line([(int(x1), yy), (int(x1), int(y(steps[si + 1][1])))], fill=LVL_STOP, width=lw)
            if steps:
                dd.text((min(x(steps[-1][0]) + round(4 * s), w - pr - round(60 * s)),
                         y(steps[-1][1]) + round(3 * s)), f"trail {steps[-1][1]:.2f}", fill=LVL_STOP, font=fl)
        marker(dd, ie, t['entry_price'], True, LVL_ENTRY, f"entry {t['entry_price']}",
               clear_y=y(win[ie]['low']))
        done = k >= ix
        if done:
            marker(dd, ix, t['exit_price'], False, win_col, f"exit {t['exit_price']} {t['r']:+.2f}R",
                   clear_y=y(win[ix]['high']))
        header(dd, head_done if done else head_live)
        frames.append(fr)
        durs.append(1400 if k == ie else 400)
    # tail context after exit on the final frame
    fr = frames[-1]
    dd = ImageDraw.Draw(fr)
    for i in tail_idx:
        candle(dd, i)
    durs[-1] = 2600
    frames[0].save(path, format='WEBP', save_all=True, append_images=frames[1:],
                   duration=durs, loop=0, quality=80, method=4)


def graph_overlay(series, title, path, w=1920, h=1080):
    """Date-aligned overlay of compounded curves: series = [(name, color, values, dates)]."""
    if len(series) < 2 or any(s0[3] is None or len(s0[3]) != len(s0[2]) for s0 in series):
        print('graph_overlay: need >=2 dated series - skipped')
        return
    import datetime as _dt
    def _ord(d):
        return _dt.date.fromisoformat(d).toordinal()
    d0 = min(_ord(s0[3][0]) for s0 in series)
    d1 = max(_ord(s0[3][-1]) for s0 in series)
    dspan = max(1, d1 - d0)
    img = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(img)
    f, fs = font(26), font(18)
    pl, pr, pt, pb = 90, 40, 90, 60
    lo = min(min(s0[2]) for s0 in series)
    hi = max(max(s0[2]) for s0 in series)
    span = max(hi - lo, 1e-9)
    for g in range(7):
        v = hi - span * g / 6
        yy = int(pt + (hi - v) / span * (h - pt - pb))
        d.line([(pl, yy), (w - pr, yy)], fill=GRID, width=1)
        d.text((10, yy - 10), f'{v:+.0f}%', fill=TXT, font=fs)
    lx = pl
    for name, col, ser, dates in series:
        pts = [(pl + (_ord(dates[i]) - d0) / dspan * (w - pl - pr), pt + (hi - v) / span * (h - pt - pb)) for i, v in enumerate(ser)]
        d.line(pts, fill=col, width=3)
        d.text((lx, 52), f'{name} {ser[-1]:+.1f}%', fill=col, font=fs)
        lx += 220
    d.text((pl, 16), title, fill=HEAD, font=f)
    img.save(path)
    print('overlay graph ->', path)


def _load_curve(base_dir, name):
    p = os.path.join(base_dir, name, 'curves.json')
    if os.path.exists(p):
        with open(p) as fh:
            c = json.load(fh)
            return c['comp_pct'], c.get('dates')
    return None, None


def graph_compare(base_dir, sym, path, w=1920, h=1080):
    """SABM p.27: overlay of the COMPOUNDED curves of R1/R2/R3."""
    series = []
    for k, col in ((1, (70, 140, 255)), (2, UP), (3, (255, 176, 32))):
        vals, dates = _load_curve(base_dir, f'{sym}_R{k}')
        if vals:
            series.append((f'R{k}', col, vals, dates))
    graph_overlay(series, f'{sym} - comparison of the 3 exit strategies, COMPOUNDED 1% risk (SABM p.27)', path, w, h)


def main():
    bars = load_bars(CSV)
    if ENTRY == 'open':
        trades, port = backtest_open(bars)
    elif EXIT_MODE == 'disc':
        if OPT:
            trades, port = (backtest_disc_options_bsm(bars) if PRICING == 'bsm' else backtest_disc_options(bars))
        else:
            trades, port = backtest_disc(bars)
    else:
        if OPT:
            trades, port = (backtest_options_bsm(bars) if PRICING == 'bsm' else backtest_options(bars))
        else:
            trades, port = backtest(bars)
    os.makedirs(OUT, exist_ok=True)
    if os.path.isdir(VID) and '--videos' not in sys.argv:
        # stats-only rerun: keep the gallery's video links for clips already rendered
        for t in trades:
            name = f"{t['n']:04d}_{t['entry_date']}_{'win' if t['r'] > 0 else 'loss'}.webp"
            if os.path.exists(os.path.join(VID, name)):
                t['video'] = 'videos/' + name
    if OPT and PRICING == 'bsm':
        # honesty battery: IV-markup sweep (exits don't depend on sigma -> exact re-pricing)
        fn = backtest_disc_options_bsm if EXIT_MODE == 'disc' else backtest_options_bsm
        sweep = {}
        for mk in (1.0, 1.15, 1.2, 1.25, 1.5):
            _, pp_port = fn(bars, markup=mk)
            sweep[f'x{mk:g}'] = {'sum_net_R': pp_port['stats']['sum_r'],
                                 'final_compounded_pct': pp_port['stats']['final_compounded_pct']}
        port['stats']['iv_markup_sweep'] = sweep
    elif OPT:
        # honesty battery (resim options doctrine): result must not be an artifact of the
        # premium guess -> sweep premium; exits don't depend on premium, so this is exact.
        sweep = {}
        for pp in (0.5, 0.75, 1.0, 1.25, 1.5):
            net, eq = 0.0, 100.0
            for t in trades:
                prem = t['entry_price'] * pp / 100 * t.get('weeks_rolled', 1)
                payoff = (t['r_gross']) * t['R_abs']
                net += (payoff - prem) / t['R_abs']
                eq *= 1 + 0.01 * (payoff / prem - 1)
            sweep[f'{pp:g}%'] = {'sum_net_R': round(net, 1), 'final_compounded_pct': round(eq - 100, 1)}
        port['stats']['premium_sweep'] = sweep
    with open(os.path.join(OUT, 'trades.json'), 'w') as f:
        json.dump(trades, f)
    with open(os.path.join(OUT, 'stats.json'), 'w') as f:
        json.dump(port['stats'], f, indent=2)
    with open(os.path.join(OUT, 'curves.json'), 'w') as f:
        json.dump({'fixed': port['fixed'], 'comp_pct': port['comp_pct'],
                   'dates': [bars[0]['date']] + [t['exit_date'] for t in trades]}, f)
    if OPT:
        lin_vals, lin_dates = _load_curve(os.path.dirname(OUT), f"{_BASE}{_SUFFIX}")
        if lin_vals:
            _lbl = 'disc' if EXIT_MODE == 'disc' else f'R{RK:g}'
            graph_overlay([(f'linear {_lbl}', (70, 140, 255), lin_vals, lin_dates),
                           (f'call d{OPT_DELTA:g} p{OPT_PREM:g}%', TGT, port['comp_pct'],
                            [bars[0]['date']] + [t['exit_date'] for t in trades])],
                          f'{SYM} {_lbl} - rough weekly call vs linear, COMPOUNDED (1% risk / 1% premium budget)',
                          os.path.join(OUT, 'graph_vs_linear.png'))
    if '--compare' in sys.argv:
        graph_compare(os.path.dirname(OUT), SYM, os.path.join(os.path.dirname(OUT), f'{SYM}_graph_compare.png'))
    graph_portfolio(trades, port['fixed'], port['comp_pct'], port['stats'], os.path.join(OUT, 'graph_portfolio.png'))
    graph_distribution(trades, os.path.join(OUT, 'graph_distribution.png'))
    print(json.dumps(port['stats'], indent=2))
    if '--videos' in sys.argv:
        os.makedirs(VID, exist_ok=True)
        force = '--force-render' in sys.argv
        for k, t in enumerate(trades):
            name = f"{t['n']:04d}_{t['entry_date']}_{'win' if t['r'] > 0 else 'loss'}.webp"
            t['video'] = 'videos/' + name
            path = os.path.join(VID, name)
            if force or not os.path.exists(path) or os.path.getsize(path) == 0:
                render_video(bars, t, path)
            if (k + 1) % 100 == 0:
                print(f'videos: {k + 1}/{len(trades)}', flush=True)
        with open(os.path.join(OUT, 'trades.json'), 'w') as f:
            json.dump(trades, f)
        print(f'videos done: {len(trades)}')


if __name__ == '__main__':
    main()
