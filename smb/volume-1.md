# SMB OPTIONS — distilled teachings from the SMB Capital YouTube channel, volume 1

This document is a curated, deduplicated distillation of the teachings of SMB Capital's YouTube channel (SMB Capital is a proprietary trading firm in Midtown Manhattan, founded 2005; the options desk material is presented mainly by head options trader Seth Freudberg, with firm co-founder Mike Bellafiore and guest trading psychologist Dr. Brett Steenbarger). Method: full video transcripts are distilled into strategy chapters — rules, setups, entry/exit criteria, sizing, management and the reasoning behind them — with every concrete number preserved and each teaching cited to its source video by YouTube id in brackets, e.g. [MmryR1iu9dA]. Marketing filler is removed; each fact appears once. Volume 1 covers the 160 most-viewed harvested videos distilled so far (initial 5 + merge batch 1 of 30 + merge batch 2 of 35 + merge batches 3, 4, 5, 6, 7 and 8 of 15 each); later batches extend these chapters and the ledger. Note on batch 3: the harvested file for [zs4pK__ncCo] ("Top 3 Options Trading Mistakes You Must Avoid") is NOT a transcript — it contains a copy of this very volume (the harvester captured the wrong NotebookLM source while the volume was being uploaded), so that video is excluded from batch 3 and must be re-harvested; the next most-viewed undistilled video [W5Gl_E2Sq-A] was substituted. Note on batch 2: two of its transcripts are duplicates — [W1HJb-ST-6Q] carries the identical audio to [-gGvWxd_iXc], and the transcript filed under [AtSAFHA2Hvc] (titled as "Blunders ep. 9: Your Back Test Proves That You're Going To Get Rich") actually duplicates the covered-call video [Vm0qcsR5-E4], so the promised backtest-blunder content is absent from the corpus.

## CHAPTER: Options basics & pricing

**What calls and puts are.** [w_BjFmbwbYA] A call option on a stock is a bet that the stock will rise beyond a strike price before expiration; the buyer pays a premium equal to 100 × the quoted option price (each contract represents 100 shares). If right, the buyer may buy 100 shares at the strike no matter how far the stock has run; if wrong, the seller keeps the premium. A put is the mirror-image bet that the stock will fall below the strike — typically bought as insurance by shareholders. Worked example: stock at $175 on May 1; buy the 180 call expiring June 30 (~2 months) for 3.50 = $350. Stock at 190 at expiry → exercise at 180, sell at 190 → $1,000 gross, $650 net (risked $350 to make $650). Stock at 160 → the call expires worthless (no one exercises the right to buy at 180 what trades at 160) and the seller pockets the $350. Put example: own 100 shares of a $60 stock, buy the 50 put for 2.05 = $205; stock closes 42 at expiry → sell shares at 50 instead of 42, saving $800 gross / $595 net of premium; stock closes 68 → put expires worthless.

**Expiration mechanics.** [w_BjFmbwbYA] At expiry the broker auto-exercises any in-the-money option. Stock call ITM: you pay strike × 100 and receive the shares (own the 95 call, stock closes 98 → pay $9,500, receive shares worth $9,800, +$300 unrealized). Options that close out-of-the-money — or exactly at-the-money — simply disappear with zero value. Stock options are American style (exercisable at any time until expiry); index options are European style (exercisable only at expiry) and are cash-settled: an index call pays $100 per point the index closes above the strike, an index put $100 per point below. Example: own a 3150 index call, index closes 3180 → account credited $3,000; own a 2950 index put, index closes 2750 → credited $20,000 per the payout rule ($100 × points ITM; the transcript's own worked example uses a 2950 put with a 2750 close paying $2,000 — note the transcript states the smaller figure).

**Expiration frequency.** [w_BjFmbwbYA] Options originally (1960s onward) expired only monthly on the third Friday; in the early 2000s weekly (every Friday) expirations spread across many stocks and indexes; SPX, NDX and their ETFs (SPY, QQQ) now have daily expirations — giving traders far more granular strategy choices, including same-day (0-DTE) trades. The daily-expiry roster also includes XSP, the mini-SPX index priced at exactly 1/10 of SPX. [t6yuG7KKSKg][Jniwt90PUS4]

**The three drivers of an option's price.** [w_BjFmbwbYA] (1) Strike distance: for calls, the higher the strike above the market the cheaper the option (less likely to be reached); for puts, the higher the strike the more expensive (more protection, more likely to finish ITM). (2) Time: more time to expiration = higher price, for both calls and puts. (3) Volatility: options on volatile underlyings cost more than on quiet ones, all else equal, because spikes are more likely to reach the strike.

**The breakeven hurdle when buying options.** [w_BjFmbwbYA] A bought option makes nothing until the underlying moves past the strike by the premium paid. Index at 1445, buy the 1500 call for 39.50 ($3,950): breakeven is 1539.50 — the index must rally 94.50 points just to break even. If the index rallies to 1590 the call pays $9,000 → +$5,050; if it rallies "only" to 1520 the call pays $2,000 but you still lose $1,950. You can be right on direction and still lose money buying options.

**Leverage: option vs shares.** [w_BjFmbwbYA] Real-stock example: stock at 157, 160 call 30 DTE at 3.00 = $300 risk. Stock closes 177 at expiry → exercise at 160, sell at 177 → $1,700 gross, $1,400 net: risk/reward 4.66:1. To make the same $1,400 with shares you'd buy 70 shares for $10,990 for the same 20-point move — risk/reward 0.127:1 and 36× the capital. Before any directional trade, check the options chain — a call or put may express the same view with far better risk/reward and far less cash. Options can be traded singly or as "complex orders" — multi-leg combinations executed simultaneously on one ticket (spreads, condors, butterflies), which any options-capable broker fills routinely as a single order.

## CHAPTER: The edge of selling options & credit spreads

**Why sellers win 4 of 5 scenarios.** [w_BjFmbwbYA][tOMQNDXnczY] There are only five outcomes for, e.g., an index call: big drop, small drop, flat, small rally, big rally. The call *buyer* loses in the first four (even a rally short of strike + premium loses); he wins only if the rally exceeds the premium-adjusted breakeven. The call *seller* wins in the first four and loses only in the fifth. In the 1445-index example the seller of the 1500 call for 39.50 profits at any close below 1539.50 — the market can rally 94.49 points against his implicit direction and he still wins. This asymmetry — "you can be very wrong about direction and still make money" — is presented as the real edge in options trading, and the reason income sellers achieve abnormally high win rates. Restated at the Las Vegas MoneyShow talk with an ATM example: index at 1900, ATM call sold for 40 — the seller wins in a big drop, small drop, flat, and even a rally up to +39.99; only a rally beyond $40 loses. "Most options contracts expire worthless and the seller pockets 100% of the premium." [tOMQNDXnczY]

**The call-buying failure demonstrated live (May 2024 experiment).** [nvJ_43579z8] The #1 beginner complaint: "I picked the stock's direction right, bought a call, and still lost." Test on the most bullish tape imaginable — SPY, first half of May 2024, S&P +5.3%: each morning buy 5 of the ~20-delta 0-DTE SPY calls (typically ~4 pts OTM; e.g. May 1 open 501.70, 506 call @ 0.59 ×5 = $295). Result over 13 trading days: 3 wins, 10 losses, net −$265 = −13% on a $2,000 account *in a blistering rally*. Losses came from every failure mode: market up but short of strike (May 3: SPY +$6.28 on the day, still a full loss); market closing pennies past the strike but under the premium-adjusted breakeven (May 8: 517 call, SPY closed 517.19, options worth $95 vs $190 paid). Same days traded instead with 5× put credit spreads sold at the first strike below the 40-delta (usually 1–2 points below the open), long put 2 points lower: every one of the 12 trades won — including two days (May 13, 16) where SPY closed below the short put and the spread was bought back before the close for a reduced but still positive result — total +$2,685, >100% return on the same capital. The lesson is conditional, not absolute: slightly-OTM put credit spreads win on ANY day the market closes up, flat, or slightly down; long calls need a large enough rally to clear strike + premium.

**Blunder: buying cheap far-OTM calls as a "strategy."** [FhUcZZB3tmU] The lure: control 100 shares of an $1,810 stock (Priceline, mid-2017) for $435 — the 10-delta 1950 call. That month it happened to work: PCLN closed 1998 at expiry, the call worth ~$48, a 10-bagger (>1,000%). But a 10-delta option expires worthless ~90% of the time; running the same trade the 12 months prior, the 10-delta call expired worthless 11 of 12 months, and the campaign *including* the 1,000% winner still lost ~$2,400 net. The breakeven required a ≥144-point rally (1810 → 1954.35); the stock could rally $4/day for 36 days and the call would still die worthless. Far-OTM long options are a lottery ticket, not a strategy.

**Why traders love credit spreads (the three structural benefits).** [6VPPI-MNUDM] (1) A giant maximum-profit zone: a call credit spread sold at 4120/4130 earns its full $570 credit at ANY close from 4120 down to zero — a "bullish" put credit spread is really bullish + neutral + slightly bearish, since a close exactly at the short strike still wins in full. (2) You can be outright wrong and still win: index enters at 4270 (put credit spread 4270/4260 for $350 credit), closes DOWN at 4268 → short put pays out $200, still +$150 net, because the payout is smaller than the credit. (3) You place the profit zone anywhere: locate the short strike at chart support. Worked example: RUT Mar 10 @ 1772.7 falling toward believed support at 1720; sell the Apr 6 1720 put @ 31.90, buy the 1700 put @ 26.50 → $540 credit; RUT bottomed in that 1700–1725 zone and closed 1754.4 → full win, and any close from 1720 to infinity pays the same. Reference wins: SPX Jun 8 open 4270, 1-month 4270/4260 put credit spread @ 48.25/44.75 → +$350, closed 4412.6; SPX Feb 1, 1-month 4120/4130 call credit spread @ 74.85/69.15 → +$570, closed 3951.3. [6VPPI-MNUDM]

**Why the losses exist and must be accepted.** [MmryR1iu9dA] The only reason anyone buys the put you sell is the genuine fear the stock reaches that level — occasionally it does, and you lose. Losses are the reason the business exists at all (analogy from Freudberg's prior career as CEO of a public property & casualty insurer: without hurricanes nobody would buy insurance and premiums would collapse). Selling options is an insurance business: statistically most contracts expire worthless, occasional claims must be paid, and the whole game is keeping those claims controlled.

**Credit spreads: the built-in stop.** [w_BjFmbwbYA] Naked short options can lose big (an index put seller owes $100/point below strike, unlimited down to zero). A credit spread builds the stop into the structure: sell an option, buy a further-OTM option in the same chain. Put credit spread example: index at 3225, sell the 3200 put for 20 ($2,000 credit). Naked, an expiry at 3120 pays out $8,000 → net −$6,000. Instead also buy the 3175 put for 11 → net credit $900; at 3120 the long put pays back $5,500, capping the loss at −$1,600 instead of −$6,000. Once the index passes the long strike, the long option gains point-for-point against the short — loss capped. A call credit spread is the mirror image (sell lower-strike call, buy higher-strike call) for a bearish/neutral view. Trade-off: less premium than naked selling. Desk rule: SMB's trade desk strongly discourages naked short options — especially overnight, where large gaps make an unstopped short position dangerous; use credit spreads. [w_BjFmbwbYA]

**"75% of all options expire worthless."** [vU64DYL3raU] Freudberg's stat for why the desk prefers selling to buying: 75% of all options actually expire worthless "but they don't tell you that at the CBOE because they want people to buy options." Options are a fear gauge — their values rise on fear and fall on its release (his insurance framing again: insurers of beachfront Florida homes stop writing or charge heavily as a hurricane approaches from Africa; you can't buy fire insurance while the living room burns — protection must be bought upfront, which is why the long wings of a spread go on at entry, never after the adverse move has started). Conditional overnight orders on ES options are no substitute: a gap-and-reverse (his example: the November 2016 US-election night, futures down >100 points, fully recovered and rallying for two months by morning) executes your stop at the worst price while you sleep. [vU64DYL3raU]

**Delta as probability — and the iron-condor PoP formula.** [UrnFowunv-E][-Dfl8YyoP0E][hbkcV1ejzJw] Every professional platform displays delta; 100 − (short put's delta) approximates the probability the put expires worthless — the whole basis of high-probability spread location. For an iron condor the probability of full profit ≈ 100 − (short call delta) − (short put delta): worked example Feb 2 → Mar 17, SPX ~4100s: sell 5× 3825P (Δ12.56) @21.70 / buy 3800P @19.70 and sell 5× 4450C (Δ11.20) @11.05 / buy 4475C @8.70 → +$2,175 credit on $10,325 capital, PoP = 100 − 12.56 − 11.20 = 76.24%; SPX fell ~250 points and closed mid-range → full win, 21% in 45 days, identical payout anywhere in the 625-point 3825–4450 zone. Companion trades from the same video: Jan SPX 3860 → 1-month 3575/3550 PCS (Δ12.6) 5-lot @18.10/15.35 → +$1,375 on $11,125 (12.35%/month, PoP 87.4%), closed 4179.78; ADBE Jan 19 @342.53 with support 320 → sell Mar 17 320P (Δ28.65) @10.20 = +$1,020 cash-secured, PoP 71.35%, closed 358.14 → win. Context: even really solid day/swing traders run 50–60% win rates — the statistical location of short options is what buys options income traders their 70–90%. [UrnFowunv-E]

**The delta trade-off doctrine (which delta to sell).** [YKjnoiKNTLs] The edge in premium selling is probability, not bullishness — options tend to imply more movement than is realized, and the seller harvests the difference like an insurer. As delta rises: premium up, risk up, probability down. Low-delta spreads = frequent small wins, fewer challenged positions, smoother equity curve, but one loss eats many winners; near-the-money (e.g. 45Δ ≈ coin flip) = bigger individual wins, more frequent losses, bigger equity swings. Worked comparison (GE, Apr 23, 29 DTE, 5-wide PCS at chart support): 20Δ → credit $1,020, margin $3,980; 45Δ → credit $2,455, margin $2,545 (larger credit even lowers margin). Both structures are positive theta, negative vega, negative gamma, positive delta — a channeling market pays both, which is why a PCS is "neutral-to-bullish." Rules that determine long-run success: ask "am I being paid enough for the risk?" not "how much can I make?"; size so that no single loss is emotionally disturbing (traders blow up from sizing, not strategy); judge by expectancy (avg win × win rate vs avg loss), not win rate; know the environment — PCS thrives in stable/rising markets with elevated-then-contracting volatility, struggles in rapidly expanding vol, sharp downtrends, rising correlation; and set profit-take, loss-exit and early-exit rules BEFORE entry, never after the trade is already losing. [YKjnoiKNTLs]

**Velocity of capital: close at ~75–80% of max profit and redeploy.** [TpAPTwLMb44] A credit spread's profit is capped at the entry credit; once most of it is earned, the remaining premium is a poor use of capital (same logic as the covered-call 10% buyback rule). Worked example: QQQ Nov 21 2025, open 588.10 sitting on the lower Bollinger Band (bullish signal): sell 10× Dec 4 (13 DTE) 588P @12.67 / buy 583P @10.76 → +$1,910 credit, margin $3,090 (transcript prints "$10,670" for the long-put cost and "$3,90" for margin — by its own prices they are $10,760 and $3,090). Four days later QQQ closed 608.89: 588P @1.64, 583P @1.20 → closing banks +$1,470 = 76% of max in 4 of 13 days. Immediately re-sell the same-expiry spread relocated to the new price: 608P @6.09 / 603P @4.41 → +$1,680 more; Dec 4 close 622.94 → both die → campaign total $3,150 vs $1,910 for passively holding the first spread. [TpAPTwLMb44] The same "≈90% captured → close" threshold appears as standard practice in the RSI call-credit-spread campaign [v_27P1SNZTU] and the RSI put-spread campaign (exit at ≥90% of premium) [t2hTAtI2OxY].

**The cheap-OTM-call arithmetic, restated on ADBE.** [_7Ay68OHOTM] The lure quantified: ADBE @572, the Jul 16 635C costs 0.96 = $96 to "control 100 shares of a $57,200 stock," and if ADBE closed 646 the call returns $1,100 → +$1,004 = >1,000%. But its delta is 6.09 → ≈94% chance of expiring worthless. Run the identical trade 16 times: ~15 losses × $96 = $1,440 burned, so the single winner must return ~1,500% *just to break even*. "The most I can lose is the cost of the option" translates to "the most I can lose is 100% of my investment — and I'll lose it ~94% of the time." Selling that same time premium — winning 94% of the time — is the desk's side of the trade. [_7Ay68OHOTM] (Same lesson as the PCLN campaign [FhUcZZB3tmU].)

**Why over 90% of options traders lose: the three hurdles of option BUYING.** [ic24mZL9Fdk] (1) *Cheap options are cheap for a reason.* TSLA Feb 5 (2024) closed 181.02 at apparent support; the 11-day 205C cost 0.57 ($57) — but its delta was 8.30, so 100 − 8.30 = 91.7% probability of expiring worthless. TSLA rallied >10% to 199.95 by the Feb 16 expiry and the call still died: right on direction, 100% loss. The better side of that trade is to SELL the 8-delta option — always as a credit spread (buy a further-OTM option on the same chain) so the rare in-the-money outcome cannot get out of hand. (2) *The premium is a hurdle even when the direction, strike and timing are all right.* Same stock, the 18-day 190C at delta 33.53 cost 3.70 ($370; ≈66.5% chance of expiring worthless); TSLA closed 191.16 — past the strike — yet the call was worth only 1.16 → sold for $116, a $254 loss. Breakeven was 193.70: if that hurdle is not realistically reachable before expiry, buying the call is a bad trade and selling it (again as a credit spread) is the better one; any analysis that ignores the option's own cost is a mistake. (3) *Implied volatility — the "V crush".* AAPL Nov 2 2023 closed 177.57 with earnings after the bell; the next-day 177.5 straddle cost 3.40 (call) + 3.18 (put) = $658. Next morning the stock was BELOW the strike, yet the put had fallen to 3.04 and the call to 0.24: once the mystery is resolved, sellers no longer need to price in a big unknown and the whole chain deflates. AAPL closed 176.50 → put worth 0.85 → the straddle lost $573. The options market prices the earnings straddle well; many traders take the other side (selling that straddle would have made ≈$573 — the transcript prints "$578"), but selling it naked is reckless — buy the outer call and put to form an iron butterfly so a massive earnings move cannot become an unbounded loss. [ic24mZL9Fdk]

**The spread-width tweak: the CLOSER the long strike, the better the trade.** [66lbCWsfnyA] Counter-intuitive but structural: for a fixed amount of capital a credit spread whose long option sits close to the short option beats a wide one — you pay far more for the protection per spread, but each spread risks so much less that you can sell many more of them inside the same broker requirement. SPX, Jul 12 2023 (index opens 4478.25 after a 670-point rally since March), 7-day chain expiring Jul 19, the same 4475 short put in all three versions. **50-wide:** sell 10× 4475P @22.70 (+$22,700), buy 10× 4425P @8.55 (-$8,550) → credit $14,150, requirement $35,850 — which is exactly the max loss (at a 4400 close the shorts pay $75,000, the longs return $25,000, net -$35,850, and it is frozen there at any close at or below 4425, because from that point the long puts reimburse dollar for dollar). **25-wide:** 21 spreads at 4475/4450 → credit $18,165 (shorts $47,760, longs $29,595) on a SMALLER requirement of $34,335. **5-wide:** 110 spreads at 4475/4470 → about $22,000 of credit on $33,000 of capital, the lowest requirement of the three. SPX closed 4565.72, so all three won in full: 39% vs 52% vs 66% return on capital. Rule: do not try to minimise the cost of your protection — with credit spreads the long strike closest to the short strike almost always delivers both the highest return and the lowest risk. [66lbCWsfnyA]

**The spread-width principle confirmed on a one-day signal trade (SPX, March 5).** [j0laz0Ks5F8] Same short strike, three geometries, identical gross risk — the narrower-and-more-lots version wins on both sides of the ratio. The SMB × InvestiQuant one-day signal called for a close above the open; SPX opened 3802 and the trade is a put credit spread with the short put at 3800. (a) **1 lot, 20 wide**: sell 3800P @19.56 (+$1,956), buy 3780P @12.43 (−$1,243) → +$713 credit, max loss $1,287, reward-to-risk 55.4% (the audio says "54"). (b) **2 lots, 10 wide**: sell 2× 3800P (+$3,912), buy 2× 3790P @15.64 (−$3,128) → +$784 credit, max loss $1,216. (c) **4 lots, 5 wide**: sell 4× 3800P (≈+$7,800), buy 4× 3795P (≈−$6,900) → +$852 credit, max loss $1,148, reward-to-risk 74.2%. The gross payout if the index sinks through the long strike is $2,000 in every version (lots × width × 100), so paying up for closer longs raises the numerator and cuts the denominator at the same time — "in almost all cases you're better off selling more spreads with a smaller width than fewer spreads with a greater width." SPX closed 3841 that day → everything expired worthless and the full credit was kept. [j0laz0Ks5F8]

**Sell put credit spreads INTO the volatility spike, not after it (the apples-to-apples proof).** [IsuWqXxvjeA] Two SPX trades one month apart, same strikes, same 50-point width, same 2 lots, both entered at nearly the same index level — only the VIX differs. **High-vol version:** Dec 18 2024, the FOMC press conference in which Powell cast doubt on the pace of 2025 rate cuts; SPX sold off from a 6047 open to close 5872, down more than 178 points (≈3%), landing on the support that had held since early November (the transcript garbles that level as "50875"), while the VIX rose 74% on the day. On the Jan 17 chain: sell 2× 5700P @70.35 (+$14,070) / buy 2× 5650P @61.55 (−$12,310) → +$1,760 credit and a broker requirement of $8,240 (the $10,000 width minus the credit; the audio garbles the sale proceeds as "$114,700"). Jan 17 SPX closed 5966 → both puts worthless → +$1,760 = a 21% return in a month. **Normal-vol control:** Nov 15 2024, SPX closed 5870 — almost exactly the same index level — but on a day down only ~79 points, with the VIX moving merely 14.31 → 16.14. Same 5700/5650 structure on the Dec 16 chain: @33.75 and @27.30 → only $1,290 of credit, i.e. $470 less — and therefore $470 MORE capital required ($8,710, +5.7%), because the broker's requirement is the width minus what you took in. It also won (SPX 6074 at the Dec 16 expiry; the audio prints "6748"), but for 14.8% (spoken as "148%"). Doctrine: a VIX spike inflates the nearer short put more than the further long put, so the same structure pays a bigger credit, ties up less capital and returns more on less risk — provided there is an actual reason to expect a bounce (a defined support area), not merely fat premium. [IsuWqXxvjeA]

## CHAPTER: Covered calls

**The base strategy.** [w_BjFmbwbYA][U8gFC00kZ58] Own 100 shares, sell a call against them at or above the current price at a fixed interval (monthly/quarterly). Two outcomes: stock closes below the strike at expiry → keep the premium, reload; stock closes above → shares are called away at the strike, and you still keep the premium. Income illustration: 100 shares of a $200 stock ($20,000) paying a 1.5% dividend ($300/yr — roughly the S&P 500 average of 1–2%); sell the one-year 220 call for 17 → $1,700 premium + $300 dividend = $2,000 = 10% cash yield, a >500% improvement over the dividend alone. If the stock closes above 220 (e.g. 228.91) shares are called away at 220: total year = $1,700 premium + $300 dividend + $2,000 capital gain = 20% on the position. Caveats: above the strike all further upside is forfeited while full downside of stock ownership is retained; called-away shares may trigger capital-gains tax — check with a tax accountant before running a covered-call program. [w_BjFmbwbYA]

Three professional keys that can double or triple conventional covered-call returns [U8gFC00kZ58]:

**Key 1 — Don't squeeze the last penny: buy calls back early at ~10% of the sale price and reload.** [U8gFC00kZ58][LWLFq1cMOdo] Baseline (sell-and-expire): investor with 300 AAPL shares, Dec 17 2021, stock ≈171.50 (AAPL yields barely 0.5% in dividends vs the S&P average 1.71% [LWLFq1cMOdo]); each quarter sell 3 of the 170 calls in the next quarterly chain. March calls sold at 11.43 → $3,429; upon March 17 expiry (AAPL ≈160) reload June 170 calls for $1,905 credit; continuing all four quarters produced $6,549 for the year (the retelling in [LWLFq1cMOdo] confirms the figure the [U8gFC00kZ58] transcript garbled as "654"; the final two quarters brought in little because AAPL traded well below 170) — still far better than AAPL's $273 of dividends on those shares in 2022, and it pays a "supplemental dividend" four times a year. Improved technique (sell-and-buyback): identical start, but buy calls back whenever they shrink to ~10% of the sale price, no matter how fast, then immediately re-sell the next available monthly. Example sequence: Feb 24 2022 AAPL gapped down to open 152.94 → March 170 call bought back at 0.69 → +$3,222 on that leg; a week later (Mar 2) AAPL bounced above 166 → sell May 170 calls (≈8.05, $2,415 credit) a month earlier than the expire-and-wait approach would allow; May 3 (17 days before May expiry) AAPL back under 160 → buy back again at ~10% of sale price. Full-year result: over $10,000 of option profit — 64% more than sell-and-expire — with 6 trades instead of 4. The per-trade average profit is only slightly better; the edge is the higher *frequency* of reloading (one trade lasted just 15 days after a lucky post-sale selloff; conversely the August calls never got cheap and were closed at expiry for a mere $60 gain — both outcomes are normal). Principle: letting a short call you've already squeezed 90% of the value out of languish for the last 10% is a poor use of capital. [U8gFC00kZ58][LWLFq1cMOdo]

**Key 2 — The synthetic covered call: replace the shares with deep-ITM calls.** Instead of buying stock, buy deep in-the-money longer-dated calls and sell the short-term OTM calls against them. Example: gold-royalty stock FNV, Jan 28 2022, trading 127.17, thesis: support ~125, resistance ~150. Buying 1,000 shares would cost $127,170. Instead: buy 10 of the July (≈6 months out) 100-strike calls at 29.30 (≈$29,300–29,400 — transcript rounds inconsistently) and sell 10 of the February (≈3 weeks out) 150 calls at 0.38 (+$380) → net outlay ≈$28,920. Feb expiry: FNV closed 147.77, short 150 calls expire worthless; re-sell 10 March 150 calls at 4.77 (+$4,770) → net cost down to $24,150. Mar 18: FNV closed 154.34 — above 150, so close the whole position (stock ≈154.60, the July 100 calls sold ≈54.60). Outcome: the option structure made over $30,000 vs $27,430 for the shares — more profit on less than a quarter of the capital, so the percentage return is several times the shares' 21.56% (the transcript garbles the option-side return as "10.29%"; by its own numbers it is ≈102.9%+). Rule: every time you consider a covered call, check whether deep-ITM calls beat owning the shares. [U8gFC00kZ58]

**Key 3 — Always sell the call at your price target, not at the juiciest premium.** [U8gFC00kZ58] Vivid example: TSLA, Jan 20 2023, stock 127.89 after a >75% fall from the 402.67 high; trader's mid-year target: 200. On the July 2023 chain the highest-premium OTM call is the 130 at 23.75 ($2,375); the call at the 200 target pays only 5.72 ($572). July 21 expiry: TSLA closed 260.02. The 130-call seller: shares called at 130 → only ~$211 share gain + $2,375 premium = $2,586 total. The 200-call seller: $7,211 share gain + $572 premium = $7,783 — triple. If you have a meaningful price target, capping yourself below it for extra premium almost always costs you money. This is the same principle stated in the basics course: set the covered-call strike where you'd be genuinely happy to sell the shares, making the trade a win-win either way. [w_BjFmbwbYA]

**A whole-portfolio covered-call program.** [XQ9OSsOra5s] Scale the idea to an investment portfolio: 8 stocks chosen to represent >90% of S&P 500 sectors (AAPL, ISRG, Goldman Sachs, Motorola, etc.), 100 shares each, total cost $163,400, natural dividends ≈$2,200/yr = 1.4% yield. Program: each month, 30 days before the monthly expiration, sell 1 call per position ~5% above the market (example: Motorola Sep 19 @ 168 → sell the Oct 18 175 call @ 1.66 = $166). Across all 8 stocks that one month brought in ≈$2,000 — about what the dividends pay in a *year*. Repeated 12 months: >$24,000 = 15.1% option yield, plus the dividends still collected → >$26,000, more than 10× the dividend-only income.

**The XOM campaign and the synthetic upgrade (quadruple the return).** [7a0BRIAufBA] Conventional: Jun 17 2022, XOM pulls back to ≈86; buy 1,000 shares ($86,090) and sell 10× Jul 97.5 calls @ 0.75 (+$750). July: XOM closes 84.54, calls die; reload monthly ~1 month out: Aug 95C @ 0.76 (+$760, close 94.03), Sep 100C @ 1.25 (+$1,250, close 93.26), Oct 105C @ 0.72 — Oct 21 XOM closes 105.86, shares called at 105 (+$105,000 in). Re-buy 1,000 shares ($105,860 — the campaign's peak capital) and continue: Nov 115C (worthless), Dec 120C @ 1.13; Dec 16 close 104.70, sell shares, done. Six-month profit $23,390 on $105,860 = 22.1%. Synthetic version, same dates: instead of shares buy 20× Jun 2023 75-strike LEAP calls @ 17.66 ($35,320) and sell 20× (not 10) of the monthly calls against them — first sale +$1,500, net risk $33,820; the doubled lot size doubles every month's call income; October's ITM calls are simply bought back @ 0.98 (−$1,960) since there are no shares to assign; wrap up in December by selling the LEAPs @ 31.60. Final profit $37,300 → 105.6% in six months — more than 4× the conventional return, on ~40% of the capital, with less absolute risk than share ownership. [7a0BRIAufBA]

**Synthetic covered call on SPY (the 25%-capital version).** [Wpl3VI2FTio] Jan 20 2023, SPY 395. Conventional: buy 100 shares ($39,500), sell the May 425 call (~7.5% OTM) @ 5.35; May 20 close 418.62 → call dies, +$2,897 to date; sell the Sep 450 call (again ~7.5% above) @ 0.31; Sep close 443.37 → final profit $5,673 = 14.67% in ~8–9 months (≈22% annualized). Synthetic: replace the shares with 1× Jan 2024 310-strike deep-ITM LEAP (85 points ITM) @ 101.36 = $10,136; sell the same 425 and 450 calls; the deep-ITM LEAP appreciates nearly point-for-point with the stock (118.49 by May, 138.26 by September). Final profit $4,526 on $9,300 net cost = 32.7% (transcript's decimals garbled) — more than double the conventional return on <25% of the capital. Rule of thumb across all three synthetic examples (FNV, XOM, SPY): whenever you'd write a covered call, price the deep-ITM-call replacement first. [Wpl3VI2FTio][7a0BRIAufBA][U8gFC00kZ58]

**The five deadly covered-call mistakes.** [CP_euDwExN0] Baseline mechanics reminder (AMZN example): buy 100 @ 105 ($10,500), sell the 1-month 110 call @ 3.50 → +$350 = 3.33% cash in a month; stock at 111 → assigned, +$500 shares +$350 premium = $850. The mistakes: **(1) Selling covered calls on a stock you're bearish on.** The only real risk of a covered call is the stock falling: stock to 90 → keep $350 but lose $1,500 on shares, net −$1,150. Covered calls are a neutral-to-bullish strategy, full stop. **(2) Staying in the campaign after you've turned bearish** — monthly premium is addictive; ask yourself at every reload "am I still neutral/bullish?"; if not, close the whole position. **(3) Selling a call below your price target on a stock you're super-bullish on.** CMG Jul 1 2021 @ 1538: selling the juicy 1-month 1550 call @ 47.06 (+$4,706) capped the trade at $5,966 when CMG ran to 1863.44 — plain shares would have made $32,604; $26,638 left on the table. If you're super-bullish, don't write the call at all (the extreme case of Key 3 above). **(4) Selling a call below your share acquisition price after a selloff.** TSLA Dec 1 2022 @ 194.70, sell Dec 200C @ 10.12; TSLA crashes to 123.18 (call dies, +$1,012); reloading at the new price — Jan 130C @ 9.02 — locks disaster: TSLA bounces to 177.90, shares called at 130, campaign net −$4,556. The floor for any reload strike is your original share cost; if the call there pays too little, either wait for a bounce or go out 2–3 months where the premium at that strike is decent. **(5) Writing covered calls on a long-held position with a huge embedded capital gain.** 100 CMG bought 2008 @ 100, now 1728 (+$162,800 unrealized): selling a 1-month 1800 call for $3,600 risks assignment that realizes a $170,000 gain → ≈$30,000 long-term capital-gains tax bill at the top US bracket — for $3,600 of premium. [CP_euDwExN0]

**Mistake 4 replayed on NVDA — the arithmetic of "never below your basis."** [RmtEzjn4Vh0] Jun 28 2024, NVDA 123.62 (up >1,000% in 21 months): buy 400 shares ($49,448), sell 4× Jul 12 124C @ 4.70 (+$1,880). Jul 12 close 129.24 → assigned at 124: +$152 shares +$1,880 premium = +$2,032 in 2 weeks. Reload at 129.24: 400 shares + 4× 130C @ 4.65. NVDA slides: close 113.06 (calls die, running +$3,893); greedy path sells 4× 114C @ 4.52 right above the market (+$1,808, running +$5,700 after they die at 104.75), then 4× 105C @ 4.75 (+$1,900) — NVDA then rips back to 129.37 and the shares get called at 105: −$9,696 on shares (bought 129.24 ×400; transcript prints "969"), wiping out all premium — the campaign ends negative. Disciplined path from the same spot: after the drop below basis, sell only the 130 strike (the acquisition price): @ 0.47 (+$188), then @ 0.14 (+$42) — tiny premiums, but when NVDA closed 129.37 the shares exit near breakeven and the campaign ends +$4,175. Note the desk observation that ~2-week ATM NVDA calls consistently priced ≈$4.50–4.75 regardless of level — high-vol stocks reload rich premium every cycle. [RmtEzjn4Vh0]

**Income-goal vs price-target campaigns (the WMT case).** [Vm0qcsR5-E4][AtSAFHA2Hvc] Chasing a fixed monthly dollar goal forces the strike so close that shares are repeatedly called away and re-bought higher, skipping chunks of the up-move. Income-goal version: Mar 2 (2022 per the chart narrative; transcript says "March of this year"), buy 1,000 WMT @130.11 ($130,110), goal ≈$2,000/month → sell 10× Apr 1 133C @2.01 (+$2,010); Apr 1 WMT >135 → called @133; re-buy @135.62, sell 10× Apr 30 137C @2.25 (+$2,250); called again @137 (WMT >139) → campaign +$8,530 so far; re-buy @139.91; May and June calls die (+$260, +$1,850); late June sell Jul 23 139C @1.84; WMT 142.43 → called @139; re-buy, sell 144C @2.32; Aug 20 WMT 151.54 → called @144 → final ≈$17,026 (transcript prints "17,26"). Price-target version, same start: decide the exit is the retest of the ~150 all-time high and sell ONLY the 150 strike every month — premiums are small ($240 the first month; $100–$800/month range) but the shares are never interrupted; WMT crosses 150 in August, shares exit at the target → >$22,000 total, beating the income-first campaign despite collecting far less premium per month. Selling the call at the price target doubles as enforced profit-taking discipline. (Campaign-level restatement of Key 3 / mistake #3.) [Vm0qcsR5-E4][AtSAFHA2Hvc]

**Quarterly covered calls on a bond ETF, and the 30-lot synthetic upgrade (TLT).** [k-VJZ95j7ec] Conventional: Feb 2024, buy 1,000 TLT @92.76 ($92,760; TLT pays a monthly dividend) and sell 10× 92C 91 DTE @3.42 (+$3,420) → net outlay $89,340. May 17 close 91.39 → calls die, +$3,420. Reload 92C Aug 16 @2.18 (+$2,180); Aug 16 close 97.44 → called @92 → trade nets +$1,420; re-buy @97.44 ($97,400). Nov: 92C @6.60 (now ITM-rich) → +$6,600, close 90.80 → keep. Feb 2025: 92C @2.14 → +$2,140, close 89.61; the re-bought shares carry a −$7,830 loss (97,400 → 89,610) → option/share net $5,750, plus the year's dividends → ≈$9,176 total (transcript garbles "$99,100 76"). Synthetic version, same dates: instead of shares buy 30× Feb 2025 81C (>11 points ITM) @14.13 ($42,390) and sell 30× 92C @3.42 (+$10,260) → outlay $32,130 — 64% less capital. May: +$10,260. Aug: 30× 92C @2.18 (+$6,540) but TLT closes 97.44 → buy the shorts back @5.40 (−$16,200) → trade −$9,660. Nov: 30× 92C @6.60 = +$19,800 → all kept. Feb: 30× 92C @2.14 = +$6,420 kept; the 81-strike longs expire with a loss; final +$10,920 — more profit than the conventional campaign on roughly a third of the capital. Keep short calls = long calls in lot count whatever size you trade. [k-VJZ95j7ec]

**The dividend-replication synthetic (SPY 2019).** [f9pJ-V2vqww] Deep-ITM LEAP + tiny monthly calls engineered to replicate the dividend: Jan 2 2019, SPY 250.20; instead of 100 shares ($25,020) buy 1× Jan 2020 130C deep-ITM @120.99 ($12,099); each month sell the ~$0.20 call 10–15 points OTM (Jan 270C @0.20 → +$20; Feb 283C @0.20; …) — ~$20/month ≈ $252/year ≈ 2% on the call's cost, matching SPY's ~2% dividend. Every monthly call expired worthless in 2019's rally (Jan close ~267 vs 270 strike, Feb ~279 vs 283…). Year end: SPY 321.13 — shares route +$7,093 + ~$500 dividends = $7,593 = 30%; call route: LEAP appreciated to 191.40 → +$7,300 + $252 = ≈$7,550 on $12,099 = 62% — same dollars, less than half the capital and risk. [f9pJ-V2vqww]

**A 1%-per-month covered-call campaign on a non-dividend growth stock (BKNG 2022).** [X5bFm3sWqkA] Rule of the campaign: every month sell the call whose premium equals ~1% of the share investment (on BKNG that strike sat ~115 points above the market). Jan 4 2022, BKNG 2466.52 (recovering off its December lows): buy 100 shares ($246,652), sell the Jan 2580C @25.30 (+$2,530); Jan expiry close 2412.94 → keep. Feb: 2670C @25.25 (+$2,525); Feb 25 close 2281.46 → keep. Every month through September pocketed ~$2,500. October trade (entered Sep 30 with BKNG down at 1654): sell the 1830C @25.15 (+$2,515); in the last 30 minutes of expiration day BKNG traded 1867.63, above the strike — to keep the shares the call was bought back @40.40 (−$4,040; the ≥$37 discount it conferred), and the campaign resumed with the Nov 2060C @26.45 (+$2,645) and a December call. Year: +$26,701 of cash flow = a 10.8% "dividend" vs the S&P's ~1.5% average yield — from a stock that pays nothing. (Note the campaign broke the "never below your basis" rule of the five-mistakes video when it sold the 1830 strike against shares bought at 2466 — it survived only by buying the ITM call back rather than letting the shares go.) [X5bFm3sWqkA]

**The poor man's covered call as a monthly 10-delta campaign (COST 2023).** [iwE_tI6foJs] Synthetic covered call for the trader who cannot afford 100 shares of a high-priced stock: end of 2022, Costco ≈−20% on the year, 100 shares = $46,145 vs a $10,000 account. Structure: buy the deep-ITM one-year LEAP the broker accepts in lieu of shares — Jan 2024 410C @96.90 ($9,690, chosen as the deepest strike under the $10k budget) — and each month sell the ~10-delta call on the next third-Friday chain: Jan 2023 510C (Δ10.72) @1.74 (+$174); Jan 20 close 465.11 → keep. Feb: 515C (Δ12.04) @1.56 (+$156); close 492.48 → keep. Six straight monthly wins in the first half (80–90% probability trades by construction). July: the short 555C (sold @1.27) closed ITM at 557.86 → buy it back (−$210 on that leg) AND sell the LEAP, now 159.72 vs 96.90 cost → +$6,282; reinstate with the Jan 2024 480C @96.05 (shares by then $55,000+ = >5× the account) and resume: Aug 585C @1.32, Aug–Nov all expired worthless. December: 620C sold @1.55 closed ITM at 658.82 → buy back @38.78 (−$3,723) and cash the 480C @181.35 → +$8,530 (transcript prints "$853"). Year: +$12,390 (transcript prints "1,390"; the itemized legs and the stated $10,000 → $22,390 = +123.9% confirm) vs COST +49% — positive cash flow every single month, the LEAP leveraging the stock's gain. The mechanism: the deep-ITM LEAP counts as the 100 shares in the broker's risk system. [iwE_tI6foJs]

**Call diagonals as a monthly income campaign (TLT, "rolling call options for a living").** [PrsUnhNjF4Y] Campaign design anchored on third-Friday chains: each month sell the call at the first strike ABOVE the close on next month's chain and buy a deep-ITM call ~11 points below that strike expiring ~a year out (the long is re-bought each month with the strike stepped up to keep costs "apples for apples"). Jan 17 2025, TLT close 87.19 (sliding since Sep 2024 on inflation/Fed uncertainty): sell 10× Feb 21 88C @1.18 (+$1,180), buy 10× Jan 2026 76C @12.55 ($12,550) → net $11,370. Feb 21 close 89.61: 76C → 14.52 ($14,520), 88C → 1.60 at expiry (pure intrinsic; −$1,600) → +$1,550 = 13.6% in ~5 weeks. Mar: 10× Mar 21 90C @1.13 / Jan 2026 78C @12.85 → net $11,720; Mar 21 close 90.70: 90C → 0.69, 78C → 13.57 → +$1,160. Apr: 10× 91C @1.16 / Jan 2026 80C @11.93 → net $10,770; TLT fell to 87.53 → the 91C expired worthless (+$1,160 realized) while the 80C sat at 9.82 — the rule for a down month: do NOT sell the long; keep selling the same strike month after month until a month closes ITM, when the long recovers and the whole diagonal is sold at a profit. Realized over the three months: +$3,870 on average capital $11,287, each month >$1,000; every month is certain to realize cash one way or the other (short calls dying, or the whole diagonal sold). The diagonal is a covered-call variant and "one of the most capital-efficient methods for producing monthly income." [PrsUnhNjF4Y]

**The diagonal beats the covered call on return (PSX, the under-$3,000 version).** [W5Gl_E2Sq-A] Apr 4 2025, tariff selloff: PSX had dropped from ~130 to close 98.81 with RSI 21 (deeply oversold). Covered call: 100 shares + sell the Jun 20 120C @2.10 → $9,671 outlay; Jun 20 close 124.78 → shares called @120 → +$2,329 = 24%. Diagonal (synthetic covered call): sell the same Jun 20 120C @2.10, buy the Mar 2026 80C (~20 pts ITM) @24.70 → cost $2,260 (<25% of the covered call); Jun 20: buy back the 120C @4.70 (no shares to deliver), sell the 80C @46.45 → +$1,915 = 84%. Less profit in dollars, on a quarter of the capital, and available to the $3,000 account that could not make the covered-call trade at all. [W5Gl_E2Sq-A]

**Covered call vs 3-lot call debit spread (SPY, Jan 2023) — 10× the return.** [9j-MhX4j6cs] Same premise as the CMG problem (100 CMG shares @2065 = $206,500). Jan 20 2023, SPY 395 (2022: −20%; dividend yield ~1.55%). Covered call: 100 shares $39,500 + sell the May 420C @7.02 → net $38,798; May expiry close 418.62 → shares $41,862, call dies → +$3,064 = 7.89%. Debit-spread mimic: buy 3× May 390C (5 pts ITM) @22.93 ($6,879), sell 3× May 420C @7.02 ($2,106) → $4,773 (≈12% of the covered call's cost); expiry: 390C = 28.62 → $8,586, 420C worthless → +$3,813 = 79.88% — more dollars AND >10× the percentage return. Trade-off: if SPY had fallen, the debit spread loses more than the covered call. [9j-MhX4j6cs]

**Rolling a covered call the pro way: the 80%-decay buyback and the "double dip" (WMT 2025).** [WDbHqMeSCHA] Third Fridays are the reliable anchor for multi-month campaigns (every chain has at least a third-Friday expiry). Baseline: Feb 21 2025, WMT close 94.78 (dividend yield <1%): buy 500 shares ($47,390), sell 5× May 16 97.5C @3.20 (+$1,600) → net outlay $45,790. May 16 close 98.24 → shares called at 97.50 ($48,750) → +$2,960. Pro rule: if the call's premium drops MORE THAN 80% from its sale price, buy it back. Mar 18 (tariff scare), WMT 85.59: the 97.5C quoted 0.61 (<20% of 3.20) → buy back, banking $1,295 of the possible $1,600 (transcript prints "$12.95"; 80% of the potential captured) while still holding the shares. Two paths from there: WMT never regains 97.5 → you keep the $1,295 and the 500 shares; or it bounces — May 2 (tariff pause), WMT 98.75: the same 97.5C now trades 3.57, MORE than the original sale → re-sell 5 for +$1,785. May 16 assignment at 97.50 as before → total +$4,440, 50% more than sell-and-expire, from two premiums on one share position. Principle: when the remaining potential profit has become a small fraction of the original, close for most of it and stay set up for the reload. (Same "don't squeeze the last 10–20%" rule as Key 1 above, stated as a hard >80%-decay trigger.) [WDbHqMeSCHA]

**The five-rule covered-call checklist (2025 restatement, new worked examples).** [DQ6nTpng7MM] Process, not prediction: (1) *Only on stocks you are fundamentally bullish on long-term* — the real risk is the stock going down and staying down. PSX Jul 1 2024 close 140.93 (−20% from its 174.0 April high): 100 shares + sell the Dec 20 150C @6.65 → net $13,428; Dec 20 close 110.37 → the call died but the position lost $2,391; the premium is dwarfed by a tanking underlying. (2) *Sell the strike where you would be happy to sell the shares (fully valued).* TSLA Apr 9 2025 close 272.10 (market-wide tech selloff): the juicy 3-month 275C @33.55 (net cost $23,855) vs a chart-target 330C — the level of Feb 24, six weeks earlier, still >100 points under the 439 year high — @14.02 (net cost $25,808). Jun 20 close 322.16: 275 route → called at 275 → +$3,645; 330 route → shares sold at 322.16 (transcript "32616") → +$6,408. Less premium, far more profit. (3) *Never write calls against a huge embedded gain unless you truly want to realize it* — TSLA bought Apr 1 2020 at a split-adjusted 29.76 (basis $2,976): assignment at 275 realizes $24,524; at a hypothetical 15% rate that is $3,678.60 of tax, more than the $3,355 call premium (consult a tax professional). (4) *Never sell a reload call below your original share cost.* QQQ Jan 2 2025 close 510.23: 100 shares + Mar 31 515C @19.60 → outlay $49,063; Mar 31 close 468.92 → call dies; reloading "right above the market" with the Jun 30 470C @23.13 is the trap: Jun 30 close 551.64 → called at 470 → the six months net only ≈$250 (transcript "$240 bucks"). Reloading at the basis strike instead — Jun 30 515C @4.55 — ends at +$2,892 (transcript "28.92"), >10× as much. (5) *If the call at/above your basis is worth almost nothing, don't sell it — wait.* AMZN Feb 18 2025 close 226.65: 2-month 230C @8.60 (+$860); Apr 17 close 172.63 (tariff selloff, −23%); the Jun 20 230C now fetches 0.36 = $36 for two months — "ridiculous" to cap AMZN for that; wait: May 13, AMZN 211.37, the Jul 18 230C pays 3.50 = $350, ~10× as much less than a month later. Covered-call trading is not robotic. [DQ6nTpng7MM] (The 2023 five-mistakes list [CP_euDwExN0] is the same doctrine with the CMG/TSLA/AMZN 2021–22 examples.)

**The monthly SPY buy-write at the "½%-of-price" call (Sep 2023 → Sep 2024).** [weUoHkMBL4A] For smaller accounts SPY (≈1/10 of SPX, options ≈1/10 the price) is the affordable whole-market vehicle. Protocol on each third Friday: own 200 shares; on next month's third-Friday chain sell the HIGHEST-strike call whose price is at least one-half of one percent of SPY's price, one call per 100 shares (a "buy-write" — bullish-to-neutral). Sep 15 2023, SPY 434.37 (mild pullback since July) → 2× Oct 20 455C @2.22 (+$444); Oct 20 close 421.19 → calls die, +$444. Nov: 2× 438C @2.14 (+$428); Nov 17 close 450.79 → shares called at 438 → trade +$1,154 (share gain vs the 434.37 cost + premium). Dec: re-buy shares (≈450.79; transcript "4579"), sell 2× 460C @2.29 (+$458); Dec 15 close 469.33 → called at 460 → +$2,300. Jan: 480C; Jan 19 close 482.43 → +$2,644. Feb: 492C; Feb 16 close 499.51 → +$2,466. Mar: 510C @2.66 → SPY fell just short, calls die (+$532). Apr: 525C @2.69 → die (+$538). May +$3,216 and Jun +$2,840 (assigned both months); Jul +$566 and Aug +$588 (calls only); Sep: calls die, and the shares bought in June at 544.09 are sold at the Sep 20 close 568.20 for +$4,832 to close the year. The transcript's stated full-year total "$2,534" is inconsistent with its own monthly legs, which sum to ≈$22,000+ — flagged. Every single month produced at least the call premium; assignment months added realized share gains; SPY's dividend comes on top. [weUoHkMBL4A]

**The covered strangle: sell a call above AND a put below against shares you own.** [pyjOcisjrTU] For a dividend investor who wants materially more cash flow than the stock itself pays: hold the shares, sell one call per 100 shares no closer than ~5% above the market, and simultaneously sell the same number of puts no closer than ~5% below, in the same expiration. PEP, Jan 19 2023, stock opens 171.28, 1,000 shares held: the coming year's dividends are $4.95/share = $4,950 = 2.89% (better than the S&P 500's 1.32% average yield, but barely half of the >5% money-market funds paid at the time). Instead sell 10× Jan 19 2024 180C @10.45 (+$10,450) and 10× 160P @7.60 (+$7,600) → $18,050 into the account on day one. PEP drifted lower and closed 165.78 a year later → the calls are worthless (no value in the right to buy at 180) and so are the puts (no value in the right to sell at 160) → keep the whole $18,050, which together with the $4,950 of dividends is $23,000, more than quadruple the dividend-only income. Both obligations must be genuinely acceptable BEFORE entry: the shares WILL be called away at 180 however far the stock runs, with whatever capital-gains tax that triggers — if you are not ready for that, pick a higher call strike and accept less premium; and $160,000 of cash must stand ready to buy 1,000 more shares if PEP closes below 160 — if not, pick a lower put strike, again for less premium. [pyjOcisjrTU]

## CHAPTER: Cash-secured puts & the wheel

**Cash-secured put: get paid to wait for your buy price.** [TOc1XyCu83I] Pick a stock you'd genuinely be happy to own at a support level, and sell puts there. Example: XOM Jun 1 2023 @ 101.56, sliding toward reliable 97–99 support that produced multiple bounces since Oct 2022. Sell 5× Jun 30 99 puts @ 2.18 → +$1,090 cash immediately; broker requires $49,500 (the cash to buy 500 shares at 99 if assigned — hence "cash-secured"). Jun 30 close 107.25 → puts die, keep $1,090 = 2.2% on the secured cash in a month; repeated monthly ≈26.4%/yr (≈$13,080). Win-win logic: either you keep the premium, or you're put the shares at a price you already decided was a good long entry. Attributed to Warren Buffett's practice. [TOc1XyCu83I]

**The wheel: a full year on SPY.** [Kg0ts5NGr0o] Premise: SPY long-term always eventually takes out its all-time highs, so being assigned SPY at a modest discount is a survivable event. Goal $1,000+/month on cash income. Protocol: each month sell 3 SPY puts ~2% below the market, 1 month out; if assigned, switch to selling 3 calls *at the assignment strike* (never below — same basis rule as covered calls) until the shares are called away at breakeven, then resume puts. The year (Nov 2022–Nov 2023): Nov 1 2022 SPY 384.52 → 3× Dec 375P @ 6.70 (+$2,010; transcript prints "$210"/"2,110" — 6.70×300 = $2,010); Dec close 406.91, expire. Dec → 3× 400P @ 6.44 (+$1,932); Jan 6 close 388.08 → assigned 300 @ 400. Feb: 3× 400C @ 4.79 (+$1,437); Feb 10 close 408.04 → called at 400, shares flat. Mar: 400P @ 5.14 (+$1,542) → assigned again; Apr: 400C @ 2.79 (+$837) → called away Apr 10 @ 409.19. May–Aug puts all expired worthless; Oct: assigned 300 @ 435; Nov: 3× 435C @ 7.79 (+$2,337); Nov 17 close 450.79 → called at 435. Campaign total $15,771 ≈ $1,300+/month average, all from premium, shares always exiting at breakeven. [Kg0ts5NGr0o]

**A low-capital wheel substitute (credit spreads + long-dated calls).** [4d6qj5vtrBQ] The classic wheel needs assignment-level cash; this variant produces the same alternating rhythm on a fraction of it — QQQ, summer 2023 (QQQ +34% YTD by early June). Income phase: every Friday sell a 25-point-wide put credit spread expiring the next Friday, short put chosen at a price ≈$0.60: Jun 2 QQQ 354.65 → sell 10× 346P @ 0.65 (+$650), buy 10× 321P @ 0.06 (−$60) = +$590/week on ≈$24,410 of margin (transcript prints "$4,410" — a 10-lot 25-wide risks $25,000 minus credit; scale the lot count down to fit any account). Weeks repeat at ~$500+: Jun 9 close 354.50, Jun 16 close 367.93 (that week +$530: 342P @ 0.61 / 317P @ 0.08)… all June–July trades expired worthless. Loss + recovery phase: Jul 28 trade (373P @ 0.59 / 348P @ 0.05, +$540) ends with QQQ below 373 → close the spread minutes before expiry (buy back 373P @ 1.02, sell 348P @ 0.01) → −$470 net on the week. Immediately switch to the call side: buy 10× Dec 29 370 calls @ 24.71 ($24,710 = the deployed capital) and sell 10× next-week 373 calls @ 3.66 (+$3,660); keep selling 373 calls weekly until QQQ closes back above 373: +$3,660 (Aug 11 close 366.24), +$1,160 (@1.16, Aug 18 close 358.13), +$300 (@0.30), +$900 (@0.90); Sep 1 QQQ closes 377.5 → buy back short calls @ 4.63 (−$3,730 on that leg) and sell the Dec calls @ 24.25 (−$460 vs cost), then resume put spreads. Three-month campaign: +$5,030 on max deployed capital $24,400 = 20.5% (≈82% annualized). "Very similar to the wheel but with much less capital." [4d6qj5vtrBQ]

**The bear-market 10-delta put ladder (SPY, the year buy-and-hold lost 14%).** [VsN4Ntw7onM] A conservative alternative to buy-and-hold when a decade-long rally (S&P +325% over the 10 years ending 2021) looks unsustainable: each month sell one ~10-delta SPY put ~3 months out, so three positions are always laddered; every expiry, replace the expiring rung. Sequence: Oct 22 2021 (SPY 453) → sell Jan 21 2022 385P @2.87; Nov 19 (SPY 469+) → Feb 395P; Dec 17 (SPY 461) → Mar 380P; continue monthly through the 2022 bear. Every put in the sequence expired worthless (Jan expiry closed 439, far above 385, etc.) because the 10-delta cushion out-ran the orderly decline. Result with SPY −14% YTD: puts +$1,830 (+~1.12% on the ≈$116,000 max committed capital) vs −$16,240 holding shares — a ~15.5% / >$18,000 swing. Win-win framing: either pocket premiums, or get assigned at a strike that was always set far below where the market traded 90 days earlier. [VsN4Ntw7onM]

**The wheel on QQQ, May 2023 → May 2024 (ATM puts, calls at the assignment strike).** [kE0T8l-p9ko] Context: short rates at 4–5% make bonds/CDs the benchmark. Protocol: on each third Friday sell the put at the first strike below the close ~1 month out; if assigned, sell the call at exactly the assignment strike until the shares are called away at breakeven, then resume puts. May 19 2023, QQQ 336.51 → sell Jun 16 336P @5.74 (+$574; $33,600 secured); close 367.93 → keep. Jul 21: 367P @7.24 (+$724); close 375.63 → keep. Aug: 375P @6.37 (+$637); close 358.13 → assigned 100 @375. Sep: 375C @1.98 (+$198); expired below 375 (transcript's close figure garbled). Oct: 375C @6.18 (+$618); expired. Nov: 375C → close 386.04 → called away @375, breakeven on the shares. Dec–Mar 2024 puts all expired worthless in the rally. Apr: 432P sold, QQQ 414.65 → assigned @432 (premium figure garbled as "$85"). May: call at 432, QQQ 451.76 → called away. Year: +$6,589 on the peak $43,200 of committed cash = 15.25%, average $549/month — plus ~5.13% money-market interest on the idle cash in the 8 of 12 months when no shares were held. [kE0T8l-p9ko]

**The wheel restated at the Orlando MoneyShow: 2-lot SPY, Sep 2023 → Sep 2024.** [tVQY5bSDodk] Framing: the options market is the one place that PAYS you for a lowball bid (a cash-secured put); only run it on something you want to own long-term (SPY: +422% over 25 years). Single-stock illustration: AMZN Aug 1 2024 @188.07 → sell the Aug 30 185P @6.98 (+$698; $18,500 secured); Aug 30 close 178.5 → assigned @185; then sell the Sep 27 175P @3.05 (+$305); close 187.97 → keep. SPY campaign: Sep 15 2023 close 443.38 → sell 2× Oct 20 443P @5.47 (+$1,094; $88,600 secured); Oct 20 close 421.19 → assigned 200 @443. Nov: 2× 443C @1.12 (+$224); Nov 17 close 450.79 → called @443 (no realized gain or loss on the shares). Dec: 2× 450P @5.19 (+$1,038; $90,000 secured); Dec 15 close 469.33 → keep. Jan +$996 (transcript prints "96"), Feb +$1,000, Mar +$1,174; Apr puts (+$1,228) assigned in the selloff; May calls at the assignment strike +$746 → called away; Jun +$1,172, Jul +$1,114, Aug +$1,401, Sep +$1,568. Year ≈ +$12,781 ≈ $1,000/month on ≈$99,650 average capital (transcript prints "2,781" and "99650" — the monthly legs sum to the larger figure). Pros/cons stated plainly: idle put-side cash earns money-market rates (≈4.7% in Oct 2024, near zero in 2021); the wheel generally OUTPERFORMS the market in flat or down markets and UNDERPERFORMS in strongly bullish ones — but always produces monthly cash flow. [tVQY5bSDodk]

**The wheel on TSLA, six months from July 2024: 20-delta puts, calls at the assignment strike (+16.5% / 33% annualized).** [8KbV5QtKFCQ] The "monthly income" protocol taught as the answer to "how do I earn consistent monthly cash": on the first Friday of the month sell the put with delta no lower than ~20 on the first-Friday chain a month out (the 20-delta put has ≈80% chance of expiring worthless); if assigned, sell the CALL AT THE ASSIGNMENT STRIKE — never below — until the shares are called away flat, then resume puts. Jul 5 2024, TSLA close 251.52 after recouping a ~50% first-half drop: sell 2× Aug 2 225P (Δ23) @6.32 → +$1,264. Aug 2 close 207.67 → assigned 200 shares @225. Sep 6 chain: sell 2× 225C @7.75 → +$1,550; close 210.73 → calls die, shares kept. Oct 4: 2× 225C → +$1,654 (stock nearer the strike, richer calls); close 250.08 → shares called away @225 — no gain, no loss on the shares, which were "a vehicle for collecting the covered-call cash and nothing else." Nov: 20-delta = 220P @6.30 → +$1,260; close 248.98 → expire. Dec 6: again 220P → +$950; post-election rally, close 389.22 → expire. Jan 3 2025: 20-delta now 345P → +$1,450; close 410.44 → expire. Six months: $8,128 collected on an average ≈$49,000 of capital = 16.5% ≈ 33% annualized. The three principles (the "right way"): (1) only wheel stocks you genuinely love long-term — if assigned and the stock keeps falling you may be selling meager calls for a long time before it recovers; (2) sell the put at a strike you'd be THRILLED to own the shares at — the 20-delta rule illustrates a consistent process, but on a stock that has run too far the 20-delta strike may be too close for comfort (a judgment call); (3) once assigned, calls only at or above the assignment price, however small the premium — chasing call premium below your basis converts an income program into realized losses. [8KbV5QtKFCQ]

**The WEEKLY wheel on SPY (Q1 2023): the "$200-or-more" put, calls at the assignment strike.** [1HXDto7qXaU] Premise: SPY has always eventually risen over 30 years, so assignment is survivable. Each Friday sell the put on NEXT Friday's chain that is as far below the market as possible while still priced at $2.00 or more (≈$200 per contract); if assigned, sell the next week's call at exactly the assignment strike until the shares leave at breakeven, then resume puts. Dec 30 2022, SPY 382.38 → sell the Jan 6 377P (>5 points below) @2.09 (+$209; transcript "$29"); cash needed $37,700. Jan 6 close 388.08 → expires. Jan 13: 381P @2.19 (+$219); close 398.50. Jan 20: 397P @2.27 (+$227); SPY closed below 397 → assigned 100 at 397 (the $39,700 set aside buys the shares; the premium is kept). Jan 27: sell the 397C @2.95 (+$295); close 405.68 → shares called at 397, no gain/loss on the shares. Feb 3: 399P @2.04 (+$204); close 412.35. Quarter: 13 trades, $2,280 total ≈ $175/trade on an average $40,200 of capital = 22.68% annualized; some weeks (e.g. the Feb 17 call) paid large, March weeks paid little, but every week paid something. Idle put-side cash should sit in a money-market fund (5%+ at 2023 rates; most brokers allow it). Scale by multiplying the lot count. [1HXDto7qXaU]

**The wheel on QQQ, Oct 2025 → Feb 2026: the monthly 3rd-Friday version, calls 25 points above the assignment price (+$5,813 vs +$488 buy-and-hold).** [K6YVPHULzPA] Premise restated: "get paid while you wait to buy a stock at the price you want" (the Buffett entry technique); prerequisite = a stock/ETF you want to own long-term (QQQ = the Nasdaq-100 basket). Oct 17 2025 (3rd Friday), QQQ 603.93 after an uptrend from the April-2025 tariff lows, high 613, sharp pullback to 589 the week before; buy target 595 on a retrace ("never buy a stock at the high"). Sell the Nov 21 595P @12.49 (+$1,249), $59,500 secured. Nov 21 close 590.70 → assigned 100 shares at 595, premium kept (≈20% annualized for 35 days). Switch to calls ~25 points above the acquisition price to give the stock room: sell Dec 19 620C @4.90 (+$490); Dec 19 close 617.05 → expires. Re-sell the same 620C for Jan 16 @9.89 (+$989 — richer because the stock is now close to the strike); Jan 16 close 621.05 → shares called at 620 → +$2,500 on the shares. Back to puts: Feb 20 595P @5.85 (+$585); Feb 20 close 608.88 → expires. Grand total $5,813 in four months on a stock that "basically didn't move" (603.93 → 608.88 = +$488 for a share buyer): 11× the buy-and-hold result. The two engines of the wheel: premium cash flow AND buying low / selling high on the assignment cycle.

**Cash-secured put vs covered call: the right tool for the situation (MSFT, Jul 2024 → Jul 2025, +$6,420 vs +$3,532 buy-and-hold).** [dU3eKVXlKQE] Both produce income and can deliver similar results, but they are different tools. Rule: when a stock sits at an all-time high / feels too rich to buy, do NOT start with a covered call (the call premium is "a drop in the bucket" if the shares then drop) — sell a cash-secured put at a price you'd be happy to own it; once the stock has pulled back and a bounce is reasonable, buy the shares and sell covered calls (a covered call is the better play when the stock has a reasonable prospect of rallying, giving both a share gain and the premium). Campaign: Jul 1 2024, MSFT 456.73 = all-time closing high → sell the Sep 20 435P (81 DTE, ~20 points below) @8.80 (+$880), broker secures $43,500 (= the trade's capital). Sep 20 close 435.27 → put expires by 27 cents. Stock now >33 points off its high → buy 100 shares @435.27 ($43,527) and sell the Dec 20 460C (just below the ATH) @11.20 (+$1,120); Dec 20 close 436.60 → expires (cash flow $2,000 so far). Sell the Mar 21 460C @12.37 (+$1,237); Mar 21 close 391.26 — shares down but the call expires (+$3,237 cumulative). Now the 460C 90 days out fetches only $1.70 → pros SIT TIGHT rather than sell a "pathetic" premium after a drop (the strike is ~70 points away, timing of any bounce unknown). May 5 2025 (days after the Apr 30 earnings the market loved), MSFT 436.17 → sell the Jul 18 460C (74 DTE) @8.97 (+$897). Jul 1 2025 MSFT 492.05, the 460C trades 33.93 → close everything: +$49,205 shares +$897 −$43,527 cost −$3,393 buyback + prior premiums → campaign profit $6,420 vs $3,532 for just buying the shares on Jul 1 2024 (+81%).

**The simplest professional trade: sell the put at the price you would be happy to own, month after month, until assigned.** [lXtcZyC1Rks] MSFT, Jun 18 2024, stock closes 449.78 having broken out above the 430 area that had capped it since late March; the trader decides he wants the shares at 430 and no higher. Sell the Jul 19 430 put @3.15 (+$315) with $43,000 of cash set aside for a possible assignment; MSFT slipped back to 437.11 by Jul 19 → the put dies → $315 kept for a month spent merely promising to buy at 430. Repeat on the Aug 16 chain: the identical 430 put now pays 10.47 (+$1,047), more than triple, purely because the stock is now only $7.11 above the strike and the market demands more for that risk. Aug 16 MSFT closes 418.47 → assigned 100 shares at 430, exactly the entry he named. Bookkeeping: $1,362 of premium collected while waiting, plus shares at 430; by Oct 20 MSFT traded 516.81 → total profit on the position $10,043. The framing to keep: a cash-secured put is the market PAYING you to bid for a stock below where it trades — and paying you again every single time the bid is not hit. [lXtcZyC1Rks]

**The put ratio spread as a share-accumulation program (TSLA, a full year).** [ygMHTNFIdbw] For the case where you want to own a stock that has just doubled and refuse to pay up: every cycle buy ONE put ~5% below the stock on the chain ~45 days out, and sell TWO puts as far below that as you can go while still collecting a little more than half the long put's price — so the structure is entered for a small CREDIT, pays you while you wait, profits from the pullback when it comes, and hands you 100 shares at the short strike (close the long put and one short put, let the other assign). Cash for 100 shares at the short strike is set aside each cycle. TSLA campaign, Aug 1 2023 (stock 261.07 after more than doubling off the 123.18 close of 2022) through Jul 2024, target 300 shares. Sep 15 chain (45 days): buy 250P @10.20, sell 2× 235P @5.65 → +$17 credit, $23,500 aside; TSLA closed 274.39 → keep $17. Oct 27 (42 days): 260P / 2× 245P → +$234, $24,500 aside; TSLA fell to 207.33 → sell the 260P at 53.22 (+$5,322) and buy back ONE 245P at 38.18 (-$3,818) → +$1,738 of option profit AND 100 shares assigned at 245. Dec 15 (49 days): 195P / 2× 180P → +$131, $18,000 aside; TSLA bounced to 250.35 → keep it. Jan 26 (42 days): 240P / 2× 225P → +$99; TSLA sold off to 183.25 → +$1,606 and 100 shares at 225. March: 175P / 2× 165P → +$85, $16,500 aside; TSLA closed 34 cents above 165 → keep it. April: 165P / 2× 155P → +$120; TSLA 147.05 → +$1,095 and 100 shares at 155. Late May: +$151 (both puts worthless after the bounce). Final July 2024 trade: +$114. Result: the 300 shares were acquired at 245, 225 and 155 ($62,500 of cost) and were worth $74,471, and with roughly $5,525 of accumulated option profits the year returned +$17,496 — against -$3,850 for simply buying the 300 shares on day one. The real money is made in the pullback; every month without one still pays, and each assignment lowers the cost basis for the bounce you wanted in the first place. [ygMHTNFIdbw]

## CHAPTER: Small-account strategies

Premise: options are highly capital-efficient; SMB has trained traders with accounts as small as a few hundred dollars, and all three strategies below fit a $1,000 account. [hsPmj_6nl5E]

**1. Iron condor (0-DTE on SPY).** Sell an OTM call and an OTM put, buy a further-OTM call and put as wings. Worked live example (Monday Aug 28, SPY opened 442.24, same-day expiration = no overnight risk): sell 10 × 445 calls @ 0.25 (+$250) and 10 × 441 puts @ 0.43 (+$430); buy 10 × 446 calls @ 0.11 (−$110) and 10 × 440 puts @ 0.27 (−$270) → net credit $300; broker margin = $700 (the worst-case loss), so it fits a $1,000 account. SPY closed 442.76 → all four strikes expire worthless → keep the $300 = +30% on the account in one day. [hsPmj_6nl5E]

**2. Call debit spread (defined-cost directional bet).** Buy a call, sell a higher-strike call in the same chain to slash the cost. Example: MSFT, June 1 2022, stock 272.42 (−20% YTD on the rate-driven tech selloff), bullish thesis. 100 shares would cost $27,242 — impossible on $1k. Instead on the June 2023 chain (1 year out): buy the 295 call @ 26.33, sell the 320 call @ 16.78 → net debit $956 (>60% cheaper than the naked call's $2,633). June 16 2023, MSFT 348.10 (AI rally): 295 call worth 53.25, 320 call worth 28.22 → close for $5,324 − $2,822 − $956 = +$1,546, turning the $1,000 account into ~$2,546 in a year. Near expiry, ITM options trade at ≈ intrinsic value (stock − strike). [hsPmj_6nl5E]

**3. Buying LEAPs, especially deep in the money.** A LEAP is simply a call/put listed with ≥12 months to expiration. Deep-ITM LEAP calls behave like stock for a third of the price. Example: H&R Block (HRB), Jan 20 2022, stock 21.58 after a multi-month selloff, bullish fundamental thesis. 100 shares = $2,158; instead buy the Jan 20 2023 15-strike call (deep ITM) for 6.90 = $690 (< 1/3 of the shares' cost). One year later HRB at 37.25, the call worth 22.90 → sell for $2,290 → +$1,600, a >230% return on risk; account grows $1,000 → $2,600. Punchline: the shares themselves would have earned only $1,567 ($3,725 − $2,158) — *less* than the option, with 3× the capital and more risk. Deep-ITM calls can beat outright stock ownership on absolute dollars, not just percentage. Professionals use this capital-efficiency constantly, not just small accounts. [hsPmj_6nl5E]

**4. The under-$100 trade: XSP ATM put credit spreads on a 20-day-SMA signal.** [Jniwt90PUS4] XSP index options price at exactly 1/10 of SPX (SPX ~6,500 → XSP ~650), created because SPX near $7,000 "priced small retail traders out"; they make option strategies possible for accounts under $100 per trade. System: when XSP closes cleanly above its 20-day SMA after having been below, sell a 2-week ATM 1-point-wide put credit spread (short put = first strike below the close); exit early only if XSP closes back below the 20-day SMA, else hold to expiry. Typical credit $30–40 per spread, broker capital $60–70 (the $100 width minus credit — structurally can never exceed $100). Trades: Apr 24 2025 close 548.48 → sell May 8 548P @9.56 / buy 547P @9.18 → +$38 credit, $62 capital; close 566.39 → +$38. Aug 4 close 632.99 → 632/631 @5.57/5.24 → +$33/$67; close 644.91 → win. Next week close 646.69 → 646/645 for +$37/$63; Sep 2 XSP gaps below the SMA to 641.55 → rule says exit: buy back 646P @6.02, sell 645P @5.42 → −$23 on the trade. Signature feature: losses run smaller than average wins because the 1-point width caps damage while the exit-signal fires early. Campaign Apr 2025 → video date: mostly wins, 3 losses each smaller than any win, net +$187 = ~62% on a conservatively-held $300 base (hold several trades' worth of capital so a losing streak can't stop the system). Prop-firm pitch attached: firms care about discipline and drawdown control, not the number of zeros in your account — a small-account track record is a real career artifact. [Jniwt90PUS4]

**5. The $1,000 daily 0-DTE iron butterfly (10% target / 20% stop).** [aC-JCii8Vg8] Every trading day right after the open: on the SPX 0-DTE chain sell the ATM straddle at the strike nearest the open and buy a 20-point-wide strangle around it (an iron butterfly; every platform has the preloaded ticket). Capital = 20 × 100 − credit. Exit at +10% of required capital, stop at −20%, either way usually inside the first 30–90 minutes — the trade monetizes the fast relative decay of the rich ATM shorts vs the cheap wings, and most days the market hasn't moved far enough by then to overwhelm that decay. Worked week (June): Mon Jun 3, SPX opens 5295.73 → sell 5295C @9.65 + 5295P @9.20, buy 5315C @2.15 + 5275P @3.20 → +$1,350 credit, capital $650; at 10:10am SPX 5290 → close all four legs → +$73 (>10%). Tue: open 5265.12, credit $1,495, capital $505 (transcript prints "$4.95"/"$55"); at 10:55 SPX 5267 (moved 2 pts) → all four legs cheapened → +$80 (>15%). Wed & Thu also profitable; Fri: open 5331, butterfly at 5330, credit $515 (transcript's "$485 capital" doesn't fit 20-point wings — flagged); market rallies 17 points by 10am, the 5330C balloons to 23.55 → stop hit at −$110 (>20%). Week: 4 wins / 1 loss ≈ +$200 on a $1,000 account (transcript prints "$21 profit… a 20% return" — internally inconsistent; the itemized legs sum to ≈+$203). Backtest your own target/stop combination before trusting 10/20. [aC-JCii8Vg8]

**6. Three income trades under $3,000 (the 2025 set).** [W5Gl_E2Sq-A] Purpose: build a fundable track record without large capital. (a) The diagonal instead of the covered call — PSX, $2,260 for +$1,915 = 84% (detailed in the Covered calls chapter). (b) A 5-month put credit spread at a chart floor: Jan 13 2025, MO back at the 50 level it had held since August; instead of 100 shares ($5,085), on the Jun 20 chain sell 15× 50P @2.54 and buy 15× 47.5P @1.62 → +$1,380 credit, broker capital $2,370 (15 × $250 width − credit); Jun 20 close 59.75 → keep all $1,380 = 58% on capital vs +$890 = 17.5% for the shares on twice the capital. (c) A post-earnings put calendar — UPS, $2,000 for +$1,100 = 55% (detailed in the Calendar chapter). [W5Gl_E2Sq-A]

**7. Capital hogs vs capital-efficient structures: the same $5,000 max loss, 25% of the margin (RUT iron condor vs iron butterfly, Oct 2024).** [iJMkj24PHqs] Many believe options need huge capital because they only met "capital hogs". Oct 1 (2024), RUT 2215.1, Oct 31 chain (30 DTE): iron condor 100 points out with 50-point wings — sell 2310C @18.30 (+$1,830) and 2110P @20.65 (+$2,065), buy 2360C @9.35 (−$935) and 2060P @12.75 (−$1,275) → +$1,685 credit; only one side can lose, so max loss = $5,000 − $1,685 = $3,315 = the broker's capital requirement. Oct 31 close 2196.65 (between all four) → +$1,685 = 50.8% on capital — but a $1,000 account could not have entered. Same day, same wings, shorts AT the money instead (iron butterfly): sell the 2210C @57.95 and the 2210P (≈$1 above; transcript garbles the put price — the pair brings in ≈$4,205 net after the 2260C/2160P wings, "$425" in the audio), buy the 2260C and 2160P → because the max payout is still $5,000 on either side, capital = $5,000 − credit ≈ $795, i.e. one quarter of the condor's. Oct 31 close 2196.65: calls worthless, short 2210P pays 13.35 points = $1,335, long put worthless → profit $2,870 = 361% on the capital required. Takeaway: structure trades to shrink the broker's capital requirement; the return on risk capital rises accordingly.

**8. The $5,000-account monthly SPY put credit spread program (2023: +55.96% vs SPY +24.23%).** [oO5SfYblvio] For the trader who feels "too small to participate" in a big market move. Protocol: on the first Friday of each month (or right after the previous trade expires) sell the SPY put closest to 10 points below the market on the chain expiring the first Friday of the next month, buy the put 50 points lower; the 50-point width caps the broker requirement at $5,000 − credit, so the whole program fits $5,000 forever. Jan 3 2023 (SPY 380.84 after a −20% 2022): Feb 3 chain sell 370P @5.27 (+$527), buy 320P @0.28 (−$28) → +$499, capital $4,501 (audio "$451"); Feb 3 close 412.35 → both expire → +$499. Mar: SPY 412.35 → sell 400P / buy 350P → +$296, capital $4,704; Mar 3 close 404.19 (sold off, still above 400) → +$296. Eight straight wins through the early-September expiry — plausible because the ONLY losing scenario is SPY closing below the short put. October: spread 440/390 sold for $296 in early September; SPY sold off to 429.54 at expiry → buy back the short put for $1,088, long expires → loss ≈$792 (audio "$832"); continue the program regardless — that is how systematic strategies are run. Nov: 420/370 @3.44 (+$344) win; Dec 1 trade (closed Dec 28 to fit 12 trades in the year) win → 11 wins of 12 → +55.96% on $5,000 vs SPY +24.23%. Bonus: credit-spread capital is margin, not spent cash → the account also earned the 4–5% money-market rate that appeared in 2023 (brokers treat MM funds as cash for margin) — add it to the return.

**The four steps that actually grow a small account (and why the condor replaces the strangle).** [7IHCmruEZUk] The beginner's model — buy a cheap call and catch a huge move — is lottery-ticket behaviour; the professional model is to sell time decay inside a range you define yourself, which requires no directional opinion at all. Teaching trade, 0-DTE SPX with the index at 6870 on the morning of December 5: sell the 6900 call 30 points up @2.27 (+$227) and the 6840 put 30 points down @5.25 (+$525) — a short strangle for $752, which the 6869.07 close converted into $752 of profit in one day. **Step 1, risk management, i.e. DEFINE the risk.** Had that same day closed 6960, the naked 6900 call alone pays out $6,000 → -$5,248: seven winning days to climb back, and a $5,000 account simply gone. Buying the 6910 call @0.95 and the 6830 put @3.85 turns it into an iron condor: the credit falls to $272, but the 6960 outcome becomes only -$728 (the long 6910 call returns $5,000), and the broker requires far less capital than for the strangle. **Step 2, journal properly** — not "today I made money" but the observations that become rules: entry at the open vs after the opening drive settles into a range; strikes far from the index vs close to it; which day types to skip (CPI, non-farm payrolls, Fed meetings, election days); whether to take profit at less than the full credit; whether to cap the loss short of the structural maximum. A rule set assembled from such notes looks like: enter at 10:00am, sell 40 points from the open, close at 90% of the credit, never lose more than $500 even though the max loss is $700, no trade on a CPI or NFP morning. **Step 3, backtest those rules** on years of data with commercial options-backtesting software — a rule set that prints money this year may not survive earlier regimes, and when it does not, use the backtest to find the modification (strikes closer in, entry at the open) rather than abandoning the work. **Step 4, compound** — a $5,000 account making about 1% of the account per week is roughly 50%/yr → $7,500; size from 10 lots to 15 in year two → $11,250; after four years past $25,000, with the same strategy, same rules and same process, only the lot size changing — and every bit of that arithmetic depends on step 1 still holding. [7IHCmruEZUk]

**9. Deep-ITM calls instead of shares: $300 per SPY point for $1,734 instead of $129,816.** [9pnSF-YE2DQ] The small-account trader's chronic complaint is watching a signal play out exactly as expected with no way to participate: 300 shares of SPY at ~463 costs $138,900 and pays $300 per point — two tenths of one percent for a one-point rally, and impossible for most accounts anyway. The fix is a deep-in-the-money call, whose delta is near 1.00 so it tracks the shares nearly point for point. Worked example, Friday Jul 9, an InvestiQuant bullish signal, SPY opening 432.72: 300 shares would cost $129,816; instead buy 3× same-day 427 calls (strike well below the open) @5.78 = $1,734 — almost 75× cheaper. SPY closed 435.51, up 2.79 on the day; the call is worth its intrinsic 8.51 because exercising buys 300 shares for $128,100 instead of the $130,653 they now cost — a $2,553 discount. Result: the calls sell for $2,553 → +$819 = over 47% on the capital deployed, versus +$834 = 0.6% on $129,816 of stock — essentially the same dollars for $128,000 less capital at risk. The same substitution works on any high-priced underlying (TSLA, CMG) and caps the loss at the premium. [9pnSF-YE2DQ]

**10. The rolling deep-ITM LEAPS campaign as a stock substitute (NFLX, Jun 2019 → Apr 2025): +113% vs +67.4% for the shares, with a smaller drawdown.** [WSsXl8Nh3PM] Rule of the campaign: each year buy the call whose price is just under HALF the share price (i.e. deep in the money), and on its expiration day sell it and roll into the next June chain under the same rule — never more than half the capital of the stock, never a margin call, loss capped at the premium. Netflix, Jun 21 2019, opened 366.94 (channeling 320–385): 100 shares = $36,694; instead buy the Jun 19 2020 195 call @180.05 = $18,005. **Jun 2020:** NFLX opens 447.82, the LEAP is worth 253.15 = $25,315 (≈ the 252.82 discount to the strike) → sell it and buy the Jun 2021 235 call @221.80 (−$22,180) → cumulative outlay $14,870. **Jun 2021:** NFLX opens 498.90, the 235 call worth 263.30 = $26,330 → roll into the Jun 2022 260 call @244.55 → cumulative outlay $12,995. **Jun 2022** (the Fed/inflation tech crash): NFLX opens 176.21, the 260 call expires WORTHLESS — and this is the instructive moment: the campaign is down $12,995, while 100 shares bought in 2019 would be down $19,073 ($36,694 → $17,621; the audio says "19,731"). The LEAP structure caps the drawdown at what you actually paid, which is what makes it possible to hold conviction through the crash. Roll on regardless: buy the Jun 2023 100 call @87 (−$8,700). **Jun 2023:** NFLX opens 444.60, that call is worth 344.65 = $34,465 → roll into the Jun 2024 245 call @220.62 → cumulative outlay $7,950 (the itemised legs give $9,292 — one of the two leap prices is garbled). **Apr 1 (video date):** the final LEAP is worth $37,225 → campaign profit $27,886, over 113% on the capital ever deployed, versus $24,733 = 67.4% for simply holding the 100 shares — and the unused half of the capital could have sat in one-year T-bills at 2023–24 rates, income excluded from that comparison. [WSsXl8Nh3PM]

## CHAPTER: Weekly & monthly credit-spread income campaigns

**Weekly ATM put credit spreads with a trend filter.** [xQfp8_5VsRU] $10,000 account. Step 1: each Friday decide bullish/bearish with an indicator you trust (example protocol: SPX above its 10-day SMA = bullish, trade on; the choice of indicator is yours). Step 2: pull the chain expiring next Friday. Step 3: sell a 5-point-wide put credit spread at the first strike below the close, lot-sized to the account. Dec 30 2022, SPX 3839.50: sell 10× 3835P @ 38.10 (+$38,100), buy 10× 3830P @ 35.90 (−$35,900) → +$2,200 credit, $2,800 margin. Jan 6 close 3895.08 → win. Week 2: 3895/3890 @ 50.80/48.45 → +$2,350; close 3999.09 → win. Week 3: 3995/3990 @ 27.85/25.75 → +$2,100; Jan 20 close 3972.61 → short put 22.39 ITM pays $22,390, long 17.39 ITM returns $17,390 → week −$2,900. Raw campaign (no filter at all), Jan–Aug 2023: +$8,770 = 87.7% on the account in 8 months; a decent filter should improve it. Note: ATM weeklies are the aggressive end of the family — wins are big but losses land often. [xQfp8_5VsRU]

**The twice-a-week far-OTM version and its hidden tail.** [Dl0O3z_5hB0] A real applicant to the desk nets ~$2,500/week: 50 SPX put credit spreads on the Wednesday chain (entered Tuesday) and 50 on the Friday chain (entered Thursday), short put placed as far OTM as still nets ≥$0.25/spread ($1,250/trade). Example: SPX 3010 → sell 50× 2990P @ 1.38 (+$6,900), buy 50× 2985P @ 1.10 (−$5,500) → +$1,400 (28¢). Next-day close 2992 → both die, keep it all. The missing piece: a 30-point overnight gap-down (close 2980) pays the long +$25,000 but the short −$50,000 → net −$23,600 ≈ 10 winning weeks erased. Freudberg's response was NOT "stop trading it": run the numbers — at ~$1,250 twice a week, 4 total-loss events/yr still yields >100% annualized, 5/yr ≈ 50%, ≥6/yr loses money. Nobody knows the gap frequency intuitively → backtest it before believing the strategy. Nine months without a loss proves nothing about tail frequency. [Dl0O3z_5hB0]

**Monthly 10-delta put credit spreads (the high-probability beginner campaign).** [xidgg27-yWU] Sell the ~10-delta put (≈90% chance of expiring worthless — delta ≈ probability of expiring ITM), buy 5 points lower, ~30 DTE, roll monthly. Dec 1 2022, SPX 4076.57: the Dec 30 3775P shows delta 10.02 — over 300 points of cushion; 10-lot: sell 3775P @ 12.70 (+$12,700), buy 3770P @ 12.30 (−$12,300) → +$400. Dec 30 close 3839.50: market fell ~237 points and the trade STILL won in full — that's the margin of safety. Jan: 3535/3530 → +$450 on $4,550 margin; close +200 pts → win. All 12 months Dec 2022–Nov 2023 won: total +$4,050 on max margin $4,750 = 85% for the year (2023's bullishness made it 12/12; expect ~90% win rate long-run, i.e. a losing month or so per year). Defense when a month goes bad — the roll: Aug 31 2022, SPX 3955, usual trade +$400; by Sep 23 SPX −268 pts to 3687 and the short put's delta has doubled 10 → 20. Response: close the spread and re-open 80 points lower at the new 10-delta (3475/3470), financing the expensive buyback by increasing size 50% (10 → 15 lots), leaving $200 of the credit alive; Sep 30 close 3585.62 → all expire worthless, +$200 saved from a losing trade. Cost of rolling: profit shrinks and capital requirement grows — keep spare capital for the rainy day. [xidgg27-yWU]

**The weekly broken-wing butterfly (SPX, ~14 DTE).** [Qj8_3eybnaE] Structure, entered ~2 weeks before a Friday SPX expiry: find the 10-delta put; SELL 20 of them; BUY 10 one strike (5 pts) above; BUY 10 further below at whatever strike leaves ≥$1,000 net credit. Example Nov 15 (SPX 3109), Nov 29 chain: sell 20× 3040P @ 7.20 (+$14,400), buy 10× 3045P @ 7.70 (−$7,700), buy 10× 3020P @ 5.40 (−$5,400) → +$1,300 credit. Rules: exit at +$1,000 profit; exit at −$2,000 max loss. Nov 25 (SPX 3122, 5 DTE): 3045P → 0.70, 3040P → 0.65, 3020P → 0.45; closing all legs leaves $1,150 of the credit → target hit. 12-month backtest through the late-2018 Christmas selloff and the May/Aug/Oct 2019 selloffs: 41/52 exits at ≥+$1,000, 11/52 at ~−$2,000, total +$22,815 on ~$28,000 of dedicated capital = 81%/yr. Sized at ~$65k it averages ≈$1,000/week — but see the "no ATM machine" warning: the average arrives lumpy, with losing weeks and sometimes consecutive ones (gaps can blow through the stop); plan personal cash flow around the average, never around every single week. [Qj8_3eybnaE]

**The broken-wing butterfly's windfall scenario (classroom deep-dive).** [vU64DYL3raU] The same 1×2×1 put structure taught live: index @1724, 10 DTE — buy 10× 1700P @5.55 (−$5,550), sell 20× 1690P @3.80 (+$7,600), buy 10× 1670P @1.90 (−$1,900) → +$150 credit, broker capital $9,850 (a 1-lot needs $985; the credit appears because the doubled middle shorts outweigh both longs, and the lower wing is set 20 points down vs 10 up — pull it closer/equidistant and the credit disappears). The five scenarios: rallies big, rallies small, flat, drops ≤24 points — all four pay the $150 credit (≈1.5% per 10 days on capital); scenario 5 splits: 5b = drop through the shorts → losses grow (stop required, as with any trade); 5a = the windfall — a gradual selloff landing between the long 1700 and short 1690: actual close 1691.80 → 1700P worth 8.20 ×10 = $8,200, all else worthless → +$8,350 on $9,850 (≈85% in 10 days; even a close at 1688 still profits after netting the shorts' payout). Extra teachings: complex orders fill via the CBOE complex order book; mid-trade you may decompose the position (he once closed the top long + half the shorts of a live 25-lot as a credit-spread order) but expect margin to change; skipping the bottom wing "to save money" is exactly the gap risk the broker margins you massively for — protection can only be bought before the fire. [vU64DYL3raU]

**Weekly 10-delta SPX put credit spreads (the "simplest high-probability" version).** [hbkcV1ejzJw] Each Friday sell next-Friday's ~10-delta SPX put, buy the put two strikes (10 points) lower. October run: last Friday of Sep, SPX 5738.7 → sell 5× Oct 4 5565P (10Δ, 173 pts OTM) @6.00 (+$3,000), buy 5× 5555P @5.30 (−$2,650) → +$350, capital $4,650; close 5751.07 → win. Oct 11: 5570/5560 → +$350; close 5815.03. Oct 18: 5670/5660 → +$275, capital $4,725; win. Oct 25: 5745/5735 → +$300; market sells off mildly yet closes 5882 → win anyway (the 10Δ cushion absorbs mild selloffs). Nov 1: 5620/5610 → +$350; close 5728.8 → win. October: 5/5, +$1,625 = 34.3% on peak capital $4,725. Caveat: thrives in flat/bullish tape, struggles in bear phases — gate it with a bull filter (index above its 50-day MA, or RSI near 30 marking oversold). [hbkcV1ejzJw]

**The 10-delta campaign on a single stock (TSLA, 60 DTE) and the delta-doubling roll.** [-Dfl8YyoP0E] The monthly-SPX protocol ported to a stock with a bounce thesis: TSLA Dec 19 2022, open ~158 after the 2022 −70% collapse (RSI in oversold <30 through Q4) → sell 10× Feb 17 105P (Δ10.36) @2.93 / buy 100P @2.34 → +$590, capital $4,410; close 208.31 → win. Successive ~60-DTE trades at the rolling 10-delta: Apr (145/140) +$600/$4,400 → close 165.08; Jun (125/120 @1.72/1.25) +$470/$4,530 → close 260.54; Aug (195/190) +$600 → close 215.49; Oct (165/160) +$590 → close 211.93; Dec (165/160) → win. Year: 6/6, +$3,370 on max capital $4,530 = 74% — expect ~90%, not 100%, long-run. Defense rule ("line in the sand"): when the short put's delta DOUBLES 10 → 20 (Mar 13, TSLA 171.57: the 145P hit 20Δ), roll the whole spread back down to the original delta: buy back 145P @5.23, sell the long 140P (+$4,180), open 130/125 (+$2,620/−$2,060) → $110 of credit left alive; Apr 21 close 165.08 → keep the $110 (transcript names the roll target once as "135/125" and once as 130/125 — figures as spoken). [-Dfl8YyoP0E]

**RSI-30 entry: the oversold 60-DTE ATM put credit spread.** [t2hTAtI2OxY] Aggressive-but-filtered variant for growing a $5,000 account: when an index RSI reads ~30 (oversold), sell an AT-THE-MONEY 5-wide SPX put credit spread ~60 days out — the 2-month runway lets the oversold condition finish selling off and then bounce; exit when ≥90% of the premium is captured. Trades: Sep 26 2023, SPX 4273.53 at RSI ≈30 → sell 15× Nov 30 4310P @97.45 / buy 4305P @95.70 → +$2,625, capital $4,875 (the entry chain quotes SPX ≈4307 at the close — transcript's index figures are garbled); Nov 30 close 4567.8 → full win. Apr 19 2024 close 4967.23 → Jun 21 4965/4960 ×15 → +$2,775, capital $4,725; close 5464.62 → win. Aug 5 2024 (SPX −500 pts in 3 weeks to 5186.33) → Sep 30 5185/5180 → +$2,550, capital $4,950; by Sep 19 SPX had rallied >500 points, the puts quoted 1.98/1.95 → close early for ≈ full credit (transcript's "$2,555 win" overstates its own arithmetic by ~$50 — flagged). Stated year: $5,000 → ≈$12,500+, "more than doubling the account" (transcript's "12,545"/"115.9%" figures are internally inconsistent — flagged). [t2hTAtI2OxY]

**RSI-70 entry: the overbought 10-delta call credit spread.** [v_27P1SNZTU] Mirror-image signal: when RSI crosses ABOVE 70 (overbought), sell a ~10-delta call credit spread ~8% above the market, ~30 DTE, 50-point wings — sized so the trade wins even if the signal fires early or is outright wrong. Trade 1: Jan 6, RUT 2051 → sell Feb 5 2210C (10Δ, 160 pts OTM) @12.35 / buy 2260C @6.30 → +$605, capital $4,395. RSI was WRONG — RUT rallied ~100+ points to 2159 — yet with 2 days left the 2210C had decayed to 0.68 (only 2 days for a 70-point rally = no bid): close @ 0.68/0.20 → +$557, >90% of max. Trade 2: Feb 5, RSI >70 again, RUT 2233 → sell Mar 2380C @11.85 / buy 2430C @6.10 → +$575, capital $4,425; Feb 26 RUT 2201 → close @0.83/0.35 → +$527. Standard exit: close credit spreads at ~90% of potential profit. Full year: the RSI fired five times (both directions) → ≈46% return on average deployed capital. The takeaway is structural, not the backtest: locating short options far from the signal price buys the wiggle room that converts a mediocre indicator into a high-probability trade. [v_27P1SNZTU]

**RSI 70/30 on DIA → two-week credit spreads placed one standard deviation away (50-lot, 2020–21).** [RbWA61gJSa4] The same principle with a statistical strike rule instead of a delta: when RSI reaches ~70 (overbought) or ~30 (oversold), have the broker platform compute the one-standard-deviation move over ~two weeks (≈32% probability of being reached) and sell the credit spread at that strike on the chain closest to two weeks out, 5-point wings. Aug 10 (2020), DIA 278 with RSI ≈70 for the first time in a while: 1 SD up ≈285 → sell 50× Aug 21 285C @0.91 (+$4,550), buy 50× 290C @0.34 (−$1,700) → +$2,850, capital $22,150 (the worst case). DIA closed ≈279 at expiry — HIGHER than at entry, so a short-stock trade on the same signal would have lost — yet both calls died → +$2,850 = >12% in 12 days. Oct 28 (2020), DIA 266, RSI ≈30 (first oversold reading in 12 months): 1 SD down ≈245 → on the Nov 13 chain (17 days) sell 50× 245P @2.29 (+$11,450), buy 50× 240P @1.66 (−$8,300) → +$3,150, capital $21,850; DIA rallied to 295 → +$3,150 = 14.4%. Every RSI signal over the 12 months (bullish → put credit spread, bearish → call credit spread, only when no trade was already working) — 10 trades, 10 full wins, >$24,000 = >100% on the capital deployed. Lesson restated: indicators are "generally reliable, not perfect"; an OTM credit spread gives the signal room to be somewhat wrong, so unless it is WAY wrong the win is almost assured. [RbWA61gJSa4]

**Weekly SPX 5-wide put credit spread with a 200-day-MA filter (2018, the year the S&P lost 6%).** [CjbWjnWXXzQ] The 15-minutes-a-week version: each week sell the first SPX put ABOVE the market and buy the put 5 points lower on the chain expiring the next Friday; only trade weeks when SPX is above its 200-day moving average (skip the week otherwise); no exit management — expiration settles it. Dec 29 2017, SPX 2686: sell the 2690P @10.62, buy the 2685P @8.54 → +$208 credit; max loss $500 − $208 = $292; Jan 5 close 2743 → keep $208. Economics: ~+$200 on a win, ~−$300 on a loss, and the market rises more weeks than it falls. 2018: SPX above the 200-DMA 41 of 52 weeks; 26 wins / 15 losses; compounding the original $300 of risk grew it to ~$2,000 (>500%) while the S&P fell 6.24%; at $3,000 of risk → ~$20,000. (Sibling of the 10-day-SMA weekly campaign above; the choice of trend filter is the trader's.) [CjbWjnWXXzQ]

**The 2017–2018 monthly 10-delta put credit spread with the 200-day filter (the "crushed the market" campaign).** [UOX2_YaAIRc] Rules: around the 10th of every month, take the monthly SPX chain ~70 days out; if SPX is above its 200-day moving average, sell the ~10-delta put and buy the put 50 points lower; EXCEPTION — if the 10-delta strike sits above the 200-DMA, sell the put AT the 200-DMA instead; skip the month entirely if SPX has closed below the 200-DMA for more than five trading days at initiation time; stop loss = twice the credit received (e.g. $475 credit → exit at −$950); otherwise let expiration settle it. Trade 1: Nov 11 2016, SPX ≈2165 with the 200-DMA below 2100 → sell the Jan 2000P @18.10 (+$1,810), buy the 1950P @13.00 (−$1,300) → +$510; broker requirement ≈$4,500; Jan 20 2017 SPX 2250 → both expire worthless. Trade 2 (Dec ~10): SPX 2253, 200-DMA 2120 = exactly the 10-delta strike → sell 2120P / buy 2070P → +$505; Feb 17 2017 SPX 2350 → win; +$1,015 after two months. Capital plan: trades last 70 days but start every 30, so two overlap — ≈$4,750 each, $9,500 total; when the third trade is due, CLOSE the first (a real cost, deducted in the results) and roll its capital forward, so capital never exceeds $9,500; letting all three run would have made more but on more capital, lowering the return. Result following the rules strictly, including losing months and skipped months: 2017 +49% vs S&P +19%; 2018 +22% vs S&P −7%. (Compare the weekly 200-DMA version [CjbWjnWXXzQ] and the 2019 60-DTE version [PgghzkCugZ8] below — same filter, different tenor.) [UOX2_YaAIRc]

**The 2019 version: 60-DTE 10-delta put credit spread, 10-wide, closed at 90% of the credit (+67% vs S&P +29%).** [PgghzkCugZ8] Rules: enter only when SPX is above its 200-DMA; sell the 10-delta put on the chain ~60 days out, buy the put 10 points lower (10-lot); close when the open profit is ≥90% of the credit; if SPX closes below the 200-DMA, wait three days and exit only if the THIRD close is still below it (filters out one-day dips that get bought); after exiting or closing for profit, re-enter as soon as a 60-day chain is available and the filter is green. 2019 sequence: the first green light was Feb 12 (the Q4-2018 selloff kept SPX under the 200-DMA until early February): SPX 2745, 10-delta put = 2575 (170 points below) → sell 10× 2575P @19.25 (+$19,250), buy 10× 2565P @18.00 (−$18,000) → +$1,250; broker requirement ≈$8,750 = worst case. Mar 28 (45 days in, 15 DTE) after a brief dip below the 200-DMA that rebounded quickly: 2575P @1.15, 2565P @1.05 → close for +$1,150 = 92% of the credit. Apr 9: SPX 2877 → sell 2715P @19.40 / buy 2705P @18.35 → +$1,050 credit on $8,950; Jun 5 (SPX had sold down, 3 DTE, puts >100 points OTM) → closed for $50, keeping 95%. Conditions were met four more times (early June, late July, September, November) → six trades in the year on a little under $9,000 → +67% return on capital — more than twice the S&P's 29% — while being OUT of the market for several months when the filter was red. Delta primer given: a put 5 points below the market has delta ≈50; 200 points below it can be 5–10 depending on time to expiry. [PgghzkCugZ8]

**Bollinger Bands + RSI double signal → 20-delta 1-month credit spreads on QQQ (2024–2025).** [AayABdqDKIc] Three steps: (1) daily QQQ chart with Bollinger Bands (20-period SMA, ±2 standard deviations — the bands widen with volatility and flag overbought/oversold extremes that tend to revert to the SMA, though price often keeps pushing for a while after a band touch, which is why a naive fade gets stopped out); (2) add RSI and require the second confirmation — bearish only when price has pierced the UPPER band AND RSI ≥70, bullish only when price has pierced the LOWER band AND RSI ≤30 (Mar 21 2024's upper-band cross without RSI >70 was skipped; the trade waited until Jun 12); (3) express the signal with a ~20-delta credit spread expiring ~1 month later — call credit spread for bearish, put credit spread for bullish — picking the first strike BELOW 20 delta, 10-point wings, because the ~20 points of room between the market and the short strike lets the signal be early and still win. Trade 1 (bearish): Jan 19 2024, QQQ close 421.18 (upper band pierced, RSI >70) → Feb 16 chain (28 DTE): sell 10× 440C (Δ17.51) @1.63 (+$1,630), buy 10× 450C @0.53 (−$530) → +$1,100. Feb 16 close 430.57 — UP 9.39 from entry — yet 9.43 below the short strike → both expire worthless → +$1,100 on a bearish trade in a rising market: "the secret sauce." Trade 2 (bullish): Apr 19 2024 close 414.65 (lower band pierced days earlier, RSI reached 30 that day) → May 17 chain: sell 10× 390P (Δ16.55) for $2,610, buy 10× 380P for $1,580 → +$1,030; May 17 close 451.76 → win. Trade 3: Jun 13 2024 bearish → 495/505 call credit spread; close 494.89, 11 cents under the short strike → full credit kept (transcript prints "130"). Trade 4: Aug 2 2024 bullish → 415/405 put credit spread (transcript "41545") → +$1,170. Two-year tally (2024–2025): every double signal won; per-trade profits cluster near each other; stated 136% over two years ≈68% annualized (the transcript's total-dollar figure is garbled as "$25") — with the explicit warning that losses will come in other periods. Principle: pair any decent reversal signal with 20-delta credit spreads and the 80% base rate of the options compounds with the signal's edge. [AayABdqDKIc]

**The Options Tribe weekly broken-wing butterfly (2013 webinar): 16-delta, sell-off-day entry, "a credit spread with a lottery ticket."** [N9mx7uz3vbw] Definitions: a conventional butterfly sells two options at/near the money and buys equidistant wings, so the total-loss risk is symmetric; the broken-wing version places the wings at unequal distances — RUT example long 1090P / short 20× 1070P / long 1020P: 20 points above the shorts, 50 points below — and is structured for a CREDIT. Payoff logic: market rallies, sits still, or dips slightly → keep the small credit; market sells off gradually into the "tent" late in the trade → very large return relative to the risk; market sells off too hard too fast, through the bottom of the tent → exit at a loss. Guidelines for a weekly put-side BWB: use index weeklies (no earnings gaps), enter about 10–14 days out, at ~16 delta, preferably on a sell-off day — volatility is up, so the credit is better and the strikes farther from the money (safer); "on the upside it's easy, you pocket the credit; on the downside you have to trade with some skill." Example 1, Dec 10 2013 (SPX selling off intraday at 12:30, market above its 20-day MA): 16-delta BWB, +$470 if held to expiry with the market anywhere above the tent. Day 2 big down day → −$610; day 3 more selling → ≈−$1,200 to −$1,260 at 8 DTE, having entered the body of the tent too EARLY (the shorts blew up); no exit trigger yet; the next day flat, then time decay over the weekend restored near-breakeven; Dec 17 another selloff to the tent's edge; Dec 18 the index sold into the center of the tent and then a Fed-announcement rally jumped price out the top — the 20 shorts sold @5.55 now @1.81 → closed for a profit of more than 1% of the capital in the trade, 8 days into a 10-day trade. Example 2, Sep 18: shorts sold @1.00, credit $157 for anything above 1700 at expiry; a rare slow grind lower INTO the tent: +$930 (≈6× the credit) mid-week, ≈15× the credit two days before expiry after a Thursday rally, and on the last day the index closed almost exactly at the short strike → ≈+$8,000 on a $9,800 worst-case position in one week — the butterfly's maximum, "not going to happen much," and no trader he knows would sit through expiration-day gamma for it (most would have exited earlier that day up less). Standard disclaimers: hypothetical prices, slippage and commissions may make them unattainable; start with very low capital. [N9mx7uz3vbw]

**The weekly DOUBLE broken-wing butterfly (SPX, ±45 points): 7% in the range, 29% in the "tent."** [toMmfKHzQXU] A weekly variant of the desk favourite, sized so both sides are entered for a credit and the trade complements a day/swing trader's book (it wins precisely when the market isn't moving). Aug 30 (2019), SPX ≈2935, Sep 6 chain: call side — buy 5× 2980C (45 points up; $2,745), sell 10× 2990C (+$3,490), buy 5× 3010C as protection (−$585) → +$160 credit; put side — buy 5× 2890P (45 points down; −$6,180), sell 10× 2880P (+$10,570), buy 5× 2860P (−$3,855) → +$535 credit; total +$695, broker margin ≈$9,300. At any expiry between the highest put (2890) and the lowest call (2980) every option dies and the $695 is kept = >7% in a week. The windfall zone: Sep 6 close 2984.10 (transcript "28 94 10"; the arithmetic that follows requires 2984.10) — all puts, the 2990C and the 3010C worthless, but the five long 2980Cs are 4.10 in the money → 5 × 4.10 × $100 = $2,050, plus the $695 credit → +$2,745 = 29% on margin in one week. The structure pays big when the index pushes just past the long strike on either side "as long as it doesn't go too far" — a two-sided version of the 5a windfall scenario [vU64DYL3raU]. [toMmfKHzQXU]

**Finding a 90%-probability trade in three minutes: the 10-delta credit spread on an RSI extreme (SPX 2024–2025).** [4dedQBgiZJA] Delta ≈ probability the option expires in the money, so the 10-delta short strike wins ~90% of the time and is so far away that even a large move AGAINST the thesis often still wins. Bullish case: Apr 7 2025, SPX 5062.25 (from >6,100 earlier in the year, −17% after the first tariff announcement; RSI in the low 20s = capitulation): May 7 chain sell the 4200P (Δ≈10, >800 points below) @47.45 (+$4,745), buy the 4100P @40.35 (−$4,035) → +$710, capital / worst case $9,290; May 7 close 5631.28 → +$710. Bearish case: June 2024, SPX 5421.03, RSI >70: sell the 10-delta 5625C @6.95, buy the 5700C @2.45 → +$450, capital $7,050. The premise was wrong — the index rallied ~200 points to 5615.35 — yet it stopped short of 5625 → full win. "With credit spreads the farther you are from the money, the more likely you win — a mathematical fact"; pros use delta as the dial for win rate.

**Bollinger-band credit spreads placed one standard deviation away (RUT, Jun–Aug 2025: 5/5, +$2,200 ≈ 90%+ annualized).** [9q32G8yLxbM] Bollinger bands (20-SMA ± 2σ) flag overbought/oversold, but reversion often is not immediate — a stock/futures trade gets stopped out before it works. Fix: express the reversion with a one-week credit spread whose short strike sits at the platform's 1-σ boundary (~68% of moves stay inside), so the trade also wins if the reversal is late or never comes. Jun 10 2025, RUT closes 2156.41 above the upper band → Jun 17 chain: sell 10× 2225C @5.10 (+$5,100), buy 10× 2230C @4.55 (−$4,550) → +$550, capital $9,450; Jun 17 close 2101.96 (straight back to the SMA) → +$550. Jul 1 upper-band close → Jul 8 chain sell 10× 2255C / buy the next strike → +$750, capital $9,250; the index kept RALLYING to 2246.23 — never reached 2255 → +$750 anyway. Aug 1 close 2166.78 through the LOWER band → Aug 8 chain sell 10× 2085P, buy 10× 2080P → +$750; Aug 8 close 2218.42 → win. Aug 13 (+$700) and Aug 22 (+$750) upper-band touches → both call-spread wins. Five for five, $2,200 in one quarter on ~$9.4k capital. Credits for a 1-σ, 5-point, 10-lot spread cluster around $550–750 because the market prices a 1-σ move similarly each time.

**The weekly SPX put broken-wing butterfly ("52 bites at the apple, with a lottery ticket").** [xrCSOh4WEGY] The desk's income traders are measured over 12 monthly cycles; this is the rules-based weekly alternative. Jun 13 (2019), SPX 2889: buy 5× 2830P @6.83 (−$3,415), sell 10× 2820P @5.56 (+$5,560), buy 5× 2800P @3.71 (−$1,855) → net credit $290; broker margin ≈$4,700 = the capital, the credit = the target (≈6% in 7–8 days). Rules: short strike = the 10-delta put (~60 points below); the upper long 10 points ABOVE the shorts in all cases; the lower long placed wherever it makes the credit ≥5% of capital; enter only when SPX is above its 20-day SMA; enter/exit Thursday ~1 hour after the open; stop = −10% of capital (the loss case is an early, fast selloff that makes the shorts too pricey); exit early if the 20-SMA is crossed. Outcome: close 2956 → all three strikes worthless → +$290. The lottery ticket: had SPX closed at 2825, the 5 long 2830P pay $500 each = $2,500 + the $290 credit = $2,790 = 59% in a week — a late-week selloff INTO the structure (60–70 points) pays >50%, while rally / flat / modest drop pay the 5–6%.

**One-day SPX credit spreads on a directional signal — the SMB × InvestiQuant backtest (Options Tribe webinar, Dec 2020).** [qabKcPmwjEA] Seth Freudberg + Scott Andrews: nine months / hundreds of hours combining InvestiQuant's adaptive one-day S&P-futures signal (ensemble of systems since 2013, raw futures win rate 65–69%) with same-day SPX credit spreads. Why a credit spread: it has layers of protection — six cases, five of them win: (1) signal very right: Mar 9 2018 open 2756, sell 2750/2730 put spread @4.45/0.95 → +$350, index +30 → full credit; (2) slightly right: open 2923, 2920/2900 → +$400, closes +1 → full; (3) flat: open 2783, 2780/2760 → +$508, +0.20 on the day → full; (4) slightly wrong but above the short strike: open 2777, 2770/2750 → +$230, close 2774 → full; (5) partial win: open 2932, 2930/2910 → +$300, close 2927 → short put pays $280 → still +$20; (6) very wrong = loss: open 2730, 2730/2710, credit $465, close 2718.60 → short pays $1,140 → −$675. Backtest Jan 1 2018 (when Mon/Wed/Fri SPX expirations began; Tue/Thu trades are closed at the bell) → Sep 30 2020, single contract, slippage + commissions included, early-close and circuit-breaker days excluded. Findings: (a) strike selection — farther OUT of the money spreads beat ATM / 1-strike-ITM on both win rate (+3.5–4 points for 5-point spreads) and profitability, "dramatically" for wider OTM spreads; (b) rounding (distance from the open to the short strike, <5 vs >5 points) changed the credit only ~14% — the least important factor ("don't be a dick for a tick"); (c) day of week — Tue/Thu credits >20% higher than M/W/F but closing debits disproportionately larger → lower expectancy (their signal is also weaker Tue/Thu); (d) implied volatility — average credit on a 20-point spread: VIX <15 $334, 15–25 $504, >25 $692; higher VIX pays more but the win rate falls (an ATR >100 makes a 20-point spread easy to breach) — profitable in all three regimes, VIX is the #1 factor; (e) entry 9:30 vs 9:45 — identical win rate, ~7% lower annual return, LOWER max drawdown (half the time a delayed entry gets MORE credit because decay in 15 minutes is small vs the move); (f) no stops, no adjustments, zero discretion — the long strike is the stop; every intraday-exit rule tested over two weeks lost money because you pay for the remaining time value when you close early; (g) the SPX first print is untradeable (an average of a subset of opens — ~25% of platform opening prices never traded in the first 10 minutes) → they model the open from futures fair value (three overnight futures sessions, dividends, rates, roll dates), which improved results. Resulting strategies: ~25–40% annual returns with drawdowns well under half of that, 10–20-point wings and others, credit-spread win rates 10–15 points above the raw signal (some >80%), trades roughly once a week to once every 10 days (many likely signals are cancelled by the last 15 minutes of pre-open action). Pre-2018 validated with a regression model of credits/debits. Long calls/puts on the signal: inconclusive — time decay flips against you. Debit spreads are economically identical; credits are just easier to teach.

**Take 50% of the credit and redeploy: 10 trades instead of 3 in the same half-year.** [tXD17g377NY] A bullish 2024 outlook (the S&P ran +14.4% through June 30) traded as a rolling 60-DTE 20-delta SPX put credit spread program starting Dec 18 2023 — the first trading day after the December third Friday, chosen because third-Friday chains are published many months in advance and are therefore always available when you want a longer-dated trade. **Hold-to-expiry version:** sell the Feb 16 4575P @33.85 (+$3,385, ~165 points below the index) and buy the 4475P @22.40 (-$2,240) → +$1,145 credit on $8,855 of capital, and by the chain's own deltas there is an ~80% chance of a close at or above 4575, where the full credit is kept; SPX expired 5005.57 → full win. Redeploy into the Apr 19 chain (63 days): sell 4800P / buy 4700P → +$1,075 on $8,925; the index actually sold off over those 63 days yet still finished comfortably above the short strike — the point of selling 20-delta options. Then the June trade, 4700/4600 → +$1,275; SPX closed 5464.61 → win. Three trades, +$3,495 = 39.15% measured against the largest capital any single trade required. **50%-of-credit version:** close each spread the moment its profit reaches half the entry credit, then immediately open a new ~60-day trade. The first spread reached +$590 (51.5% of its credit) on January 11, only 24 days in — both puts had shrunk on a mild rally plus 24 days of decay — so it was closed and the Mar 15 4645 put spread opened for $1,045, which itself passed the 50% mark by January 25 (SPX opening 4892.10). Same six months, ten trades instead of three, several of them hitting 50% within 7 to 10 days. The principle is opportunity cost: waiting another 50 days for the second half of a credit ties up capital that could be earning the fast first half all over again — professionals optimise the utilisation of capital, not the last penny of any one trade. (The same doctrine at a 75-90% threshold: [TpAPTwLMb44][v_27P1SNZTU].) [tXD17g377NY]

**The Weekly Options Income Machine, in full (the InvestiQuant workshop numbers).** [DGnUHMPbcJA] Background to the partnership: since Jan 1 2018 SPX has listed Monday, Wednesday and Friday expirations — from 12 expirations a year to more than 150 — which is what makes a daily-signal credit-spread system possible at all. Scott Andrews' firm InvestiQuant (North Carolina) spent four years and $1.5 million, working with Duke University's Center for Quantitative Modeling, building the "IQ adaptive ensemble signal", a multi-indicator algorithm that each morning calls the close higher than the open, lower than the open, or too close to call. SMB and InvestiQuant then spent ten months testing which credit spread best expresses that signal — strikes near the money vs far, entry at 9:30 vs waiting until 9:45, every weekday vs only the Mon/Wed/Fri expiration days — and shipped the resulting system: long signal ⇒ put credit spread, short signal ⇒ call credit spread, at a proprietary location. **Why a credit spread beats buying the direction:** of six possible outcomes the trade wins five — market closes much higher, slightly higher, exactly at the open, below the open but above the short strike (all four = full credit), and slightly below the short strike (a partial win); only a close well below the short strike loses. Worked example, Mar 1 (2021), SPX opens 3869: sell the 3860 put @9.51 (+$951) / buy the 3840 put @4.71 (−$471) → +$480 net. Close at 3901 → both worthless → +$480. Counterfactual close at 3857 — three points INSIDE the short strike — pays out $300 on the short put, so the "wrong" direction still nets +$180. **Live-signal results since the Mon/Wed/Fri chains existed (468 tested periods):** win rate 86.4% — 76.1% full wins (356 of 468), ~10% partial wins, 10.9% partial losses, and under 3% maximum losses. Returns scale with account size because each trade consumes only about $1,700–$1,800 of capital: $20,000 account → 42%, $15,000 → 56%, $10,000 → 85% (the marketing headline is "40%+ yearly average"). Capital doctrine from the Q&A: $20,000 recommended, $10,000 the floor — never an account equal to one maximum loss, since the sub-3% total-loss case would wipe it out; you must hold multiples of the max loss. Time commitment: 10–15 minutes a week. Desk colour from the same session: SMB is home to 50+ traders, and the options desk traders are mostly in their 40s, 50s and 60s and entirely virtual (US, Europe, Asia, Australia). [DGnUHMPbcJA]

## CHAPTER: Non-directional income strategies

**The concept.** [w_BjFmbwbYA] Market-neutral option-selling strategies (straddles, strangles, iron condors, butterflies, calendars, double diagonals) profit whether the market rises or falls, as long as it stays inside a price range. You only need to get the *range* right, not the direction; with wide-range structures like iron condors the win probability can be set north of 80% and even 90%. This is why traders "fall in love" with options income trading.

**Iron butterfly — worked example.** [w_BjFmbwbYA] Friday in early June, index ≈1880; pull the chain 8 weeks out (late July). In a single complex order: sell the 1880 call @ 83.95 and the 1880 put @ 84.40 (at-the-money straddle), buy the 1980 call @ ~37.55 and the 1780 put @ 49.65 as 100-point wings. Net credit $8,115; broker margin requirement ≈$1,885 (the worst case; note cash credit + margin = wing width $10,000 — the transcript's "18.85"/"18 150" figures are garbled). The credit earns interest while held if the broker pays interest on cash. Expiry July 29: index closed 1885.23 → only the short 1880 call is ITM, paying out $523; everything else worthless → profit $7,592, a >400% return on margin in 8 weeks. Had the index instead closed 1840, the short put would have paid out $4,000 and the trade still made ≈$4,115. General rule: the butterfly wins whenever the payout on the tested short strike is less than the credit collected — breakevens are short strike ± credit ÷ 100 points (here 1880 ± 81.15 → ≈1798.85 / 1961.15; the transcript misstates these as "1718"/"1881.15" by mixing up the center strike).

**Why professionals trade broad-based index options for income.** [tOMQNDXnczY] Income trading is the one style where you want the market NOT to move, and indexes are the ultimate diversification: no single company's earnings surprise or industry shock can send the whole index "wacko." Traders use SPX, NDX, RUT. Index options are cash-settled, very liquid with efficient fills, offer multiple expirations per week (SPX daily — ~250 "bites at the apple" a year vs 12 in the monthly-only era), and carry tax advantages worth asking an accountant about. Professional income traders find a high-probability structure, backtest it, then trade it over and over; when the market escapes the range (the ~15%), they don't sit like ducks — they have adjustment techniques to extend the range. [tOMQNDXnczY]

**Iron condor sized to a chart channel (60–64 DTE).** [tOMQNDXnczY] Dec 15 2022: SPX had channeled 3500–4300 for eight months. Bracket the channel on the Feb 17 chain (64 DTE): sell 10× 4350C @ 15.20 (+$15,200) and 10× 3500P @ 23.20 (+$23,200); buy 10× 4375C @ 12.70 (−$12,700) and 10× 3475P @ 20.95 (−$20,950) → +$4,750 credit, $20,250 margin (the worst case). Short strikes sit at the channel's resistance and support; statisticians put ~85% on the index staying inside that 850-point range for 60 days. Feb 17 close 4079 → all four legs die → +$4,750 = 23.4% on capital in nine weeks. [tOMQNDXnczY]

**Iron condor at 5-delta, 60 days, rolled as a year-long campaign.** [m8R_564Kp6k] Use the delta column instead of a chart: sell the ~5-delta call AND ~5-delta put (each ≈95% likely to die worthless → ≈90% probability of full profit for the combination), wings 25 points out, entered on a third-Friday chain ~2 months from expiry, then immediately re-enter on expiry. Sep 15 2023, SPX 4450.32, Nov 17 chain (63 DTE): sell 10× 4800C @ 4.30 (+$4,300), buy 10× 4825C @ 3.30 (−$3,300), sell 10× 3875P @ 9.40 (+$9,400), buy 10× 3850P @ 8.80 (−$8,800) → +$1,600 credit, $23,400 margin; a 925-point (≈20%-wide) profit zone; close 4514.02 → win. The year's six trades: +$1,600, +$1,500 (4875/4900C–3950/3925P, close 4839.81 — only ~35 pts under the short call and still a full win), +$1,550 (range 4275–5200), +$1,550 (range 4575–5575 — ranges widen when vol rises), +$1,450 (range 4725–5700), and the Sep 2024 trade +$1,570 (1175-pt range; closed 10 days early for $130 because barely any value remained). Total ≈$9,220 on max margin $23,550 ≈ 39% for the year — 4–5× a historical equity return, every trade starting ≈90% likely to win. [m8R_564Kp6k]

**Iron condor, six-month RUT channel version — 107% on margin.** [bDhYEMCLm9k] Mar 9 2023: RUT at 1826, almost exactly the middle of a year-long 1650–2000 channel; condor traders like entering mid-channel. Sep 15 chain (~6 months): sell 5× 2000C @ 55.95 (+$27,975), buy 5× 2050C @ 39.90 (−$19,950); sell 5× 1650P (+$22,525 per transcript's "2,525" garble ≈ @45.05), buy 5× 1600P @ 41.20 (−$20,600) → stated net credit $12,950 with ≈$12,050 margin (transcript prints "$1250"; legs as transcribed sum to $9,950 — flagged, the wing width 50 × 5 lots caps total at $25,000 either way). Sep 15 close 1847.03, mid-range → all worthless → keep the full credit, stated as a 107% six-month return on margin. The trade pays identically at ANY close in the 350-point 1650–2000 zone; want more safety → move both spreads further out for less credit. [bDhYEMCLm9k]

**Adjusting an iron condor: roll the threatened side (swing-trade version).** [QsccAA3k_1o] You are never a sitting duck once a short strike is approached — the trades "don't begin and end with the same position." Worked example on an unnamed ~$1,060 stock (real prices), 51 DTE January chain: sell 4× 1125C @21.85 (+$8,740) / buy 1150C @14.30 (−$5,720); sell 4× 1000P @19.45 (+$7,780) / buy 975P @14.25 (−$5,700) → +$5,100 credit, profit zone 1000–1125. Pre-set adjustment rule: if the stock comes within 5 points of either short strike, roll that side 50 points farther out. Nov 20 (19 days in) the stock hits 1003 → roll: buy back 1000P (−$15,780), sell the long 975P (+$11,980), sell 950P (+$8,640), buy 925P (−$6,560) → roll cost $1,720, leaving $3,380 of credit and a widened 950–1125 zone (125 → 175 points). Expiry: stock closes 980 — BELOW the original short put (which would have been "killed") but above the rolled one → all four legs die → +$3,380 kept. You can roll more than once and still finish positive if the move keeps grinding. [QsccAA3k_1o]

**High-win-rate danger and portfolio design** are covered in the principles chapter — these income structures win most of the time by design, which is precisely what makes over-sizing them lethal. [MmryR1iu9dA]

**The iron butterfly as the desk's core income setup — the SPX 2815 example.** [FNKIDMBPcaI] Most options income traders on the desk gravitate to the butterfly: excellent initial risk/reward (typically 3:1 up to 10:1 depending on structure) and easy modification mid-trade to adapt to market conditions while keeping profit potential. Worked 10-lot with ±25-point wings, SPX at 2815: sell 10× 2815C (>$18,000) and 10× 2815P (>$17,000), buy 10× 2840C @6.95 (−$6,950) and 10× 2790P (≈−$10,000) → net credit $19,400; broker margin $5,600 (the worst case: $25,000 wing width − credit) → R:R >3:1. Frame the trade as "give back as little of the $19,400 as possible." Mar 13 expiry close 2810.90: both calls and the 2790P die; the short 2815P is 4.10 ITM → −$4,100 → keep $15,300 (transcript prints "15,400" then "15,300 profit"; 19,400 − 4,100 = 15,300). Caveat from the teacher: most butterflies do not end this well, and most pros would have started closing/cashing chips earlier than expiration. Index-option payoff drill in the same lesson: SPX 3000, 3010C → +$500 at 3015, worthless at 3009 or lower; 2985P → +$1,000 at 2975, worthless at 2985 or higher. [FNKIDMBPcaI]

**Iron condor at 10 delta, two months out, closed at 50% of the credit (the "first strategy I ever learned").** [F4d_OIVawns] Freudberg's beginner recommendation and his own first options trade 18 years earlier: on the third Friday, on the third-Friday chain ~2 months out, sell the ~10-delta call and the ~10-delta put and buy wings 50 points beyond each. Probability logic spelled out: a 10-delta short call has ~10% chance of finishing ITM (the long call above it even less), likewise the put side, so ~20% chance that either side pays and ~80% that all four options die — the "high-probability iron condor." Management rule: close the whole position (reverse all four legs) as soon as the open profit reaches ≥50% of the initial credit, then wait in a disciplined way for the next third-Friday entry so the campaign runs exactly six times a year; trying to squeeze the rest of the credit "can backfire" when a trade that had hit a nice number turns bad. Worked campaign, RUT 2023: Jun 16, RUT open 1898.54, Aug 18 chain: sell 1× 2100C (10Δ) @6.15 (+$615), buy 2150C @3.35 (−$335); sell 1690P (10Δ) @10.40 (+$1,040), buy 1640P @7.35 (−$735) → +$585 credit, broker capital $4,415 (= $5,000 wing width − credit = worst case). Jul 12, RUT 1935.7: legs 3.50 / 1.50 / 3.25 / 2.35 → closing nets +$295 (>50%) → out. Aug 18 (afternoon, RUT ≈1862), Oct chain: 10Δ calls = 2050, 10Δ puts = 1650, wings 2100 / 1600 → +$667 credit, capital $4,333 (transcript prints "433"); Sep 5, RUT 1893.7 → again slightly above 50% → out. All six two-month trades of the year closed at the 50% mark → >$1,800 of profit against the most capital any trade needed ($4,490 for the June trade). Two takeaways: in a campaign you need not squeeze every dollar out of each trade; and even if you are forced to sit to expiration, the low deltas mean a high chance the index finishes between the shorts. The decay mechanism is time: a month later with the index only ~37 points higher, the 2100 call — still 165 points away but with a month less to get there — is worth far less. [F4d_OIVawns]

**The 10-delta 60-day SPX iron condor through the 2022 bear market (6/6, +127%) — and the delta-doubling roll.** [KPcDNIqd4OI] The "80% win-rate, no direction needed" campaign: six times a year, on the chain ~60 days out, sell the ~10-delta call and ~10-delta put and buy the options 10 points further out. Trade 1 — Jan 3 2022 (SPX opened the year at 4788.89 after +27% in 2021), Feb 28 chain: sell 10× 5050C (Δ10.77 → 89.23% chance of expiring worthless) @10.20 (+$10,200), buy 10× 5060C @9.20 (−$9,200); sell 10× 4260P (Δ10.11) @22.90 (+$22,900), buy 10× 4250P @22.30 (−$22,300) → +$1,600 credit, broker requirement $8,400 (worst case). Feb 28 close 4373.94 (the year's selloff already >400 points) → still >100 points above the short put → all four die → +$1,600. Trade 2 — Mar 1 open 4368.19: 4790C/4800C + 3650P/3640P → +$1,750; Apr 29 close 4131.93 → win. May–Jun: shorts 4570C / 3390P → +$1,900. Jul–Aug: range 3200–4230 (1,000 points wide), close 3955 → +$1,750. Sep–Oct: range 3380–4340, close 3871.98 — but on Oct 13 (SPX 3553 after touching 3491) the 3380P's delta exceeded 20: the doubling of the loss probability is the line in the sand → close the 3380/3370 puts and re-open at the new 10-delta, 3250/3240, at a cost of $1,150 (transcript later says "$150"; 1,800 − 1,150 = 650 confirms $1,150) → the trade finishes +$650 instead of +$1,800. Nov–Dec: similar, a win. Year: 6/6, total $10,750 on a maximum $8,400 of capital = 127% — "not normal": in a bear year that channeled, everything expired worthless; expect ~80% long-run (100 − 10 − 10). The roll's cost is the price of safety; "in the long run applying sound risk management is always the right decision." (Compare the 5-delta 2023–24 campaign [m8R_564Kp6k] and the RUT 10-delta 50%-exit version [F4d_OIVawns]; the delta-doubling trigger is the same rule as in [-Dfl8YyoP0E] and [xidgg27-yWU].) [KPcDNIqd4OI]

**Blunder #7 — "Why waste money buying long options to protect my short options?" (short strangle vs iron condor).** [4iCQciAzjJY] August 2019, NDX 7966, 29 DTE (Aug 30 chain): a 1-lot short strangle — sell the 8325C (~350 points above the all-time high) @14.80 and the 7350P (~600 points below, a level not seen for months) @25.30 (first spoken as "23.60" — garble) — for +$4,010 of premium; broker requirement ≈$83,000 (also "83,600"), because the risk beyond the strikes is unlimited at $100/point. Aug 30 at 2pm, NDX 7677: call 0.25, put 0.17 → close for +$3,968 = 4.7% on the capital. The "dumb-looking" alternative: also buy the 8350C @11.75 (−$1,175) and the 7325P @23.60 (−$2,360) → a 25-wide iron condor for only +$475 — but the broker margins it at $2,025 (= $2,500 width − credit), because the longs cap the loss 25 points past each short. Trade 20 of them: +$9,500 credit on ≈$40,500 of capital — less than HALF the strangle's requirement — closed on the same day for +$9,360 = 23% vs 4.7%, with a hard-capped instead of infinite worst case. "Infinity is a lot": the strangle's $83k margin is a finite number for a theoretically unbounded loss. Protection is not wasted money; it is what makes the return on capital. [4iCQciAzjJY]

**Turning a threatened iron butterfly into an iron condor with a call-side butterfly (the profit-zone expansion).** [ud2KQ-Di57Q] The butterfly is the desk's most popular strategy partly because its large initial profit potential can be *spent* mid-trade to widen the range over which it wins. Worked SPX iron butterfly, Feb 1 2019, index ≈2725: sell the 2725C (>$4,300) and 2725P (>$5,600), buy the 2825C @8.95 (−$895) and the 2625P (≈−$2,500; wings 100 points each side) → net credit $6,623; broker margin $3,400 (the worst case). Profit range at expiry ≈2660–2790 with the maximum at 2725. Pre-set game plan: adjust if the index touches either breakeven. Feb 22: SPX reaches the upside breakeven 2790 → BUY a call-side butterfly centered on the existing long call: buy 1× 2725C, sell 2× 2825C, buy 1× 2925C, cost $5,139 → credit remaining $1,484. Position algebra: the new long 2725C cancels the short 2725C; the existing long 2825C plus two sold 2825Cs = short 1× 2825C; a new long appears at 2925 → the iron butterfly has become an iron condor (short 2825C / long 2925C above, short 2725P / long 2625P below). Mar 14 (last trading day) close 2810 → every option finishes OTM → the whole remaining $1,484 is kept (spoken "$1,400"), versus a loss of >$1,500 had the original butterfly been held with the index above its 2790 breakeven. Pros "don't sit there and allow their trades to lose money"; the earlier 0-DTE butterfly-roll and condor-roll teachings are the same move on a same-day clock. [ud2KQ-Di57Q]

**The pre-election one-week iron butterfly rescued by a PUT-side butterfly roll (Oct 2020).** [qm5ENAPUCEA] Binary-event tendency: ahead of a presidential election the market pauses in a channel (2016: four months in 2100–2200 before the post-election breakout; 2020: 3200–3600 while flagging near the highs) — a family of range strategies prospers in that pause. Oct 16 2020, SPX ≈3500, one week out (Oct 23 chain): sell 3× 3500C @37.85 (+$11,355) and 3× 3500P @35.81 (+$10,743); buy 3× 3590C (−$1,938) and 3× 3410P (90-point wings; the transcript's "11,850" for the long puts cannot be — the stated $16,821 net requires ≈$3,339, i.e. ≈11.13 per put) → +$16,821 credit, broker requirement a little over $10,000. Since the index will not close exactly at 3500, one short side WILL pay out; the trade profits as long as that payout is smaller than the credit — breakevens from the risk graph ≈3443 / ≈3556, profit rising toward the 3500 centre. Pre-set rule: adjust when either breakeven is exceeded. Oct 19 (three days in): SPX below 3443 → put butterfly roll: buy back the 3× 3500P (expensive after the drop), SELL 6× 3410P (flipping the 3 longs into 3 shorts; transcript once says "3420"), buy 3× 3320P 90 points lower → a little over $7,000 of the credit remains; margin rises ~20% to a little over $12,000. Oct 23 close 3465 → the 3500C/3590C are above the market, the 3410P/3320P below → all expire worthless → keep the ≈$7,000 = ≈60% in a week. Not a promise of 60% per week: the point is that a calm-market trade hit by an outsized move was "not at all a lost cause" because the repair was ready in advance and widened the profit zone. [qm5ENAPUCEA]

**The double diagonal as a monthly campaign on a flat chart (TLT 2025, +77.5%).** [YLrRxUUHl44] Presented as "the most consistently profitable options strategy" for traders of all levels, with a three-item checklist before any entry: (1) a FLAT price chart — TLT (20–30-year Treasury ETF) had spent two years mostly between 87 and 100 (extremes 82–109) and closed 87.57 on the first trading day of 2025; (2) at least one expiration every month of the coming year (some chains are quarterly-only — disqualifying); (3) tight bid-ask spreads, typically 1–3 cents on TLT. Entry protocol on the third Friday, 12 times a year: on next month's third-Friday chain sell the first call and the first put whose delta is BELOW 20 (10 lots each in the example); on the chain one further month out buy calls 5 points above the short call and puts 5 points below the short put, same lot size. Delta reminder: a 20-delta option has ≈20% probability of expiring with value, so each short has ≈80% chance of dying. Trade 1 — Jan 17 2025, TLT close 87.19: sell 10× Feb 21 91C (Δ18.23) @0.36 (+$360) and 10× 83P (+$340); buy 10× Mar 21 96C (−$240) and 10× 78P (−$220) → +$240 net credit; broker requirement $4,760 = worst case. Feb 21 close 89.61: both shorts expire worthless; the March longs still carry 28 days of life — 96C worth 0.11 (sell for $110), 78P ≈0.01 (+$10) → trade profit $360. Trade 2 (entered Feb 21): short Mar 93C (Δ18.36) / 86P (Δ13.39), long Apr 98C / 81P → +$250 credit, capital $4,750; Mar 21 close 90.70 → shorts die, longs sold @0.10 / 0.02 → +$370. Trade 3 (Mar 21): short Apr 94C / 88P, long May 99C / 83P → +$280, capital $4,720; Apr 17 close 87.53 — BELOW the 88 short put: protocol = buy the ITM short back before expiry to avoid assignment (cost 0.47 = −$470) while the long puts had "blown up" and were sold for $470 (the transcript calls them "the 88 puts we own in May"; per the entry they are the May 83 puts — flagged) and the long calls for $60 → still +$340 despite the range breaking slightly. That was the only month of the twelve in which a short did not expire worthless; every later month TLT finished between the shorts. Year: +$3,645 = 77.5% on the ~$4,750 capital — with the explicit caveat that other years will include losses, and that finding the flat chart is the hard part. [YLrRxUUHl44]

**Why income trading wins so often: the 60-day 10-delta iron condor campaign on AMZN (2019, +56% through September).** [8u89hMA2was] "Options income trading" = build a wide zone of prices over which the trade profits by combining short and long options; the iron condor is the simplest form. The 10-delta option is far from the stock, and the more volatile the stock, the farther away it sits. Nov 20 2018, AMZN 1502, Jan 18 2019 monthly chain (60 DTE): sell the 1900C (10Δ, 400 points up) @8.81 (+$881), buy the 2000C @4.77 (−$477); sell the 1200P (10Δ, 300 points down) @15.03 (+$1,503), buy the 1100P @7.22 (−$722) → +$1,185 credit, capital ≈$9,000, a 700-point max-profit zone (≈80% statistical likelihood of staying inside). Jan 18 close ≈1696 → all four expire → +$1,185. Roll the freed capital every ~60 days: Mar 15 chain 2050C/1400P (650 wide) +$907, close ≈1710 → win; May 17 chain 2000C/1450P (550 wide) +$1,011, close ≈1810 → win; July chain +$913 (550 wide, AMZN 1881 at entry), close ≈1969 → win; Sep chain 2250C/1700P, close 1794 → win. Five for five = $5,082 = 56% on $9,000; Nov trade 2050C/1550P open with AMZN 1770 mid-range. Homework recipe: a stock priced ≥$300 (commissions matter less), chain ~60 days out, shorts ~15% OTM or at the 10-delta, longs a few strikes beyond, credit ≥$1.00 for the whole condor, paper-trade it first.

**Managing an iron condor like a pro: scalp each side when its remaining reward is minuscule vs its risk (GOOGL, Oct–Dec 2019, +$1,562 with 17 days left).** [cSI1eXFW6Ms] A viewer-suggested trade from the AMZN video's homework: Oct 25 2019, GOOGL 1266 near its 1289 all-time high, Dec 20 chain (57 DTE): sell 2× 1400C (>100 points above the ATH = resistance thesis) @4.81 (+$962), buy 2× 1520C @0.38 (−$76); sell 2× 1100P (a level not seen since early summer) @5.14 (+$1,028), buy 2× 980P @1.10 (−$220) → ≈+$1,694, 84% probability of profit. Nov 7: GOOGL blasts through the ATH to 1322 → the put spread sold at 4.04 is worth 0.56 (−86%) → close the put side for $112 total, locking +$696 and eliminating all downside risk (had GOOGL crashed to 1075 by expiry the 2 short puts would have cost $5,000). Dec 3: GOOGL sells off, the call spread sold at 4.43 is worth 0.10 → close for $20 → +$866. Total ≈$1,562 ("over $1,500"), no position left, no risk to zero or infinity. Doctrine: "a professional trader knows when to shut down risk when the remaining profit potential of any aspect of a trade is minuscule compared to the remaining risk" — risk/reward relationships change over the life of an income trade; take the profit.

**Scalp each side of the condor at ~80% of ITS OWN credit.** [cSKJpuNX2lU] An iron condor is two independent credit spreads, and the desk's rule is to close either side as soon as it can be bought back for a profit equal to about 80% of that side's original credit — the remaining 20% is very poor payment for continuing to carry the full risk of that side. SPX, Dec 17 2018 at 2552 in the middle of the Q4 selloff, end-of-January chain, 20-point wings, 10 lots: sell 2660C @29.50 (+$29,500) / buy 2680C @24.03 (-$24,030) → call side +$5,470; sell 2330P (+$19,200) / buy 2310P @16.85 (-$16,850) → put side +$2,350; total credit $7,820 with $12,180 of required capital, which is also the absolute worst case. On Dec 24 at 12:45pm the market had crashed to 2366: the 2660 calls were 4.10 and the 2680s 2.98 → closing the call side (pay $4,100, receive $2,980) banks $4,350 = 80% of its $5,470 maximum, and from that instant a bounce is irrelevant to the trade because there are no calls left to worry about. By Jan 10 SPX had rebounded to 2596 with the puts collapsed (2330P at 3.00, 2310P at 2.58) → closing the put side banks $1,930 = 82% of its $2,350. Total +$6,280 = more than 51% of the capital at risk. What greed would have cost: SPX ended January at 2704.10, so the untouched condor pays out $44,100 on the ten short calls against $24,100 returned by the longs → -$12,180, the entire maximum loss, on a trade that had been worth +$6,280 in hand. Once a spread has shrunk to a very small cost to close, the remaining reward is not worth the risk of giving back everything — and this is the mistake professionals almost never make. [cSKJpuNX2lU]

**The weekly SPY iron condor and the put condor roll (Dec 10–17, 2021).** [LcqiRgKeGXg] Context for the trade: holiday and summer periods, when volume thins and no direction is discernible, are exactly when market-neutral income strategies earn their keep. SPY at all-time highs, 468.50 on Dec 10; on the chain expiring exactly a week later sell 8× 474C @1.16 (+$928) about 5.5 points above the market and 8× 463P @2.75 (+$2,200) about 5.5 points below, buying 8× 484C @0.10 (−$80) and 8× 453P @1.12 (−$896) ten points further out as wings → +$2,152 credit (the stated broker requirement, "28.48", is garbled; the structure's arithmetic maximum loss is $8,000 − $2,152 = $5,848). Four days later SPY sold through the 463 short put — and instead of taking the loss, **roll the whole put side down five points**: buy back 8× 463P (−$3,800), sell the 8× 453P wings (+$1,264), sell 8× 458P (+$2,320), buy 8× 448P (−$712) → a stated net cost of $918 (the itemised legs sum to $928), leaving $1,234 of the original credit. Dec 17 SPY closed 461 — above the relocated 458 short put and far below the untouched 474 call — so all four options died and the trade banked $1,234 for the week. The lesson is the mechanic, not the number: a condor roll WIDENS the range the underlying may close in, converting a threatened side into a smaller but intact win. [LcqiRgKeGXg]

**Building the condor in two steps — and dialling its probability yourself (SPY, Oct 10–17).** [ASsnZOKLXGg] Step 1: sell an OTM call well above and an OTM put well below the price. Step 2: buy a further-OTM call and put as protection — four legs, but every broker has a preloaded iron-condor ticket where you only fill in strikes. Why it works: the time premium of every out-of-the-money option is sucked out a little each day, so instead of fighting decay as a buyer you let it pay you. Worked trade, SPY 653.02 at the Oct 10 close, 7 DTE chain: sell 10× 666C @1.83 (+$1,830) and 10× 640P @3.17 (+$3,170) — both 13 points out — buy 10× 668C @1.35 (−$1,350) and 10× 638P @2.81 (−$2,810) → +$840 credit; maximum loss and broker requirement $2,000 − $840 = $1,160, whatever happens. Oct 17 SPY closed 664.39, inside all four strikes → keep the $840. **The loss case:** SPY at 695 → buy back the 666 calls for $29,000, sell the 668 calls for $27,000 → −$1,160, and the same −$1,160 at 700, 800 or infinity (at $800 the legs are $134,000 and $132,000 — always exactly $2,000 apart). **The partial-win zone:** SPY 666.50 → the short call costs $500 to close → still +$340; the true breakeven is 666.84, i.e. the profit range extends past the short strike by the credit per share. **The probability dial:** the chain's delta column doubles as the chance an option finishes in the money, so the condor's probability of full profit = 100 − short-call delta − short-put delta. This trade: 100 − 21.24 − 25.14 = 53.61%. Push the shorts out to the 670 call (13.30Δ) and the 626 put (11.67Δ) and the probability rises past 75% — but the credit falls to $430 while the capital required rises to $1,570. That is the whole trade-off, and it is entirely the trader's choice: more probability costs more capital and pays less, which is often the right purchase when the market is volatile. [ASsnZOKLXGg]

## CHAPTER: Calendar spreads & overnight trades

**Why calendars work.** [i5JOd15b_w0][oxNvLwZ0dGo][UG4f752OXq8] Sell an option on a near chain, buy the same strike on a later chain: the short option always sheds time value faster than the long one because it has less life left; near expiry the short can go to ~zero while the long must retain value to cover the days it still has. The relative decay is the profit engine — direction matters much less than the passage of a night or a day without a big move.

**Overnight IWM call calendar for ~$200.** [i5JOd15b_w0] Mon Nov 11, IWM closes 241.68 (year high): sell 1× next-day 242C @ 0.91 (+$91), buy 1× 242C expiring a week later @ 3.07 (−$307) → net cost $216 = max risk. Target: +5% of cost (~$11) — deliberately modest because the exit often comes minutes after the next open; pair it with a similarly modest stop or the economics break (find the exact target/stop combo by backtesting). Day 1: next morning 15 min in, stock 241.75 (barely moved): short call 0.91 → 0.57 (−34¢) while the long only 3.07 → 2.90 (−17¢) → close for $233, +$17 = 7.8% overnight. Day 2 (entered at 237.36 close: 237C next-day @ 1.92 vs week-later @ 3.49, cost $157): stock opens +1.73 — both calls RISE, but the long rises more (+62¢ vs +43¢) → +$19 = 12.1%. Day 3 (235 strike, cost $168): five minutes after the open short −30¢ vs long −19¢ → +$11 = 6.5%. Three consecutive days: +26.4% on capital at risk. IWM options are liquid enough to scale the same trade to many lots. [i5JOd15b_w0]

**Overnight SPY call calendar (daily-expiration version).** [oxNvLwZ0dGo] Daily expirations (only ~3 years old) make this an every-day strategy. Enter in the last 30 minutes: Jun 10, SPY 602.43 at 3:30pm → sell 10× 602C expiring tomorrow @ 2.59 (+$2,590), buy 10× 602C expiring in a week @ 5.43 (−$5,430) → cost $2,840 = worst case. Next day SPY closes 601.38 → short expires worthless; long (a week of life left, 27¢ OTM) still worth 4.56 → sell for $4,560 → +$1,720 = 60% overnight. Honest framing: this was an unusually good outcome — a big overnight move in either direction loses (a hard selloff guts the long call below the entry cost). Standard practice: backtest, then run ~10% profit target with ~10% stop, trade tiny for a long time, scale only after live results match the backtest. Context that year: SPY all-time high 613 in February, tariff-scare selloff into early April, recovered to 603.08 by Jun 10. [oxNvLwZ0dGo]

**0-DTE calendar.** [UG4f752OXq8] Same principle compressed into hours: Oct 16 2023, 10:30am, SPX 4375.09 → sell the same-day 4375C @ 10.70, buy the next-day 4375C @ 18.50 → cost $780 = worst case. Close 4373.63: the day's call expires worthless (even 1 cent OTM = zero), the tomorrow-call must keep overnight-move value → still 13.35 → +$555 = 71% in a day. [UG4f752OXq8]

**The one-month ATM calendar (SPX).** [rjHviGxmAKA] The cleanest long-horizon illustration of the decay differential: Sep 18 2019, SPX exactly at 3000 → sell the Oct 18 3000C @44.48 (+$4,448), buy the Nov 15 3000C @66.08 (−$6,608) → debit $2,160 = max risk (the two-month option must cost more, since two months of rally-risk exceeds one). Six days later, SPX back at ~3000: short −3.94 vs long −3.49 → +$45 unrealized — the differential grinding daily. Oct 18, SPX 2986: the short expires worthless (+$4,448 of premium fully earned) while the long, with 28 days of life, still sells for 32.97 → net profit >$1,100 on $2,160 ≈ >50% in a month. That outcome needed SPX to finish near the strike — infrequent, but the payoff when it happens is why calendar traders accept the small-debit risk. [rjHviGxmAKA]

**Post-earnings put calendar (UPS) — the small-account version.** [W5Gl_E2Sq-A] Thesis: a stock that moves on earnings but chops between reports is a calendar candidate the day after its release. Apr 30 2025, UPS closed 95.30 the day after earnings: sell 25× Jun 20 95P @4.45 (+$11,125), buy 25× Jul 18 95P @5.25 (−$13,125) → net cost exactly $2,000 (the shorts "drive down the price," which is why calendars suit small accounts). Convention: the trade is over the day the short expires. Jun 20 close 99.27: the short puts die; the July puts, with <1 month left and the stock 4 points away, are worth 1.24 → $3,100 → +$1,100 = 55%. The engine, restated: the earlier-expiring option always loses value faster; the later one always retains value because it must still cover the remaining downside risk. [W5Gl_E2Sq-A]

**The one-week vs three-week ATM call calendar on SPX (45% in under a week).** [0M8oc0T66yk] The cleanest short-horizon statement of the relative-decay engine: May 14 (2021), SPX opened ≈4150, hovering at its all-time highs for over a month → a market-neutral view. Sell 3× May 21 4150C @34.14 (+$10,242) and buy 3× Jun 4 4150C @60.45 (−$18,135) → net debit $7,893 = the initial capital. Why the later call costs nearly twice as much at the same strike: two extra weeks of potential rally the seller must be paid for. May 20 at ~11:15am (the May 21 calls are AM-settled and stop trading the afternoon before), SPX almost exactly where it was a week earlier: the short call has fallen from 34.14 to 13.30 (−20.8 points) while the long has only slipped 60.51 → 51.66 (−8.85; the transcript quotes the long's entry price both as 60.45 and 60.51). Close both: sell the long for $15,498, buy back the short for $3,990 → +$3,615 = >45% in under a week "purely because the S&P ended up at around the same price" — the key sentence: at the same strike and the same index price, farther-dated options lose value much more slowly than nearer-dated ones, because the market's likely move in five hours is far smaller than over the next two weeks. [0M8oc0T66yk]

**The overnight 20-delta SPX iron condor (May 2025: +$710 on $1,790 = 39% overnight).** [8BjBWBuiEh8] For traders who want profits in less than a day and will accept overnight risk, which the options market pays for. May 27 (2025), ~3:30pm, SPX 5914.87 after bouncing >1,000 points from the Apr 7 intraday low 4835: on the NEXT-day chain sell the call closest to 20 delta (5950C, +36 points) @6.00 (+$600) and the ~20-delta put (5875P) @6.45 (+$645); buy the wings 25 points beyond, 5975C @2.00 (−$200) and 5850P @3.35 (−$335) → +$710 credit, broker capital / worst case $1,790. Each 20-delta short has ~80% probability of expiring worthless. Next day: gap up to ~5940, reversal, close 5886.55 (−35) — never touched 5875 → all four expire → +$710. It will not win every time: a push past a short strike costs $100/point (a partial win if less than the credit, a loss up to $1,790 beyond). Pro protocol: backtest with options software to set a stop well below the max loss and a target below the max credit; trade small at first to test your psychology; SKIP the trade when a major company reports after the close or before the next open, or when NFP / CPI land the next morning.

**The double diagonal as a rolling campaign (SPX, Nov 2020).** [5UNql894bD4] Structure: buy a wide long strangle in a chain roughly two weeks out, sell a narrower short strangle in the NEXT chain in time (a few days out), then repeatedly buy the shorts back minutes before they expire and re-sell the SAME strikes in the following chain. Every such roll necessarily brings in cash, because the option you are selling always has more time left — and therefore more risk for its seller — than the one you are buying back. Worked campaign: Nov 16 2020, SPX at 3621 after making all-time highs off the March COVID lows. Buy the Dec 2 3690 call @20.40 (-$2,040) and the Dec 2 3550 put @32.65 (-$3,265) — 70 points either side, a distance set by the market's implied volatility rather than chosen at random → -$5,305 laid out. Sell the Nov 18 (three-day) 3670 call and 3570 put, 50 points either side → +$1,273. Nov 18, fifteen minutes before expiry with SPX at 3581: the expiring shorts are nearly worthless → buy them back and re-sell the identical strikes in the Nov 20 chain (the 3670 call fetches only about 0.57, but the 3570 put fetches a full 16.22 because the market sits 11 points above it with two days left) → net outlay down to $2,401. Roll again on Nov 20 (SPX 3571) into the Nov 23 chain → outlay down to about $1,000; by the Nov 27 → Nov 30 roll the cumulative cash flow has turned POSITIVE at +$442. Nov 30 close 3621 → the shorts expire worthless and all that remains is the original long strangle, sold for $172 (call) + $217 (put) → total +$831, better than 15% in two weeks. The generalisation: options income trading is in many cases simply selling short options against long options until the accumulated credits exceed what the longs cost. [5UNql894bD4]

**The double calendar around a MACRO event — booking the profit before the event happens (Brexit, 2016).** [CNEYo3P-CRk] The same mechanic as the earnings double calendar, applied to FOMC days, CPI and jobs reports, or a referendum: the options market grows more nervous as the event approaches, and that nervousness is itself the tradable object — you can collect it and be flat before the violent move. Setup: the UK's EU referendum was set for Jun 23 2016; start about a month earlier, May 23 2016, with SPX channelling between 2000 and 2100 for two months, the consensus being that nothing much happens before the vote. Sell 10× Jun 17 (pre-event) 2100 calls at resistance @5.25 (+$5,250) and 10× Jun 17 2000 puts at support @13.90 (+$13,900); buy the SAME strikes in the Jun 30 (post-event) chain: 10× 2100C @11.90 (−$11,900) and 10× 2000P @23.85 (−$23,850) → net debit $16,600, which is the entire risk. Jun 16, 12:30pm ET: SPX 2064 with three and a half hours of life left in the short options — they would need a 36-point rally or a 64-point break to have any value, so the market has marked them to pennies; the long options, still exposed to the referendum seven days later, retain nearly all of their (implied-volatility-inflated) value. Close it: sell the long calls for $13,750 and the long puts for $15,300, buy back the short calls for $130 and the short puts for $250 → +$12,070 = more than 72% in under a month, with zero exposure on the night of the vote. [CNEYo3P-CRk]

## CHAPTER: 0-DTE strategies

**Why 0-DTE.** [UG4f752OXq8][c49FJM6UDvo] Options expiring the same day: less capital than longer-dated trades, the outcome is known at the 4pm bell, zero overnight risk by construction, and with SPX/NDX expiring every trading day a strategy gets ~250 repetitions a year to express its statistical edge (vs 12 in the monthly era).

**0-DTE put credit spread (directional follow-through bias).** [UG4f752OXq8] Aug 29: SPX rallies +64 points; bias = follow-through tomorrow. Aug 30 open, index 4568: sell the just-below-market put @ 9.55, buy the put 15 points lower @ 4.35 (transcript's strike digits garbled — short ≈4555, long 15 pts down) → +$520 credit, $980 max loss. Close 4548.7, 9.87 points above the short strike → both die → +$520 = 53% return on risk in a day. [UG4f752OXq8]

**0-DTE iron condor (listless-day bias).** [UG4f752OXq8] Best on days that smell rangebound (late summer, December holidays). Aug 11, 10am, SPX 4461: sell the ~15-pts-OTM 4475C @ 5.50 and 4445P @ 5.70, buy 10-pts-further 4485C @ 2.90 and 4435P @ 2.60 → +$470 credit, $530 margin. Close 4464.5 → all four die → +$470; any close in the 30-point 4445–4475 zone pays identically. [UG4f752OXq8]

**0-DTE iron butterfly with the butterfly-roll rescue.** [c49FJM6UDvo] Apr 28, 10am, SPX ~4129 open (ATM strike 4140): sell 5× 4140C @ 6.90 (+$3,450) and 5× 4140P @ 10.90 (+$5,450); buy 5× 4170C @ 0.53 (−$265) and 5× 4110P @ 2.12 (−$1,060) → +$7,575 credit, $7,425 margin. Adjustment trigger: the per-lot credit is $1,515, so the breakeven-per-side sits ~15 points out (≈4155 up / ≈4125 down; transcript's "42485" is garbled). SPX rallies to ~4155 → execute a call butterfly roll: buy back all 5× 4140C, sell 10× 4170C (flipping through flat into 5 short), buy 5× 4200C — the butterfly becomes an iron condor (shorts now 4170C/4140P). The roll consumed over half the credit, leaving +$3,315. Close 4169.48 — pennies below the rolled short call → everything dies → keep $3,315 = 44% on capital in a day. Doctrine: enter direction-neutral, let the market tell you where it's going, move the tested side instead of predicting. [c49FJM6UDvo]

**0-DTE ATM iron butterfly on a 90-minute clock.** [-h1mAx67OxA] A desk trader's system (approximate parameters, exact timing proprietary): morning entry, ~6-lot ATM iron butterfly with ±80-point wings, exit 90 minutes after entry unless a stop or target hits first. Jun 6, SPX opens at all-time high 5357.80; at 5350: sell 6× 5350C @ 10.65 (+$6,390) and 6× 5350P @ 9.15 (+$5,490); buy 6× 5430C @ 0.08 (−$48) and 6× 5270P @ 0.33 (−$198) → credit ≈$11,634 (transcript prints "$1,644"; the stated $36,366 margin = 80-wide 6-lot $48,000 minus this credit, confirming it), margin $36,366. Ninety minutes of time decay with the index roughly unchanged: buy back calls @ 9.00 (−$5,400) and puts @ 6.45 (−$3,870), longs near zero → +$2,466 kept. 2023 backtest of the daily repetition: most months positive, February/April/June negative, average a bit over $1,200/week. (The 5-step development process this trade illustrates is in the "Developing a strategy" chapter.) [-h1mAx67OxA]

**0-DTE 30-delta iron condor with a time-boxed exit — and an AI-built calendar filter.** [Ko9E9OFYsf8] Jul 16, SPX gaps open ~6255: sell 3× 6270C (delta 29.3) @ 5.00 (+$1,500) and 3× 6240P (delta 29.4) @ 5.50 (+$1,650); buy 3× 6340C @ 0.07 (−$21) and 3× 6170P @ 0.37 (−$111) → +$3,018 credit, $17,982 margin (70-point wings). Management: close at +25% of the credit (≈$755) whenever reached; otherwise close at 11:30am regardless of P&L — a ≤2-hour trade. That day at 10:30 the short call had collapsed 5.00 → 1.62 while the short put only rose 5.50 → 6.25 → closing everything banked +$774, over target. Loss anatomy: had the index instead slid through the short put (6234.35), the short put balloons to 14.40 and the exit costs ≈−$1,026 (transcript prints "$1,26"). The trader then fed his backtest's loss DATES into ChatGPT and asked which scheduled economic releases (FOMC, NFP, CPI, PPI, GDP, PCE, claims…) clustered on them; the answer defined no-trade days (~25% of sessions skipped). Result, verified live + simulated: win rate 62% → 86%, profitability more than doubled while trading less. Three weeks of work; "the best hitters know when to lay off a pitch." [Ko9E9OFYsf8]

**0-DTE iron condor: rolling the threatened side intraday.** [t6yuG7KKSKg] The condor counterpart to the butterfly roll — move the tested side away instead of sitting like a duck. Context: SPX in a tight 90-point range 4460–4550 for a week (typical of low-volume summer tape → condor conditions). Aug 10, open 4503 (mid-range): sell 10× 4540C @1.25 (+$1,250) + 10× 4460P @1.80 (+$1,800); buy 10× 4565C @0.22 (−$220) + 10× 4435P @0.65 (−$650) → +$2,180 credit, margin $22,820 (transcript garbles the put strikes as "4450"/"3435" in two spots — the structure is ±~40-pt shorts, 25-pt wings). By 1pm SPX drops >25 points to 4475 → roll the put side down 10 points: buy back 4460P @4.60 (−$4,600), sell the long 4435P @1.18 (+$1,180), sell 4450P @2.65 (+$2,650), buy 4425P @0.73 (−$730) → roll cost $1,500, leaving +$680 and restoring a 25-point cushion. Close 4468.83 → all four (rolled) legs expire worthless → +$680 kept on a trade that was heading for the loss column. "Trade adjustments are what separate professional traders from amateurs." [t6yuG7KKSKg]

**Expiration-day pinning: the max-open-interest iron condor.** [rHFJdAw4PtQ] Monthly (third-Friday) expirations retain outsized open interest from the pre-weeklies era. Theory ("expiration-day pinning"): market makers short large call OI must buy stock as price approaches a heavy strike to hedge, and that buying tends to pin the stock near the maximum-open-interest strike into the close. Trade: TSLA monthly expiry, the 450 call strike held >24,000 contracts of open interest (~2× the 440 and 460 strikes, dwarfing all others) → build a same-day iron condor bracketing the pin: sell 10× 465C @4.52 (+$4,520) + 10× 430P @2.23 (+$2,230), buy 10× 470C and 10× 425P → net credit $2,060, margin ≈$2,940 (transcript prints "29.60"). TSLA opened near 450, sold off, rallied back to ~450 into the final half hour (visible pinning pressure), then slipped to close 442 — inside the deliberately wide 430–465 window → all four legs die → +$2,060 ≈ 70% on risk in a day. Give the pin thesis room: the trade wins if pinning is "correct enough," not exact. [rHFJdAw4PtQ]

**The 10-delta 0-DTE SPX iron condor (the "one-day income" template).** [IdbLc1JBYYI] History note: SPX added Monday/Wednesday/Friday expirations in 2018 — about 150 same-day opportunities a year (before the later move to daily expirations), enough to make one-day index trades "a viable way to trade for a living." Setup, entered ~15 minutes after the open on a Friday with SPX ≈4440–4442: sell 4× 4475C (Δ11.7, ~32 points above the market) @1.05 (+$420) and buy 4× 4485C @0.51 (−$204); sell 4× 4405P (Δ9.2, ~37 points below) @2.14 (+$856) and buy 4× 4395P @1.18 (−$472) → net credit $600; broker requirement $3,400 (the worst case) — entered as one complex order. The deltas are chosen so each short has ≈90% odds of finishing OTM. Close 4455 → all four legs expire worthless → keep the $600 = 17.6% on capital in a day ("more than the market goes up in an average year"). [IdbLc1JBYYI]

**Rescuing a 0-DTE iron CONDOR with the call butterfly roll (December 2024).** [6-Q6xjAX7aM] The condor counterpart of the iron-butterfly roll above. Dec 11, SPX opened near its highs at 6067.51 after rallying all year; holiday-season "meandering days" are the thesis. 15 points above the open: sell 10× 6080C @3.35 (+$3,350), buy 10× 6090C @1.30 (−$1,300); sell 10× 6050P @2.88 (+$2,880), buy 10× 6040P @1.58 (−$1,580) → +$3,350 credit; margin $6,650 = worst case; wins in full at any close between 6050 and 6080. 10:10am (40 minutes in): SPX +14 points, through the 6080 short calls — every point above 6080 now costs $1,000 for the 10-lot. Call butterfly roll: buy back the 10× 6080C @6.95 (−$6,950), sell 20× 6090C @2.63 (+$5,260 — closes the long and leaves 10 short), buy 10× 6100C @0.88 (−$880) → the call side is now short 6090 / long 6100, out of danger with the index at 6081; credit left after the roll: $780. Close 6084.19 → every option (6090C, 6100C, 6050P, 6040P) expires worthless → +$780. Unadjusted: the 6080C would have paid 4.19 × 100 × 10 = $4,190 → the trade ends −$840; the roll turned a −$840 loss into a +$780 win, a $1,620 swing "instead of allowing ourselves to be sitting ducks." [6-Q6xjAX7aM]

**The 0-DTE iron condor CALL condor roll (Oct 31 2023: a losing 4-lot rescued to +$1,216).** [l7BHgd2PO6A] Every-day expirations make 0-DTE income attractive because each trade resolves by the bell — but the market will not always fit the plan; the pro's second choice is to FIX the trade. Oct 31 2023, SPX opens 4165.9 (mid-October selloff): sell 4× 4190C (+25) @4.05 (+$1,620), buy 4× 4215C @0.70 (−$280); sell 4× 4140P (−25) @4.60 (+$1,840), buy 4× 4115P @1.38 (−$552) → +$2,628 credit, capital / worst case $7,372. 2pm: the index has rallied 25 points and exceeds 4190 — "do you sit like a sitting duck" paying $400 per point? Condor roll of the call side: buy back the 4190C @5.00 (−$2,000), sell 4× 4200C @1.38 (+$552), sell the 4215C @0.17 (+$68), buy 4× 4225C @0.08 (−$32) → remaining credit $1,216. Close 4193.83: above the ORIGINAL short strike (the unrolled condor would have paid out), below 4200 → all four options expire worthless → +$1,216 (audio also says "$1,260"). Adjustments always cost something; they keep you in the game and turn many losers into winners.

**The 0-DTE iron condor built around the overnight-futures support and resistance zones.** [Mn5fYhFqxvs] Method: from the overnight e-mini action set the day's initial support and resistance ZONES, then sell a same-day-expiry iron condor with the short strikes at the centre of each zone and the protective legs 25 points beyond — the trade wins if the zones do what zones usually do (buyers step in at perceived bargains, sellers cash in at perceived overheat). There is no guarantee they hold; the edge is that experienced traders know reversals around those levels are more likely than not, and options let you monetise that without predicting direction. Worked example, Jun 16 2020: SPX had closed 3124 the previous day; the pre-market zones were 3152-3160 resistance and 3102-3110 support. Sell the 3155 call @8.94 (+$894) and buy the 3180 call @2.82 (-$282); sell the 3105 put @7.16 (+$716) and buy the 3080 put @3.15 (-$315) → net credit $1,013 (the transcript states $1,030; its own prices give $1,013, which matches the stated 68% return) against $1,487 of risk and required capital. Sellers appeared about 10 points before the resistance zone at midday and drove the index all the way back to the support zone, where a late bounce closed it at 3113 — inside both zones → all four options expire worthless → +$1,013 = 68% in a single session. The lesson the desk draws is the combination of disciplines: the technical work that produces credible zones plus the options knowledge to build a structure that pays on a day most traders saw no opportunity in. High market volatility is what makes these one-day setups both frequent and well paid. [Mn5fYhFqxvs]

## CHAPTER: Market internals & technical filters for 0-DTE (Garrett Drinon)

From the desk's indicator specialist, a four-part series on deciding WHAT kind of day it is before deploying 0-DTE trades. Only 10–20% of days are trend days; trading trend tactics daily gets you chopped up — the internals detect the "higher-timeframe participant" (institutions that take all day to build positions, producing one-way tape). [CeEksKNSGMQ]

**The three internals (a hierarchy, slowest to fastest).** [CeEksKNSGMQ] (1) **VOLD ratio** — total volume into advancing stocks ÷ volume into declining stocks (build it as $UVOL/$DVOL; most platforms list the components as index tickers). ≥3:1 puts a trend day on the table; <2:1 suggests chop/range/rest. Extremes matter: 6:1 or 10:1 readings mark the standout days — roughly once a month in a dull market, daily during the COVID crash; "this kind of trade can make your month." The most powerful but slowest-turning internal; check it first each morning. (2) **Advance-decline line** ($ADD; $ADD-Q for NASDAQ) — count of up stocks minus down stocks. The signature trend pattern: pinned at +2000 (or −2000, very bearish below −2500) all day; a +2000 open that immediately decays back to zero is the anti-signal. Faster than VOLD — regime changes show here first. (3) **TICK** ($TICK; $TICK-Q) — stocks currently on an uptick minus downtick, published ~20×/minute. Trend day = TICK holding above/below zero essentially all day (wicks through zero are fine; watch the candle bodies), with repeated extreme prints (±1000, up to ±1200/1500). Fastest of the three — use it for execution timing; entry trick: in a below-zero regime, fade the isolated HIGH-tick spikes (all the buyers could do), entering as TICK reclaims the downside. Cumulative TICK trending confirms.

**Turning an internal signal into a 0-DTE trade.** [CeEksKNSGMQ] Garrett's sweet spot: ~30-delta options (also his default for weeklies). If the ETF you watch has no same-day expiry, trade the index that mirrors it (QQQ signal → NDX options — in 2020 QQQ only had Friday expirations). Worked examples, all entered ~11am after ≥90 minutes of confirmation: (a) Mon Apr 6 2020, VOLD 6:1 all day: NDX 7873.52 → buy 30-delta 7930C @ 19.50 ($1,950); close 8081.66 → worth $15,166 → +$13,216 = 677% in a day. (b) Sep 13 2022 (CPI gap-down), A/D pinned < −2500: NDX 12,158.85 → buy 30-delta 12150P @ 25.65 ($2,565); close 12,033.62 → worth $11,638 → +$9,073, >3.5×. (c) Feb 21 2023, TICK below zero all day: NDX ~12,158 → put DEBIT spread: buy 12110P @ 24.40, sell 12060P @ 10.70 → $1,370 cost (nearly half the naked put's); close 12,060.30 — the short put expires 30¢ OTM, worthless, while the long is 49.7 ITM ($4,970) → +$3,600 = 262% in a day. Debit-spread trade-off: cheaper entry and lower dollar risk, but profit freezes once the close passes the short strike (payouts offset point-for-point); with 0-DTE decay and a hold-to-close plan, spreads suit this trade well ("I buy spreads two months out and the move happens that day — here the window is defined"). [CeEksKNSGMQ]

**The risk-on/risk-off ETF filter (conviction layer).** [qPkolXAi4BM] A watchlist that reads the day's tone: offensive/risk-on — XLK (tech), XLY (discretionary), SMH (semis), ARKK (high growth); defensive/risk-off — XLU (utilities), XLP (staples), XLV (healthcare), UVXY (vol); macro theme — DXY (dollar), TLT (rates proxy, inverse), HYG (high-yield credit), crypto (GBTC). Columns: relative volume (what's in play), % change from the open (NOT from prior close — gaps get faded; what matters is where money flows after 9:30), absolute change from open; sort by each. Read: a rally led by staples/utilities is suspect; risk-off tone = HYG sold hard, UVXY bought, TLT sold (rates up), ARK weakest, dollar bid — e.g. Feb 21 2023, which closed at the lows. Decision rule: ETF filter bearish AND internals strongly bearish AND price action confirming → high conviction → aggressive trade: QQQ 11am @ 296.28, put debit spread — buy 40× 295P @ 0.59 (−$2,360), sell 40× 294P @ 0.32 (+$1,280) → $1,080 risk; close 294.03 → long worth 0.97 ($3,880), short worthless → +$2,800 (transcript says "29%"; on $1,080 risk this is ≈259% — flagged). ETF filter bearish but internals lukewarm → lower conviction → sell a slightly-OTM call credit spread instead: sell 297C @ 0.80 (+$1,200), buy 298C (−$720) → +$480 credit, $1,020 worst case (lot count as printed is internally consistent with a 15-lot) — wins even if you're outright wrong up to 297, and did (+$480 at the 294.03 close). General law: fewer winning scenarios → bigger reward; more winning scenarios → smaller reward. [qPkolXAi4BM]

**Momentum buying of 0-DTE options: the three-indicator setup.** [Z4a5wkLfqlU] The opposite of premium selling: buy cheap 0-DTE OTM calls/puts to catch an explosive intraday trend — dangerous because decay is brutal if price stalls, so every element exists to avoid sitting in a non-moving position. All on 5-minute charts, liquid names only (futures, QQQ, SPY, SPX, high-beta megacaps — NVDA, TSLA, META…), ideally "in play" (relative volume: 1.2 OK / 1.5 great for indexes; 1.5 OK / 2+ great for single names — a name at 2–3× rVol with a catalyst while the market signals fire can be the A+ trade). (1) **Compression:** Bollinger Band squeeze — 20-period BB (2 SD) trading fully inside the 20-period Keltner Channel (1.5 ATR) = quantified rest/energy (TTM-squeeze red dots; want ≥~5 bars of squeeze). Says only that energy exists, not direction. (2) **Trend fuel:** TICK holding above/below zero (≈80%+ of candle bodies) — the context that says a breakout can run; watch TICK first, then hunt squeezes. (3) **Entry/exit discipline:** ATR trailing stop, 3-period, 1×ATR, 5-min. Aggressive entry = first close through the ATR stop line (half position), rest on break of the consolidation; exit = first close back through the trailing stop — it keeps you in through pauses (no panic-booking at +80% that fades to +30%) and forces you out when the trend actually ends. Strike selection: pick a chart-based price target and buy the option AT that target's strike (deltas shift too fast intraday to size by delta alone). Fully mechanizable/backtestable. [Z4a5wkLfqlU]

**MACD as the 0-DTE entry trigger (custom 3/9/5 settings) + conviction-tiered structures.** [B9myhwUaSsQ] Garrett's protocol for the trader who identifies the A+ setup but freezes on entry (or chases and gets shaken out). The setup comes FIRST — this is not a MACD strategy: a momentum stock breaking key daily support/resistance by 10am on above-average volume (preferably 2–3× average), ideally with its sector confirming. Then the trigger, on a custom MACD (fast 3, slow 9, signal 5 — deliberately faster than stock settings): (1) the initial break prints a new momentum high/low on the MACD; (2) wait for the MACD line to return to zero (the pullback — often through TIME, sideways consolidation, rather than price); (3) enter when the MACD line re-crosses the signal line after touching zero. The wait supplies patience: the first break often pulls back and shakes out early entries. Structure matched to trade grade: A+ conviction → buy 30-delta 0-DTE options outright ("far enough to be cheap, close enough to be reachable"); B-grade (level is there but volume/sector missing) → sell an ATM put credit spread instead, which pays in full even if the stock goes nowhere. Trade 1 (real desk trade, A+): NVDA Apr 19, breakdown with SMH and SMCI confirming on high volume; 11:15am cross with NVDA @819 → buy 4× same-day 810P (30Δ) @2.63 = $1,052; NVDA closed 762 → puts @47.20 = $18,880 → +$17,828 in five hours. Trade 2 (B-grade, relative-strength day): 1:25pm cross, NVDA 868.13 → sell 5× 867.5P @3.30 (+$1,650), buy 5× 857.5P, margin $3,350; NVDA closed 877.35 → +$1,650 — and the identical payout would have arrived at an unchanged close of 868.13, only 0.63 above the short strike. [B9myhwUaSsQ]

**The squeeze setup traded live on QQQ (Garrett's 4th video) — and the intraday leg-in to risk-free.** [s1jRE-Kg4dQ] Same three tools (TICK regime, Bollinger-inside-Keltner squeeze, 3-period 1×ATR trailing stop on 5-min bars — settings credited to John Carter/Simpler Trading's squeeze work), applied only within a market environment that already argues for a trend day (internals, sector leadership, catalyst). Execution nuances: if a wick high sits far above the consolidation don't buy the break of that high — enter earlier, when price starts holding the ATR stop, on the break of the mini-consolidation; a consolidation right off the open is the favorite (tight stop against the high); exit on the first close back through the trailing stop, because with 0-DTE long options "the time decay is unbelievable" and sideways is death. Bearish example: QQQ selling off all morning, 11am @354.85 → buy 15× same-day 353P (nearest 30Δ) @0.62 = $930; close 350.32 → puts ≈2.71 (≈intrinsic) → +$3,135, more than tripling the risk even without using the earlier ATR exit. Bullish example (Nov 3): 11am QQQ 366.26 → buy 15× 367C (38Δ — take the nearest available) @0.60 = $900; by 12:30 the rally had lifted the 368C to 0.77 → sell 15× 368C (+$1,155) → the position is now a long call vertical that has already banked +$255 more than it cost: at ANY close below 367 both calls die and the trade still makes $255; risk fully removed 90 minutes in. Close 367.71: 367C worth 0.71 → $1,065 for the 15 (transcript prints "1155"), 368C worthless → total ≈ +$1,320 (transcript states $1,410 — flagged; ">50% of risk" as spoken). The maneuver is Garrett's habitual way to pull risk out of a 0-DTE long-option trade once the move starts. Single names work when they are "market stocks" (NVDA) so that TICK, a market-breadth reading, remains relevant. [s1jRE-Kg4dQ]

**The seven kinds of market-breadth day — and the option structure for each (Garrett's 3rd video).** [MkWozp1MFmg] Read all three internals TOGETHER (VOLD, advance-decline, TICK) plus the sector ETF filter — never any one alone, since price can run against any single signal. (1) **Breadth extreme** — usually a gap-and-go on a catalyst: extreme VOLD from the open, A/D pinned at +2000 (or −2000) all morning and afternoon, TICK holding one side of zero, offensive sectors leading; signals are readable early — the trend-day setup covered in the first video. (2) **Breadth reversion** — a gap down where the A/D rallies right off the open instead of pinning to −2000 and returns toward zero quickly even while VOLD still reads very negative: expect a reversion to the mean / gap fill; Garrett rarely trades these (moves lack power) but the read tells him NOT to short — "not shorting is sometimes even more important." (3) **Breadth crescendo** — how most trend days actually unfold: no or small gap, neutral-to-slightly-positive readings early, then VOLD and A/D climb all day, reaching extreme levels by midday and into the close; the tell is TICK holding above zero all day, which lets the A/D and VOLD keep rallying. (4) **Biased range day** — a decent gap down, negative VOLD and negative (but not pinned) A/D all day, yet a messy TICK flipping above and below zero: price holds lower in a range; do NOT play downside continuation ("you'll get chopped up shorting lows"); the only trade is fading the big TICK spikes that carry price into resistance (three such fades that day) back to the range bottom — a trade he doesn't jump at. (5) **Breadth divergence** (a favorite, traded live): a sizable gap down with VOLD slightly POSITIVE at the open — "alarming, unusual" — and A/D reverting to zero; switch attention to the ETF filter and require tech/discretionary/semis to be strongest off the open with staples, utilities, healthcare weakest → play the reversion: targets = gap fill, then the 2-day VWAP; not a trend day, be out by the 2-day VWAP at the latest. (6) **Breadth neutral** — the most common day: A/D between +500 and −500, VOLD between −2 and +2, TICK both sides of zero, price balancing around the prior day's volume area and closing mid-range — a fantastic signal for market-neutral option income trades. (7) **Trifecta** — VOLD and A/D at an extreme AND pinned, TICK holding one side of zero all day, AND the offensive sectors (tech, semis, discretionary) leading — "the day you can make your month"; with a catalyst on top (Nov 10 2022, the first cold CPI print) a "quadfecta." On unclear days he simply doesn't trade the market (goes to an in-play stock instead). Freudberg's options overlay: a neutral-breadth call → 0-DTE iron condor, Jan 12 2024, 11am, SPX 4776.54: sell 5× 4795C (~20 pts up) @2.65 (+$1,325) and 5× 4755P (~20 pts down) @2.35 (+$1,175); buy 5× 4805C (−$565) and 5× 4745P (−$590) → +$1,345 credit, capital $3,655 (scale the lot size down to fit the account); SPX channeled and closed 4783.83, ~7 points higher → all four legs worthless → +$1,345 = >36% in five market hours. A trifecta call → the **risk reversal**, Nov 10 2022, NDX 11,396.14 at 11am (QQQ then had only certain-day expirations, so trade the NDX 0-DTE chain): buy 1× 11460C (nearest 30 delta) @21.65 (−$2,165); sell 1× 11350P (a put priced meaningfully ABOVE the call) @33.25 (+$3,325); buy 1× 11225P @8.00 (−$800) as protection → net +$360 credit at entry; worst case $12,140 (the broker's requirement). Close 11,605.96 → the call pays (11,605.96 − 11,460) × 100 = $14,596; both puts expire worthless → total ≈$14,956 for the day (transcript prints "14,960"). Forgiveness built in: at ANY close above 11,350 all three options die and the $360 is kept as a "consolation prize"; above 11,460 the call's value stacks on top — you can be wrong about the rest of the day and still not lose. [MkWozp1MFmg]

## CHAPTER: Earnings trades (implied-volatility around announcements)

**The pricing physics.** [WYya6HGDYYg][IkGV8x5uz_A] Ahead of earnings, market makers must charge enough on ATM options to survive the near-certain post-release jump, so the ATM straddle inflates severely: an ~1870 stock's weekly ATM straddle cost 23.42 in a normal week but 97.56 (call 49.47 + put 48.09) 15 minutes before the pre-earnings close at 1740 — ~4× normal [WYya6HGDYYg]. GOOGL: 25-pts-OTM weekly call 3.86 on a random day 34 days out vs 10.90 one hour before earnings — ~3× — because implied volatility (the move the price implies) explodes as the event nears [IkGV8x5uz_A]. Two opposite trades monetize this:

**Short the inflated straddle: earnings iron butterfly (overnight).** [WYya6HGDYYg] Day before earnings: sell the ATM call + ATM put, buy wings ±60 points. On the 1740 stock: credit $5,278; broker capital / worst case just $722. Next morning (earnings liked, stock +52 to 1792, news out): short call 49.47 → 52.50 (deep ITM ≈ intrinsic), short put 48.09 → 0.58, long call 22.18 → 9.21, long put → 0.53 — the crushed put side pays for everything → close all for +$974 on $722 ≈ +130% by 10:30am (≈300% an hour later). Works when the actual move is smaller than the options market priced; a violent move loses, so ALWAYS small size. Candidate screen: stocks whose options have historically overestimated the post-earnings move (e.g. by ~80% vs the pre-earnings ATM straddle price) over the last 2–3 years. [WYya6HGDYYg]

**Long the pre-earnings straddle (buy the run-up, exit before the number).** [IkGV8x5uz_A] A desk trader's backtested basket play: ~9–11 days before earnings buy the ATM straddle on a chain expiring one day AFTER the release (that placement is what keeps IV support under it). AAPL example (earnings Oct 30 post-close; entered Oct 21): 5.68 call + 6.00 put = $1,168. Exit: +15% of cost — many leave a GTC sell order at +15% working (discipline automation; he may run ten of these at once); absolute rule: be OUT before the announcement. Downside is floored ≈−10% because climbing IV props the straddle even if the stock goes nowhere: 4 hours before earnings with AAPL back within 2 points of entry the straddle was still +$16 — versus a control straddle in a no-earnings week (May, entry $457, same 11-day life) that lost >50% in days at an unchanged stock price. Either direction of movement wins (Oct 28: AAPL +10 → call 11.30/put 2.22 = $1,352, target hit); only total stillness threatens, and the IV floor blunts even that. A built-in floor + repeatable 15% winners = the risk-control formula pros hunt for. [IkGV8x5uz_A]

**Earnings iron butterfly: pull the wings IN to multiply return on capital.** [7q7AJXYOq7s] A desk trader proposed the standard pre-earnings iron butterfly on AAPL at 3:15pm before the release (stock 243): short the ATM 242.5 call and put, wings 20 points out (262.5C / 222.5P), broker margin $9,200. Freudberg's improvement: pull the longs to 12.5 points from the shorts — the closer wings cost more, but capital drops to $3,650. Executed 10-lot: sold 242.5C @6.20–6.22 and 242.5P @5.60–5.68, bought the wings @1.52 and 1.48 (transcript's wing strikes garble as "255 and 240"; the stated distance is 12.5 points) → $8,900 net credit received. Next morning ~11am, AAPL up mildly to 245, mystery gone, every option deflated (vol crush): close all legs for $5,300 → +$3,600 ≈ 99% return on the $3,650 capital overnight. The original 20-point-wing version would have made MORE dollars ($5,350 — farther wings are cheaper) but only 58% on its $9,200 capital; doubling the tight-wing trade to $7,240 of capital would have produced ~$7,200 — more profit than the wide version on less capital. Lesson: on capital-margined trades, spending a little more on protection can massively raise return on capital — risk control IS the return engine. [7q7AJXYOq7s]

**The IV build and the V crush, measured on NVDA (Nov 2024 earnings iron butterfly, 100% overnight).** [Stfx1brjj0k] NVDA reported after the close on Nov 20 2024 (close 145.89; 143.93 when the trade was placed 45 minutes before the bell). On the Nov 22 chain (2 DTE) sell 10× 145C @6.20 (+$6,200) and 10× 145P @7.20 (+$7,200), buy 10× 160C and 10× 130P as ±15-point wings (transcript prints the long call cost as "$15.90" and the long puts as "$1,550"; the stated net credit is $9,900 with a $5,100 broker requirement = worst case, which the legs as transcribed do not reproduce — flagged). ATM implied volatility was 153.13 (calls) / 152.46 (puts). A week earlier (Wed Nov 13, same structure, NVDA in the same neighbourhood) the ATM IV was 39.97 / 38.69 and the identical butterfly collected only $3,580 — the pre-earnings "IV build" is worth almost 3× the credit. Next morning: open 149.35, 10am 144.26 — essentially unchanged from entry — yet the short calls and puts had lost more than half their value and the wings had gone to pennies (the "V crush": the unknown became a known, mild reaction). Close: buy back calls $2,150 and puts $2,830, sell the longs for pennies → +$5,100 = exactly 100% on the $5,100 capital, "a fluky coincidence." Loses when the stock moves much farther than the options priced; but every earnings season offers many such setups. [Stfx1brjj0k]

**The pre-earnings 10-delta iron condor (NVDA, Feb 2024) — why earnings condors are wider AND richer.** [ipzry05eP00] Feb 21 2024, NVDA opened 680.58 (pulling back from 744 days earlier) with earnings after the close. On the Feb 23 chain (2 DTE): sell 20× 840C (Δ9.93) @4.50 (+$9,000; transcript "$99,000"), buy 20× 845C @4.18 (−$8,360); sell 20× 590P (Δ≈10) @4.47 (+$8,940), buy 20× 585P @3.88 (−$7,760) → +$1,820 credit, broker requirement $8,180; probability ≈80% (100 − 10 − 10) of NVDA closing inside the 250-point 590–840 window (calls >150 points above, puts >95 below). Next morning NVDA gapped +79 (+11%) to ≈754 — and the CALLS collapsed too: 840C → 0.77, 845C → 0.64 (>80% lower) because the stock would now need another 85 points in two days with the mystery gone; the puts went under 0.10. Close at the open: buy back 840C (−$1,540), sell 845C (+$1,280), buy back 590P (−$140), sell 585P (+$120) → +$1,540 kept. Apples-to-apples a week earlier (NVDA 734.30, no event, 2 DTE): the 10-delta call sat only 54 points above and the 10-delta put 40 below — a 95-point-wide condor for $1,460, every option under $2 and MORE capital required (the smaller the credit, the larger the requirement). Two effects of the event: option prices inflate, and the 10-delta strikes move much farther out — a wider AND better-paid condor. Loss case: an earnings reaction "way beyond what anyone expected" blows through a short side. Screen: backtest the last 4–8 releases of the stock and trade only if the condor was profitable a comfortable share of the time. [ipzry05eP00]

**The pre-earnings long straddle held THROUGH earnings (Yanni's "B straddle" playbook).** [EP6MBURnM-A] Opposite side of the earnings-vol trade, for stocks whose options systematically UNDER-price the post-earnings move. Screen/checklist: liquid stock with highly anticipated earnings; historical average post-earnings move >6–8% AND greater than the currently implied move (the lower the IV the better — this is the anti-IV-crush condition); buy the chain with MORE than a week of remaining life (typically 2–3 weeks — never the weekly); no run-up/run-down of 2–3 weeks into the report (a flat pre-earnings chart — if the move already happened before earnings there's little left after); some short interest; elevated rVol into the report; hot market and sector. Entry: buy the ATM straddle at the close (or midday, when premiums are cheapest in chop) the day before earnings; risk 10–15% of the position. IBM was the standout: 10-year automated backtest (buy ATM straddle at the pre-earnings close, sell next day) ≈ 40 instances, average +21% per trade, ≈ +1,000% cumulative (>100%/yr); implied weekly move 5% vs 6.6% average max move over 19 years (6.8% over the last 12 reports); filtering to the quarters where IV < historical move: 6 wins / 3 losses / 3 no-trades, ~18% average; modeled expectancy stays positive at a 59% win rate over 100 trades. Also positive: NFLX, UPS, INTC, CSCO. Management: next morning cut the losing side and scale the winner out (his real trade: Apr 30 133 calls, ~$680 risk, target 145 nearly hit day 2); reasons-to-sell list: target reached, intraday uptrend breaks, adverse news, hourly 50-MA fails, unusual tape seller, daily Bollinger fails, or MIXED earnings (mixed = stock goes nowhere = sell). Freudberg's counterpoints: an almost-worthless losing leg (≤5–10% of value, "worth a nickel or less") may be better kept as a hedge/lottery than sold at the low; cutting the cost further via a call debit spread + put debit spread at your price targets (a bought "reverse iron butterfly") sacrifices only the runaway tail; and the mirror-image edge exists — stocks that persistently OVER-price earnings moves (AAPL circa 2010–2015) are short-straddle / far-OTM-short-strangle / iron-condor candidates that harvest the vol crush. Build a stable of ~20–25 researched tickers, trade each only when the checklist passes, and expect the mispricing to eventually be arbitraged away — keep re-backtesting. [EP6MBURnM-A]

**Owning the earnings call "for free": finance it with a put credit spread.** [y6NpvN0VLX0] Bullish-on-earnings structure with positive entry cash flow: BBBY, 3:30pm Sep 30 2020 (earnings that evening; stock ~15, recently bounced from ~4): on the chain expiring 2 days later (day after the release) buy 10× 17.5C @0.23 (−$230), financed by selling 10× 14.5P @0.85 (+$850) and buying 10× 14P @0.60 (−$600) → net +$20 CREDIT at entry; margin $480 = worst case (only if the stock breaks below the put spread). Built-in wiggle room: at ANY close above 14.50 all three options can die and the trade still nets +$20 (≈4% on margin in two days) — long shares would lose on any pullback. Outcome: earnings loved, stock +$5 to 20.60 at the Oct 2 expiry → the calls finish 3.10 ITM → +$3,100 ≈ 650% on the $480 margin. The honest comparison: the same $480 buys just 32 shares @15 → +$179.20 on the same move (and −$12.80 at 14.60, where the option structure still makes $20); only a deep collapse makes the shares the better hold. [y6NpvN0VLX0]

**Buying the pre-earnings IV ramp on a recency-bias drift (GOOGL, July).** [7Wwy58T83W0] A directional way to own the IV explosion WITHOUT holding through the release. Observation: some stocks tend to drift into an earnings report the way they reacted to the previous one (scans exist for this recency-bias tendency). GOOGL had dropped >100 points after its April report; Jul 11 (16 days before the Jul 24 release), stock 1143, the ATM option expiring in 2 days cost 3.24. Trade: buy 2× puts ~10 points below the market (1132.5 strike) on the chain expiring two days AFTER earnings — deliberately, so the options carry the event premium — @12.19 (transcript's total "$4,038" is inconsistent with 2 × $1,219 = $2,438; flagged). Minutes before the release GOOGL had sold down to 1132: the puts, now ATM with 2 days of life, quoted 26.86 — 8× what ATM 2-day options cost two weeks earlier — and were closed for a stated +$1,328 (arithmetic on the quoted legs gives ≈+$2,934; transcript figure as spoken). GOOGL then rallied >100 points on the actual report — irrelevant, because the trade was out before the number. Edge stated: an IV explosion into earnings that shares cannot give you. (The 3.86 → 10.90 pre-earnings call comparison in the same video is registered under [IkGV8x5uz_A].) [7Wwy58T83W0]

**Pulling the risk out of a pre-earnings long strangle: the weekly double-diagonal roll campaign (CMG, Oct 2019).** [t8VszTqb7iY] Setup: CMG ≈835 had channeled 780–850 for six weeks; Q3 earnings due Oct 22; earnings usually break a stock out of its pre-report range. Sep 20 (33 days before earnings, 36 days before the long options expire): buy the Oct 25 855C @27.51 ($2,751) and the Oct 25 775P @14.52 ($1,452) → a $4,203 long strangle that expires AFTER the report. Against it, in the front week, sell a tighter strangle at the channel edges: the 850C for $471 and the 780P for $82 → the whole combination is a double diagonal; net outlay $3,650. Each week (a few hours before the short options expire, when 850/780 are far from the price and the market "knows" they won't be reached in five hours) buy the shorts back for pennies and re-sell the SAME strikes on the next weekly: week 2 (CMG 817) buy back @0.07 + 0.35 ($42 total), sell next week's 850C @1.48 and 780P @2.63 → outlay down to $3,281; week 3 (CMG ≈820) buy back @0.12 + 0.20, sell @2.28 + 2.81 → outlay ≈$2,800; week 4 (CMG 841) buy back for $64, sell for $862 → outlay ≈$2,000, half the original cost. Expiration week is the whole point: the new shorts (same 850C / 780P) now expire AFTER earnings, four days away, with CMG at 845 — the market pumps their prices: 850C @27.88 and 780P @8.81 → $3,669 for the pair versus ~$500–1,000 in the earlier weeks. Cumulative cash flow flips POSITIVE: +$1,517 — the original strangle has been paid for entirely and then some, with all four options still on. Oct 25 expiry after a disliked report: CMG closed 792 → the 855C, 850C, 780P and 775P all expire worthless → the trade ends with the +$1,517 (spoken "$1,500") of collected cash. Caveat stated: had CMG closed above 850 or below 780 the profit could have been as little as ≈$1,000 — but once the final expiration-week shorts were sold there was no scenario in which the trade lost money. Principle: pro traders exploit the predictable change in option pricing as earnings approach. [t8VszTqb7iY]

**The pre-earnings call calendar: short the chain that expires BEFORE the number, long the chain that expires after (AAPL Apr 2019: +36% in 4 days).** [RP5xIYMrXKE] The IV build measured: Apr 12 2019, AAPL 199.70, the 6-day 200C costs 2.17; Apr 30, five hours before the release, AAPL 199.69, a 4-day 200C costs 5.10 — +135% for the same moneyness because that option lives through earnings. Trade (a desk trader's idea): Apr 22, AAPL 203.70, 8 days before the Apr 30 after-close report: sell 10× Apr 26 202.5C @2.83 (+$2,830), buy 10× May 3 202.5C @5.92 (−$5,920) → debit $3,090 = capital. Apr 26 2:30pm, stock at the same price: the short calls have fallen to 1.24 (−64%) — normal calendar decay PLUS no earnings premium to hold them up — while the long calls (post-earnings chain) are 5.45 (−8%), still propped by the imminent release. Close: sell longs +$5,450, buy back shorts −$1,240 → $4,210 → +$1,120 = 36% in four days. Works best on stocks that tend to settle around a price into earnings (the exit assumed an unchanged stock).

**The double calendar into earnings — exited BEFORE the report.** [qblhVcLltZQ] Any option expiring AFTER an earnings release is priced with the anticipated move built in; the same strike expiring just BEFORE the release is not, because its seller is not exposed to the event. The double calendar harvests the widening gap between the two and never holds through the announcement: sell the pre-earnings chain and buy the post-earnings chain at the same strikes, one pair about 10 points above the stock and one about 10 points below. CRM, earnings due June 4; on May 3 around noon the stock is ~163, with a May 31 chain (pre-earnings) and a June 7 chain (post-earnings). Call side at the 172.5 strike: May 31 @0.94 vs June 7 @2.52 — nearly three times the price a full month before the event — so buy the June 7 and sell the May 31 → $158 per lot. Put side at 152.5: May 31 @1.24 vs June 7 @2.58 → $134 per lot. Total $292 per lot, 10 lots = $2,920, and that debit is the entire risk of the trade. By May 31 at 2:15pm the stock had sold off to 152.59, sitting exactly on the put strike two hours before the short options expired: both 172.5 calls were nearly worthless (20 points away), the May 31 152.5 put had shrunk to 0.37 despite the market being right at the strike (two hours is not enough time to matter), while the June 7 152.5 put had ballooned to 4.74 — at the money with earnings days away, exactly the option nobody wants to be short. Closing the whole structure returned $4,385 → +$1,465, about 50% in 28 days, with no directional call and no earnings exposure taken. [qblhVcLltZQ]

**The double calendar into earnings, the second worked case (AMZN, Jan–Feb 2021).** [7XBsrrQOdQU] Location matters as much as the volatility mechanic: place the two strikes at the range the stock has respected, because the earnings report is the catalyst most likely to break it. Amazon had run into resistance around 3500 through the second half of 2020 and found support near 2950, with earnings due Feb 1. Sell the pre-earnings chain (Jan 29) and buy the post-earnings chain (Feb 5) at those same strikes: buy 2× Feb 5 3500C @29.95 (−$5,990) / sell 2× Jan 29 3500C @15.20 (+$3,040); buy 2× Feb 5 2950P @44.73 (−$8,946) / sell 2× Jan 29 2950P @25.83 (+$5,166) → total debit $6,730 = the whole risk. By Jan 27, with AMZN having drifted only ~2% to 3217, the two-days-to-expiry short options are nearly worthless (a 3500 call and a 2950 put are 280–300 points away with no catalyst left in their lifetime) while the post-earnings longs have held almost all their value, because whoever is short them must still price a report that can send the stock through either level. Close by selling the longs and buying back the shorts: long calls $8,376, short calls −$676, long puts $5,686, short puts −$472 → $12,914 − $6,730 = **+$6,184, a 91% return in two weeks** — and the position never took earnings risk. The generalisable statement: an option expiring after the announcement MUST hold value; the same strike expiring before it MUST decay. Selling the one and owning the other is the whole trade. [7XBsrrQOdQU]

## CHAPTER: Directional swing trades with options (the pro playbook)

**Deep-ITM calls as synthetic stock (the ~90-delta position).** [pUD2sXdXHbI] To express a bounce thesis, replace shares with deep-in-the-money calls at ~90+ delta: they track the stock nearly point-for-point, cost a fraction of the shares, and let the same dollars control a multiple of the exposure. Worked example: AMZN after its Jul 10–early-Aug 2024 selloff (−16% in ~3 weeks), close 167.90; thesis = bounce over ~6 months. Instead of 100 shares ($16,790), buy 3× Feb 21 2025 120C (Δ91.02, >47 points ITM) @53.80 → $16,140 (transcript twice rounds this to "$15,900") — ≈300 shares of exposure for less than 100 shares' cost. Expiry: AMZN 216.58 (after peaking 242); the calls quote 96.72 ≈ pure intrinsic → sell for $29,016 → ≈ +$12,876 (transcript prints "13,16") vs +$4,868 = 29% for the 100 shares. Honest downside: three deep-ITM calls lose faster than 100 shares in a selloff (though call deltas fall as the stock drops, softening the pace); trigger context: QQQ had just fallen 12% in a month (ATH 548.10 Feb 19 → 473.63 Mar 18). [pUD2sXdXHbI]

**The breakout trade with cheap OTM weeklies — and phase-2 risk removal (Max's AMZN trade).** [WO3fecu15dk] A desk equity trader's playbook for a binary breakout: AMZN in a ~300-point year-long range, bull flag against 3525 resistance; base built at 3440 then a strong-volume Friday drive to 3510 → thesis: weekend gap-and-go through 3525 to all-time highs, which would also EXPLODE implied volatility (new-high speculation brings call demand). Structure: buy 80× 3700C (Δ≈11) on the chain 2 weeks out, avg 7.07 = $56,560 (bought between 5.25 and 8.00) — deliberately OTM, not ATM, because OTM strikes capture the IV explosion far more than ATM/ITM (deep-ITM value is nearly all intrinsic, indifferent to IV); deliberately 2 weeks, not 1, so the thesis has time (though he later judged splitting into some next-week 1Δ-cheaper strikes would have paid more). Risk math defined upfront: one day of theta + the delta-equivalent share exposure; plan = sell immediately if Monday doesn't gap. Monday (Jul 6): gap and go — on the opening drive sell 50 of the 80 @ avg 18.30 = +$73,560 > the entire cost → trade now RISK-FREE with 30 "free calls" left; scale the rest out on an ATR basis (~40–50 points) into strength through the day at avg 47.39 (+$142,170), going risk-off at the first failed-high pullback; final sales ~3670s. Delta migration en route: 11 → 21 → 29 — the position's share-equivalence nearly tripled per option while risk was already zero. Total ≈ +$159,000. Second lesson: once the IV thesis has PAID, options stop being the right vehicle — swap remaining exposure into shares to keep the deltas without theta/vol-crush bleed (an inside day would have collapsed the IV; even at the close the calls were 22 points OTM and worth ~47 only because two weeks remained — on expiration day the same price action would have been worth zero). [WO3fecu15dk]

**Bearish put broken-wing butterfly on a correlation divergence (XOM).** [HpXE6fr-q4g] The thesis: oil and oil equities historically move together; in 30 years there were only three occasions when crude fell 10–20% while oil stocks made 52-week highs, and each time the stocks pulled back 5–10% within about a month. Late Nov 2022 was the fourth: crude had slid orderly from 122 (Jun 8) toward 81 while XOM hit 52-week highs. Wait for price confirmation — Nov 28's gap down 113 → 111 — then structure a bearish put BWB on the Dec 30 chain, entered days later @110.42: buy 75× 113P @4.97 (−$37,275), sell 150× 107P @2.36 (+$35,400), buy 75× 104P @1.54 (−$11,550) → net debit $13,425 = theoretical max loss (run a stop far smaller). Dec 20 (11 DTE), XOM ≈107: 113P sell for $52,125, 107P bought back flat at $35,400, 104P salvaged for $6,900 → +$13,050 ≈ 97% in three weeks. Wrong-direction case quantified: had XOM instead RALLIED to 111 by expiry, the 113P alone finishes $2 ITM → $15,000 − $13,425 = still +$1,525 — profitable while outright wrong, the signature of well-located option structures. [HpXE6fr-q4g]

**The bull call spread (ITM debit spread) — and the roll-down that turns a loser into a winner.** [if0P_RU5zWc] Jul 12 2023, SPX breaks out to its year high, close 4472.16; on the Aug 10 chain buy the 4350C @158.65 (−$15,865) and sell the 4450C @87.00 (+$8,700) — a 100-wide spread entirely IN the money, debit $7,795. At expiry the spread is worth exactly $10,000 at ANY close ≥4450 (above the short strike the two legs move point-for-point), so max profit is fixed at $2,205 (28.3%) and it is earned even if the index goes nowhere or slightly down: Aug 10 close 4468.83 (below the entry) → 4350C = 118.83 ($11,883), 4450C = 18.83 (−$1,883) → $10,000 → +$2,205 (transcript prints "$225" with the correct 28.2%). Re-entry on the Sep 7 chain, same strikes: 4350C @157.30 / 4450C @83.25 → debit $7,405 (transcript "7,45"), max profit $2,595. SPX then fell to 4346.90 by Aug 18: the spread could be closed for $4,680 (sell 4350C @69.75, buy back 4450C @22.95) → −$2,725, i.e. down about the trade's max profit — the point at which bull-call-spread traders roll: close, move the spread down to the next 25-point strike (4325/4225, still 100 wide) and INCREASE size to a 2-lot to restore the income potential: buy 2× 4225C ($31,880), sell 2× 4325C ($17,080) → total invested $17,525. Sep 7 close 4451.14: 4225C ×2 = $45,228, 4325C ×2 = −$25,228 → $20,000 → +$2,475 = 14.1% on a trade that was heading for a loss. Prerequisite: keep the capital for a possible roll in reserve from the start. [if0P_RU5zWc]

**Converting a winning long call into stock + a target-strike short strangle (the desk's Tesla trader, Nov 2019).** [mY0x0Mc8iqk] A desk day/swing trader had bought 3× TSLA Sep 2020 285C @34 ($10,200) months earlier; TSLA gapped from ~250 to 300 on the Oct 23 earnings and by mid-November traded ≈347, the calls quoting 92.45. Anatomy: intrinsic value = 347 − 285 = 62 (exercise-and-flip would net $18,600 gross, +$8,400); the remaining 30.45 is TIME premium — the market's collective bet that TSLA won't rise more than another ~$30 by September; selling the calls outright therefore yields $27,735, about $9,000 more than exercising. Freudberg's advice, built on the trader's own answers (happy to sell at 390, happy to double the position at 280), four near-simultaneous moves: (1) sell the three 285 calls → lock +$17,535, because the $30.45 of time premium will bleed to zero by expiry; (2) buy 300 actual shares (≈$104,100) — shares carry no time premium to lose; (3) sell 3× Sep 2020 390C; (4) sell 3× Sep 2020 280P — the two short options bring in over $20,000 of cash (≈$12,000 from the calls), which is yours to keep whatever happens next. Scenarios: TSLA ≥390 → shares called away at the trader's own target, PLUS the ≈$12,000 call premium for "something you would have done anyway," PLUS the put premium → total profit >$50,000 ≈ 49% on the trade, about $20,000 more than simply selling the calls, buying shares and selling at 390; TSLA stays between 280 and 390 until September → both shorts expire worthless, pocket the ≈$20,000 and keep the shares; TSLA ≤280 → assigned 300 more shares at the price he already called a bargain, having been paid for the wait. Every branch of the tree matches the trader's stated goals — the generalization of "get paid for the trade you'd make anyway" from covered calls and cash-secured puts to a full swing plan. [mY0x0Mc8iqk]

**The bullish risk reversal on a 2-month horizon (SPX, Jul–Aug 2020): zero outlay, +108% if right, a credit if wrong.** [pW2ZZAAPVMI] Setup: a market bouncing hard off a crash low but still short of its all-time high (2020: pandemic lows in mid-March, by Jul 1 much recovered; the 2022–23 analogue: uptrend from the Oct 13 reversal day, index still ~15% under the highs). Jul 1 2020, Aug 31 chain (2 months): buy 2× 3300C (a couple of hundred points above the market) @68.20 (−$13,640); sell 2× 3000P (>100 points below) @91.85 (+$18,370); buy 2× 2800P for protection (transcript quotes "99.30" — impossible for a lower put; the stated $1,620 net credit implies ≈15.55) → +$1,620 CREDIT at entry; broker requirement $38,380 = the 200-point put spread less the credit (the theoretical worst case, which no sensible trader would sit through). Aug 31 close exactly 3500.00 (a new record): both puts die; the calls are 200 points ITM → 2 × 200 × $100 = $40,000 + $1,620 = +$41,620 = >108% in two months, with no entry cost to subtract. Wrong-direction case: a close at 3001 leaves all three options worthless and the $1,620 is the "consolation prize" — the trade profits at EVERY close above 3000, i.e. it can be "a little wrong" and still win, and pays more the more right it is. (The 0-DTE version on NDX is in the internals chapter [MkWozp1MFmg].) [pW2ZZAAPVMI]

**The September-seasonality put diagonal (SPY): long the Sep put, short the Dec put 10 points lower.** [vFTpvP8kwzY] Seasonality: September is historically the worst month (Dow Jones data), while the remaining months and especially December (the "Santa Claus rally") are positive. Structure entered at the Sep 1 close: buy the end-of-September put at the first strike below SPY, sell the Dec 31 put 10 points lower — a put diagonal that is entered for a CREDIT because the three-month option is worth far more than the one-month one despite its lower strike. Keep enough cash to accept 100 shares at the short strike. 2021: SPY closed Sep 1 at its all-time high ≈451.88 (transcript "4188"): buy Sep 30 450P @5.58, sell Dec 31 440P @13.17 → +$759. Sep 30 close 429.14 → the 450P is worth 21.39 → sell it (+$2,139) → cash flow $2,898; Dec 31 close 474.96 → the 440P dies → +$2,898. 2022 (a down year): Sep 1 close 396.42: long Sep 395P / short Dec 385P → +$640; Sep 30 close 357.18 → sell the 395P @37.68 → stated cash flow $4,448 (the legs give $4,408 — flagged); Dec 30 close 382.43, 2.5 points BELOW the short put → buy it back @2.52 (−$252) → stated final +$4,156 (arithmetic gives $4,196 — flagged): a handsome profit even with the short put in the money. 2023: Sep 1 SPY 451.19: long 450 Sep / short 440 Dec → +$348; Sep 29 close 427.48 → sell the 450P @22.81 → $2,629; Dec 29 close 475.31 → 440P dies → +$2,629. Two fallbacks make it robust: if December finishes well below the short strike, take assignment at the short strike and wait for the bounce "which has historically always come"; if September never sells off and the market rallies through year-end, both puts expire worthless and the entry credit is the profit. "Match the right strategy with the right market pattern." [vFTpvP8kwzY]

**The bearish broken-wing butterfly on SPY after a five-month rally — profit from the pullback AND own the bounce.** [lRj741LUAFo] Context: five months of relentless rally (S&P +1,000 points since mid-October, the largest and fastest in three years) → some pullback is inevitable; the illustration uses the previous rally, mid-March → Aug 1 2023 (SPY +76 points, +20% in <6 months). Aug 1 2023, Oct 20 chain (80 DTE): buy 1× 452P (just below the market) @7.88 (−$788), sell 2× 434P (5% below) @4.24 (+$848), buy 1× 250P @0.11 (−$11) purely for margin control → +$49 credit; broker requirement $16,550. Oct 20 close 421.19 (the rollover happened): minutes before the close sell the 452P @30.55 (+$3,055) and buy back ONE 434P @12.58 (−$1,258) — executed as a put-credit-spread order — → options cash flow $1,846; the 250P dies; the remaining short 434P is assigned → 100 SPY bought at 434 vs a 421.19 market. Hold into the year-end rally: sell at the Dec 29 close 475.31 → +$4,131 on the shares → stated total +$5,997 (the legs give $5,977 — flagged). Wrong-thesis case: with every strike at 452 or lower, a market that never pulls back lets everything expire worthless and the $49 credit is kept — "outright wrong and still profit." Dual purpose: profit from the selloff and acquire the shares at a great price for the bounce. [lRj741LUAFo]

**The tight call debit spread as a swing vehicle (target price = the short strike).** [LHx19knh8x4] When a swing thesis has a specific target, buy the call at the entry level and sell the call at the target: the debit is tiny, the reward-to-risk far exceeds anything a share trade offers, and the debit doubles as a stop that cannot shake you out. GS had held a 185-215 channel for about four months; on November 2 it dropped to the bottom of that channel — read as a bullish signal that buyers get active there — so on the Nov 27 chain (25 days) buy 5× 210C @1.30 (-$650) and sell 5× 215C @0.82 (+$410) → net debit $240, which is simultaneously the maximum loss and the broker's entire capital requirement. At any close at or above 215 the spread is worth $2,500 (5 points × 100 × 5 contracts) → maximum profit $2,260, better than 9:1 on the risk, and it is the same $2,260 whether GS finishes at 215 or at 300; below 210 both calls die and $240 is the whole loss. GS closed above 235 on Nov 27: both sides were auto-exercised — shares bought at 210 for $105,000 and sold at 215 for $107,500 → +$2,500 gross → +$2,260, a return above 941% over the 25 days of the trade. The structural advantage over trading the shares: a share position gets stopped out on a temporary move against you and then watches the target get hit from the sidelines, whereas the debit spread simply sits until expiry with the loss already fixed at the amount you chose to risk. [LHx19knh8x4]

**Hedging a large unrealized gain for free: the bear put spread financed by a covered call.** [-huhEgn9TRg] The problem: a big embedded profit in a stock you do not want to sell — a long-term thesis plus a capital-gains bill if you do — facing a chart that has gone parabolic. The structure given to a desk trader for his TSLA position: buy a put just below the market, sell a put down at the level where the stock last found support, and sell a call up at the level where the stock last failed; the short call finances the put spread, so the whole hedge goes on for a CREDIT. Dec 20 2023: TSLA opens 256.41 after a 26% run off its Oct 31 low, and the trader is long 500 shares at a $110 cost basis (about $55,000 originally invested). On the Feb 16 chain: buy 5× 250P @15.48 (-$7,740), sell 5× 195P @2.16 (+$1,080, the Oct 31 support), sell 5× 265C @1.65 (+$825, the early-October resistance) → +$1,360 net credit. Feb 5 2024, the morning after a badly received Q4 report, TSLA is at 184.26 with 11 days left: the 265 calls are 0.03 → buy back for about $20; the 250 puts are 66.15 → sell for $33,075; the 195 puts are 12.95 → buy back for roughly $6,475 → the hedge closes at +$27,940 having cost nothing to establish. Side by side: unhedged, the position went from +$73,205 of unrealized profit on Dec 20 to a -$35,865 drawdown on Feb 5, back to +$75,000 by Jul 15 with TSLA at 260; hedged, the Feb 5 drawdown was only $7,923 and the Jul 15 total was above $100,000. The obligations to accept before entering: the short calls are covered by the 500 shares so the loss is NOT unlimited, but the upside is capped at 265 and you must be content selling there; the short 195 puts can be assigned, adding 500 more shares at 195 (which a long-term bull may welcome), though closing the structure before expiry makes that unlikely; and at any close at or below 265 with both puts worthless the original credit is kept as a consolation prize, with the profit growing from 250 downward and stopping at 195, where the short puts switch it off. [-huhEgn9TRg]

**Selling 6-month 40-delta put spreads into a VIX>50 panic (the four instances in ten years).** [vfpqix1O30U] Observation: the VIX exceeding 50 is rare — four times in a decade (Aug 2015 China devaluation, Feb 2018, the Mar 2020 Covid crash, and Aug 5 2024, when SPX gapped down ~225 points, more than 4.2%, and the VIX printed 65 against its normal 13–19 range) — and after every spike the VIX mean-reverted. The play at the open of such a morning: on SPY, go out roughly six months, sell the ~40-delta put (i.e. close to the money, where the panic premium is richest) and buy the put 5 points lower, 100 lots. **Aug 2015:** SPY opened 183.87 after a ~7% drop; on the Mar 18 2016 chain sell 100× 180P @13.66 (Δ43.2) / buy 100× 175P @11.57 → +$20,900 credit against $29,100 of capital (the audio garbles the two leg totals as "$136,00" and "$15,700"). SPY expired 204.37 → both worthless → **+71.8% in six months**. **Feb 2018:** July 20 chain, sell the 260 put / buy the 255 put, same size → +$15,100 credit, $34,900 capital (audio "155,100"); SPY closed 279.68 → +43.2%. **Mar 6 2020:** SPY gapping down another 3% to 293.38; September chain, sell 100× 285P / buy 100× 280P → +$17,200 against $32,800 of risk; SPY closed 330.65 on Sep 18 → another full win (+52.4%). Why it repeats: a VIX above 50 usually means the selling has turned frantic and emotional — near the end of the move — AND put premium is inflated far above normal, so the credit (and therefore the return, since capital = width minus credit) is abnormally large; the subsequent volatility normalisation, the bounce and simple time decay all pay the seller. Patience is the cost: the setup appears roughly once every 2–3 years. [vfpqix1O30U]

**The "win-win-win" modified risk reversal at a generational floor (TLT, Oct–Dec 2023).** [WP7JVyd6bjM] Structure: a put credit spread whose short strike sits at a price the underlying has never traded below, plus a long call bought with — but not all of — the credit, so that the entry cash flow stays POSITIVE. That constraint is what makes every outcome a win. Instrument choice: TLT (iShares 20+ Year Treasury Bond ETF) had not closed below 80 at any point in the millennium (briefly under 81 in 2004); on Oct 3 2023 it closed at its 2023 low, 85.06, with RSI near 20. On the Dec 29 2023 chain: sell 10× 80P @1.59 (+$1,590) / buy 10× 70P @0.30 (−$300) → +$1,290, capital $8,710; then buy 10× 93C @1.00 (−$1,000) → net credit still +$280, total capital $9,720. **The three outcomes:** (1) TLT above 93 → keep the $280 AND cash the calls; (2) TLT between 80 and 93 → everything expires worthless, keep the $280; (3) TLT below 80 → assigned 1,000 shares of long-duration Treasuries at the lowest price in twenty-five years, a position hard to lose on eventually. Outcome (1) happened: TLT closed 98.88, the 93 calls worth 5.92 = $5,920 → total +$6,210 = over 63% in under three months. [WP7JVyd6bjM]

**The modified risk reversal on the index during a correction (SPX, Jul–Oct 2024).** [Fet_MWkqemw] Same shape, index version, and the cleanest statement of the payoff map. Jul 24 2024: SPX had made an all-time high of 5669 on Jul 16 and then lost nearly 250 points, closing 5427.13. On the Oct 18 chain (~3 months): sell the 5400P @118.60 (+$11,860) — 27 points below the market — buy the 5200P @71.75 (−$7,175) for a $4,685 net put-spread credit, then buy a call priced just UNDER that credit: the 5750C @43.85 (−$4,385) → entry cash flow +$300, capital $19,700 (the 200-point width minus the credit). **Payoff:** any close at or above 5400 pays at least the $300 — flat market, mild sell-off, rally that stalls at 5750, all +$300 — and above 5750 it adds $100 per point. Only a close below 5400 can lose, and the $300 cushions the first points of it. The market first fell further (the trade looked wrong) then rallied from early August: Oct 18 close 5864.67 → the call is 114.67 points in the money = $11,467 → total profit $11,767 = 59.7% on capital. Desk framing: this is the crash playbook — you are paid to be slightly wrong, and only "wrong by a lot" loses. [Fet_MWkqemw]

**The "bear trap": a broken-wing put condor that pays for a pullback and still profits if the rally continues (SPX, Aug–Sep 2022).** [BY2qOpNoDdI] The problem it solves: you think a pullback is due but shorting risks getting run over. Structure, Aug 1 2022 with SPX pressing the top of its year-long downward channel: buy 5× 4000P (a bit more than 100 points below the market), sell 5× 3950P @64.65 (+$32,325), sell 5× 3900P @54.05 (+$27,025), buy 5× 3800P (the four legs cost $38,550 and $18,875) → net POSITIVE cash flow $1,925 on entry, broker requirement and worst case $23,075 (mid-September expiry, about six weeks). Because the entry credit is positive, **any close at or above 4000 — including a continued rally to new highs — returns the $1,925**; the trade only becomes a real loss if the index falls all the way to the far wing. The thesis then paid: the market rallied first, then sold off, and on Sep 16 SPX settled 3873.33 — the long 4000 puts 126.67 points in the money (+$63,335), the short 3950 puts 76.67 ITM (−$38,335), the short 3900 puts 26.67 ITM (−$13,335), the long 3800 puts worthless → **+$13,590 = over 58%** on the $23,075. [BY2qOpNoDdI]

**Swing-trading a capitulating momentum stock with a risk reversal, then hedging it with shares (Steve Spencer, TSLA, May 2019).** [nMq1TZFBToE] A desk partner's four-most-frequent options setups, bullish variant. Read: TSLA had been in a daily downtrend from the January 380 high; the last leg accelerated after the capital raise priced at 243, the Musk cost-control email leaked, a Morgan Stanley analyst published a $10 worst case (while keeping a $230 target), and Consumer Reports questioned Autopilot safety — the crescendo of bearish headlines that typically marks a bottom. When a higher-timeframe downtrend steepens, the steeper trend cannot sustain itself and price snaps back toward the older trendline. Entry, Monday, with the stock gapping below 200 to 197: sell 10× 185 puts and buy 10× 215 calls in the chain expiring the FOLLOWING Friday (1–2 weeks, never the same week — the bounce may take days), taken as a single complex order for a credit of close to $4 per share. Strike doctrine: sell puts 5–10% below the extended price (here 185, also the multi-year 180–182 support — you must genuinely want to own the stock there), buy calls 5–10% above. **Management is the point:** stop = if it keeps falling a few dollars further (below 194), take off half; when the bounce delivers ~5% (it traded 205–206), hedge 20% of the position with SHORT common stock — that short pays for the time decay of the calls if the bounce stalls and protects the downside if it rolls over; another 5% up, hedge another 20%; then sit and let the remaining unhedged calls run. Ahead of an expected gap-down (Wednesday closed 192, below entry) he bought short-dated 180 puts as a one-day insurance overlay, to be sold into the gap. Levels for the capitulation morning were mapped pre-open (S1 184, S2 182, the long-term support); the leaked Musk email saying orders were tracking to beat the record December quarter bounced the stock ~$15, and half of the 205 short hedge was removed on the flush below 194. Stance: stay bullish while the stock keeps making higher lows. [nMq1TZFBToE]

## CHAPTER: Legging into risk-free spreads (financing the long option after the move)

**The principle.** [kG0YKGa6kc0][-gGvWxd_iXc][W1HJb-ST-6Q] Buy a directional option first; when the market then moves your way, sell a further-out-of-the-money option of the same type for MORE than you paid — from that moment the position cannot lose: worst case is the locked-in net credit, while the spread between the strikes remains as a "lottery ticket." This is trade risk management by construction — professional traders constantly hunt for the chance to make a trade risk-free at the earliest possible point. The same move works inside a single 0-DTE session: Garrett's 11am long 367C turned into a 367/368 call vertical at 12:30 with +$255 banked, unlosable for the rest of the day (see the internals chapter). [s1jRE-Kg4dQ]

**Swing version (RUT, six-month puts).** [kG0YKGa6kc0] Jan 27 2023: RUT 1911.50 pierces an established down-trendline from below (bearish signal — any indicator you trust works: VIX, MACD, RSI). Buy the Jun 30 1910P @89.25 ($8,925 risk). By Mar 13 (banking crisis; regionals are a meaningful RUT component) the index has sold off so hard that the 1770 put — 140 points lower — trades ABOVE the original cost: sell it @101.20 (+$10,120) → net cash +$1,195 with both legs still on. Three outcomes at the June expiry: RUT >1910 → both die → +$1,195 (the WORST case); between the strikes, e.g. 1834 → 1910P pays $7,600 → +$8,795; ≤1770 → payouts offset point-for-point below the short strike → frozen maximum +$15,195. [kG0YKGa6kc0]

**Whipsaw version (GOOG in the COVID seesaw, 1 week).** [-gGvWxd_iXc][W1HJb-ST-6Q] In a violently alternating tape (March 2020: panic selloffs alternating daily with stimulus rallies), buy the put on a RALLY day and sell the lower put on the next PANIC day. Fri Mar 13 2020 (big rally day): buy GOOG Mar 20 1125P @38.92 (−$3,892). Mon Mar 16 (market tanks on weekend virus news): sell the 1090P @40.62 (+$4,062) → +$170 locked, all risk gone. Mar 20 close 1072.30: long 1125P worth 52.70 (+$5,270), short 1090P costs −17.70 (−$1,770) → total +$3,670 on a trade that could no longer lose from day 2. [-gGvWxd_iXc][W1HJb-ST-6Q]

## CHAPTER: VIX trades

**Selling VIX puts at complacency support ("scalping the spike").** [cTX7BettDqk] The VIX has well-defined support floors that mark maximum complacency — ~12 in 2018–2019, rarely below 11 in 2013–2014 — and out of those complacent periods come recurring spikes (readings of 30, 40, briefly 50: summer 2011, summer 2015, early 2018, late 2018), plus smaller spikes multiple times a year. The trade: when the VIX sits at support, sell VIX puts at/near that support strike — downside is limited by the floor's tendency to hold, and a spike lets you buy the puts back for pennies long before expiry. Worked example: Jan 18 2018, VIX ~12 → sell 10× 12P @1.25 (+$1,250), broker capital ≈$2,400. Three weeks later (week of Feb 5 2018) the VIX exploded into the 30s, pulled back to 23 midweek → the puts, with 42 days still to run (Mar 21 chain), quote 0.22 → buy back for $220 → +$1,030. Common rule of thumb: close when the put has shrunk to half the credit; also decide a minimum entry income before trading it. Origin: desk income strategies entered in low-vol regimes draw down when vol spikes — this position profits from exactly that event, so it started as a portfolio-balancing companion trade but stands alone as a profit center. [cTX7BettDqk]

## CHAPTER: Developing a strategy like a professional (the 5-step process)

[-h1mAx67OxA] Think like a scientist: hypothesis → experiment. **(1) Hypothesis** — a simple repeatable trade idea (e.g. "the 90-minute ATM iron butterfly every morning"). **(2) Backtest** on real historical options data with commercial software (available to retail); accept that NO strategy wins every day/week/month — the 2023 test above made money in 9 months, lost in 3, and averaged $1,200+/week; conclusions come from a year of data, not a week. **(3) Paper trade ~1 month** — learn the broker's complex-order tickets (iron butterflies are a preloaded ticket everywhere) without real money, and stare at each paper loss asking "can I truly eat this number?"; a backtest runs in seconds and teaches no emotions, paper trading runs at life speed. **(4) Go live at minimum size** — the 1-lot version of the 6-lot target trade (≈16% of the P&L swing): live trading surfaces issues backtests can't, and execution errors born of nervousness should cost small-size money ("send the monkey up before the astronaut"). **(5) Scale gradually** — raise capital every month or two only after honestly answering "did I endure the last loss non-emotionally?"; scaling too fast ends with bailing at the worst moment, right before the win streak that would have restored the equity curve. Corollaries from the other case studies: quantify the tail before trusting a win streak (the $2,500/week trader had 9 loss-free months yet his year hinged on whether −$23,600 gaps strike 4 or 6 times [Dl0O3z_5hB0]); mine your own loss dates for the conditions that cause them and filter those days out (the ChatGPT economic-calendar filter, win rate 62→86% [Ko9E9OFYsf8]); overlay indicators only after they too survive a backtest [Dl0O3z_5hB0].

**Trade like the casino: build the edge, then let expectancy do the work.** [rpFL_mEFPSg] The house never predicts the ball; it rigs the payoff. A roulette wheel carries 18 red and 18 black numbers plus two green (0 and 00) → the player wins 47.3% of the time and the house 52.7%, an edge of 5.4%: $1,000,000 wagered in a day pays the casino $54,000, and 1,000 bets of $1,000 produce 527 wins against 473 losses = +$54,000. The amateur option buyer stands on the player's side of exactly such a rigged game: Hasbro at 82.69 on December 1 (its high for the year), the 46-day 87.5 call costs 1.40 ($140) and its delta is 29.47 — a 70.53% probability of expiring worthless, printed right there on the chain. HAS did rally, closed 86.20 on January 16, and the call still died: right on the rumour, right on direction, total loss, because he never looked at the probabilities. The professional's version is a rigorously backtested repeatable trigger plus a FIXED reward-to-risk ratio. Example from a desk trader (the trigger itself is proprietary; it fires when a strong directional day is likely and says which way): Mar 29 2018 SPX closed 2640.87; Apr 2 it opened 2634.27 and the bearish trigger fired → on the 11-day chain, per his protocol, buy the put nearest 75 delta (the 2700P, delta 76.61) @77.25 (-$7,725) and sell the put nearest 25 delta (the 2565P) @16.40 (+$1,640) → a put debit spread costing $6,085. Protocol: take profit at 15% of the debit, stop at 7.5% — deliberately a 2:1 reward-to-risk. That day the $912.75 target was met by 10:15am (2700P at 91.50, 2565P at 20.60 → close for $7,090, +16%); the index went on to close 2581.88. Years of backtesting put the win rate near 60%, so the expectancy formula (win% x average win − loss% x average loss) gives 0.60 × $900 − 0.40 × $450 = $360 per trade → $36,000 over 100 trades on about $6,000 of capital per trade. The failsafe is the payoff ratio: even if the win rate decayed to a coin flip, expectancy is still 0.50 × $900 − 0.50 × $450 = +$225 per trade. Design systems where the probability AND the payoff ratio both work, so that deterioration in either one still leaves a positive-expectancy business — and note that a 60% win rate already beats the casino's 52.7%, with numerous option strategies running well above it. [rpFL_mEFPSg]

## CHAPTER: Trading principles & risk management (the "ten things" doctrine)

Distilled from Freudberg's brain-dump mentoring session — the patterns he says distinguish successful from unsuccessful traders across hundreds of traders over a decade. [MmryR1iu9dA]

**1. Never increase capital because of a winning streak.** Options income trades are statistical: a fixed expectation of wins and losses per year (a typical strategy "is going to win nine months out of the year"). Each consecutive win brings you *closer* to the inevitable losing month, so scaling up on a streak positions maximum capital exactly where the loss lands. Cautionary tales: a student called a taught strategy "an ATM machine" after 3 winning months, raised capital, and the predictable losing month hit at max size; Freudberg himself once quadrupled capital after a 6-month winning streak and gave back nearly the whole year's gains in the first month at the new size. Increase capital only because the strategy has proven itself over long periods — slowly. "When you start feeling invincible, get very, very scared" (the Buffett greed/fear rule applied to your own psychology).

**2. Trading large capital is different from trading small capital.** With a 10% stop, a $10,000 account risks $1,000; the same strategy on $100,000 means sitting through a $9,000 drawdown while still correctly in the trade. Risk tolerance is a muscle that must be built gradually — jump sizes too fast and you'll panic out of normal drawdowns, converting statistical wins into locked-in losses. Traders are ironically *more* nervous trading firm capital than their own (being watched, need for approval). When a firm funds you, it hired you for the strategy you already trade — "if it ain't broke don't fix it"; keep the style, accept larger dollar (not percentage) swings. Execution also changes with size: a 10-lot iron condor usually fills at once; a 500-lot fills piecemeal, slowly, and may require price concessions.

**3. Backtesting is not live trading.** A backtest is a technical simulation, not an emotional one; only live capital tests emotions. Live trading adds: slippage (you won't always get mid — pay up on debits, accept less on credits), execution errors (buying 100 spreads instead of 10 — they happen, especially early), and the temptation to lock in profits early when dollar P&L looks big at new size — cutting winners short destroys the "bank" needed to absorb the strategy's inevitable losers and still produce the expected annual return.

**4. Be consistent — but not foolishly consistent.** The strategy earned its place through long-term results; plan the trade, trade the plan. Abandoning a system after one losing first month is immature: a 5-year backtest with ~20% losing months means the first live month can easily be a loser without saying anything about the edge. Exception (foolish consistency): if you're up 9% against a 10% target and tomorrow brings a binary macro event (major FOMC, jobs report, Brexit-style vote), take the 9% — don't expose a nearly-complete win to a known large move for the last 1%.

**5. Never trade to feel better.** Cutting risk mid-trade to soothe fear, when the system doesn't call for it, means fear is making the decisions — and fear-driven traders fail long-term. Reference: *Way of the Turtle* (Curtis Faith) — the prop firm demanded only that traders follow the system, win or lose, yet most couldn't; those who varied from emotion failed. Related failure mode: exiting on minor up-ticks to "preserve" small profits (trades commonly oscillate +1%, −3%, +4%, −2% before finishing +10%) — you sacrifice the year's return. And panicking out of options trades guarantees the worst execution (everyone's exiting at once): a loss that would have been −6% becomes −10%. Panic never works.

**6. Successful traders know how to lose.** Ego — the belief that great traders don't lose — is childish; the best traders on the desk are losing all day somewhere. At SMB, *not taking your stop* is the capital offense, not losing: it reveals a discipline/character flaw. Take the stop, live to trade another day. Note: the best months of the year often directly follow a losing month — quitting after a loser regularly forfeits the year's best month.

**7. Diversify across the three pricing factors.** Option prices respond to time, underlying price, and volatility, so an ideal monthly-income portfolio mixes: (a) time diversification — ladder entries at e.g. 160, 145, 130 days to expiration to catch different market price points; (b) volatility diversification — pair strategies that benefit from volatility rises with ones that benefit from falls, smoothing the equity curve; (c) price/direction diversification — mix trades that do well in selloffs with ones that do well in rallies, *leaning toward downside-friendly structures* because options strategies' worst scenarios usually occur to the downside (true even through a historic bull market).

**8. Keep it simple — avoid the "octopus."** Adding a tweak every day for 30–60 days produces a monstrous position that is expensive and dangerous to exit: more slippage, more commissions, more execution-error risk (Freudberg once needed 15 separate executions and an hour of planning to exit one such trade). Toward the end of a trade's life, deliberately simplify so the final exit takes 2–3 transactions.

**9. Patience — in career, execution, learning, and sizing.** Career: don't quit the day job before you've proven skill; all SMB desk options traders keep full-time professions while trading remotely. Execution: there's a right price for each strategy; pros wait — sometimes 3 days — for their fill instead of overpaying. Learning curve: plan for 6–24 months before consistent success (fastest ever seen on the desk: 6 months; up to 2 years is normal). Capital sizing: don't put large capital at risk until you've traded 12–24 months and seen more of what the market can do.

**10. The market can do whatever the hell it wants, whenever it wants.** (His first options mentor's warning; exhibit: the May 2010 flash crash — no news, a violent plunge, full bounce by day's end.) Therefore plan for the worst-case scenario every day: exit orders / conditional (contingent) orders ready with the broker even on calm days; never leave a position unattended for hours without protection. The single technical key to long-term success in options income trading: these wide, high-win-rate trades win in most scenarios by construction — all you must do is keep the size of the losses controlled. Letting losses run through sloppiness is a discipline failure, not bad luck.

**Controlling emotions is ≥50% of the battle** — the major determinant of success in any trading style. Tools: mindfulness training, and visualization (taught at SMB): calmly breathing through imagined market scenarios so live versions don't trigger overreaction. [MmryR1iu9dA]

**Blunder #4 — "I'll pay my bills out of my options income."** [Is9CVUBT9y0] Income strategies produce their average UNEVENLY; treating trading income like a salary or bond coupon is childish. Illustration: a backtested SPX strangle protocol (sell 12 calls 5% above and 12 puts 5% below monthly, targeting ~$60,000/yr ≈ $5,000/mo). April 2019 trade: SPX 2864 → sell 12× 3000C @0.97 (+$1,164) + 12× 2725P @7.63 (+$9,156) = +$10,320; expiry day SPX 2939, both sides @0.03 → close for $360 + $360 → +$9,600. May trade: SPX 2923 → 3075C/2775P for +$14,148; expiry SPX 2757 → the puts finish 18 points ITM @18.03 → closing costs >$21,000 → month −$7,838. A hypothetical 2019 of this strategy hits the annual average with 4 losing months out of 12. Consequences: (a) benchmark = an accomplished options income trader earns 2–4% per MONTH on capital — size the account from that, not hope; (b) excess winnings in good months are RESERVES for losing months, not spending money; (c) start with a cash reserve equal to a few months of backtested drawdown, because the losing months may come first; (d) drawing the account below its working capital level after losses breaks the math that produced the backtested return. [Is9CVUBT9y0]

**Blunder #5 — "I always win eventually if I keep rolling my short puts down."** [SmMsPFLFqc0] Technically true, practically insane — the martingale of options. The worked horror: Aug 17 2015, SPX ~2100 → sell 10× 2040P 12 DTE @3.45 (+$3,450); broker holds $255,000 (naked puts). Roll protocol: when the short put's delta reaches ~20, buy back and re-sell at the new 10-delta, adding enough size to keep ~$1,000 of net credit (most traders wait until ~10:30am to adjust after an open). Aug 20 gap-down: the 2040P is at 41Δ, buyback costs 16.25 (−$16,250) → roll to 35× 1975P @3.95 → capital requirement $819,000. Next day SPX 2015: 1975P at 27Δ → roll to 75× 1925P (buying back 35 @12.15) → capital $1,616,000. End of Aug 21: roll to 218× 1800P, running P&L −$154,000, capital >$4,000,000. Three days later: −$314,000, roll to 365 puts, capital $6,500,000. The market then bounced and the campaign ended "very slightly profitable" — which is exactly the trap: a $3,450 Valentine's-money idea escalated to needing $6.5M of margin and a $314k drawdown to eke out breakeven. Nobody has unlimited capital and no emotions; in the real world you cry uncle mid-sequence and eat a catastrophic loss. Professionals never martingale rolls. [SmMsPFLFqc0]

**Blunder #10 — chasing the holy-grail strategy / chasing returns.** [dLZYl7kC468] Every valid strategy has predictable losing periods (a 95%-PoP trade loses 5% of the time, and that loss returns a chunk of prior profits at once); traders who backtested and KNEW this still abandon the system when the loss arrives live, hop to whichever strategy won last year, and repeat. Real six-year illustration from two desk strategies: 2013 — A ≈ breakeven, B +178%; 2014 — A the better year; 2015 — A slightly better; 2016 — A takes its big loss, B +24%; 2017 — both solid, A outperforms; 2018 — A nice, B weaker. Buy-and-hold: A alone +409% over the six years, B alone +578% — but the return-chaser who each January switched into the prior year's winner did WORSE than either, systematically arriving in each strategy just in time for its weak period. Strategies have complementary strengths and weaknesses across market regimes that are near-impossible to time; trade both, persevere through the predictable setbacks, and never rank systems on one year. [dLZYl7kC468]

**Blunder #1 in full — "I'll trade $500,000 the same way I trade $5,000."** [-rwYS0Dq6Ro] The opening episode of the ten-part blunders series; Freudberg calls it the most devastating mistake. Worked arithmetic: a $5,000 account trading a monthly income strategy with a $500 (10%) target and a $500 stop (1:1 is fine given the high win rate), where the trade routinely draws down ~$400 before recovering. Six months: +$350; +$500 (after a −$400 drawdown); −$500 stopped; +$350 (after −$400); −$100; +$400 (after −$400) → +$1,000 = 20%, worst drawdown $500. The fatal thought: "on $500,000 that's $100,000." He funds $500k and runs the identical strategy; the same −$400 mid-trade dip is now −$40,000 (the stop is at −$50,000, but he has never seen −$40,000) → panic, close, repeat: five of six trades closed at −$40,000 → −$135,000 = −27%, where the un-panicked version would very likely have made the $100,000. "I have never met anyone who hasn't failed in this exact scenario." Freudberg's own start: six straight winning months on small capital before the first loss — the cocky phase. The desk's traders draw down $75,000–$100,000 intraday and make millions a year — a tolerance built like weight training: start at 50 lb, add 5 lb (10%) at a time, at 150 lb the same 5 lb is 3%; one trader reached 500 lb (+1,000%) over years, never in three days. Prop accounts can reach $20M; nobody gets there from $5k in one jump. Scars from a premature blow-up often leave traders permanently trading scared, which does not work either. [-rwYS0Dq6Ro]

**The ATM-machine blunder in full arithmetic: the 8-delta RUT iron condor, 2024.** [FYNpBJDuXhU] A complete worked case of principle #1 (never scale on a streak). Feb 1 2024, RUT open 1964.07 (up >300 from the Oct 2023 low 1633). On the Mar 1 chain (30 DTE) sell the ~8-delta call and put, buy wings 40 points beyond: sell 2150C (Δ8.27) @4.40, buy 2190C @2.50; sell 1790P (Δ8.11) @5.30, buy 1750P @3.55 → +$365 credit, broker capital $3,635 (= $4,000 width − credit), i.e. ~10% cash-on-capital; PoP = 100 − 8.27 − 8.11 = 83.62% → expect ~10 wins and ~2 losses in 12 months. Mar 1 close 2076.39 → +$365 = 10.04%. Apr 5 chain: 2290C/2330C + 1880P/1840P → +$410 on $3,590 = 11.42%. Five consecutive 1-lot wins Feb–Jun: +$1,964 = 54.44% in five months — the "ATM machine" feeling. Jul 5, RUT 2052.87: the trader jumps to a 10-lot (short 2210C / 1900P, +$3,560 credit). The index broke out and closed 2254.48 at expiry: short calls 44.48 ITM → −$44,480, the long 2250C returns only $4,480 → trade −$36,440; the six-month campaign ends −$34,476. Entirely predictable — a trade that loses ~2 of 12 months will lose, and the 10× size was placed exactly where the loss landed. Then the worst part: the trader quits (out of capital or confidence). SMB raises its traders' capital very gradually for precisely this reason; the retail trader must impose that discipline on himself. "There is no Santa Claus, there is no ATM-machine trade." [FYNpBJDuXhU]

**Blunder #2 — "I own the call for free" (financing a long call with a naked short put).** [tT08tJdsH_E] FB at an all-time high 217: buy the 220C @2.80 (−$280) and sell the 210P @2.80 (+$280) → zero cash outlay, "a free call". At expiry FB 174.89: the put is exercised, the trader owns 100 shares at 210 → −$3,500+ — to save $280 he turned a defined $280 risk into one more than ten times larger. The insurance analogy: insuring a $100,000 house for $500 and buying a lawn mower with the premium is not a free lawn mower. Free of cash flow ≠ free of risk; pros "hardly even acknowledge the cash-flow aspect" and look only at the full risk/reward of the structure; selling an option is entering an obligation — if you don't understand it, don't trade it.

**Blunder #6 — strategy hopping ("I'm switching to the strategy that's crushing it").** [LwZ9s2ud68s] After two or three losing months traders envy the "flavor of the month" strategy everyone is bragging about and switch. Every options income strategy is cyclical — no strategy works in every market environment, and the backtest that justified it ALREADY showed those losing periods (often the worst periods precede the best). Real backtest of two SMB course strategies: 2013 — bearish butterfly <1%, "the Bull" +61.6%; 2014 — bearish butterfly +146%, Bull +26.8%; 2015 — bearish butterfly +107.6%, Bull +8.6%: the hopper who switched after 2013 missed the two triple-digit years, and sticking to EITHER beat hopping. Rule: abide by the backtest that admitted the strategy; switch only if the market has fundamentally changed in a way that renders it ineffective (rare); learning from others' sustained success is fine — a few recent wins vs your few recent losses is not data.

**The worst mistake a beginner makes: sizing up 10× after a winning streak.** [ftmEH4ikBy4] Setting: SPX weekly 10-delta iron condors with 50-point wings, traded 2 lots, started on the last day of Q1 2023 with the index at 4109.31. Trade 1, entered near the close on the Apr 6 chain: sell 2× 4200C @2.60 (delta 8.87) and 2× 4000P @8.20 (delta 9.74), buy 2× 4250C and 2× 3950P @3.46 → +$894 credit; SPX closed 4105.02 → all four die. Trade 2 (Apr 14 chain): shorts at 4210 and 3980 → +$1,274; index 4137 at expiry → win. Why the win rate is about 80%: a 10-delta option has roughly a 10% chance of expiring with value, so each short has a 90%+ chance of dying and the longs an even better one; combining a call side and a put side around the market gives approximately 100 − 10 − 10. The streak ran to TEN consecutive wins totalling $9,718 — an average of $971.80 a week on roughly $9,000 of capital per trade — at which point the "virtual ATM machine" reasoning took over: fund the account to $100,000 and trade 20 lots instead of 2. The very next trade: shorts 4390C / 4190P → +$9,200 credit against about $90,800 of requirement; SPX rallied to 4409.59, its first close above 4400 all year → 19.59 points × $100 x 20 lots = $39,180 of payout → -$29,980 in one week, wiping out all ten wins. At the original 2 lots the identical loss would have been -$2,998. Finishing the quarter back at 2 lots (Jun 23 +$726, Jun 30 -$3,278), the actual campaign ended at -$22,800, whereas staying at 2 lots the whole time would have produced +$4,168, about 44% on the peak capital a 2-lot condor required. Freudberg says he has never met a trader who psychologically recovered from such a loss; they lose faith in well-researched systems and go back to the career they were trying to leave. The doctrine: **treat risk tolerance as a muscle that is built gradually** — after a quarter at 2 lots go to 3, at most 4; then watch how a loss at the new level actually feels, since your faith in the research is what is really being tested; and, counter-intuitively, **never raise size right after a winning streak while you feel cocky — raise it after a loss**, once you know you can absorb one at the current level. A best practice stated as a rule: do not increase the capital level until you have experienced at least one loss at the current level. (Freudberg's own version of the mistake: six straight winning months, capital up 2,500%, sized up, got killed, never traded that strategy again [FDpmRhFsp5s].) [ftmEH4ikBy4]

**The five deadliest mistakes (and the arithmetic behind each).** [i0h4_uVeDtY] Framing: high-win-rate income strategies (the Rhino's historical win rate is 80%) produce winning streaks that feel like invincibility — which is precisely the most dangerous feeling a trader can have; a mentoring student who called credit spreads "an ATM machine" was forbidden from ever saying it again ("what would you call an ATM machine that reached into your wallet and took cash out — because that is what a trading loss is"). **(1) Scaling capital off a short winning streak.** Real case: a trader ran a $25,000 account as an experiment, was +22% in five months with a 100% win rate, concluded he had been an idiot to trade small, and moved his entire planned $500,000 in at once; June brought the first, statistically inevitable loss and it erased every dollar of the gains plus another $29,000 — a year that was heading for +30% ($7,500 on the original size, then a judicious ~20% capital increase the next year) turned into a career-ending experience instead. Options income strategies tend to yield roughly 30% a year on the capital actually used, and only if the capital used stays constant. **(2) Market orders instead of limit orders at the mid.** Real NDX iron butterfly, 10 lots: executed at mid prices the spread brings in $140,850 net, the broker requires $9,150 (the worst case) and the maximum reward-to-risk is 15.39:1; the identical spread entered as a market order — selling at the bid, buying at the ask on all four legs — brings in over $10,000 LESS, and because the requirement is driven by what you took in, the broker then demands more than double the capital and the reward-to-risk falls below half. Most options trades execute at or near the mid; the order type alone is worth a fortune over a career. **(3) Strategy hopping (recency bias).** Strategy A returns 30% for the year but delivers five winning months, then three flat-to-losing ones through August; a trader who abandons it in September for strategy B — which also returned 30% for the year but front-loaded its good months — walks straight into B's weak stretch and ends the year at 4%. If you back-tested the strategy and know it has down periods, the drawdown is not evidence of breakage. **(4) Buying cheap far-OTM options.** GIS closed 74.92 on Jul 15 2022; 10× September 85 calls cost 13 cents = $130 total — "not much risk" — but their delta was 2.76, i.e. a 97.24% chance of expiring worthless, and on Sep 16 GIS closed 75.25 exactly as predicted. Check the delta before buying: cheap is cheap. **(5) Believing your back-test.** Live results are worse than the back-test essentially always, for five reasons: execution errors (which must be reversed immediately, at a cost, plus double commissions and a worse entry on the intended trade), slippage against the mid prices back-tests assume, commissions omitted from the test, portfolio interaction (in a big move you are managing every open position at once, so you blow through a stop the back-test would have honoured), and human emotion — greed or fear making you deviate, at which point you are no longer trading the strategy you tested. Experience narrows the gap but never closes it. [i0h4_uVeDtY]

## CHAPTER: Trader psychology & performance (Steenbarger)

From Dr. Brett Steenbarger's talk to SMB traders (he has worked with top hedge funds, asset managers, and SMB since 2007). [mKQq33Rtdfo]

**Know who you're making money from.** Edge begins not with setups but with knowing whose behavioral tendencies you exploit. Today's opportunity: the multistrat hedge-fund world has exploded — funds of $20–40B are common, a *starting* book for a new hire is $200M — while allowable drawdowns have tightened from ~20% (when he started at a macro fund) to 5–10% now. Result: crowded trades plus hair-trigger risk limits → forced unwinds. A short-term trader who reads the tape can be quicker than that herd and catch the crowd getting in and out. Example crowded idea: the past year's persistent (and so far wrong) recession/rate-cut positioning around the inverted yield curve — while the money was made elsewhere (oil, copper, select equities). Knowing what the crowd chases tells you where the *un*crowded opportunity is.

**Ideas before setups.** Institutions enter trades from researched ideas (central-bank policy, economic data, geopolitics); the setup/chart is only the final translation of idea into risk-reward. Retail traders who start at the setup are starting at the wrong end.

**Reading the big players.** Volume — especially relative volume (volume vs normal for that time of day) — is the footprint of institutional participation; a breakout on surging relative volume means new large players, not retail three-lots. Rotation: a "choppy" market is often institutional money *rotating* (growth↔value, discretionary↔staples, large↔small cap); track relative strength between sectors — the trend may be in the relative play even when the index is rangebound. Patterns of relative strength/weakness tend to *precede* patterns of absolute strength/weakness (his example: regional banks and commercial real estate unable to make new highs in a raging bull market as an early warning). Trapped-trader pattern (his most reliable): persistent buying pressure that can't make new highs, or persistent selling that can't make new lows — read via the NYSE TICK (upticking minus downticking stocks, published ~20×/minute) and via whether transactions lift offers or hit bids; sellers repeatedly hitting bids with no new lows are shorts about to be squeezed, because larger players are absorbing them (iceberg orders). Creativity tool: volume bars instead of time bars — in Chicago quant firms each bar = e.g. 10,000 futures contracts traded, not N minutes; market cycles become far more regular in volume-time, which helps time entries (buy the short-term oversold in an uptrend) and improves risk-reward enough to trade bigger size. For cycle work: short-term RSI on trending series still shows cycles; John Ehlers' MESA software formally identifies dominant cycles.

**Positive psychology of performance.** Build on strengths, not just fix problems: journal what you did *well* and how to repeat it, not only "how I shit the bed." Study yourself at your best — your peak trading experiences point to your niche; early on, deliberately trade different markets, timeframes, and patterns until something clicks. Four dimensions to keep firing: happiness, fulfillment, energy, affection — an unbalanced all-trading life makes your psychology ride the P&L and leads to burnout (which kills creativity and productivity); many trading problems come from the *absence of positives*, not inner conflicts. Broaden-and-build (Fredrickson): open, positive mindsets literally widen perception — the best traders simply look at more things in more ways (the standout trait of SMB's Kenny "Shark": far more screens, faster processing, more perspectives). Flow states (deep absorbed focus) enhance the creativity that generates trade ideas.

**Mentoring, teams, practice.** Every elite performance field shows two constants: mentoring/coaching (nobody becomes elite alone), and more time spent practicing than performing — the big reason traders fail is they only want to *trade*, skipping practice. Successful hedge funds are organized in multi-specialty teams with an "each one teach one" culture; build a network with the same property. Trading is multiple processes: idea generation → trade structuring (use trends *and* cycles for timing/risk-reward) → trade management → portfolio construction. For a short-term trader, the "portfolio" is what you trade *over time*: diversify across instruments, timeframes, and patterns so something is always working; a one-trick pony has all eggs in one basket.

**Metrics to track (works across any market).** Average win vs average loss; profitability vs number of trades placed (do you make or lose more when overtrading?); profitability as a function of holding period. Diagnostic example: a trader whose positions started profitable then reversed was running a momentum (long-volatility) style in a low-volatility market — low volatility on average means more reversals, less follow-through; the stats revealed it. Career longevity: most who wash out don't lack ability or motivation — they put money at risk too quickly and lose too much to survive the learning curve (echoing [MmryR1iu9dA] on sizing patience). The traders with the longest careers trade for meaning beyond money (building a business, mentoring, philanthropy — Brooks' "second mountain"). Context datum: in his Chicago short-term-trading days the average holding time was six minutes. [mKQq33Rtdfo]

**Thinking like a hedge fund, trading like an intraday trader (Steenbarger with SMB's head of trader development).** [rnETl_NteAo] Two separate processes at the big funds: IDEA GENERATION (synthesizing macro data, earnings, cross-market developments into differentiated views) and TRADE CONSTRUCTION (only then translating the idea into a trade with good reward-to-risk). They think in THEMES across currencies, rates, and equity sectors — e.g. post-election US assets stronger than overseas (dollar, US stocks); rising long-end yields pressuring rate-sensitive sectors (utilities, homebuilders, real estate weak); overseas economic weakness → reduced commodity demand (XLB weak); strong US growth expectations → growth over value (XLK strong) — and assemble a diversified portfolio of trades from several themes. A short-term trader borrows the themes to know what is relatively strong and weak, and — more important — HOW the strength is playing out: momentum markets (everything up or down) vs ROTATIONAL markets (total money unchanged, capital shifting between segments) — in rotational tape what you trade matters as much as how. Sector breadth is the confirmation: all sectors moving together = trend; sectors diverging = rotation → trade the rotation or hunt trends inside the unusually strong/weak sectors. A playbook that "suddenly stops working" is usually the right trade in the wrong environment — treat it as information that the environment changed (the snowy-field football analogy), not as a personal failure; the first clue is usually that trades built on one set of assumptions stop playing out. The desk's environment grid, scored at ~9:45am, midday (many use the European close), and the end of day, each time asking only "is the earlier read still holding?": **high strength / low weakness** — trending momentum tape, every pullback bought, breadth across names and sectors; up-moves retrace less than half before the next leg → momentum and trend-continuation plays, hold longer, expand your reasons to sell; **low strength / high weakness** — the mirror image, "sellers in control"; **low strength / low weakness** — choppy, cyclical: quick moves into resistance fail and grind back to support and vice versa; instruments not even moving one ATR; momentum trades still appear but their expected value collapses — trade the cycle up and down with short holds, and don't force the breakout that everyone expects at the range edges; **high strength / high weakness** — the desk's favorite: sustained moves followed by aggressive full retracements; typically an elevated VIX; the whole playbook is on the table, including reversion trades. Update frequency scales with volatility. The intraday trader's edge over the funds: he can act within minutes when participation shifts (relative strength/weakness and relative volume changes between sectors are the real-time clues), letting the big players' research and positioning become his information. New traders on the desk start with scalping (the "scalp radar" tool). [rnETl_NteAo]

## CHAPTER: Getting started: brokers, practice, capital

All from the beginners' course. [w_BjFmbwbYA]

**Broker requirements (eliminate any broker missing these):** full options chains for all major stocks/indexes; pre-filled strategy menus and complex-order tickets (iron condors, butterflies, calendars, diagonals, vertical spreads); detailed profit graphs (P&L vs underlying price at expiry — essential for seeing breakevens and risk at a glance as positions get complex); the Greeks displayed in the platform — at minimum delta (option price sensitivity to underlying move), vega (sensitivity to volatility), theta (daily gain/loss from time passing). The three platforms most active options traders use: thinkorswim, Interactive Brokers, tastyworks.

**Cost structure to compare, cheapest ≠ best:** per-contract commissions typically $0.15–$2.00 (charged on entry *and* exit — think round-trip; at least one major broker waives the exit commission); zero-commission brokers monetize order flow and may have limited capability; ticket charges — a $10 ticket + $0.20/contract broker costs $10.20 for a 1-lot, worse than a $1.50/contract no-ticket broker; watch for stacked extra fees (clearing, regulatory, exchange access, membership) vs all-in pricing — clarify before opening the account; market-data fees — subscribe only to the data you'll actually trade; assignment/exercise charges vary by broker. High-volume traders: commissions are negotiable — probe before deciding.

**Sequence before risking real money:** (1) get a comprehensive options education (strategies, capital/margin requirements, adjustment skills, Greeks) — without it you'll wander into dangerous positions; (2) backtest each strategy on real historical options data to learn its rhythm and build "muscle memory" of wins and losses; (3) paper trade on the broker's free simulated account long enough that operating the platform is second nature — never learn the platform with live capital; (4) go live *small*: early losses are tuition, so keep tuition cheap; mistakes are magnified by unnecessary size.

**Capital levels:** minimum recommended funding $5,000 — enough to practice all major strategies. Pattern-day-trading rules: below $25,000 the broker's risk software limits your trades per week if you trade more than minimally; fund $25,000+ to trade actively. Brokers will also screen your options knowledge before granting options permissions. [w_BjFmbwbYA]

**Getting a funded options account (Andrew Falde, funded SMB options trader).** [fTbHswbCOls] Five steps: (1) MODEL an edge, don't invent one — take an existing, proven, describable edge (via study, mentoring, working with professionals ahead of you) and execute it with skill, care and diligence; traders fail by trying to be too unique. (2) Prove it historically first — backtest/incremental historical execution with documentation takes days-to-weeks of part-time work, and share it with potential funders for feedback BEFORE burning years building a live record on something they'd never fund. (3) Prove it live — ANY amount of real-world time with similar results is enough once the historical proof exists; no 3–5-year track record needed to get a foot in the door; tiny size is fine (it still proves you can execute and get filled; live beats sim). (4) Present professionally — not a stack of brokerage statements: document why the edge exists, journal it, produce graphs and statistics (Sharpe ratio, max drawdown, drawdown duration, return-on-drawdown, flat periods, largest losses) in a summary report that makes the funding decision easy. (5) Be optimistic yet humble — 3–4 months of stellar results may be luck; funders specifically screen for the humility to recognize when the edge stops performing and act accordingly, rather than fight the market. [fTbHswbCOls]

**The ten traits of the desk's successful options traders — the funding checklist (Freudberg).** [25ej9CwzTGQ] What SMB looks for before allocating capital, and therefore what to work on: (1) **Solid theoretical training** — options pricing is not intuitive (own the 120C on a $100 stock, the stock goes to 115 with three days left, and the call is DOWN: time, volatility and price all move it); you need the intellectual framework. (2) **Worked with a mentor** — nobody learns golf from a book; studies show mentoring predicts trader success; most desk traders were mentored in-house. (3) **Experience of the right shape** — neither backtests alone (a trader presented strategies to a weekly online group for two years before anyone realized he had never traded live; the #1 reason traders fail is not following their own discipline, which only live trading tests) nor 3–6 months of live trading alone; the desk wants ≥5 years of backtest + live combined so the strategy has met rough markets. His own lesson: after four winning months he told his office partner "this is like stealing candy from a baby" and "got murdered" the next month; a mentoring student's "ATM machine" phrase was banned on the spot. A bullish strategy that won nearly every month of 2013 would have been wrecked in Feb and Q4 2018 — if you never backtested through 2008 you don't know how bad it gets. (4) **A bread-and-butter strategy** — the core monthly trade you have seen work across market environments and feel confident putting on every month (one desk trader needed ~2 years to find his); it should make some money in its worst environment and real money in its best. (5) **An account that is neither too small nor too large** — the desk's minimum allocation is $100,000; a trader used to a $1,000 account (10% stop = $100) freezes at a $10,000 loss and abandons a trade that would have come back; the sweet spot is a ≥$25,000 personal account; a $2M "high roller" given $200k gets bored by swings in the thousands instead of six figures. Risk tolerance is a muscle: 100 lb → 125 lb, not 100 → 1,000. (6) **Returns** — 24–36 months of live trading above 30%/yr, plus backtests to ≥5 years combined, graded on a curve against the desk's own results in the same years and specifically examined in rough markets. (7) **Live-traded through a rough market**, and backtests that include the stress episodes: October 2008 (a current desk strategy had its best month then), the May 2010 flash crash, Aug–Dec 2011 (European sovereign-debt crisis + S&P's US downgrade), the August 2015 China-currency crash, Nov–Dec 2016 (post-election rally), February 2018 ("the volatility apocalypse"), Q4 2018 (three-month near-correction). (8) **Not just lucky** — naked straddles/strangles, weekly-only strategies (long runs then "kaboom"), one well-timed bottom-buy of cheap calls, or the "secret sauce" fund that sold far-OTM puts (9 of 10 expire worthless) for years and then went bankrupt on the tenth — a high win rate with catastrophic downside is a predictor of failure, not success. (9) **A team player** — passion for markets, hard work, appetite for learning and experimenting, willingness to share ideas and take advice, not cocky ("the cocky ones haven't been tested yet"). (10) **Maturity** — knows how to lose (take the stop: at SMB not taking your stop ends your tenure); not greedy (up 9% of a 10% target with Brexit tomorrow → take it — the "foolish consistency" rule); does NOT take profits too early (down 2%, back to +0.5%, target 10% → let it work); prepares: at 8:30am ET knows where futures are, has an upside and a downside plan and complex-order tickets pre-staged, watches the economic calendar (NFP, FOMC, minutes, speakers), keeps a disaster-recovery plan (he traded from a Starbucks during a Philadelphia snowstorm power cut), and covers absences with contingent orders or a "trading buddy" — every desk trader has one who monitors his positions. Summary: income trades win ~9 of 12 months; winning is the easy part — the successful ones control the losses in the losing months. Remedies for a failed self-test: serious education, a mentor, an options community (the desk's "options tribe" chat), find the bread-and-butter trade, and keep careful records — "nobody at a prop firm will talk to you if you can't prove your assertions." [25ej9CwzTGQ]

**The transition into a professional options trader (Freudberg's own path, and what the desk wants).** [FDpmRhFsp5s] Biography as a case study: 15 years as CEO of a property & casualty insurer (an industry he rates 135th of 194 for returns, where policyholders, claimants, regulators and juries are all angry at you at once), retired 2006, nine months under a non-compete spent deciding what to do next; the first trading "education" he encountered was a two-day $100 seminar that pitched a $10,000 course and taught the audience how to shuffle the fee across maxed-out credit cards — the reason he insists there must be a better way to learn than paying scammers. He chose options income trading on the basis of a personality inventory he suggests others run on themselves: he hates to lose (a flaw, but real); he prefers to think things through rather than make snap decisions, sometimes modelling a trade for two hours; he likes bets with many ways to win; he knows he is bad at picking market direction; and he is willing to sacrifice return for safety — he actually likes it when his hedges lose money, because that means the underlying trade is working. Then the misadventures: an iron-condor strategy that won six months in a row and grew his capital by 2,500%, which he promptly sized up, got killed on, and has never traded since; several other strategies that each revealed a weakness that was a weakness FOR HIM; and four years of searching before he found his bread-and-butter trade, the "Rhino" — chosen not for return but for shape: 25-30% a year with drawdowns that rarely exceed 5-6%, in deliberate preference to strategies that make 100% a year at the cost of a 30% drawdown along the way ("that is just not the way I am built"). Career mechanics: he took SMB's five-week equity course at 50 (surrounded by 25-year-olds), was asked to become the firm's options guy, and built the Options Foundation course plus the Options Tribe community — one webinar on May 15 became every Tuesday at 4:30pm ET, close to 500 recorded sessions over nine years, with premium archive access at $30/month. **What the desk looks for:** traders who know iron condors in their sleep and many sophisticated structures besides; who have found their bread-and-butter trade; whose focus is risk management rather than profit ("the key is controlling the size of your losing months, because you are going to have so many winning months"); who expect to win every time they put a trade on yet are comfortable with losing; consistency of returns over grand slams followed by strikeouts; and professional habits — always at the desk at 9:30, protective orders in place before leaving it. Desk traders are remote (Indonesia, Australia, California, Slovakia) and many hold demanding full-time jobs, because range-based income trading does not require constant screen time: one traded from 9:30 to local midnight, then entered his final and protective orders and slept; another, Andre in Slovakia, did not know what a call or a put was when he took the course and now trades hundreds of thousands of the firm's capital every month. **Why people fail:** not treating it as a business (of 10 mentees a month who had each paid $6,000 for a course including 13 mentoring sessions, five never answered the scheduling email at all, two attended once or twice and vanished, and one of the remaining three never finished — against a roughly 20% success rate across all forms of trading, so "half of life is just showing up"); getting cocky with one strategy and sizing up; trading like a robot that never deviates however obviously conditions have changed; and the opposite failure, planning the trade and then not trading the plan. **Two rules he repeats:** never bump capital in a strategy until you have taken a loss in it, because you do not know how you will feel afterwards and the loss may expose a recurring flaw; and *trade, do not merely follow rules* — up 90% of target profit with the Brexit referendum tomorrow, take the trade off, whatever the rule says about waiting for 100%. His teaching example of an income trade: a two-month SPX iron condor entered Apr 20 2020 with the index near 2900 and expiring Jun 19, short the 3400 call and the 2200 put → $28,000 of profit at ANY close between those two strikes, i.e. it needed a 700-point drop to the pandemic low or a 500-point rally to the February all-time high in 60 days to fail; it won in full. Tooling from the same talk: roughly 75% of options income traders use thinkorswim, about 15% Interactive Brokers and about 10% tastyworks; dedicated analytical software (OptionVue, OptionNet Explorer) costs around $1,000 a year and he "wouldn't know how to trade without it". Learning curve: options income takes longer to learn than equities — two or three months of study before the light bulbs go on — but is easier to execute once learned, and does not require quitting your job, because the trade is a bet on a RANGE rather than the next tick (his golf analogy: you are not trying to hole the first putt, you are trying to land inside a five-foot radius). Desk nicknames worth recognising in the literature: the jeep, the Caspian Sea Monster, the rhino, the butterfly, the speeding train, tranche warfare, the weirdor. [FDpmRhFsp5s]

## CHAPTER: Real numbers from the desk

Registry of every concrete number in the five videos (for backtest-realism parameters). "≈" marks values the auto-transcript garbles; the reconstruction is noted.

| # | Instrument / context | Strategy | Numbers | Source |
|---|---|---|---|---|
| 1 | SPY, Mon Aug 28 (2023), open 442.24, close 442.76 | 0-DTE iron condor | Sell 10× 445C @ $0.25 (+$250), 10× 441P @ $0.43 (+$430); buy 10× 446C @ $0.11 (−$110), 10× 440P @ $0.27 (−$270); net credit $300; margin/max loss $700; all expired worthless → +$300 = +30% on a $1,000 account in one day | [hsPmj_6nl5E] |
| 2 | MSFT, Jun 1 2022 @ 272.42 (−20% YTD) | 1-year call debit spread | Buy Jun 2023 295C @ 26.33 ($2,633), sell 320C @ 16.78 ($1,678) → debit $956 (>60% below naked call). Jun 16 2023 MSFT 348.10: 295C = 53.25, 320C = 28.22 → close $5,324 − $2,822 − $956 = +$1,546; $1,000 acct → ~$2,546 in 1 yr | [hsPmj_6nl5E] |
| 3 | HRB, Jan 20 2022 @ 21.58 | Deep-ITM LEAP call | Buy Jan 20 2023 15C @ 6.90 = $690 (vs $2,158 for 100 shares). Jan 2023 HRB 37.25, call = 22.90 → +$1,600 = >230% on risk; shares alt.: $3,725 − $2,158 = +$1,567 (less than the option) | [hsPmj_6nl5E] |
| 4 | Small accounts generally | — | Trainees started with accounts of a few hundred dollars; all three strategies sized for a $1,000 account | [hsPmj_6nl5E] |
| 5 | AAPL, Dec 17 2021 @ ~171.50, 300 shares | Quarterly covered calls (sell-and-expire) | Sell 3× Mar 170C @ 11.43 → $3,429; Mar 17 expiry AAPL ≈160, worthless; reload 3× Jun 170C → $1,905; full-year total $6,549 ([LWLFq1cMOdo] confirms the figure [U8gFC00kZ58] garbled as "654"); vs AAPL dividends $273 on 300 shares in 2022; AAPL dividend yield ~0.5% vs S&P avg 1.71% | [U8gFC00kZ58][LWLFq1cMOdo] |
| 6 | AAPL, same campaign | Covered calls, sell-and-buyback @ ~10% rule | Feb 24 2022 gap-down open 152.94 → buy back Mar 170C @ 0.69 → +$3,222 leg; Mar 2 AAPL >166 → sell 3× May 170C ≈8.05 (+$2,415); May 3 (17 DTE) AAPL <160 → buy back at ~10%; year total >$10,000 = +64% vs sell-and-expire; 6 trades vs 4; shortest trade 15 days; worst leg (Aug calls) +$60 | [U8gFC00kZ58] |
| 7 | FNV (Franco-Nevada), Jan 28 2022 @ 127.17; support 125 / resistance 150 | Synthetic covered call (deep-ITM calls + short OTM calls) | Buy 10× Jul 100C @ 29.30 (≈$29,300–29,400); sell 10× Feb 150C @ 0.38 (+$380) → net ≈$28,920. Feb expiry FNV 147.77 → shorts worthless; sell 10× Mar 150C @ 4.77 (+$4,770) → net $24,150. Mar 18: FNV close 154.34 (stock 154.60 at exit; Jul 100C sold ≈54.60). Options profit >$30,000 vs shares +$27,430 on $127,170; shares return 21.56%, options return ≈102.9% (transcript garbles as "10.29%") | [U8gFC00kZ58] |
| 8 | TSLA, Jan 20 2023 @ 127.89 (2022 high 402.67, −75%); target 200 | Covered call strike placement | Jul 2023 chain: 130C @ 23.75 vs 200C @ 5.72. Jul 21: TSLA close 260.02. 130C route: ~$211 shares + $2,375 premium = $2,586. 200C route: $7,211 shares + $572 premium = $7,783 (≈3×) | [U8gFC00kZ58] |
| 9 | Generic stock XYZ @ 175, May 1 | Long call teaching example | 180C exp Jun 30 @ 3.50 = $350; stock 190 → +$650 net; stock 160 → −$350 | [w_BjFmbwbYA] |
| 10 | Generic stock ABC @ 60, Aug 1 | Protective put | 50P exp Oct 21 @ 2.05 = $205; stock 42 → saves $800 gross / $595 net; stock 68 → put worthless | [w_BjFmbwbYA] |
| 11 | Generic stock @ 98 close, 95C owned | Exercise mechanics | Pay $9,500, receive $9,800 of shares → +$300 unrealized | [w_BjFmbwbYA] |
| 12 | Index @ 1445, Mar 1 | Long index call / seller's edge | 1500C exp Apr 30 (60 DTE) @ 39.50 = $3,950. Index 1620 → payout $12,000, +$8,050. Index 1590 → payout $9,000, +$5,050. Index 1520 → payout $2,000, −$1,950. Breakeven 1539.50 (94.50-pt rally to break even); seller wins at any close < 1539.50 — can be "wrong by 94.49 points" and profit | [w_BjFmbwbYA] |
| 13 | Index @ 1425 | Long index put | 1350P @ 52.25 = $5,225; index 1280 → payout $7,000, +$1,775 | [w_BjFmbwbYA] |
| 14 | Index put cash settlement | — | 2950P, index closes 2750 → transcript states $2,000 payout (rule $100/pt would give $20,000; transcript example as spoken) | [w_BjFmbwbYA] |
| 15 | Real stock @ 157 | Long call vs shares leverage | 160C 30 DTE @ 3.00 = $300; stock closes 177 → +$1,400, R/R 4.66:1. Shares alt.: 70 sh × $157 = $10,990 for the same +$1,400, R/R 0.127:1 | [w_BjFmbwbYA] |
| 16 | Stock XYZ @ 200, 100 shares, 1.5% dividend ($300/yr; S&P 500 avg dividend 1–2%) | Covered call income math | Sell 1-yr 220C @ 17 → $1,700; income $2,000 = 10% (>500% over dividend alone). Called away at 228.91 → +$1,700 + $300 + $2,000 cap gain = 20% year | [w_BjFmbwbYA] |
| 17 | Index @ 3225 | Naked put vs put credit spread | Sell 3200P @ 20 → +$2,000; index 3120: naked loss −$6,000 ($8,000 payout). Spread: also buy 3175P @ 11 → net credit $900; long put pays $5,500 → loss capped at −$1,600 | [w_BjFmbwbYA] |
| 18 | Index ≈1880, Friday early June, 8-week (late-July) chain | Iron butterfly | Sell 1880C @ 83.95 + 1880P @ 84.40; buy 1980C @ ~37.55 + 1780P @ 49.65 → credit $8,115; margin ≈$1,885 (transcript garbled; wing width $10,000 − credit). Expiry Jul 29 index 1885.23 → pay $523 → +$7,592 = >400% on margin in 8 weeks. Alt close 1840 → put payout $4,000, still ≈+$4,115. Breakevens = 1880 ± 81.15 pts (≈1798.85/1961.15; transcript misstates "1718/1881.15") | [w_BjFmbwbYA] |
| 19 | Iron condors / neutral strategies | Win-rate claim | Range strategies settable at >80%, even >90% probability of winning; marketing segment claims a strategy with "statistical 80% probability of profit month in and month out" | [w_BjFmbwbYA][MmryR1iu9dA] |
| 20 | Broker economics | Costs | Commissions $0.15–$2.00/contract (entry and exit; one major broker waives exit); ticket-charge example: $10 ticket + $0.20/contract = $10.20 for a 1-lot vs $1.50 flat elsewhere | [w_BjFmbwbYA] |
| 21 | Account funding | Capital minimums | Recommended start ≥$5,000; $25,000+ to avoid pattern-day-trader trade limits | [w_BjFmbwbYA] |
| 22 | Income-strategy seasonality | Expectation setting | A typical income strategy wins ~9 months out of 12; a 5-yr (60-month) backtest showed ~20% losing months | [MmryR1iu9dA] |
| 23 | Sizing / stops | Risk framework | 10% trade stop examples: $10,000 acct → $1,000 stop; $100,000 → riding a $9,000 drawdown; panic exit turns a −6% loss into −10% (4 pts of slippage); student tripled → capital after 3 winning months, then max-size loss; Freudberg quadrupled capital after a 6-month streak and gave back nearly the year | [MmryR1iu9dA] |
| 24 | Execution / fills | Liquidity by size | 10-lot iron condor typically fills at once; 500-lot fills piecemeal with price concessions; octopus-trade exit took 15 executions, ~1 hr planning; simplify exits to 2–3 transactions; pros wait up to 3 days for the right fill | [MmryR1iu9dA] |
| 25 | Learning curve | Timeline | 6–24 months to consistent success (desk record 6 months; up to 2 years normal); hold capital small for the first 12–24 months | [MmryR1iu9dA] |
| 26 | Diversification ladder | DTE laddering | Enter trades at 160 / 145 / 130 days to expiration for time diversification | [MmryR1iu9dA] |
| 27 | Foolish-consistency exit | Management trigger | Up 9% of a 10% target with a binary macro event next day → exit and bank the 9% | [MmryR1iu9dA] |
| 28 | Market history | Tail risk | May 2010 flash crash — sudden crash and full intraday recovery on no news: always keep exit/conditional orders working | [MmryR1iu9dA] |
| 29 | Hedge-fund landscape | Market structure | Multistrat funds $20–40B AUM common; smallest starting book for a new hire $200M; allowable drawdown tightened from ~20% to 5–10% before shutdown | [mKQq33Rtdfo] |
| 30 | Chicago short-term trading | Holding time | Average holding time 6 minutes; NYSE TICK published ~20×/minute; quant volume bars of e.g. 10,000 contracts/bar | [mKQq33Rtdfo] |
| 31 | SMB firm claims | Context | Founded 2005; 50+ traders on the desk (65+ per [tOMQNDXnczY]); develops 7- and 8-figure/yr traders; top traders ≈$20M net trading profit each in a single year (marketing claims, not verified); Freudberg: 20 yrs as P&C insurance CEO before options | [mKQq33Rtdfo][w_BjFmbwbYA][tOMQNDXnczY] |
| 32 | QQQ, Jun 2 2023 @ 354.65 (+34% YTD) | Weekly 25-pt put credit spread campaign | Sell 10× 346P @ 0.65 (+$650), buy 10× 321P @ 0.06 (−$60) → +$590/wk; margin ≈$24,410 (transcript prints "$4,410" — garble; 10-lot 25-wide risks $25,000−credit); short put priced ~$0.60 each week; Jun 9 close 354.50; wk2: 342P @ 0.61 / 317P @ 0.08 → +$530, close 367.93 | [4d6qj5vtrBQ] |
| 33 | QQQ, Jul 28 2023 loss week + recovery | Credit-spread wheel substitute | Jul 28: 373P @ 0.59 / 348P @ 0.05 → +$540; close < 373 → buy back @ 1.02 / sell @ 0.01 → −$470 net. Recovery: buy 10× Dec 29 370C @ 24.71 ($24,710), sell weekly 373C: @3.66 (+$3,660, close 366.24), @1.16 (+$1,160, close 358.13), @0.30 (+$300), @0.90 (+$900); Sep 1 close 377.5 → buy back @ 4.63 (−$3,730 leg), sell Dec calls @ 24.25 (−$460). Campaign: +$5,030 (transcript "5,30" garbled) on $24,400 max = 20.5%/3 mo ≈ 82% annualized | [4d6qj5vtrBQ] |
| 34 | XOM, Jun 17 2022 @ ~86.09, 1,000 sh | Conventional covered call campaign | Cost $86,090; monthly calls: Jul 97.5C @ 0.75 (+$750, close 84.54), Aug 95C @ 0.76 (+$760, close 94.03), Sep 100C @ 1.25 (+$1,250, close 93.26), Oct 105C @ 0.72 → Oct 21 close 105.86, called @ 105; rebuy @ 105.86 ($105,860 peak capital); Nov 115C worthless, Dec 120C @ 1.13; Dec 16 close 104.70. Profit $23,390 = 22.1%/6 mo | [7a0BRIAufBA] |
| 35 | XOM, same dates | Synthetic covered call (LEAP) | Buy 20× Jun 2023 75C @ 17.66 ($35,320), sell 20× monthly calls (doubled lots); initial risk $33,820; Oct buyback @ 0.98 (−$1,960); close: sell LEAPs @ 31.60 → profit $37,300 = 105.6%/6 mo (>4× conventional) | [7a0BRIAufBA] |
| 36 | SPX, Nov 15 entry, Nov 29 expiry, index 3109 | Weekly broken-wing butterfly (~14 DTE) | Sell 20× 10-delta 3040P @ 7.20 (+$14,400), buy 10× 3045P @ 7.70 (−$7,700), buy 10× 3020P @ 5.40 (−$5,400) → +$1,300 credit (rule: lowest long chosen to keep ≥$1,000). Exit +$1,000 / stop −$2,000. Nov 25 (SPX 3122): legs 0.65/0.70/0.45 → keep $1,150. 12-mo test: 41/52 wins, 11 losses, +$22,815 on ~$28,000 = 81%/yr; $65k sizing ≈ $1,000/wk average | [Qj8_3eybnaE] |
| 37 | SPX, Aug 30 open 4568 (after +64-pt day) | 0-DTE put credit spread | Sell just-below-market put @ 9.55, buy 15 pts lower @ 4.35 (strike digits garbled in transcript, short ≈4555) → +$520, max loss $980; close 4548.7 (9.87 pts above short) → +53% in a day | [UG4f752OXq8] |
| 38 | SPX, Aug 11, 10am @ 4461 | 0-DTE iron condor | Sell 4475C @ 5.50 + 4445P @ 5.70; buy 4485C @ 2.90 + 4435P @ 2.60 → +$470; margin $530; close 4464.5 → full win; 30-pt profit zone 4445–4475 | [UG4f752OXq8] |
| 39 | SPX, Oct 16 2023, 10:30am @ 4375.09 | 0-DTE call calendar | Sell same-day 4375C @ 10.70, buy next-day 4375C @ 18.50 → cost/max loss $780; close 4373.63 → short worthless, long 13.35 → +$555 = 71%/day | [UG4f752OXq8] |
| 40 | SPX ~3010, Wed+Fri chains | Twice-weekly 50-lot far-OTM PCS ($2,500/wk trader) | Sell 50× 2990P @ 1.38 (+$6,900), buy 50× 2985P @ 1.10 (−$5,500) → +$1,400 (28¢/spread; rule ≥25¢, ≥$1,250/trade); short puts ~20 pts below market. Tail: 30-pt gap close → −$23,600 (≈10 weeks of gains). Math: 4 losses/yr → >100% ann.; 5 → ~50%; ≥6 → negative. Trader had 9 loss-free months | [Dl0O3z_5hB0] |
| 41 | SPY, May 1–17 2024 (S&P +5.3%), $2,000 acct | 20-delta 0-DTE call buying (failure demo) | Daily 5× ~20Δ calls: May 1 open 501.70, 506C @ 0.59 ($295), close 500.83 → loss; May 2 −$215; May 3 513C $285, SPY +$6.28 → loss; May 6 515C $165 → +$620; May 8 517C $190 (0.38), close 517.19 → calls worth $95 → loss while ITM. Total 3W/10L, −$265 = −13% | [nvJ_43579z8] |
| 42 | SPY, same days | 40-delta 0-DTE put credit spreads (contrast) | Daily 5× spreads at first strike below 40Δ (1–2 pts below open), long 2 pts lower: May 1 sell 500P @ 1.29 / buy 498P @ 0.69 → +$300, margin $700; May 2 502/500 → +$260/$740. 12/12 wins incl. May 13 & 16 (closed below short put; bought back before close, still positive) → +$2,685, >100% return | [nvJ_43579z8] |
| 43 | AMZN teaching example @ 105 | Covered call outcomes | Buy 100 @ 105 ($10,500), sell 1-mo 110C @ 3.50 (+$350 = 3.33%/mo); close 111 → +$850; close 90 → net −$1,150 (premium kept, shares −$1,500) | [CP_euDwExN0] |
| 44 | CMG, Jul 1 2021 @ 1538 | Covered-call mistake: capping a super-bullish stock | Sell Jul 30 1550C @ 47.06 (+$4,706); Jul 30 close 1863.44 → total +$5,966 vs +$32,604 holding shares; $26,638 left on table | [CP_euDwExN0] |
| 45 | TSLA, Dec 1 2022 @ 194.70 | Covered-call mistake: strike below basis | Sell Dec 30 200C @ 10.12 → net cost $18,458; Dec 30 close 123.18 (+$1,012 kept); sell Jan 130C @ 9.02; Jan close 177.90 → called @ 130 → campaign −$4,556 | [CP_euDwExN0] |
| 46 | CMG held since Apr 2008 @ 100 | Covered-call mistake: huge embedded gain | 100 sh cost $10,000, now 1728 ($172,800; +$162,800 unrealized); sell 1-mo 1800C @ 36 (+$3,600); assignment → realized $170,000 gain → ≈$30,000 LT cap-gains tax at top US bracket | [CP_euDwExN0] |
| 47 | S&P 500 avg dividend yield | Context | 1.74% [CP_euDwExN0]; 1.71% [LWLFq1cMOdo] | [CP_euDwExN0][LWLFq1cMOdo] |
| 48 | SPX, Jun 6, open ATH 5357.80, entry @ 5350 | 0-DTE ATM iron butterfly, 90-min hold | Sell 6× 5350C @ 10.65 (+$6,390) + 6× 5350P @ 9.15 (+$5,490); buy 6× 5430C @ 0.08 (−$48) + 6× 5270P @ 0.33 (−$198) → credit ≈$11,634 (transcript "$1,644" garbled; margin $36,366 = $48,000 − credit confirms); exit 90 min later: buy back @ 9.00 / 6.45 → +$2,466. 2023 backtest: 9 mo up, Feb/Apr/Jun down, avg >$1,200/wk; 1-lot ≈ 16% of 6-lot | [-h1mAx67OxA] |
| 49 | IWM, Nov 11 close 241.68 (year high) | Overnight call calendar, ~$200 capital | Sell next-day 242C @ 0.91, buy week-later 242C @ 3.07 → cost $216; target +5% (~$11). D1: 15 min in, stock 241.75, short −34¢ vs long −17¢ → +$17 = 7.8%. D2 (237 strike, $157): stock +1.73 → long +62¢ vs short +43¢ → +$19 = 12.1%. D3 (235 strike, $168): short −30¢ vs long −19¢ → +$11 = 6.5%. 3 days = +26.4% on capital | [i5JOd15b_w0] |
| 50 | XOM, Jun 1 2023 @ 101.56, support 97–99 | Cash-secured put | Sell 5× Jun 30 99P @ 2.18 → +$1,090; broker holds $49,500; close 107.25 → 2.2%/mo, ≈26.4%/yr ≈ $13,080 | [TOc1XyCu83I] |
| 51 | TSLA, Feb 1 @ 181.41, 200 sh ($36,282) | Covered call (non-dividend growth stock) | Sell 2× 200C @ 7.62 → +$1,524; Mar 3 close 197.79 → worthless; annualized >50%, >$18,000/yr on the position | [TOc1XyCu83I] |
| 52 | SPX, Jan 3 close 3824.14 | 1-month PCS ~50 pts OTM | Sell 2× Feb 2 3775P @ 72.65 (+$14,530), buy 2× 3750P @ 63.70 (−$12,740) → +$1,790; margin/worst case $3,210; Feb 2 close 4179.76 → win | [TOc1XyCu83I] |
| 53 | 8-stock sector portfolio, $163,400 | Portfolio covered-call program | Dividends $2,200/yr = 1.4%. Sell monthly calls 5% OTM 30 days out (MSI Sep 19 @ 168 → Oct 175C @ 1.66 = $166); ≈$2,000/mo across 8 → >$24,000/yr = 15.1% + dividends → >$26,000 (>10× dividends) | [XQ9OSsOra5s] |
| 54 | VOLD ratio thresholds | Market internal | ≥3:1 trend possible; <2:1 chop; extremes 6:1–10:1 ≈ once/month in dull markets, daily in COVID crash; trend days only 10–20% of all days | [CeEksKNSGMQ] |
| 55 | NDX, Mon Apr 6 2020, 11am @ 7873.52 (VOLD 6:1) | 0-DTE 30Δ long call on internals | Buy 7930C @ 19.50 ($1,950); close 8081.66 → $15,166 → +$13,216 = 677% in a day | [CeEksKNSGMQ] |
| 56 | NDX, Sep 13 2022, 11am @ 12,158.85 (A/D < −2500) | 0-DTE 30Δ long put | Buy 12150P @ 25.65 ($2,565); close 12,033.62 → $11,638 → +$9,073 (>3.5×) | [CeEksKNSGMQ] |
| 57 | NDX, Feb 21 2023, 11am (TICK sub-zero all day) | 0-DTE put debit spread | Buy 12110P @ 24.40, sell 12060P @ 10.70 → $1,370; close 12,060.30 → long 49.7 ITM ($4,970), short 30¢ OTM worthless → +$3,600 = 262%/day. A/D pin levels ±2000; TICK extremes ±1000–1500 | [CeEksKNSGMQ] |
| 58 | SPX, Dec 15 2022, channel 3500–4300 (8 mo) | 64-DTE channel iron condor | Sell 10× 4350C @ 15.20 + 10× 3500P @ 23.20; buy 10× 4375C @ 12.70 + 10× 3475P @ 20.95 → +$4,750; margin $20,250; ~85% prob. inside 850-pt range; Feb 17 close 4079 → +23.4% | [tOMQNDXnczY] |
| 59 | SPX index-option mechanics recap | Teaching numbers | 4130C @ 68.45 = $6,845; 4130P @ 57.95 = $5,795; index close 4032: 4000C worth $3,200, 4075P worth $4,300, 4075C & 4000P worthless; ~250 trading days/yr = daily-expiry "bites" | [tOMQNDXnczY][c49FJM6UDvo] |
| 60 | SPX, Jun 8 open 4270 | 1-month tight PCS | Sell 4270P @ 48.25, buy 4260P @ 44.75 → +$350; Jul 7 close 4412.6 → win; partial-win math: close 4268 → payout $200 < credit → +$150 | [6VPPI-MNUDM] |
| 61 | SPX, Feb 1 | 1-month call credit spread | Sell 4120C @ 74.85, buy 4130C @ 69.15 → +$570; Mar 1 close 3951.3 → win; full profit at any close ≤4120 | [6VPPI-MNUDM] |
| 62 | RUT, Mar 10 @ 1772.7, support 1720 | Support-located PCS | Sell Apr 6 1720P @ 31.90, buy 1700P @ 26.50 → +$540; close 1754.4 → win | [6VPPI-MNUDM] |
| 63 | SPX, Apr 28, 10am, ATM 4140 | 0-DTE iron butterfly + butterfly roll | Sell 5× 4140C @ 6.90 + 5× 4140P @ 10.90 (+$8,900); buy 5× 4170C @ 0.53 + 5× 4110P @ 2.12 (−$1,325) → +$7,575; margin $7,425; adjust when index ≈ strike ± $15.15 (credit/lot). At ~4155: buy back 4140C, sell 10× 4170C, buy 5× 4200C → iron condor; credit left $3,315; close 4169.48 → +$3,315 = 44%/day | [c49FJM6UDvo] |
| 64 | SPY, Jan 20 2023 @ 395 | Conventional vs synthetic covered call | Conventional: 100 sh $39,500 + May 425C @ 5.35; May 20 close 418.62 (+$2,897); Sep 450C @ 0.31; Sep close 443.37 → +$5,673 = 14.67% (~22% ann.). Synthetic: Jan 2024 310C LEAP @ 101.36 ($10,136, 85 pts ITM); LEAP 118.49 (May) → 138.26 (Sep 15); net cost $9,300 → +$4,526 = 32.7% on <25% of the capital | [Wpl3VI2FTio] |
| 65 | ~1870/1740 stock (unnamed), earnings | Straddle inflation + earnings iron butterfly | Normal-week ATM straddle 23.42; pre-earnings @ 1740: 49.47C + 48.09P = 97.56 (~4×). Iron fly ±60 wings: credit $5,278, capital $722; next AM stock 1792: legs 9.21 / 52.50 / 0.58 / 0.53 → +$974 = ~130% overnight (~300% 1 hr later). Screen: options that overestimated post-earnings moves by ~80% over 2–3 yrs | [WYya6HGDYYg] |
| 66 | NVDA, Jun 28 2024 @ 123.62 (+1,000%/21 mo), 400 sh | Covered-call basis rule | Buy $49,448, sell 4× Jul 12 124C @ 4.70 (+$1,880); close 129.24 → called: +$2,032/2 wks. Greedy path: reload @ 129.24, 130C @ 4.65; close 113.06 (+$1,860); 114C @ 4.52 (+$1,808), close 104.75; 105C @ 4.75 (+$1,900); Aug 23 close 129.37 → called @ 105 → shares −$9,696 (transcript "969") → campaign negative. Basis-rule path: 130C @ 0.47 (+$188), 130C @ 0.14 (+$42) → campaign +$4,175. 2-wk ATM NVDA premium stable ≈$4.50–4.75 | [RmtEzjn4Vh0] |
| 67 | AAPL, entered Oct 21 (earnings Oct 30 PM) | Pre-earnings long straddle | ATM straddle on chain expiring 1 day post-earnings: 5.68C + 6.00P = $1,168; target +15% (GTC order), worst ≈−10% (IV floor), MUST exit pre-announcement; Oct 28 (+10 pts): 11.30C + 2.22P = $1,352 → target. 4 hrs pre-earnings, stock ≈ entry: still +$16. Control (no earnings, May, entry $457): >50% lost in days at unchanged price. Up to 10 concurrent positions | [IkGV8x5uz_A] |
| 68 | GOOGL ~1200 → 1274.50 | Pre-earnings IV inflation | 25-pt-OTM 5-day call: 3.86 at 34 days out vs 10.90 one hour pre-earnings (~3×); breakeven move 29 → 36 pts | [IkGV8x5uz_A] |
| 69 | 0-DTE momentum setup parameters | Indicator settings | 5-min charts; BB 20-period/2 SD inside Keltner 20-period/1.5 ATR (TTM squeeze, ≥~5 bars); TICK bodies ~80%+ above/below zero; ATR trailing stop 3-period, 1×ATR; rVol thresholds: index 1.2 OK/1.5 great, single names 1.5 OK/2+ great; strike = chart price target | [Z4a5wkLfqlU] |
| 70 | SPX, Dec 30 2022 close 3839.50, $10k acct | Weekly ATM 5-wide PCS + 10-day SMA filter | Wk1: sell 10× 3835P @ 38.10 / buy 3830P @ 35.90 → +$2,200, margin $2,800; close 3895.08 → win. Wk2: 3895/3890 @ 50.80/48.45 → +$2,350; close 3999.09. Wk3: 3995/3990 @ 27.85/25.75 → +$2,100; close 3972.61 → short 22.39 ITM → −$2,900. Raw campaign Jan–Aug 2023: +$8,770 = 87.7%/8 mo | [xQfp8_5VsRU] |
| 71 | SPX, Dec 1 2022 close 4076.57 | Monthly 10-delta 5-wide PCS campaign | Dec 30 3775P Δ10.02 @ 12.70 / 3770P @ 12.30 → +$400; close 3839.50 (−237 pts, still full win). Jan: 3535/3530 → +$450, margin $4,550. 12/12 wins Dec 22–Nov 23: +$4,050 on max $4,750 = 85%/yr (10Δ ≈ 90% long-run win rate) | [xidgg27-yWU] |
| 72 | SPX, Aug 31 2022 @ 3955 → Sep 23 @ 3687.29 | The roll-down rescue | Original 10-lot 3555/3550 PCS +$400; short put Δ 10→20 (−268 pts) → roll to new 10Δ 80 pts lower (3475/3470) at 15 lots (+50% size), $200 credit remains; Sep 30 close 3585.62 → +$200 saved | [xidgg27-yWU] |
| 73 | SPX, Sep 15 2023 @ 4450.32 → year of 3rd-Friday trades | 5-delta 60-DTE iron condor campaign | Nov: sell 10× 4800C @ 4.30 / buy 4825C @ 3.30; sell 3875P @ 9.40 / buy 3850P @ 8.80 → +$1,600, margin $23,400, 925-pt zone, close 4514.02. Jan: +$1,500/$23,500, close 4839.81. Mar: +$1,550 (4275–5200). May: +$1,550 (4575–5575). Jul: +$1,450 (4725–5700). Sep 24: +$1,700 credit, 1175-pt range, closed early for $130 → +$1,570. Year ≈ +$9,220 (transcript "$922" garbled; legs sum confirms) on $23,550 max = 39%/yr; 5Δ IC ≈ 90% PoP | [m8R_564Kp6k] |
| 74 | RUT, Mar 9 2023 @ 1826, channel 1650–2000 | 6-month iron condor | Sep 15 chain: sell 5× 2000C @ 55.95 (+$27,975) / buy 2050C @ 39.90 (−$19,950); sell 5× 1650P (+$22,525 per garbled "2,525") / buy 1600P @ 41.20 (−$20,600); stated credit $12,950, margin ≈$12,050 (transcript "$1250"; leg arithmetic gives $9,950 — flagged); close 1847.03 → full win, stated 107%/6 mo; 350-pt profit zone | [bDhYEMCLm9k] |
| 75 | SPX, Jul 16, gap open ~6255 | 0-DTE 30Δ iron condor + calendar filter | Sell 3× 6270C @ 5.00 (+$1,500) + 3× 6240P @ 5.50 (+$1,650); buy 3× 6340C @ 0.07 (−$21) + 3× 6170P @ 0.37 (−$111) → +$3,018; margin $17,982. Exit +25% of credit (≈$755) or 11:30am hard stop. 10:30 example: short call 1.62, short put 6.25 → +$774. Loss case (index 6234.35): short put 14.40 → ≈−$1,026 (transcript "1,26"). ChatGPT report-day filter: skip ~25% of days → win rate 62%→86%, profit >2× | [Ko9E9OFYsf8] |
| 76 | SPY, Nov 2022–Nov 2023, 3-lot | Wheel campaign | Nov: 375P @ 6.70 (+$2,010; transcript "210"/"2,110" garbled), close 406.91. Dec: 400P @ 6.44 (+$1,932) → assigned @ 400 (close 388.08). Feb: 400C @ 4.79 (+$1,437) → called @ 400 (close 408.04). Mar: 400P @ 5.14 (+$1,542) → assigned (close 385.91). Apr: 400C @ 2.79 (+$837) → called (close 409.19). May–Aug puts expire. Oct: assigned @ 435 (close 431.52). Nov: 435C @ 7.79 (+$2,337) → called (close 450.79). Year: +$15,771 ≈ $1,300+/mo | [Kg0ts5NGr0o] |
| 77 | PCLN, mid-2017 @ 1810 | Far-OTM call-buying blunder | Jul 21 1950C (10Δ) @ 4.35 = $435; expiry 1998 → ~$48 = >10×. Prior 12 months: 11/12 expired worthless; campaign net ≈ −$2,400 incl. the 10-bagger; breakeven 1954.35 (+144 pts needed) | [FhUcZZB3tmU] |
| 78 | SPY, Jun 10, 3:30pm @ 602.43 (close 603.08; Feb ATH 613) | Overnight call calendar 10-lot | Sell 10× next-day 602C @ 2.59 (+$2,590), buy 10× week-later 602C @ 5.43 (−$5,430) → cost $2,840 = max risk; next-day close 601.38 → long @ 4.56 → +$1,720 = 60% overnight (atypical; standard: ~10% target / ~10% stop); daily expirations ≈3 yrs old | [oxNvLwZ0dGo] |
| 79 | QQQ, Feb 21 2023, 11am @ 296.28 | Conviction-tiered 0-DTE pair | High conviction: put debit spread — buy 40× 295P @ 0.59 (−$2,360), sell 40× 294P @ 0.32 (+$1,280) → risk $1,080; close 294.03 → +$2,800 (transcript "29%"; = 259% on risk — flagged). Low conviction: call credit spread — sell 297C @ 0.80 (+$1,200), buy 298C (−$720) → +$480, worst case $1,020 (consistent with 15-lot); close 294.03 → +$480 | [qPkolXAi4BM] |
| 80 | ETF filter composition | Risk-on/off watchlist | Risk-on: XLK, XLY, SMH, ARKK; defensive: XLU, XLP, XLV, UVXY; macro: DXY, TLT, HYG, GBTC/crypto; columns: rVol, %chg from open, abs chg from open | [qPkolXAi4BM] |
| 81 | AAPL, 3:15pm pre-earnings @ 243 | Earnings iron butterfly, wing-width lesson | 10-lot: sell 242.5C @6.20–6.22 + 242.5P @5.60–5.68; buy 12.5-pt wings @1.52/1.48 (transcript garbles wing strikes "255/240") → credit $8,900; margin $3,650 (also spoken "3,620") vs $9,200 for 20-pt wings. Next AM AAPL 245: close for $5,300 → +$3,600 = 99% overnight; 20-pt version +$5,350 = 58%; doubled tight version: $7,240 capital → ~$7,200 | [7q7AJXYOq7s] |
| 82 | XSP (1/10 SPX; SPX ~7,000 era), 20-day-SMA cross signal | 2-week ATM 1-wide put credit spreads under $100 | Apr 24 2025 close 548.48: sell May 8 548P @9.56 / buy 547P @9.18 → +$38, capital $62. Aug 4 close 632.99: 632/631 @5.57/5.24 → +$33/$67; close 644.91 → win. Next wk close 646.69: 646/645 @4.68 sale → +$37/$63; Sep 2 exit below SMA @641.55: buy back 6.02 / sell 5.42 → −$23. Typical credit $30–40, capital $60–70. Campaign: 3 losses (each < any win), net +$187 = 62% on $300 base; SPY buy-hold benchmark ≈10%/yr | [Jniwt90PUS4] |
| 83 | Unnamed index @ 1724, 10 DTE | Broken-wing butterfly 1×2×1 (credit) | Buy 10× 1700P @5.55 (−$5,550), sell 20× 1690P @3.80 (+$7,600), buy 10× 1670P @1.90 (−$1,900) → +$150; capital $9,850 ($985/1-lot). Close 1691.80 → 1700P = 8.20 → +$8,350 (≈85%/10 days); 4/5 scenarios pay $150 ≈ 1.5%/10 days. Claim: 75% of all options expire worthless | [vU64DYL3raU] |
| 84 | RUT, Jan 27 2023 @ 1911.50, trendline break | Zero-cost put (leg-in) | Buy Jun 30 1910P @89.25 (−$8,925); Mar 13: sell Jun 1770P @101.20 (+$10,120) → +$1,195 locked. Outcomes: >1910 → +$1,195 (worst); 1834 → +$8,795 (≈98% on original risk); ≤1770 → max +$15,195 | [kG0YKGa6kc0] |
| 85 | TSLA, Dec 19 2022 open ~158 (2022: −70%, low 123.18; RSI <30) | 60-DTE 10Δ put credit spread campaign (single stock) | Feb: 10× 105P (Δ10.36) @2.93 / 100P @2.34 → +$590, cap $4,410, close 208.31. Apr: 145/140 → +$600/$4,400, close 165.08. Jun: 125P @1.72 / 120P @1.25 → +$470/$4,530, close 260.54. Aug: 195/190 → +$600, close 215.49. Oct: 165/160 → +$590, close 211.93. Dec: 165/160 → win. Year 6/6: +$3,370 on max $4,530 = 74% | [-Dfl8YyoP0E] |
| 86 | TSLA same campaign, Mar 13 @ 171.57 | Delta-doubling roll rule | Short 145P delta 10 → 20 → roll to original delta: buy back 145P @5.23, sell 140P (+$4,180), sell 130P (+$2,620), buy 125P (−$2,060) → net credit remaining $110; Apr 21 close 165.08 → +$110 (roll target spoken both "135/125" and 130/125 — garble) | [-Dfl8YyoP0E] |
| 87 | SPX, Aug 10, open 4503, week range 4460–4550 | 0-DTE iron condor + threatened-side roll | Sell 10× 4540C @1.25 + 4460P @1.80; buy 4565C @0.22 + 4435P @0.65 → +$2,180, margin $22,820. 1pm @ 4475 → roll puts −10: buy 4460P @4.60, sell 4435P @1.18, sell 4450P @2.65, buy 4425P @0.73 → −$1,500 → +$680 left; close 4468.83 → +$680 kept | [t6yuG7KKSKg] |
| 88 | SPX, June week, $1,000 account | Daily 0-DTE ATM iron butterfly ±20 wings, TP 10% / SL 20% of capital | Mon open 5295.73: sell 5295C @9.65 + 5295P @9.20, buy 5315C @2.15 + 5275P @3.20 → +$1,350, capital $650; 10:10am @5290 close → +$73. Tue open 5265.12: credit $1,495, cap $505 (transcript "4.95"/"55"); 10:55 @5267 → +$80. Fri open 5331 @5330 fly: credit $515; +17-pt rally by 10am, 5330C → 23.55 → −$110 stop. Week 4W/1L ≈ +$200 (transcript "$21"/"20%" inconsistent) | [aC-JCii8Vg8] |
| 89 | NVDA, Apr 19, 11:15am @ 819 (A+ breakdown, SMH/SMCI confirm, 2–3× vol) | MACD(3,9,5)-triggered 0-DTE 30Δ put buy | Buy 4× 810P (30Δ) @2.63 = $1,052; close 762 → 47.20 = $18,880 → +$17,828 in 5 hrs | [B9myhwUaSsQ] |
| 90 | NVDA, next Friday, 1:25pm @ 868.13 (B-grade rel-strength day) | MACD-triggered ATM put credit spread | Sell 5× 867.5P @3.30 (+$1,650), buy 5× 857.5P (10 pts lower), margin $3,350; close 877.35 → +$1,650; identical payout at any close >867.50 (entry only 0.63 above strike) | [B9myhwUaSsQ] |
| 91 | SPX, Apr 1 2019 @ 2864 / May 1 @ 2923 | Monthly 5%-OTM 12-lot short strangle (income-unevenness demo) | Apr: sell 12× 3000C @0.97 (+$1,164) + 12× 2725P @7.63 (+$9,156) = +$10,320; expiry SPX 2939, both @0.03 → close $360+$360 → +$9,600. May: 3075C/2775P → +$14,148; expiry 2757, puts @18.03 → close >$21,000 → −$7,838. Model year: 4 losing months of 12, avg $5,000/mo | [Is9CVUBT9y0] |
| 92 | Income benchmarks | Cash-flow planning | Accomplished options income trader ≈ 2–4%/month on capital; hold reserves = a few months of backtested drawdown; bank excess winnings as reserve, never spend the average | [Is9CVUBT9y0] |
| 93 | TSLA monthly expiration, 450 strike OI >24,000 (≈2× the 440/460) | Expiration-day pinning iron condor | 10-lot same-day: sell 465C @4.52 (+$4,520) + 430P @2.23 (+$2,230), buy 470C + 425P → +$2,060 credit, margin ≈$2,940 (transcript "29.60"); close 442 (rallied to ~450 in final half hour, faded last 15 min) → +$2,060 ≈ 70%/day | [rHFJdAw4PtQ] |
| 94 | SPX, early Jan @ 3860 (post-Oct-2022 3500 bounce) | 1-month 12.6Δ put credit spread | Sell 5× Feb 2 3575P @18.10 (+$9,050), buy 3550P @15.35 (−$7,675) → +$1,375, capital $11,125; PoP 87.4%; close 4179.78 → +12.35%/month | [UrnFowunv-E] |
| 95 | SPX, Feb 2 → Mar 17 | Iron condor PoP formula demo | Sell 5× 3825P (Δ12.56) @21.70 / buy 3800P @19.70; sell 4450C (Δ11.20) @11.05 / buy 4475C @8.70 → +$2,175, capital $10,325; PoP = 100−12.56−11.20 = 76.24%; SPX −250 pts, closes mid-range → +$2,175 = 21%/45 days; 625-pt zone | [UrnFowunv-E] |
| 96 | ADBE, Jan 19 @ 342.53, support 320 | Cash-secured put at support | Sell Mar 17 320P (Δ28.65) @10.20 → +$1,020; PoP 71.35%; close 358.14 → win; ADBE later 550 (assignment would have been fine); day-trader baseline win rate 50–60% | [UrnFowunv-E] |
| 97 | SPX, Aug 17 2015 @ ~2100 | Martingale roll-down horror sequence | Sell 10× 2040P 12 DTE @3.45 (+$3,450), capital $255,000. Aug 20 (Δ41): buy back @16.25 → 35× 1975P @3.95, cap $819,000. Aug 21 (SPX 2015, Δ27): → 75× 1925P (buyback @12.15), cap $1,616,000; EOD → 218× 1800P, P&L −$154,000, cap >$4M. +3 days: −$314,000 → 365 puts, cap $6.5M; market bounced → "very slightly profitable". Roll trigger Δ≈20 → new 10Δ; adjust ~10:30am | [SmMsPFLFqc0] |
| 98 | SPX RSI≈30 signals, $5,000 account | 60-DTE ATM 5-wide PCS ×15, exit ≥90% premium | Sep 26 2023 (4273.53): Nov 30 4310/4305 @97.45/95.70 → +$2,625, cap $4,875; close 4567.8. Apr 19 2024 (4967.23): Jun 21 4965/4960 → +$2,775, cap $4,725; close 5464.62. Aug 5 2024 (5186.33): Sep 30 5185/5180 → +$2,550, cap $4,950; Sep 19 quotes 1.98/1.95 → early close ≈ full credit (transcript's $2,555 off by ~$50). Year: account "more than doubled" (final-total figures garbled) | [t2hTAtI2OxY] |
| 99 | GOOG, Mar 13 → 16 2020 (COVID seesaw) | Legged risk-free put spread | Fri (rally): buy Mar 20 1125P @38.92 (−$3,892). Mon (tank): sell 1090P @40.62 (+$4,062) → +$170 locked. Mar 20 close 1072.30: 1125P = 52.70, 1090P = −17.70 → +$3,670 total | [-gGvWxd_iXc][W1HJb-ST-6Q] |
| 100 | WMT, Mar 2 @ 130.11, 1,000 sh | Income-goal covered-call campaign ($2,000/mo) | Sell 10× Apr 1 133C @2.01; called @133 (WMT 135+); rebuy @135.62, 137C @2.25; called @137 (>139), +$8,530 to date; rebuy @139.91; May +$260, Jun +$1,850; Jul 23 139C @1.84 → called @139 (142.43); rebuy, 144C @2.32; Aug 20 @151.54 → called @144. Total ≈ +$17,026 (transcript "17,26") | [Vm0qcsR5-E4][AtSAFHA2Hvc] |
| 101 | WMT, same start | Price-target covered-call campaign (150 strike only) | Sell only 150C monthly: first month $240; range $100–$800/mo; shares never called until WMT >150 in Aug → sold @150 → total >$22,000 (beats income-goal campaign) | [Vm0qcsR5-E4][AtSAFHA2Hvc] |
| 102 | SPX, Fridays, Oct run (Sep close 5738.7) | Weekly 10Δ 2-strike-wide PCS ×5 | Wk1: 5565P @6.00 / 5555P @5.30 → +$350, cap $4,650; close 5751.07. Wk2: 5570/5560 → +$350; close 5815.03. Wk3: 5670/5660 → +$275, cap $4,725. Wk4: 5745/5735 → +$300; close 5882 despite mild selloff. Wk5: 5620/5610 → +$350; close 5728.8. October 5/5: +$1,625 = 34.3% on peak $4,725; bull filter advised (50-day MA / RSI≈30) | [hbkcV1ejzJw] |
| 103 | QQQ, Nov 21 2025 open 588.10 (lower Bollinger touch) | Velocity of capital: PCS closed at 76% of max in 4 days + redeploy | Sell 10× Dec 4 588P @12.67 / buy 583P @10.76 → +$1,910, margin $3,090 (transcript "10,670"/"3,90" garbled). Nov 25 close 608.89: 1.64/1.20 → +$1,470 (76% of max). Re-sell 608/603 @6.09/4.41 → +$1,680; Dec 4 close 622.94 → win. Campaign $3,150 vs $1,910 passive | [TpAPTwLMb44] |
| 104 | TLT, Feb 2024 @ 92.76, 1,000 sh, quarterly 92C | Conventional covered-call year | Entry: shares $92,760, 10× 92C 91-DTE @3.42 → net $89,340. May 17 close 91.39 → +$3,420. Aug: 92C @2.18 → close 97.44, called @92 → +$1,420; rebuy $97,400. Nov: 92C @6.60 → +$6,600 (close 90.80). Feb 2025: 92C @2.14 → +$2,140 (close 89.61); share loss −$7,830 → net $5,750 + monthly dividends → ≈$9,176 (transcript "$99,100 76" garbled) | [k-VJZ95j7ec] |
| 105 | TLT, same dates | Synthetic covered call, 30-lot deep-ITM | Buy 30× Feb 2025 81C @14.13 ($42,390), sell 30× 92C @3.42 (+$10,260) → outlay $32,130 (64% less). May +$10,260; Aug: 92C @2.18 (+$6,540) but buy back @5.40 (−$16,200) → −$9,660; Nov 92C @6.60 → +$19,800; Feb 92C @2.14 → +$6,420; long 81C expires at a loss → final +$10,920 (> conventional on ⅓ capital) | [k-VJZ95j7ec] |
| 106 | GE, Apr 23, 29 DTE, 5-wide PCS at support | Delta trade-off comparison | 20Δ: credit $1,020, margin $3,980 (≈80% PoP). 45Δ: credit $2,455, margin $2,545 (≈50/50). Both positive theta / negative vega / negative gamma / positive delta; both profitable through the mid-trade pullback to entry price | [YKjnoiKNTLs] |
| 107 | AMZN, ~Aug 5 2024 close 167.90 (−16%/3 wks) | Deep-ITM synthetic stock | Buy 3× Feb 21 2025 120C (Δ91.02) @53.80 = $16,140 (transcript "15,900") vs $16,790 for 100 sh. Expiry AMZN 216.58 (peak 242): calls @96.72 → $29,016 → ≈+$12,876 vs +$4,868 (29%) on shares. Trigger context: QQQ ATH 548.10 Feb 19 → 473.63 Mar 18 (−12%/month) | [pUD2sXdXHbI] |
| 108 | RUT, RSI>70 signals | 30-DTE 10Δ call credit spreads ~8% OTM | Jan 6 @2051: sell Feb 5 2210C @12.35 / buy 2260C @6.30 → +$605, cap $4,395; RUT rallies to 2159 (signal wrong) → Feb 3 close @0.68/0.20 → +$557 (>90% of max). Feb 5 @2233: 2380C @11.85 / 2430C @6.10 → +$575, cap $4,425; Feb 26 @2201 → 0.83/0.35 → +$527. Year: 5 signals → ≈46% on avg deployed capital | [v_27P1SNZTU] |
| 109 | ADBE @ 572 | Cheap far-OTM call math | Jul 16 635C @0.96 = $96, Δ6.09 → ~94% worthless. If ADBE 646: +$1,004 = >1,000%. But 16 reps: 15 losses = $1,440 → the 1 win needs ~1,500% just to break even | [_7Ay68OHOTM] |
| 110 | SPY, Jan 2 2019 @ 250.20 | Dividend-replication synthetic covered call | Jan 2020 130C deep-ITM @120.99 ($12,099) vs shares $25,020; sell ~$0.20 calls monthly 10–15 pts OTM (Jan 270C, Feb 283C…) → $252/yr ≈ 2% ≈ SPY dividend (~$500/yr on shares, avg <2%). Dec 2019: SPY 321.13; call @191.40. Shares: +$7,593 = 30%; synthetic: ≈+$7,550 = 62% on half the capital | [f9pJ-V2vqww] |
| 111 | Two real desk strategies, 2013–2018 | Return-chasing fallacy | 2013: A ≈ 0%, B +178%; 2016: A big loss, B +24%; 2017 A > B. Six years: A +409%, B +578%; annual switcher into last year's winner < both | [dLZYl7kC468] |
| 112 | VIX, Jan 18 2018 @ ~12 (support; 2013–14 floor ~11) | Short VIX puts at complacency support | Sell 10× 12P @1.25 (+$1,250), capital ≈$2,400; Feb 5 week spike into 30s → VIX 23 midweek: puts (Mar 21 chain, 42 DTE) @0.22 → buy back $220 → +$1,030. Rule of thumb: close at half the credit. Spike history: 2011, 2015, early/late 2018 spikes to 30–50 | [cTX7BettDqk] |
| 113 | IBM, 10-yr backtest | Long earnings straddle edge (B straddle) | Buy ATM straddle at pre-earnings close, sell next day: ~40 events, avg +21%/trade, ≈+1,000% cumulative (>100%/yr). Implied weekly move 5% vs avg max move 6.6% (19 yrs) / 6.8% (last 12). IV<hist filter: 6W/3L/3 skip, avg ≈18%; expectancy positive at 59% win rate. Also works: NFLX, UPS, INTC, CSCO; criteria: hist move >6–8%, >IV; 2–3 wks to expiry; flat pre-earnings chart; rVol 2.3 on entry day | [EP6MBURnM-A] |
| 114 | IBM, live trade | B-straddle management | Apr 30 133 ATM calls leg, ~$680 risk, price target 145 (nearly hit day 2); risk 10–15% of position; cut losing side at open (Seth: keep legs worth ≤5–10% / "a nickel or less" as hedge); scale out ¼ on new high etc.; AAPL 2010–2015 = the over-estimation (short-straddle) counterexample; alternative structure: reverse iron butterfly (debit spreads to targets) | [EP6MBURnM-A] |
| 115 | SPX, Sep 18 2019 @ 3000 | 1-month ATM calendar | Sell Oct 18 3000C @44.48, buy Nov 15 3000C @66.08 → debit $2,160 = max risk. +6 days @~3000: short −3.94 vs long −3.49 → +$45. Oct 18 close 2986: short worthless, long @32.97 → >+$1,100 = >50%/month | [rjHviGxmAKA] |
| 116 | Unnamed ~$1,060 stock, 51-DTE Jan chain | Iron condor + 50-pt defensive roll | Sell 4× 1125C @21.85 / buy 1150C @14.30; sell 4× 1000P @19.45 / buy 975P @14.25 → +$5,100. Rule: within 5 pts of a short → roll that side 50 pts. @1003: buy 1000P $15,780, sell 975P +$11,980, sell 950P +$8,640, buy 925P −$6,560 → cost $1,720 → +$3,380 left, zone 950–1125. Close 980 → win +$3,380 | [QsccAA3k_1o] |
| 117 | SPY, Oct 2021 → 2022 bear (SPY −14% YTD) | Laddered 3-month 10Δ put-selling program | Oct 22 2021 (453): sell Jan 385P @2.87; Nov 19 (469+): Feb 395P; Dec 17 (461): Mar 380P; monthly thereafter. All expired worthless (Jan close 439) → +$1,830 (≈+1.12%) on ≈$116,000 max capital vs −$16,240 buy-and-hold — ≈15.5% / >$18,000 swing | [VsN4Ntw7onM] |
| 118 | AMZN breakout (range ~3225–3525, base 3440→3510) | Max's 2-week OTM call trade, phase-2 risk removal | Buy 80× 3700C (Δ11) avg 7.07 = $56,560 (fills 5.25–8.00). Opening drive: sell 50 @ avg 18.30 = +$73,560 → risk-free, 30 free calls; scale out at avg 47.39 (+$142,170) on ~40–50-pt ATR steps; total ≈ +$159,000. Delta 11 → 21 → 29 intraday; calls still 22 pts OTM at close @3678 | [WO3fecu15dk] |
| 119 | BBBY, Sep 30 2020, 3:30pm @ ~15, earnings that evening | "Free" earnings call financed by PCS | Buy 10× 17.5C @0.23 (−$230); sell 10× 14.5P @0.85 (+$850), buy 10× 14P @0.60 (−$600) → +$20 credit, margin $480 = worst case. Oct 2 close 20.60 → calls 3.10 → +$3,100 ≈ 650%. Any close >14.50 → ≥ +$20 (≈4%/2 days). Comparison: $480 = 32 sh @15 → +$179.20 same move | [y6NpvN0VLX0] |
| 120 | XOM, entry ~Dec 1 @ 110.42 (post Nov 28 gap 113→111); oil 122→81 divergence | Bearish put broken-wing butterfly (debit) | Dec 30 chain: buy 75× 113P @4.97 (−$37,275), sell 150× 107P @2.36 (+$35,400), buy 75× 104P @1.54 (−$11,550) → debit $13,425 = theoretical max loss. Dec 20 (XOM ≈107): sell 113P $52,125, buy 107P $35,400, sell 104P $6,900 → +$13,050 ≈ 97%/3 wks. If XOM 111 at expiry: 113P = $2 → +$1,525 (wrong direction, still profitable). Base stat: 3 crude-down-10–20%-vs-oil-stock-52wk-high divergences in 30 yrs, each → 5–10% pullback within ~1 month | [HpXE6fr-q4g] |
| 121 | Index option payoff drills | Teaching numbers | 3100C, index 3150 → $5,000; 2900P, index 2800 → $10,000; at 2900/2901 → $0 [vU64DYL3raU]. 4000C @ close 4032 → $3,200; 4075P → $4,300 [v_27P1SNZTU]. 1410C @1415 → $500; 1385P @1375 → $1,000 [Is9CVUBT9y0][SmMsPFLFqc0]. 2000P @ close 1975 → $2,500 [kG0YKGa6kc0] | [vU64DYL3raU][v_27P1SNZTU][Is9CVUBT9y0][SmMsPFLFqc0][kG0YKGa6kc0] |
| 122 | SPX @ 2815, 10-lot, ±25-pt wings (Mar 13 expiry) | Iron butterfly (desk core setup) | Sell 10× 2815C (>$18,000) + 10× 2815P (>$17,000); buy 10× 2840C @6.95 (−$6,950) + 10× 2790P (≈−$10,000) → credit $19,400; margin $5,600 (= $25,000 − credit); R:R >3:1 (typical butterfly 3:1–10:1). Close 2810.90 → short put 4.10 ITM (−$4,100) → keep $15,300 (transcript also says "15,400"). Payoff drill: 3010C @3015 → $500; 2985P @2975 → $1,000 | [FNKIDMBPcaI] |
| 123 | COST, end-2022 (−20% yr), 100 sh = $46,145, $10,000 acct | Poor man's covered call, monthly 10Δ calls vs 1-yr deep-ITM LEAP | Buy Jan 2024 410C @96.90 ($9,690); Jan 2023 510C Δ10.72 @1.74 (+$174, close 465.11); Feb 515C Δ12.04 @1.56 (+$156, close 492.48); 6 straight wins H1. Jul: 555C @1.27 → close 557.86 → buy back (−$210), sell LEAP @159.72 (+$6,282); reinstate Jan 2024 480C @96.05 (shares now $55,000+); Aug 585C @1.32; Aug–Nov wins. Dec: 620C @1.55, close 658.82 → buy back @38.78 (−$3,723), LEAP @181.35 (+$8,530; transcript "853"). Year +$12,390 (transcript "1,390"), $10,000 → $22,390 = +123.9% vs COST +49% | [iwE_tI6foJs] |
| 124 | QQQ, 11am @354.85 (morning selloff, TICK <0, squeeze) | 0-DTE 30Δ long put on the squeeze setup | Buy 15× 353P @0.62 = $930; close 350.32 → puts ≈2.71 → +$3,135 (>3× risk) | [s1jRE-Kg4dQ] |
| 125 | QQQ, Nov 3, 11am @366.26 (bullish squeeze) | 0-DTE long call → intraday leg-in to risk-free vertical | Buy 15× 367C (38Δ) @0.60 = $900; 12:30 sell 15× 368C @0.77 (+$1,155) → +$255 banked, risk-free. Close 367.71: 367C = 0.71 → $1,065 (transcript "1155") → total ≈+$1,320 (transcript "$1,410" — flagged). ATR stop: 3-period, 1×ATR, 5-min | [s1jRE-Kg4dQ] |
| 126 | TLT, Jan 17 2025 close 87.19 → monthly 3rd-Friday campaign | Call diagonal (short 1-mo call 1st strike above close / long ~1-yr call ~11 pts below) | Jan: sell 10× Feb 21 88C @1.18 (+$1,180), buy 10× Jan 2026 76C @12.55 ($12,550) → net $11,370; Feb 21 close 89.61: 76C 14.52, 88C 1.60 → +$1,550 = 13.6%. Mar: 90C @1.13 / 78C @12.85 → net $11,720; close 90.70: 90C 0.69, 78C 13.57 → +$1,160. Apr: 91C @1.16 / 80C @11.93 → net $10,770; close 87.53 → 91C dies (+$1,160 realized), 80C @9.82 held. 3 months realized +$3,870 on avg capital $11,287 | [PrsUnhNjF4Y] |
| 127 | BKNG, Jan 4 2022 @2466.52, 100 sh ($246,652) | Monthly covered calls sized to 1% premium | Jan 2580C @25.30 (+$2,530; close 2412.94); Feb 2670C @25.25 (+$2,525; close 2281.46); ~$2,500/mo through Sep. Oct (entered Sep 30 @1654): 1830C @25.15 (+$2,515) → last 30 min stock 1867.63 → buy back @40.40 (−$4,040); Nov 2060C @26.45 (+$2,645); Dec call sold. Year +$26,701 = 10.8% yield vs S&P avg ~1.5% | [X5bFm3sWqkA] |
| 128 | RUT, Feb 1 2024 open 1964.07 (Oct 2023 low 1633), Mar 1 chain (30 DTE) | 8Δ iron condor, 40-pt wings, 1-lot | Sell 2150C Δ8.27 @4.40 / buy 2190C @2.50; sell 1790P Δ8.11 @5.30 / buy 1750P @3.55 → +$365, capital $3,635 (10.04%); PoP 83.62% (≈10 W / 2 L per yr); close 2076.39 → win. Apr 5 chain: 2290C/2330C + 1880P/1840P → +$410 / $3,590 (11.42%). Feb–Jun 5/5: +$1,964 = 54.44% | [FYNpBJDuXhU] |
| 129 | RUT, Jul 5 2024 @2052.87 — 10-lot after the streak | The scaling blunder quantified | 10× short 2210C / 1900P → +$3,560 credit; expiry close 2254.48 → short calls 44.48 ITM = −$44,480, long 2250C +$4,480 → trade −$36,440; 6-month campaign −$34,476 | [FYNpBJDuXhU] |
| 130 | GOOGL, Jul 11 @1143 (16 days pre-earnings; Apr report → −100 pts) | Pre-earnings directional put on recency-bias drift, exit before release | ATM 2-day option Jul 11: 3.24. Buy 2× 1132.5P (chain expiring 2 days post-earnings) @12.19 (transcript total "$4,038" vs 2×$1,219 — flagged); minutes pre-release GOOGL 1132 → puts 26.86 (8× the earlier ATM 2-day price) → stated +$1,328 (legs imply ≈+$2,934 — flagged). GOOGL +100 pts after the report (not held) | [7Wwy58T83W0] |
| 131 | $5,000 account, monthly income strategy, TP $500 / SL $500 | Blunder #1 arithmetic | 6 months: +350, +500 (after −400 DD), −500, +350 (after −400), −100, +400 (after −400) → +$1,000 = 20%, max DD $500. At $500,000: −$400 DD → −$40,000 (stop −$50,000); panics out 5 of 6 → −$135,000 = −27%. Desk traders draw down $75–100k intraday; prop accounts up to $20M; weight-training ladder 50 lb +5 lb (10%) → 150 lb (+3%) → 500 lb (+1,000%) over years | [-rwYS0Dq6Ro] |
| 132 | SPX, Jul 12 2023 close 4472.16 (year high), Aug 10 chain | Bull call spread (ITM 100-wide debit) | Buy 4350C @158.65 (−$15,865), sell 4450C @87.00 (+$8,700) → debit $7,795; max value $10,000 at any close ≥4450 → max profit $2,205 (transcript "$225") = 28.2–28.3%; close 4468.83 (below entry) → 4350C 118.83 / 4450C 18.83 → +$2,205 | [if0P_RU5zWc] |
| 133 | SPX, Aug 10 → Sep 7 2023 chain; Aug 18 @4346.90 | Bull call spread roll-down + size-up | Entry 4350C @157.30 / 4450C @83.25 → debit $7,405, max +$2,595. Aug 18: close-out value $4,680 (sell 4350C @69.75, buy 4450C @22.95) → −$2,725 ≈ max profit → roll: 2× 4225C ($31,880) / 2× 4325C ($17,080) → total invested $17,525. Sep 7 close 4451.14: $45,228 − $25,228 = $20,000 → +$2,475 = 14.1% | [if0P_RU5zWc] |
| 134 | QQQ, May 19 2023 @336.51 → May 2024 | Wheel: ATM monthly puts, calls at assignment strike | Jun 336P @5.74 (+$574; $33,600), close 367.93. Jul 367P @7.24 (+$724), close 375.63. Aug 375P @6.37 (+$637), close 358.13 → assigned @375. Sep 375C @1.98 (+$198); Oct 375C @6.18 (+$618); Nov 375C → close 386.04 → called @375. Dec–Mar puts expire. Apr 432P → 414.65 assigned (premium garbled "$85"); May 432C → 451.76 called. Year +$6,589 on max $43,200 = 15.25%, avg $549/mo; idle cash ≈5.13% MM rate 8 of 12 months; bonds/CDs 4–5% | [kE0T8l-p9ko] |
| 135 | SPX, Dec 29 2017 @2686, weekly, 200-DMA filter | Weekly 5-wide PCS (first put above market) | Sell 2690P @10.62, buy 2685P @8.54 → +$208; max loss $292; Jan 5 close 2743 → win. 2018: above 200-DMA 41/52 wks; 26 W (~$200) / 15 L (~$300); $300 → ~$2,000 (>500%); $3,000 → ~$20,000; S&P 2018 −6.24%; long-run stocks ~7%/yr, bonds 1–3% | [CjbWjnWXXzQ] |
| 136 | AMZN, Aug 1 2024 @188.07 | Cash-secured put (MoneyShow demo) | Sell Aug 30 185P @6.98 (+$698; $18,500 secured); close 178.5 → assigned @185. Sep 27 175P @3.05 (+$305; $17,500); close 187.97 → win | [tVQY5bSDodk] |
| 137 | SPY, Sep 15 2023 close 443.38 → Sep 2024, 2-lot | Wheel campaign (MoneyShow) | Oct: 2× 443P @5.47 (+$1,094; $88,600) → close 421.19 → assigned 200 @443. Nov: 2× 443C @1.12 (+$224) → close 450.79 → called @443. Dec: 2× 450P @5.19 (+$1,038; $90,000) → close 469.33. Jan +$996 ("96"), Feb +$1,000, Mar +$1,174, Apr +$1,228 assigned, May calls +$746 called, Jun +$1,172, Jul +$1,114, Aug +$1,401, Sep +$1,568. Year ≈+$12,781 (transcript "2,781") ≈ $1,000/mo on ≈$99,650 avg capital; SPY +422%/25 yrs; MM rate ≈4.7% Oct 2024 | [tVQY5bSDodk] |
| 138 | SPY, Jan 20 2023 @395, May chain (dividend 1.55%) | Covered call vs 3-lot call debit spread | CC: 100 sh $39,500 + 420C @7.02 → $38,798; close 418.62 → +$3,064 = 7.89%. Debit spread: 3× 390C @22.93 ($6,879) / 3× 420C @7.02 ($2,106) → $4,773; 390C = 28.62 → $8,586 → +$3,813 = 79.88% (>10×). CMG @2065 → $206,500/100 sh | [9j-MhX4j6cs] |
| 139 | Desk funding criteria | Trader-selection numbers | Min desk allocation $100,000; ideal personal account ≥$25,000 ($1,000 too small: $100 loss → $10,000; $2M too large); 24–36 months live >30%/yr; ≥5 yrs backtest+live; income trades win ~9 of 12 months; stress periods to test: Oct 2008, May 2010, Aug–Dec 2011, Aug 2015, Nov–Dec 2016, Feb 2018, Q4 2018; pre-market routine 8:30am ET; 120C example (stock 100→115, 3 DTE, call down) | [25ej9CwzTGQ] |
| 140 | PSX, Apr 4 2025 close 98.81 (from ~130; RSI 21), Jun 20 chain | Covered call vs diagonal | CC: 100 sh + 120C @2.10 → $9,671; close 124.78 → called @120 → +$2,329 = 24%. Diagonal: 120C @2.10 / Mar 2026 80C @24.70 → $2,260; Jun 20: 120C 4.70 (buy back), 80C 46.45 → +$1,915 = 84% | [W5Gl_E2Sq-A] |
| 141 | MO, Jan 13 2025 @50.85 (50 support since Aug), Jun 20 chain | 5-month put credit spread ×15 | Sell 15× 50P @2.54, buy 15× 47.5P @1.62 → +$1,380; capital $2,370; close 59.75 → +$1,380 = 58% vs shares +$890 = 17.5% on $5,085 | [W5Gl_E2Sq-A] |
| 142 | UPS, Apr 30 2025 close 95.30 (day after earnings) | Put calendar ×25 | Sell 25× Jun 20 95P @4.45 (+$11,125), buy 25× Jul 18 95P @5.25 (−$13,125) → cost $2,000; Jun 20 close 99.27 → short dies, long 1.24 → $3,100 → +$1,100 = 55% | [W5Gl_E2Sq-A] |
| 143 | CMG, Sep 20 2019 @ ≈835, channel 780–850, earnings Oct 22 | Pre-earnings double diagonal (long Oct 25 strangle, weekly short strangle rolled at the channel edges) | Buy 855C @27.51 ($2,751) + 775P @14.52 ($1,452) = $4,203; sell wk-1 850C $471 + 780P $82 → outlay $3,650. Wk2 (CMG 817): buy back 0.07/0.35 ($42), sell 1.48/2.63 → $3,281. Wk3 (≈820): 0.12/0.20 back, 2.28/2.81 sold → ≈$2,800. Wk4 (841): $64 back, $862 sold → ≈$2,000. Expiry week (CMG 845, earnings in 4 days, options expire 7 days out): 850C @27.88 + 780P @8.81 = $3,669 (vs $500–1,000 earlier weeks) → cumulative +$1,517. Oct 25 close 792 → all four worthless → +$1,517; worst alternative ≈+$1,000 | [t8VszTqb7iY] |
| 144 | TLT, third-Friday monthly campaign 2025 (flat chart 87–100 for 2 yrs; Jan 2 2025 close 87.57) | Double diagonal: short <20Δ call/put 1 mo out ×10, long 5 pts wider 2 mo out ×10 | Jan 17 (close 87.19): sell Feb 21 91C Δ18.23 @0.36 (+$360) + 83P (+$340); buy Mar 21 96C (−$240) + 78P (−$220) → +$240; capital $4,760. Feb 21 close 89.61: longs sold 0.11 / 0.01 → +$360. Feb→Mar: short 93C Δ18.36 / 86P Δ13.39, long Apr 98C / 81P → +$250, cap $4,750; Mar 21 close 90.70; longs 0.10 / 0.02 → +$370. Mar→Apr: short 94C / 88P, long May 99C / 83P → +$280, cap $4,720; Apr 17 close 87.53 → buy back 88P @0.47 (−$470), sell long puts $470 + long calls $60 → +$340. Rest of year all shorts expired worthless. Year +$3,645 = 77.5%; bid-ask 1–3¢ | [YLrRxUUHl44] |
| 145 | SPX, Friday ~9:45am @ ≈4440–4442 (Mon/Wed/Fri expirations since 2018 ≈150 days/yr) | 0-DTE 10Δ iron condor, 10-pt wings, 4-lot | Sell 4× 4475C Δ11.7 @1.05 (+$420), buy 4485C @0.51 (−$204); sell 4× 4405P Δ9.2 @2.14 (+$856), buy 4395P @1.18 (−$472) → +$600; capital $3,400; close 4455 → all worthless → +$600 = 17.6%/day | [IdbLc1JBYYI] |
| 146 | SPX, May 14 (2021) open ≈4150 (ATH area for a month) | 1-week/3-week ATM call calendar ×3 | Sell 3× May 21 4150C @34.14 (+$10,242), buy 3× Jun 4 4150C @60.45 (−$18,135) → debit $7,893. May 20 11:15am, SPX ≈ unchanged: short 13.30 (buy back $3,990), long 51.66 (sell $15,498) → +$3,615 = >45% in <1 week | [0M8oc0T66yk] |
| 147 | RUT, Jun 16 2023 open 1898.54 → Aug 18 chain (≈2 mo) | 10Δ iron condor, 50-pt wings, 1-lot, close at ≥50% of credit | Sell 2100C @6.15 / buy 2150C @3.35; sell 1690P @10.40 / buy 1640P @7.35 → +$585, capital $4,415; PoP ≈80%. Jul 12 RUT 1935.7: legs 3.50/1.50/3.25/2.35 → +$295 → close. Aug 18 (RUT ≈1862) Oct chain: 2050C/2100C + 1650P/1600P → +$667, cap $4,333 ("433"); Sep 5 RUT 1893.7 → ≈50% → close. 6 trades/yr all closed at 50% → >$1,800 on max capital $4,490 | [F4d_OIVawns] |
| 148 | SPX, Feb 1 2019 @ ≈2725, Mar 14 expiry | Iron butterfly ±100 wings → call-butterfly adjustment → iron condor | Sell 2725C (>$4,300) + 2725P (>$5,600); buy 2825C @8.95 (−$895) + 2625P (≈−$2,500) → credit $6,623; margin $3,400; breakevens ≈2660 / 2790. Feb 22 SPX 2790 → buy 2725C / sell 2× 2825C / buy 2925C for $5,139 → credit left $1,484; new position short 2825C, long 2925C, short 2725P, long 2625P. Mar 14 close 2810 → all OTM → +$1,484 (vs >−$1,500 unadjusted) | [ud2KQ-Di57Q] |
| 149 | SPX, Dec 11 (2024) open 6067.51 | 0-DTE iron condor 10-lot + call butterfly roll | Sell 10× 6080C @3.35 (+$3,350) / buy 6090C @1.30 (−$1,300); sell 6050P @2.88 (+$2,880) / buy 6040P @1.58 (−$1,580) → +$3,350; margin $6,650. 10:10am SPX 6081: buy back 6080C @6.95 (−$6,950), sell 20× 6090C @2.63 (+$5,260), buy 10× 6100C @0.88 (−$880) → credit $780. Close 6084.19 → +$780; unadjusted: 6080C pays $4,190 → −$840; swing $1,620 | [6-Q6xjAX7aM] |
| 150 | Breadth-day thresholds | Market internals classification | Neutral day: A/D between +500 and −500, VOLD between −2 and +2, TICK both sides of zero. Extreme/trifecta: A/D pinned ±2000, extreme VOLD, TICK one side of zero all day, offensive sectors leading (+ catalyst = "quadfecta", e.g. Nov 10 2022 cold CPI). Divergence day: gap down with VOLD slightly positive at the open. Reversion targets: gap fill, 2-day VWAP | [MkWozp1MFmg] |
| 151 | SPX, Jan 12 2024, 11am @ 4776.54 (neutral breadth) | 0-DTE iron condor ±20-pt shorts, 10-pt wings, 5-lot | Sell 5× 4795C @2.65 (+$1,325) + 5× 4755P @2.35 (+$1,175); buy 4805C (−$565) + 4745P (−$590) → +$1,345; capital $3,655; close 4783.83 → +$1,345 = >36% in 5 hrs | [MkWozp1MFmg] |
| 152 | NDX, Nov 10 2022, 11am @ 11,396.14 (trifecta day) | 0-DTE risk reversal (long 30Δ call financed by short put + protective put) | Buy 1× 11460C @21.65 (−$2,165); sell 1× 11350P @33.25 (+$3,325); buy 1× 11225P @8.00 (−$800) → +$360 credit; worst case $12,140. Close 11,605.96 → call = $14,596, puts worthless → ≈+$14,956 ("14,960"). Any close >11,350 keeps ≥$360 | [MkWozp1MFmg] |
| 153 | TSLA, 3× Sep 2020 285C bought @34 ($10,200); stock 250 → 300 on Oct 23 2019 earnings → 347 | Time premium anatomy + conversion to stock & short strangle | Call @92.45: intrinsic 62, time premium 30.45; exercise-and-flip $18,600 gross / +$8,400 vs selling calls $27,735 / +$17,535. Then buy 300 sh (≈$104,100), sell 3× Sep 2020 390C (≈$12,000) + 3× 280P → >$20,000 cash. TSLA 390 → profit >$50,000 = 49% (+$20,000 vs plain target sale); 280–390 → keep $20,000 + shares; ≤280 → +300 sh @280 | [mY0x0Mc8iqk] |
| 154 | SPX, Nov 11 2016 @ ≈2165 (200-DMA <2100) → 70-day Jan chain | Monthly 10Δ 50-wide PCS with 200-DMA filter (2017–18 campaign) | Sell Jan 2000P @18.10 (+$1,810), buy 1950P @13.00 (−$1,300) → +$510; capital ≈$4,500; Jan 20 2017 SPX 2250 → win. Dec: SPX 2253, 200-DMA 2120 = 10Δ → 2120P/2070P → +$505; Feb 17 SPX 2350 → win. Rules: 10Δ or the 200-DMA strike if higher; skip if >5 days below 200-DMA; stop = 2× credit ($475 → $950); ≈$4,750/trade, 2 overlapping = $9,500 max; close trade 1 when trade 3 opens. 2017 +49% (S&P +19%); 2018 +22% (S&P −7%); buy-and-hold long run ≈7%/yr; 2008 drawdown >50% | [UOX2_YaAIRc] |
| 155 | SPX, Feb 12 2019 @ 2745 (first day above 200-DMA in 2019) | 60-DTE 10Δ 10-wide PCS ×10, exit at ≥90% of credit / 3rd close below 200-DMA | Sell 10× 2575P @19.25 (+$19,250), buy 10× 2565P @18.00 (−$18,000) → +$1,250; capital ≈$8,750. Mar 28 (15 DTE): 1.15 / 1.05 → +$1,150 (92%). Apr 9 SPX 2877: 2715P @19.40 / 2705P @18.35 → +$1,050, cap $8,950; Jun 5 close for $50 (95%). 6 trades (Feb, Apr, Jun, Jul, Sep, Nov) on <$9,000 → +67% vs S&P +29%. Delta primer: 5 pts OTM ≈ Δ50; 200 pts OTM ≈ Δ5–10 | [PgghzkCugZ8] |
| 156 | QQQ, Jan 19 2024 close 421.18 (upper Bollinger + RSI>70) | Bollinger+RSI → 1-month 20Δ call credit spread ×10 | Sell 10× Feb 16 440C Δ17.51 @1.63 (+$1,630), buy 450C @0.53 (−$530) → +$1,100; Feb 16 close 430.57 (+9.39, still 9.43 under strike) → +$1,100 | [AayABdqDKIc] |
| 157 | QQQ, Apr 19 2024 close 414.65 (lower Bollinger + RSI 30) and later signals | Bollinger+RSI → 20Δ put/call credit spreads | May 17 390P Δ16.55 ×10 ($2,610) / 380P ($1,580) → +$1,030; close 451.76 → win. Jun 13 bearish: 495/505 CCS, close 494.89 → full credit ("130"). Aug 2 bullish: 415/405 PCS → +$1,170. 2024–25: all double signals won; 136% / 2 yrs ≈ 68%/yr (dollar total garbled "$25"). BB: 20-SMA ±2 SD; RSI 30/70 | [AayABdqDKIc] |
| 158 | SPX weekly, 2013 (Options Tribe) | Put-side broken-wing butterfly, 16Δ, 10–14 DTE, entered on sell-off days | RUT template long 1090P / short 20× 1070P / long 1020P (20 up / 50 down). Ex.1 Dec 10 2013: max +$470 at expiry; day 2 −$610; day 3 −$1,200/−$1,260 (8 DTE); Dec 18 Fed rally → shorts 5.55 → 1.81 → exit >1% of capital. Ex.2 Sep 18: shorts @1.00, credit $157 (profit anywhere >1700); grind into tent → +$930 (≈6×) → ≈15× → last day at short strike ≈+$8,000 on $9,800 worst case. Options Tribe hosted since May 2011 | [N9mx7uz3vbw] |
| 159 | TSLA, Jul 5 2024 close 251.52, 2-lot | Wheel: 20Δ first-Friday puts, calls at assignment strike | Aug 2 225P Δ23 @6.32 (+$1,264); close 207.67 → assigned 200 @225. Sep 6 225C @7.75 (+$1,550); close 210.73. Oct 4 225C (+$1,654); close 250.08 → called @225 flat. Nov 220P @6.30 (+$1,260); close 248.98. Dec 6 220P (+$950); close 389.22. Jan 3 2025 345P (+$1,450); close 410.44. 6 months $8,128 on avg $49,000 = 16.5% ≈ 33%/yr | [8KbV5QtKFCQ] |
| 160 | Market-environment grid (desk) | Intraday regime classification | Checks ≈9:45am, midday (European close), end of day. HS/LW: pullbacks retrace <½ of the up-leg; LS/LW: moves <1 ATR, cyclical; HS/HW: elevated VIX, full retracements — desk favorite. Themes cited: post-election US > overseas assets; XLU/homebuilders/real estate weak on rising long rates; XLB weak on overseas demand; XLK strong on US growth | [rnETl_NteAo] |
| 161 | SPY, Sep 1 2021 close ≈451.88 (transcript "4188"; ATH) | September put diagonal (long Sep 30 450P @5.58 / short Dec 31 440P @13.17) | Entry credit +$759; Sep 30 close 429.14 → 450P sold @21.39 (+$2,139) → cash flow $2,898; Dec 31 close 474.96 → 440P dies → +$2,898 | [vFTpvP8kwzY] |
| 162 | SPY, Sep 1 2022 close 396.42 / Sep 1 2023 close 451.19 | September put diagonal, 2022 & 2023 | 2022: long Sep 395P / short Dec 385P → +$640; Sep 30 close 357.18 → sell 395P @37.68 → stated $4,448 (legs: $4,408 — flagged); Dec 30 close 382.43 → buy back 385P @2.52 (−$252) → stated +$4,156 (legs: $4,196 — flagged). 2023: long Sep 450P / short Dec 440P → +$348; Sep 29 close 427.48 → sell 450P @22.81 → $2,629; Dec 29 close 475.31 → +$2,629 | [vFTpvP8kwzY] |
| 163 | WMT, Feb 21 2025 close 94.78, 500 sh ($47,390); dividend <1% | Covered-call roll: >80%-decay buyback + re-sell | 5× May 16 97.5C @3.20 (+$1,600) → net $45,790. Baseline: May 16 close 98.24 → called @97.50 ($48,750) → +$2,960. Pro: Mar 18 close 85.59, call 0.61 → buy back → +$1,295 (transcript "$12.95"); May 2 close 98.75, 97.5C @3.57 → re-sell 5 (+$1,785); assigned May 16 → total +$4,440 (+50%) | [WDbHqMeSCHA] |
| 164 | SPY, Aug 1 2023 (after +76 pts / +20% from March), Oct 20 chain (80 DTE) | Bearish broken-wing butterfly 1×2×1 + margin-control wing | Buy 452P @7.88 (−$788), sell 2× 434P (5% below) @4.24 (+$848), buy 250P @0.11 (−$11) → +$49; requirement $16,550. Oct 20 close 421.19: sell 452P @30.55 (+$3,055), buy back 1× 434P @12.58 (−$1,258) → cash $1,846; assigned 100 @434; sold Dec 29 @475.31 (+$4,131) → stated +$5,997 (legs: $5,977 — flagged). No selloff → keep $49 | [lRj741LUAFo] |
| 165 | SPY, Dec 30 2022 close 382.38, weekly chains, Q1 2023 | Weekly wheel: lowest put ≥$2.00 (>5 pts OTM), calls at assignment strike | Jan 6 377P @2.09 (+$209; transcript "$29"), $37,700 secured, close 388.08. Jan 13 381P @2.19 (+$219), close 398.50. Jan 20 397P @2.27 (+$227) → assigned @397. Jan 27 397C @2.95 (+$295), close 405.68 → called @397. Feb 3 399P @2.04 (+$204), close 412.35. Q1: 13 trades, $2,280 ≈ $175/trade, avg capital $40,200 → 22.68% annualized; idle cash → money market ≈5% | [1HXDto7qXaU] |
| 166 | DIA, Aug 10 (2020) @278, RSI ≈70 | 2-week call credit spread at +1 SD (≈285, ~32% reach probability), 50-lot | Sell 50× Aug 21 285C @0.91 (+$4,550), buy 50× 290C @0.34 (−$1,700) → +$2,850; capital $22,150; DIA ≈279 at expiry (short stock would have lost) → +$2,850 = >12% / 12 days | [RbWA61gJSa4] |
| 167 | DIA, Oct 28 (2020) @266, RSI ≈30 | 17-day put credit spread at −1 SD (≈245), 50-lot | Sell 50× Nov 13 245P @2.29 (+$11,450), buy 50× 240P @1.66 (−$8,300) → +$3,150; capital $21,850; DIA 295 at expiry → 14.4%. Year: 10 RSI signals, 10/10 wins, >$24,000 = >100% on capital | [RbWA61gJSa4] |
| 168 | SPX, Jan 3 2022 open 4788.89 (2021 +27%), Feb 28 chain (~60 DTE) | 10Δ iron condor, 10-pt wings, 10-lot | Sell 5050C Δ10.77 @10.20 (+$10,200) / buy 5060C @9.20 (−$9,200); sell 4260P Δ10.11 @22.90 (+$22,900) / buy 4250P @22.30 (−$22,300) → +$1,600; capital $8,400; close 4373.94 → win. Mar 1 open 4368.19: 4790/4800C + 3650/3640P → +$1,750; Apr 29 close 4131.93 → win. May–Jun 4570C/3390P → +$1,900. Jul–Aug 3200–4230 range, close 3955 → +$1,750. Sep–Oct 3380–4340, close 3871.98 → +$1,800 before roll | [KPcDNIqd4OI] |
| 169 | SPX, Oct 13 2022 @3553 (low 3491) | Iron-condor put-side roll at delta >20 | 3380P delta >20 → close 3380/3370, open 3250P (Δ10)/3240P; roll cost $1,150 (later spoken "$150") → trade +$650 instead of +$1,800. Year 2022: 6/6, $10,750 on max $8,400 = 127% (long-run expectation ≈80% PoP) | [KPcDNIqd4OI] |
| 170 | NVDA, Nov 20 2024, entry 143.93 (close 145.89), earnings after close, Nov 22 chain | Earnings ATM iron butterfly ±15 wings, 10-lot | Sell 145C @6.20 (+$6,200) + 145P @7.20 (+$7,200); buy 160C ("$15.90") + 130P ("$1,550") → stated credit $9,900, capital $5,100 (legs as transcribed don't sum — flagged). ATM IV 153.13/152.46 vs 39.97/38.69 a week earlier (Nov 13), when the same fly paid $3,580. Next AM open 149.35, 10am 144.26: buy back calls $2,150 + puts $2,830, longs pennies → +$5,100 = 100% overnight | [Stfx1brjj0k] |
| 171 | NDX, Aug 2019 @7966, Aug 30 chain (29 DTE) | Short strangle vs iron condor (blunder #7) | Strangle: sell 8325C @14.80 + 7350P @25.30 (first spoken "23.60") → +$4,010; capital ≈$83,000 ("83,600"). Aug 30 2pm NDX 7677: 0.25 / 0.17 → +$3,968 = 4.7%. Iron condor: + buy 8350C @11.75 (−$1,175), 7325P @23.60 (−$2,360) → +$475/lot, margin $2,025; 20-lot: +$9,500 credit on ≈$40,500 → closed +$9,360 = 23% | [4iCQciAzjJY] |
| 172 | SPX, Jul 1 2020 (post-crash recovery), Aug 31 chain (2 mo) | Bullish risk reversal 2-lot (long 3300C / short 3000P / long 2800P) | Buy 2× 3300C @68.20 (−$13,640); sell 2× 3000P @91.85 (+$18,370); buy 2× 2800P (transcript "99.30" impossible; ≈15.55 implied) → +$1,620 credit; capital $38,380. Aug 31 close 3500.00 → calls $40,000 + $1,620 = +$41,620 = >108%. Close 3001 → keep $1,620 | [pW2ZZAAPVMI] |
| 173 | PSX, Jul 1 2024 close 140.93 (April high 174.0), Dec 20 chain | Covered call on a falling stock (rule 1) | 100 sh + 150C @6.65 → net $13,428; Dec 20 close 110.37 → −$2,391 despite the premium | [DQ6nTpng7MM] |
| 174 | TSLA, Apr 9 2025 close 272.10 (2025 high 439; Feb 24 ≈330), Jun 20 chain | Strike at target vs juiciest premium (rule 2) + embedded-gain tax (rule 3) | 275C @33.55 → net $23,855; 330C @14.02 → net $25,808. Jun 20 close 322.16: 275 route +$3,645; 330 route +$6,408. Basis Apr 1 2020 split-adj 29.76 ($2,976) → assignment @275 realizes $24,524 → 15% tax $3,678.60 > $3,355 premium | [DQ6nTpng7MM] |
| 175 | QQQ, Jan 2 2025 close 510.23, quarterly calls | Reload below basis (rule 4) | 100 sh + Mar 31 515C @19.60 → $49,063; Mar 31 close 468.92 → expires. Jun 30 470C @23.13 → Jun 30 close 551.64 → called @470 → six months ≈+$250 (transcript "$240"). Alternative Jun 30 515C @4.55 → +$2,892 ("28.92"), >10× | [DQ6nTpng7MM] |
| 176 | AMZN, Feb 18 2025 close 226.65 | Wait instead of selling a worthless basis-strike call (rule 5) | Apr 17 230C @8.60 (+$860); Apr 17 close 172.63 (−23%); Jun 20 230C @0.36 ($36) → don't sell; May 13 close 211.37 → Jul 18 230C @3.50 ($350) | [DQ6nTpng7MM] |
| 177 | TSLA, Feb 5 (2024) close 181.02 | Cheap-call hurdle (reason 1) and premium hurdle (reason 2) | Feb 16 205C @0.57, Δ8.30 → 91.7% worthless; Feb 16 close 199.95 (+10%) → −$57. Feb 23 190C Δ33.53 @3.70; close 191.16 → worth 1.16 → −$254; breakeven 193.70 | [ic24mZL9Fdk] |
| 178 | AAPL, Nov 2 2023 close 177.57, earnings after close | Long ATM straddle into earnings (V-crush demo) | Next-day 177.5C @3.40 + 177.5P @3.18 = $658; next AM call 0.24, put 3.04; close 176.50 → put 0.85 → −$573 (short straddle ≈+$573; transcript "578") | [ic24mZL9Fdk] |
| 179 | SPX, Oct 16 2020 ≈3500 (pre-election channel 3200–3600; 2016 channel 2100–2200), Oct 23 chain | 1-week iron butterfly ±90 wings, 3-lot + put butterfly roll | Sell 3× 3500C @37.85 (+$11,355) + 3× 3500P @35.81 (+$10,743); buy 3× 3590C (−$1,938) + 3× 3410P (transcript "11,850"; ≈$3,339 implied) → +$16,821; capital ≈$10,000+; breakevens ≈3443 / 3556. Oct 19 SPX <3443 → buy back 3× 3500P, sell 6× 3410P, buy 3× 3320P → ≈$7,000+ left, capital ≈$12,000 (+20%). Oct 23 close 3465 → all worthless → ≈+$7,000 = ≈60%/week | [qm5ENAPUCEA] |
| 180 | SPX, Aug 30 (2019) ≈2935, Sep 6 chain | Weekly double broken-wing butterfly (±45 pts, 5/10/5) | Calls: buy 5× 2980C ($2,745), sell 10× 2990C (+$3,490), buy 5× 3010C (−$585) → +$160. Puts: buy 5× 2890P (−$6,180), sell 10× 2880P (+$10,570), buy 5× 2860P (−$3,855) → +$535. Total +$695, margin ≈$9,300 (>7%/wk in 2890–2980). Close 2984.10 ("28 94 10") → 2980C 4.10 ITM ×5 = $2,050 + $695 = +$2,745 = 29% | [toMmfKHzQXU] |
| 181 | SPY, Sep 15 2023 close 434.37 → Sep 20 2024 close 568.20, 200 sh | Monthly buy-write: highest call priced ≥0.5% of SPY | Oct 455C @2.22 ×2 (+$444), close 421.19. Nov 438C @2.14 (+$428), close 450.79 → called → +$1,154. Dec (rebuy ≈450.79; "4579") 460C @2.29 (+$458), close 469.33 → +$2,300. Jan 480C, close 482.43 → +$2,644. Feb 492C, close 499.51 → +$2,466. Mar 510C @2.66 (+$532, expired). Apr 525C @2.69 (+$538). May +$3,216, Jun +$2,840, Jul +$566, Aug +$588; Sep: shares from June @544.09 sold @568.20 (+$4,832). Stated year total "$2,534" (legs sum ≈$22,000+ — flagged) | [weUoHkMBL4A] |
| 182 | NVDA, Feb 21 2024 open 680.58 (ATH 744), earnings after close, Feb 23 chain | Pre-earnings 10Δ iron condor 20-lot, 5-pt wings | Sell 840C Δ9.93 @4.50 (+$9,000; "$99,000"), buy 845C @4.18 (−$8,360); sell 590P @4.47 (+$8,940), buy 585P @3.88 (−$7,760) → +$1,820; capital $8,180; 250-pt window. Next AM gap +79 (+11%) to ≈754: 840C 0.77, 845C 0.64, puts <0.10 → close: −$1,540 +$1,280 −$140 +$120 → +$1,540. Normal-day comparison (NVDA 734.30, 2 DTE): 10Δ call +54 / put −40 → 95-pt condor, $1,460 credit, more capital | [ipzry05eP00] |
| 183 | AAPL, Apr 22 2019 @203.70, earnings Apr 30 after close; Apr 12 199.70 / Apr 30 199.69 | Pre-earnings call calendar (short pre-earnings chain, long post-earnings chain) | IV build: 6-day 200C 2.17 (Apr 12) vs 4-day 200C 5.10 five hours before the report (+135%). Sell 10× Apr 26 202.5C @2.83 (+$2,830), buy 10× May 3 202.5C @5.92 (−$5,920) → debit $3,090. Apr 26 2:30pm same price: shorts 1.24 (−64%), longs 5.45 (−8%) → close $4,210 → +$1,120 = 36% in 4 days | [RP5xIYMrXKE] |
| 184 | RUT, Oct 1 2024 @2215.1, Oct 31 chain (30 DTE), close 2196.65 | Iron condor 100 out / 50 wings vs ATM iron butterfly 50 wings | IC: sell 2310C @18.30, 2110P @20.65; buy 2360C @9.35, 2060P @12.75 → +$1,685; capital = 5,000 − 1,685 = $3,315; all expire → +$1,685 = 50.8%. Iron fly: sell 2210C @57.95 + 2210P (≈ garbled), buy 2260C/2160P → credit ≈$4,205 (audio "$425"), capital ≈$795 (25% of IC); short put pays 13.35 → $1,335; profit $2,870 = 361% | [iJMkj24PHqs] |
| 185 | QQQ, Oct 17 2025 @603.93 (high 613, pullback 589), 3rd-Friday monthly wheel | Wheel: put at the retrace target, calls 25 pts above assignment | Nov 21 595P @12.49 (+$1,249; $59,500 secured); Nov 21 close 590.70 → assigned @595. Dec 19 620C @4.90 (+$490), close 617.05 → expires. Jan 16 620C @9.89 (+$989), close 621.05 → called @620 → +$2,500 shares. Feb 20 595P @5.85 (+$585), close 608.88 → expires. Total $5,813 vs $488 buy-and-hold (603.93→608.88) | [K6YVPHULzPA] |
| 186 | SPX, Apr 7 2025 @5062.25 (RSI low 20s, −17% tariff crash), May 7 chain | 10-delta put credit spread, 100 wide | Sell 4200P (Δ≈10) @47.45 (+$4,745), buy 4100P @40.35 (−$4,035) → +$710; capital $9,290; May 7 close 5631.28 → +$710 | [4dedQBgiZJA] |
| 187 | SPX, June 2024 @5421.03 (RSI >70), monthly chain | 10-delta call credit spread, 75 wide | Sell 5625C (Δ≈10) @6.95, buy 5700C @2.45 → +$450; capital $7,050; close 5615.35 (+~200 against the thesis, short of 5625) → full win +$450 | [4dedQBgiZJA] |
| 188 | SPY, 2023, $5,000 account, first-Friday monthly chains | Monthly put credit spread ~10 pts below, 50 wide (capital ≤ $5,000) | Jan 3 (380.84): Feb 3 370P @5.27 / 320P @0.28 → +$499, capital $4,501 (audio "$451"), close 412.35 win. Mar: 400P/350P → +$296, cap $4,704, close 404.19 win. 8 straight wins to early Sep. Oct: 440/390 +$296, SPY 429.54 → buy back short $1,088 → ≈−$792 (audio "$832"). Nov 420/370 @3.44 win; Dec win; Dec 1–28 win → 11/12 → +55.96% vs SPY +24.23%; plus 4–5% money market on the unspent cash | [oO5SfYblvio] |
| 189 | SPX, Jun 13 2019 @2889, next-week chain | Weekly put broken-wing butterfly 5/10/5 (10Δ shorts) | Buy 5× 2830P @6.83 (−$3,415), sell 10× 2820P @5.56 (+$5,560), buy 5× 2800P @3.71 (−$1,855) → credit $290; margin ≈$4,700; close 2956 → +$290 ≈ 6%/week. Lottery case close 2825: 5× $500 + $290 = $2,790 = 59%. Rules: SPX > 20-SMA, Thursday ~10:30 entry/exit, credit ≥5%, stop −10% | [xrCSOh4WEGY] |
| 190 | SPX, Oct 31 2023 open 4165.9, 0-DTE, close 4193.83 | 4-lot ±25 iron condor, 25 wings + call condor roll | Sell 4× 4190C @4.05 (+$1,620), buy 4215C @0.70 (−$280), sell 4140P @4.60 (+$1,840), buy 4115P @1.38 (−$552) → +$2,628, capital $7,372. 2pm roll: buy 4190C @5.00 (−$2,000), sell 4200C @1.38 (+$552), sell 4215C @0.17 (+$68), buy 4225C @0.08 (−$32) → credit $1,216; all expire → +$1,216 | [l7BHgd2PO6A] |
| 191 | AMZN, Nov 20 2018 @1502, Jan 18 2019 monthly (60 DTE) → rolled every ~60 days through 2019 | 10-delta iron condor, 100-pt wings, ~$9,000 capital | Jan: sell 1900C @8.81, buy 2000C @4.77, sell 1200P @15.03, buy 1100P @7.22 → +$1,185 (700 wide), close ≈1696 win. Mar 2050C/1400P +$907 (650 wide), close ≈1710. May 2000C/1450P +$1,011 (550), close ≈1810. Jul +$913 (550, AMZN 1881), close ≈1969. Sep 2250C/1700P, close 1794. Σ $5,082 = 56% by Sep; Nov 2050C/1550P open (AMZN 1770) | [8u89hMA2was] |
| 192 | GOOGL, Oct 25 2019 @1266 (ATH 1289), Dec 20 chain (57 DTE) | 2-lot iron condor + side scalping | Sell 2× 1400C @4.81 (+$962), buy 1520C @0.38 (−$76), sell 2× 1100P @5.14 (+$1,028), buy 980P @1.10 (−$220) → ≈+$1,694, POP 84%. Nov 7 (1322): put spread 4.04 → 0.56 → close for $112 → +$696. Dec 3: call spread 4.43 → 0.10 → close for $20 → +$866. Σ ≈$1,562, 17 days early, zero risk | [cSI1eXFW6Ms] |
| 193 | MSFT, Jul 1 2024 @456.73 (ATH) → Jul 1 2025 @492.05 | Cash-secured put, then covered calls (quarterly) | Sep 20 435P @8.80 (+$880; $43,500 secured), close 435.27 expires. Buy 100 @435.27; Dec 20 460C @11.20 (+$1,120), close 436.60. Mar 21 460C @12.37 (+$1,237), close 391.26. 460C 90 DTE @1.70 → skipped. May 5 (436.17): Jul 18 460C @8.97 (+$897). Jul 1 2025: 460C 33.93 → close: +49,205 +897 −43,527 −3,393 + prior cash → +$6,420 vs +$3,532 buy-and-hold (+81%) | [dU3eKVXlKQE] |
| 194 | SPX, May 27 2025 3:30pm @5914.87, next-day chain; close 5886.55 | Overnight 20-delta iron condor, 25-pt wings | Sell 5950C @6.00 (+$600), 5875P @6.45 (+$645); buy 5975C @2.00 (−$200), 5850P @3.35 (−$335) → +$710; capital $1,790; all expire → +$710 = 39% overnight. Skip on post-close mega-earnings / NFP / CPI | [8BjBWBuiEh8] |
| 195 | FB @217 (ATH), same-expiry | "Free call": long 220C financed by short 210P | Buy 220C @2.80, sell 210P @2.80 → $0 outlay; expiry 174.89 → assigned @210 → −$3,500+ vs the $280 the call alone risked (>10×) | [tT08tJdsH_E] |
| 196 | SMB course strategies backtest 2013–2015 | Bearish butterfly vs "the Bull" | 2013: BB <1% / Bull +61.6%; 2014: BB +146% / Bull +26.8%; 2015: BB +107.6% / Bull +8.6% — either held beats hopping | [LwZ9s2ud68s] |
| 197 | SPX one-day credit spreads on the InvestiQuant signal, Jan 2018–Sep 2020 backtest (single contract, slippage+commissions) | Same-day 10/20-pt put or call credit spread, no stops/adjustments | Cases: 2756 → 2750/2730 @4.45/0.95 +$350; 2923 → 2920/2900 +$400; 2783 → 2780/2760 +$508; 2777 → 2770/2750 +$230 (close 2774); 2932 → 2930/2910 +$300, close 2927 → +$20; 2730 → 2730/2710 +$465, close 2718.60 → −$675. Avg credit 20-pt spread: VIX<15 $334, 15–25 $504, >25 $692; Tue/Thu credit +20% but lower expectancy; rounding <5 vs >5 pts = 14% credit difference; 9:45 vs 9:30 entry: same win rate, −7% return, lower DD; raw signal 65–69% → spreads +10–15 pts, some >80%; strategies 25–40%/yr; ~25% of platform SPX open prints untradeable | [qabKcPmwjEA] |
| 198 | RUT, Jun–Aug 2025 Bollinger-band touches, 1-week chains | 1-σ 5-pt credit spreads, 10-lot | Jun 10 (2156.41 > upper band): sell 2225C @5.10 / buy 2230C @4.55 → +$550, cap $9,450, close 2101.96 win. Jul 1: 2255C spread +$750, cap $9,250, high 2246.23 → win. Aug 1 (2166.78 < lower band): 2085P/2080P +$750, close 2218.42 win. Aug 13 +$700, Aug 22 +$750 → 5/5, $2,200/quarter | [9q32G8yLxbM] |

| 199 | SPX, Dec 18 2023 → Jun 2024 (H1 2024 bullish program), 60-day third-Friday chains | 20-delta 100-wide put credit spreads: hold-to-expiry vs close at 50% of credit | Hold version: sell Feb 16 4575P @33.85 (+$3,385) / buy 4475P @22.40 (−$2,240) → +$1,145, capital $8,855, SPX expires 5005.57 → full win; Apr 19 chain (63 days) 4800/4700 → +$1,075, capital $8,925, mild selloff, close >7 points above the short → win; June 4700/4600 → +$1,275, SPX 5464.61 → win. Three trades, +$3,495 = 39.15% on the $8,925 peak capital. 50%-rule version: first spread closed Jan 11 (24 days in) for +$590 = 51.5% of credit; Mar 15 4645 PCS opened for +$1,045, past 50% by Jan 25 (SPX opens 4892.10) → 10 trades instead of 3 in the same half-year, several reaching 50% in 7–10 days (the transcript's total for the 50% version is garbled) | [tXD17g377NY] |
| 200 | SPX, Jun 16 2020; prior close 3124; pre-market e-mini zones resistance 3152–3160, support 3102–3110 | 0-DTE iron condor around the zones, 25-pt wings | Sell 3155C @8.94 (+$894), buy 3180C @2.82 (−$282); sell 3105P @7.16 (+$716), buy 3080P @3.15 (−$315) → credit $1,013 (transcript states "$1,030"); risk and capital $1,487; both zones held, close 3113 → all four expire → +$1,013 = 68% in a day | [Mn5fYhFqxvs] |
| 201 | SPX 0-DTE, Dec 5, index 6870 at entry, close 6869.07 | 30-point short strangle vs 10-point-wing iron condor | Strangle: sell 6900C @2.27 (+$227) + 6840P @5.25 (+$525) → +$752, all worthless → +$752 in a day. Same day closing 6960 instead: the 6900C pays $6,000 → −$5,248 (nearly seven winning days to recover; a $5,000 account is wiped out). Iron condor: also buy 6910C @0.95 and 6830P @3.85 → credit $272; at 6960 the long 6910C returns $5,000 → loss only $728, on far less margin. Compounding math: $5,000 at ~1%/week ≈ 50%/yr → $7,500 → $11,250 → >$25,000 in 4 years, sizing 10 lots → 15 lots | [7IHCmruEZUk] |
| 202 | SPX, Jul 12 2023 open 4478.25, Jul 19 chain (7 days), close 4565.72 | Same 4475 short put, three spread widths | 50-wide: sell 10× 4475P @22.70 (+$22,700) / buy 10× 4425P @8.55 (−$8,550) → +$14,150, capital $35,850 → +39%. 25-wide: 21 spreads 4475/4450 → +$18,165 (shorts $47,760, longs $29,595), capital $34,335 → +52%. 5-wide: 110 spreads 4475/4470 → ≈+$22,000, capital $33,000 → +66%. All three win in full; tighter long strike = more lots on LESS capital at a higher return | [66lbCWsfnyA] |
| 203 | TSLA, Aug 1 2023 close 261.07 (2022: >400 → 123.18) through Jul 2024; goal 300 shares | Rolling put ratio spread (buy 1 put ~5% OTM, sell 2 puts priced just over half of it), ~45 DTE | Sep 15: buy 250P @10.20, sell 2× 235P @5.65 → +$17 credit, $23,500 aside; TSLA 274.39 → +$17. Oct 27: 260P / 2× 245P → +$234, $24,500 aside; TSLA 207.33 → sell 260P @53.22 (+$5,322), buy back one 245P @38.18 (−$3,818) → +$1,738 and 100 shares assigned @245. Dec 15: 195P / 2× 180P → +$131, $18,000 aside; TSLA 250.35 → +$131. Jan 26: 240P / 2× 225P → +$99; TSLA 183.25 → +$1,606 and 100 shares @225. Mar: 175P / 2× 165P → +$85, $16,500 aside; TSLA closes $0.34 above 165 → +$85. Apr: 165P / 2× 155P → +$120; TSLA 147.05 → +$1,095 and 100 shares @155. Late May +$151; final Jul 2024 trade +$114. Campaign: 300 shares at 245/225/155 (cost $62,500) worth $74,471 plus ≈$5,525 of option profits → +$17,496, vs −$3,850 for buying the 300 shares outright on day one | [ygMHTNFIdbw] |
| 204 | PEP, Jan 19 2023 open 171.28, 1,000 shares held; 1-year chain to Jan 19 2024 | Covered strangle (10 calls ~5% above + 10 puts ~5% below) | Dividends alone: $4.95/share = $4,950 = 2.89% (S&P avg 1.32%; money-market funds >5% at the time). Sell 10× 180C @10.45 (+$10,450) and 10× 160P @7.60 (+$7,600) → +$18,050; PEP closed 165.78 → both sides worthless → premium + dividends = $23,000, >4× the dividend-only income. Obligations: shares called at 180 (plus capital-gains tax) on a rally; $160,000 of cash needed to take 1,000 more shares below 160 | [pyjOcisjrTU] |
| 205 | MSFT, Jun 18 2024 close 449.78; willing owner at 430 (resistance since late March) | Repeating one-month cash-secured puts until assignment | Sell Jul 19 430P @3.15 (+$315), $43,000 set aside; Jul 19 close 437.11 → keep $315. Sell Aug 16 430P @10.47 (+$1,047 — triple the first premium, the stock now only 7.11 above the strike); Aug 16 close 418.47 → assigned 100 shares @430. Premium collected while waiting $1,362; Oct 20 MSFT 516.81 → total position profit $10,043 | [lXtcZyC1Rks] |
| 206 | SPX, Nov 16 2020 @3621; long strangle in the Dec 2 chain, shorts rolled every 2–3 days | Double diagonal campaign | Buy Dec 2 3690C @20.40 (−$2,040) + 3550P @32.65 (−$3,265) → −$5,305. Sell Nov 18 3670C/3570P (50 points out) → +$1,273. Nov 18, SPX 3581, 15 minutes to expiry: buy the shorts back for pennies and re-sell the same strikes in the Nov 20 chain (3670C ≈0.57, 3570P 16.22) → outlay down to $2,401. Nov 20 (SPX 3571) roll again → outlay ≈$1,000. After the Nov 27 → Nov 30 roll cumulative cash flow is +$442. Nov 30 close 3621 → shorts die; sell the longs (call $172, put $217) → +$831 ≈ 15% in two weeks. Structural rule: rolling a short option to the same strike in a later chain always brings in cash | [5UNql894bD4] |
| 207 | GS, Nov 2 at the bottom of a 185–215 four-month channel; Nov 27 chain (25 days) | 5-wide call debit spread, 5 lots | Buy 5× 210C @1.30 (−$650), sell 5× 215C @0.82 (+$410) → debit $240 = max loss AND the entire broker requirement. Spread worth $2,500 at any close ≥215 → max profit $2,260 = >9:1 reward:risk, identical at 215 or at 300. GS closed >235: exercised — buy at 210 ($105,000), sold at 215 ($107,500) → +$2,500 gross → +$2,260 = >941% in 25 days. The debit is a stop that cannot shake you out of a temporary adverse move | [LHx19knh8x4] |
| 208 | Roulette vs options; HAS Dec 1 @82.69; SPX Apr 2 2018 | Casino expectancy and a 75Δ/25Δ put debit spread system | Roulette: 18 red + 18 black + 2 green = 38 → player 47.3%, house 52.7% → 5.4% edge; $1,000,000 wagered → $54,000; 1,000 bets of $1,000 → 527 wins / 473 losses → +$54,000. Option-buyer's version: HAS 87.5C (46 DTE, Jan 16) @1.40 = $140, delta 29.47 → 70.53% chance of zero; HAS rallied to 86.20 → 100% loss. Desk system: Mar 29 2018 SPX close 2640.87; Apr 2 open 2634.27, bearish trigger → 11-DTE chain: buy 2700P (Δ76.61) @77.25 (−$7,725), sell 2565P (≈25Δ) @16.40 (+$1,640) → debit $6,085; target 15% of debit ($912.75), stop 7.5% ($450). 10:15am: 2700P @91.50 / 2565P @20.60 → close for $7,090 → +16%; index closed 2581.88. Backtest 60% win rate, +$900 win / −$450 loss → expectancy 0.60×900 − 0.40×450 = $360/trade → $36,000 per 100 trades; at a 50% win rate expectancy is still +$225/trade | [rpFL_mEFPSg] |
| 209 | SPX, Mar 31 2023 close 4109.31 → Jun 30 2023; weekly 10-delta iron condors, 50-point wings | The 10× size-up blowup | 2-lot trade 1 (Apr 6): sell 4200C @2.60 (Δ8.87) / buy 4250C, sell 4000P @8.20 (Δ9.74) / buy 3950P @3.46 → +$894; SPX 4105.02 → win. Trade 2 (Apr 14): shorts 4210C/3980P → +$1,274, close 4137 → win. First 10 trades all won: +$9,718 (avg $971.80/week) on ≈$9,000 of capital per trade. Account then funded to $100,000 and a 20-lot put on: shorts 4390C/4190P → +$9,200 credit, requirement ≈$90,800; Jun 16 SPX closed 4409.59 (first close >4400 that year) → 19.59 pts × $100 × 20 = $39,180 payout → −$29,980, exactly 10× the −$2,998 a 2-lot would have lost. Rest of the quarter at 2 lots: Jun 23 +$726, Jun 30 −$3,278 → actual campaign −$22,800; staying 2-lot throughout: +$4,168 ≈ 44% on the peak 2-lot requirement | [ftmEH4ikBy4] |
| 210 | SPX, Dec 17 2018 @2552; end-of-January chain, 20-point wings, 10 lots | Iron condor scalped side by side at ~80% of each side's own credit | Entry: sell 2660C @29.50 (+$29,500) / buy 2680C @24.03 (−$24,030) → call side +$5,470; sell 2330P (+$19,200) / buy 2310P @16.85 (−$16,850) → put side +$2,350; total credit $7,820, capital and max loss $12,180. Dec 24 12:45pm, SPX 2366: buy back 2660C @4.10 (−$4,100), sell 2680C @2.98 (+$2,980) → call side banked $4,350 = 80% of its credit. Jan 10, SPX 2596: buy back 2330P @3.00 (−$3,000), sell 2310P @2.58 (+$2,580) → put side banked $1,930 = 82%. Total +$6,280 = >51% of capital. Counterfactual: SPX ended January at 2704.10 → the untouched condor pays $44,100 on the short calls against $24,100 back on the longs → −$12,180, the full maximum loss | [cSKJpuNX2lU] |
| 211 | Freudberg's own career; SPX iron condor Apr 20 → Jun 19 2020 | Career, community and venue numbers | Property & casualty insurance CEO for 15 years (industry ranked 135th of 194 for returns), retired 2006; $10,000 seminar scam encountered 2006; joined SMB 2010. First strategy: monthly iron condors, six straight winning months, capital +2,500% → sized up → "got killed" the next month and never traded it again; four years to find the bread-and-butter trade (the "Rhino": 25–30%/yr with drawdowns rarely beyond 5–6%, chosen over strategies making 100%/yr with 30% drawdowns). Options Tribe: first webinar May 15, every Tuesday 4:30pm ET, ~500 recorded over nine years, premium archive $30/month. Mentoring cohort: 10 traders/month who had each paid $6,000 — five never answered the scheduling email, two quit after 1–2 sessions, one of the remaining three never finished the 13 sessions; success rate across all trading styles ≈20%. Teaching condor: entered Apr 20 2020 with SPX ≈2900 for Jun 19 expiry, short 3400C / short 2200P → $28,000 at ANY close between 2200 and 3400 (needing a 700-point drop or a 500-point rally in 60 days to fail) → won in full. Platform share among options income traders: ≈75% thinkorswim, ≈15% Interactive Brokers, ≈10% tastyworks; analysis software (OptionVue / OptionNet Explorer) ≈$1,000/yr | [FDpmRhFsp5s] |
| 212 | TSLA, Dec 20 2023 open 256.41 (+26% off the Oct 31 low); desk trader long 500 shares at a $110 cost basis (≈$55,000) | Bear put spread financed by a covered call (Feb 16 chain) | Buy 5× 250P @15.48 (−$7,740), sell 5× 195P @2.16 (+$1,080, at the Oct 31 support), sell 5× 265C @1.65 (+$825, at the early-October resistance) → +$1,360 net CREDIT (the hedge costs nothing). Feb 5 2024, day after Q4 earnings, TSLA 184.26 with 11 days left: 265C @0.03 → buy back ≈$20; 250P @66.15 → +$33,075; 195P @12.95 → −$6,475 → hedge closed at +$27,940. Unhedged path: +$73,205 unrealized on Dec 20 → −$35,865 drawdown Feb 5 → +$75,000 by Jul 15 (TSLA 260). Hedged path: >$100,000 by Jul 15 and only a $7,923 drawdown at the Feb 5 low. Caps: shares called at 265; possible assignment of 500 more shares at 195; profit grows from 250 down to 195 and stops there; at any close ≤265 with both puts worthless the $1,360 credit is kept | [-huhEgn9TRg] |
| 213 | CRM, May 3 ~noon @163; earnings Jun 4; May 31 (pre-earnings) and Jun 7 (post-earnings) chains, 10 lots | Double calendar exited BEFORE the report | Call side: buy Jun 7 172.5C @2.52 / sell May 31 172.5C @0.94 → $158 per lot. Put side: buy Jun 7 152.5P @2.58 / sell May 31 152.5P @1.24 → $134 per lot. Total debit $292 × 10 = $2,920 = the entire risk. May 31 2:15pm, CRM 152.59 sitting on the put strike: both 172.5 calls ≈worthless; May 31 152.5P down to 0.37 (two hours left); Jun 7 152.5P blown up to 4.74 (earnings two days away) → closing value $4,385 → +$1,465 ≈ 50% in 28 days, with no earnings exposure taken | [qblhVcLltZQ] |
| 214 | SPY, Dec 10 2021 @468.50 (all-time highs); Dec 17 chain (1 week), 8 lots | Weekly iron condor + put condor roll | Sell 8× 474C @1.16 (+$928) / buy 8× 484C @0.10 (−$80); sell 8× 463P @2.75 (+$2,200) / buy 8× 453P @1.12 (−$896) → +$2,152 credit (stated requirement "28.48" garbled; structural max loss $8,000 − $2,152 = $5,848). Four days later SPY breaks 463 → roll the put side 5 points down: buy back 463P (−$3,800), sell the 453P wings (+$1,264), sell 8× 458P (+$2,320), buy 8× 448P (−$712) → stated roll cost $918 (legs sum to $928), credit left $1,234. Dec 17 SPY 461 → all four expire → +$1,234 for the week | [LcqiRgKeGXg] |
| 215 | AMZN, Jan 2021, resistance 3500 / support 2950; earnings Feb 1; Jan 29 (pre) and Feb 5 (post) chains, 2 lots | Double calendar into earnings, exited before the report | Buy 2× Feb 5 3500C @29.95 (−$5,990) / sell 2× Jan 29 3500C @15.20 (+$3,040); buy 2× Feb 5 2950P @44.73 (−$8,946) / sell 2× Jan 29 2950P @25.83 (+$5,166) → debit $6,730 = whole risk. Jan 27, AMZN 3217 (+~2%): sell longs $8,376 + $5,686, buy back shorts −$676 − $472 → $12,914 → +$6,184 = 91% in two weeks, no earnings exposure | [7XBsrrQOdQU] |
| 216 | SPX, March 5, IQ bullish signal, open 3802; same 3800 short put, three geometries | Spread width vs lot count (gross risk fixed at $2,000) | 1 lot 20-wide: sell 3800P @19.56 (+$1,956) / buy 3780P @12.43 (−$1,243) → +$713, max loss $1,287, R:R 55.4% ("54" in audio). 2 lots 10-wide: +$3,912 / −$3,128 (3790P @15.64) → +$784, max loss $1,216. 4 lots 5-wide: ≈+$7,800 / ≈−$6,900 (3795P) → +$852, max loss $1,148, R:R 74.2%. SPX closed 3841 → all worthless | [j0laz0Ks5F8] |
| 217 | SPY, Oct 10 close 653.02; Oct 17 chain (7 DTE), 10 lots | Iron condor: construction, max loss, breakeven, probability dial | Sell 10× 666C @1.83 (+$1,830) / buy 10× 668C @1.35 (−$1,350); sell 10× 640P @3.17 (+$3,170) / buy 10× 638P @2.81 (−$2,810) → +$840 credit, capital and max loss $1,160. Oct 17 close 664.39 → +$840. Loss case SPY 695: pay $29,000, receive $27,000 → −$1,160 (identical at 800: $134,000 vs $132,000). Partial: close 666.50 → −$500 → +$340; breakeven 666.84. PoP = 100 − 21.24Δ − 25.14Δ = 53.61%; widened to 670C (13.30Δ) / 626P (11.67Δ) → >75% PoP but credit $430 and capital $1,570 | [ASsnZOKLXGg] |
| 218 | SPX, Dec 18 2024 (FOMC): open 6047 → close 5872 (−178, ≈3%), VIX +74%; vs Nov 15 2024 close 5870 (−79), VIX 14.31→16.14 | Same 5700/5650 put credit spread, 2 lots, in high vs normal volatility | High-vol (Jan 17 chain): sell 2× 5700P @70.35 (+$14,070) / buy 2× 5650P @61.55 (−$12,310) → +$1,760, capital $8,240; Jan 17 SPX 5966 → +$1,760 = 21%/month. Normal-vol (Dec 16 chain): @33.75 / @27.30 → +$1,290 ($470 less) and $8,710 capital ($470 more, +5.7%); Dec 16 close 6074 (audio "6748") → +14.8% (audio "148%") | [IsuWqXxvjeA] |
| 219 | Career/mistake arithmetic: a $25k→$500k account; a 10-lot NDX iron butterfly; strategy A vs B; GIS Jul–Sep 2022 | The five deadliest mistakes | Sizing: $25,000 account +22% in 5 months, 100% win rate → funded to $500,000 → June's first loss erased all gains plus $29,000 (sensible path: +30% = $7,500, then ~+20% capital next year). Orders: NDX iron fly 10-lot at MID → +$140,850 credit, requirement $9,150, max R:R 15.39:1; as a MARKET order → >$10,000 less credit, >2× the capital, <half the R:R. Hopping: strategy A +30%/yr with 3 flat months to August; switching to B in September → +4% for the year. Cheap options: GIS 74.92 on Jul 15 2022, 10× Sep 85C @0.13 = $130, Δ2.76 (97.24% worthless) → Sep 16 GIS 75.25 → total loss. Income strategies ≈ 30%/yr on constant utilised capital; Rhino win rate 80% | [i0h4_uVeDtY] |
| 220 | SPX Mon/Wed/Fri chains since Jan 1 2018 (12 → 150+ expirations a year); 468 tested periods | SMB × InvestiQuant "Weekly Options Income Machine" — full workshop statistics | Signal built over 4 years / $1.5M with Duke's Center for Quantitative Modeling; 10 months of joint research on spread location and entry time. Win rate 86.4% = 76.1% full wins (356/468) + ~10% partial wins; 10.9% partial losses; <3% maximum losses. Capital per trade ≈$1,700–$1,800 → $20,000 account 42%, $15,000 56%, $10,000 85% (headline "40%+ yearly average"); recommended account $20,000, floor $10,000 (never one max loss). Worked trade Mar 1: SPX opens 3869, sell 3860P @9.51 (+$951) / buy 3840P @4.71 (−$471) → +$480; close 3901 → +$480; counterfactual close 3857 → pay $300 → still +$180. Desk: 50+ traders, options desk mostly 40s–60s, fully virtual | [DGnUHMPbcJA] |
| 221 | TLT, Oct 3 2023 close 85.06 (2023 low, RSI ≈20); never below 80 this millennium; Dec 29 2023 chain, 10 lots | "Win-win-win" modified risk reversal | Sell 10× 80P @1.59 (+$1,590) / buy 10× 70P @0.30 (−$300) → +$1,290, capital $8,710; buy 10× 93C @1.00 (−$1,000) → net credit +$280, capital $9,720. Outcomes: >93 → credit + call value; 80–93 → keep $280; <80 → assigned 1,000 TLT at a 25-year low. Dec 29 TLT 98.88 → calls 5.92 = $5,920 → +$6,210 = >63% in <3 months | [WP7JVyd6bjM] |
| 222 | SPY after VIX>50 spikes — the only four in ten years (Aug 2015, Feb 2018, Mar 2020, Aug 5 2024); 100 lots, ~6 months out, 5-wide | 40-delta put credit spread into a panic | Aug 2015 (SPY opens 183.87, ≈7% drop): sell 100× Mar 2016 180P @13.66 (Δ43.2) / buy 100× 175P @11.57 → +$20,900, capital $29,100; expiry 204.37 → +71.8%. Feb 2018: Jul 20 260P/255P → +$15,100, capital $34,900; close 279.68 → +43.2%. Mar 6 2020 (SPY 293.38, −3%): Sep 285P/280P → +$17,200, risk $32,800; Sep 18 close 330.65 → +52.4%. Aug 5 2024 reference: SPX gapped −225 pts (>4.2%), VIX 65 vs normal 13–19 | [vfpqix1O30U] |
| 223 | TSLA, May 2019: capital raise priced 243 → gap below 200 to 197; support 180–182 (S1 184, S2 182) | Swing risk reversal (short 185P / long 215C) hedged with short common | Monday entry, chain expiring the FOLLOWING Friday: sell 10× 185P, buy 10× 215C → credit ≈$4/share. Rules: puts 5–10% below an extended price, calls 5–10% above, 1–2 weeks out; cut half if it drops below 194; at a ~5% bounce (205–206) short common against 20% of the calls, another 20% per further 5%; short-dated 180 puts bought as gap insurance after Wednesday's 192 close; half the 205 short covered on the flush below 194. Headline context: Morgan Stanley $10 worst case (with a $230 target), Musk cost-control email, Consumer Reports Autopilot story, then a leaked email on orders beating the record December quarter → stock +≈$15 | [nMq1TZFBToE] |
| 224 | SPX, Jul 24 2024 close 5427.13 (ATH 5669 on Jul 16); Oct 18 chain (~3 months) | Modified risk reversal (put credit spread financing a long call) | Sell 5400P @118.60 (+$11,860) / buy 5200P @71.75 (−$7,175) → $4,685; buy 5750C @43.85 (−$4,385) → entry credit +$300, capital $19,700. Payoff: +$300 at ANY close ≥ 5400, plus $100/point above 5750; only a close <5400 can lose. Oct 18 close 5864.67 → call 114.67 ITM = $11,467 → +$11,767 = 59.7% | [Fet_MWkqemw] |
| 225 | SPX, Aug 1 2022 at the top of the year-long down channel; mid-September chain (≈6 weeks), 5 lots | "Bear trap" broken-wing put condor (long 4000P / short 3950P / short 3900P / long 3800P) | Buy 5× 4000P (−$38,550), sell 5× 3950P @64.65 (+$32,325), sell 5× 3900P @54.05 (+$27,025), buy 5× 3800P (−$18,875) → +$1,925 entry credit, capital and worst case $23,075. Any close ≥4000 (including a continued rally) → +$1,925. Sep 16 SPX 3873.33: 4000P 126.67 ITM (+$63,335), 3950P 76.67 ITM (−$38,335), 3900P 26.67 ITM (−$13,335), 3800P worthless → +$13,590 = >58% | [BY2qOpNoDdI] |
| 226 | NFLX, Jun 21 2019 open 366.94 (100 shares = $36,694) → Apr 1 (video date) | Rolling deep-ITM LEAPS campaign (each year buy the call priced just under half the stock) | Buy Jun 2020 195C @180.05 (−$18,005); Jun 2020 NFLX 447.82 → sell @253.15 (+$25,315), buy Jun 2021 235C @221.80 → outlay $14,870. Jun 2021 NFLX 498.90 → sell 235C @263.30 (+$26,330), buy Jun 2022 260C @244.55 → outlay $12,995. Jun 2022 NFLX 176.21 → 260C worthless (campaign drawdown $12,995 vs $19,073 on the shares; audio "19,731"); buy Jun 2023 100C @87 (−$8,700). Jun 2023 NFLX 444.60 → sell @344.65 (+$34,465), buy Jun 2024 245C @220.62 → stated outlay $7,950 (itemised legs give $9,292 — a leap price is garbled). Final leap sold @$37,225 → +$27,886 = >113% vs +$24,733 = 67.4% for the shares | [WSsXl8Nh3PM] |
| 227 | SPX, May 23 2016 (channelling 2000–2100), Brexit referendum Jun 23; Jun 17 (pre) and Jun 30 (post) chains, 10 lots | Double calendar around a MACRO event, closed before it | Sell 10× Jun 17 2100C @5.25 (+$5,250) and 10× Jun 17 2000P @13.90 (+$13,900); buy 10× Jun 30 2100C @11.90 (−$11,900) and 10× Jun 30 2000P @23.85 (−$23,850) → debit $16,600 = max risk. Jun 16 12:30pm, SPX 2064 with 3.5 hours left (needs +36 or −64): sell longs $13,750 + $15,300, buy back shorts −$130 − $250 → +$12,070 = >72% in under a month, flat before the vote | [CNEYo3P-CRk] |
| 228 | SPY, Friday Jul 9 (IQ bullish signal), open 432.72, close 435.51 (+2.79) | Deep-ITM 0-DTE call instead of 300 shares | 300 shares = $129,816; instead buy 3× 427C @5.78 = $1,734 (≈75× cheaper). At the close the call is worth its intrinsic 8.51 (exercise buys the shares for $128,100 vs $130,653) → sell for $2,553 → +$819 = >47% on capital, vs +$834 = 0.6% on $129,816 of stock. Reference: 300 shares at ~463 = $138,900 pays $300/point = 0.2% | [9pnSF-YE2DQ] |


## CHAPTER: NLM-extracted videos (hybrid pipeline — NotebookLM extraction, figure-gated)

> Extracted by NotebookLM from the verbatim transcript archives, then gated by `trial_verify_figures.py`: every figure below appears in the raw transcript unless marked **⚠unverified** (not found as digits or spoken words — treat as suspect until a human or Claude pass adjudicates it). Claude did not read these transcripts.

### [j2PxP-o-M1E] A Simple Options Strategy for Monthly Income (27,000 views)

PART A — Handbook Chapter Content

### Setup
*   **Instrument**: **SPY ETF** (iShares S&P 500 ETF, which mirrors the S&P 500 Index).
*   **Structure**: **Cash-Secured Put Selling** (selling put options monthly while maintaining the cash required to buy the stock if assigned).
*   **Strikes/Deltas**: Select out-of-the-money strike prices that yield a premium representing **as close as possible to a one percent return** on the cash-secured capital requirement. Examples include the **410 strike** and **400 strike** puts.
*   **DTE (Days to Expiration)**: Approximately **one month**, targeting options chains that expire on the **third Friday** of each month.
*   **Entry Trigger**: Initiated as a systematic, recurring monthly campaign. This strategy is deployed when a trader expects the equity market to take a breather or digest a major run-up, or during a projected decade of market underperformance/decelerated growth where broad market buy-and-hold returns are expected to be anemic.

### Management and Exit Rules
*   **Expiration worthless**: If the stock closes above the sold put strike price at expiration, the puts expire worthless ("die and go to options heaven"). The trader simply walks away keeping the entire upfront premium cash flow as net profit.
*   **Capital Security Requirement**: The trader must maintain sufficient cash in the account to cover the full obligation of buying the underlying shares should the puts expire in-the-money. For a 10-lot trade at a 410 strike, the trader must tie up **410 000** in cash.
*   **Assignment Resolution**: If the stock closes below the put strike on expiration day, the trader is assigned and must buy 100 shares of SPY per contract. This position is then managed using **the wheel strategy** (selling covered calls to eventually dispose of the assigned shares).

### Stated Edge or Statistics
*   **Broad Index Diversification**: Broad indexes like SPY lack single-stock earnings events and individual corporate scandals (such as CEOs getting cuffed) that can cause catastrophic price gaps, making them much safer and more consistent for systematic premium selling.
*   **12-Month Campaign Performance**: A 12-month campaign starting in April 2021 achieved a **100% win rate**, winning all 12 monthly trades and collecting a total cash profit of **53 610** dollars.
*   **Return on Capital Outperformance**: Tying up an average capital level of **four hundred twenty two thousand five hundred dollars** in the program yielded a return of **over twelve percent**. This return was **more than two and a half times** the buy-and-hold SPY return of **4.92** over the same period.

### Caveats
*   **Heavy Capital Allocation**: To safely run a cash-secured put campaign without taking on leverage, significant capital must be tied up (e.g., **410 000** to trade 10 contracts of 410 puts), capping the monthly return on absolute capital at around 1%.
*   **Downside Assignment Risk**: If the market enters an aggressive bearish trend, the put strikes will be breached, forcing the trader to buy the shares at the strike and experience unrealized paper losses on the stock until it recovers or is wheeled out.

***

PART B — Spoken Numbers Table

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Option Contract Terms** | Put Option Contract | Entitles the buyer to sell **100** shares of stock per contract |
| **Capital Yield Target** | SPY Put Selling Campaign (1-year duration) | Target cash inflow of "**as close as possible to a one percent**" (1%) of capital level each month |
| **May Trade Entry & Capital** | SPY cash-secured put. Sold 10 contracts at 410 strike. Expiry May 21st. | Credit received: "**four thousand five hundred twenty dollars**" (also spoken as "**45 20**"); capital requirement: "**410 000**" in cash |
| **May Trade Settlement** | SPY put expiration (May 21st) | SPY closed at "**4 14 94**"; puts expired worthless; net profit kept: "**45 20**" (\$4,520) |
| **June Trade Entry & Capital** | SPY cash-secured put. Sold 10 contracts at 400 strike expiring June 18th (third Friday in June). | Put option price: "**3.78**"; cash premium collected: "**37.80**" (representing \$3,780 **⚠derived** (transcript says price 3.78 / premium 37.80; ×100 not spoken)) |
| **June Trade Settlement** | SPY put expiration (June 18th) | SPY closed at "**right under 415**"; puts expired worthless; net profit kept: "**37.80**" (\$3,780 **⚠derived** (transcript says price 3.78 / premium 37.80; ×100 not spoken)) |
| **1-Year Campaign Totals** | SPY cash-secured put campaign (April 2021 to April, 12 months) | Won "**all 12 months**"; total cash profit: "**53 610**" dollars; average capital tied up: "**four hundred twenty two thousand five hundred dollars**" (\$422,500 ✓verified (spoken: "four hundred twenty two thousand five hundred dollars")); return on capital: "**over twelve percent**" (12%); buy-and-hold SPY return baseline: "**4.92**" (options campaign return was "**more than two and a half times**" the stock return) |

### [goK0QOsQRvQ] If you want to win at Options trading, enter and exit like this (27,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: **TLT ETF** (iShares 20+ Year Treasury Bond ETF) [1].
*   **Structure**: **Cash secured put selling** [1, 2].
*   **Strikes/Deltas**: **Nearly 30 Delta puts** [3]. Strike selection examples include the **86 put, 87 put, and 88 put** [3-5].
*   **DTE (Days to Expiration)**: **One month** [6].
*   **Entry Trigger**: Continuous reloading campaign on a high-liquidity stock or ETF you are willing to own at the strike price [2, 3, 6].

### Management and Exit Rules
*   **The Velocity of Capital Matrix**: Split the trade's duration into time-based quartiles to take profits early and reload rather than holding blindly to expiration [4, 6]:
    *   **Week 1**: Take profit if the trade reaches **50% of the maximum 100% profit** (original credit collected) [6, 7].
    *   **Week 2**: Take profit if the put price shrinks to **40% of its original price**, capturing a **60% profit** [5, 6].
    *   **Week 3**: Take profit if the trade exceeds a **75% minimum profit requirement** of the original cash flow [7].
    *   **Week 4**: Hold to expiration morning, cashing out for a **90% profit** when the option gets down to **10% of its original price** [4].
*   **The Reload Rule**: Immediately start a new trade and redeploy capital at a full premium once a profit target is hit, avoiding late-stage capital stagnation [5, 6].

### Stated Edge or Statistics
*   **Baseline Unmanaged Campaign**: Over a 3-month period, a static "set it and forget it" campaign allowed to expire produced **\$2,440** in profit [3].
*   **Managed Campaign**: Using the quartile profit matrix over the exact same period and asset produced a final profit of **\$3,050 **⚠unverified** (absent from transcript in any spoken form) (absent from transcript in any spoken form)** [7].
*   **Return Boost**: The active management approach generated **25% more profit** than the unmanaged expiration technique [7].

### Caveats
*   **Increased Workload**: Active management requires "more work" than a simple unmanaged approach [7].
*   **Assignment Risk**: If the stock drops and closes below the short strike, the trader will be assigned and must come up with the capital to purchase **10,000 shares of TLT** (or 100 shares per contract) [3, 8].
*   **Languishing Capital**: Holding a trade near expiration for the remaining tiny premium yields a slow profit pace, unnecessarily tying up valuable capital [6, 7].

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Unmanaged Baseline: Month 1** | TLT ETF, Cash Secured Put, 86 put strike [3] | Stock closed **\$3.61 61 cents** above strike; pocketed **\$1,30** (as spoken) in put premium [3] |
| **Unmanaged Baseline: Month 2** | TLT ETF, Cash Secured Put, 88 put strike [3] | Put sold at **nearly 30 deltas** for **65 cents**; brought in **\$650** [3] |
| **Unmanaged Baseline: Month 3** | TLT ETF, Cash Secured Put, 88 strike [3], expired March 21st (the third Friday in March) | Stock closed at **9070** (as spoken); win of **\$650** [3]; assignment requires owning **10,000 shares of TLT** [3] |
| **Unmanaged Baseline Campaign Totals** | TLT ETF, Cash Secured Puts, 3-month campaign [3] | Produced a final profit of **\$2,440** [3] |
| **Exit Matrix Matrix Benchmarks** | One-month options trade duration split into quartiles [6] | First week profit target: **50%** of maximum **100%** profit; second week option target: put shrinks to **40%** of original price for a **60%** profit [6] |
| **Managed Campaign: Trade 1** | TLT ETF, Cash Secured Put, 87 put strike [4], TLT trading at 8831 | Sold put for **76** (76 cents), collecting **\$760**; held to expiration morning; put dropped to **10%** of original price; closed for **90%** profit; paid **6 cents** to buy back for a final profit of **\$700** [4] |
| **Managed Campaign: Trade 2** | TLT ETF, Cash Secured Put, 86 put strike [5], TLT trading at 8742 | Sold **30 delta puts** priced at **86** (86 cents), collecting **\$860**; moved forward **12 days** to January 29th; put trading at **34 cents** (**40%** of original price); buyback triggered at **60%** profit; net profit of **\$520** [5] |
| **Managed Campaign: Trade 3** | TLT ETF, Cash Secured Put, 87 put strike ("30 delta calls" as spoken [5]), expires February 28th | Collected **\$860** positive cash flow; waited **a week** to the morning of February 5th; TLT opens up **a\$ 13** (as spoken); put dropped to **35 cents** (**less than 50%** of original price of 86); closed for profit of **510** (more than 50% in first week) [7, 9] |
| **Managed Campaign: Trade 4** | TLT ETF, Cash Secured Put, March 7th trade [7] | Closed in the third week; exceeded the **75%** minimum profit requirement; net profit of **\$700** [7] |
| **Managed Campaign: Trade 5** | TLT ETF, Cash Secured Put, March 28th trade [7] | Received **680** upfront; closed within the week under the **50%** minimum week-one requirement; net profit of **370** [7] |
| **Managed Campaign: Trade 6** | TLT ETF, Cash Secured Put, April 4th trade cut short to March 21st [7] | Truncated trade; net profit of **just \$250** [7] |
| **Managed Campaign Totals & Contrast** | TLT ETF, Managed 6-trade campaign vs Unmanaged [7] | Managed campaign final profit of **\$3,050 **⚠unverified** (absent from transcript in any spoken form) (absent from transcript in any spoken form)**; generated **25%** more profit than the unmanaged technique [7] |

### [EYA6mxeZmzg] How to Make $1,000/month owning certain dividend stocks (and options) (27,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: **UPS stock (United Parcel Service)**. The strategy is designed to perform best on solid, long-term high-yield dividend stocks that have experienced some recent sell-off [1].
*   **Structure**: **Covered Call** (owning stock and selling 1 call contract for each 100 shares owned) [2].
*   **Strikes/Deltas**: Select out-of-the-money call options located as high as possible on the options chain that yield a premium price of **at least 90 cents** to meet the monthly income target [2, 3].
    *   *Month 1*: **136 strike** call option (with stock closing at **13.58** [garbled/as spoken] on August 1st) [1, 2].
    *   *Month 2*: **136 strike** call option [4].
    *   *Month 3*: **145 strike** call option [4].
*   **DTE (Days to Expiration)**: Approximately **one month** (e.g., August 30th options chain [2]; October 4th options chain expiring in **35 days** [3]; November 1st options chain expiring in **about 30 more days** [4]).
*   **Entry Trigger**: Continuous monthly execution targeting a specific monthly portfolio cash goal (e.g., **\$1,000 a month**) by combining quarterly dividend cash flows with monthly call premiums [5, 6]. Stock selection prioritizes companies with consistent histories of dividend growth, such as UPS (which raised its dividend for **22 years in a row**) [6].

### Management and Exit Rules
*   **Expiration worthless**: If the stock closes below the sold call strike price at expiration, the calls expire worthless with zero value [7]. The trader simply pockets the upfront premium cash flow as net profit and re-opens a new covered call position about a month out [3, 7].
*   **Broker requirements**: The trader must hold the physical shares of stock in the account so the broker can deliver them to the call buyer should the call buyer choose to exercise the options at the strike price [8].
*   **Protection against losses**: Never sell covered calls at a strike price lower than the initial acquisition cost basis of the stock [9]. This avoids being assigned and forced to sell the shares below cost, which would permanently lock in a realized capital loss on the shares [9].

### Stated Edge or Statistics
*   **Income Enhancement**: Combining naturally modest dividend yields with monthly covered call premium payments allows investors to achieve monthly cash goals much faster [5].
*   **Campaign Metrics**: On an initial holding of **700 shares** of UPS valued at **\$92,700 **⚠inferred** (transcript garbled: "worth $927"; 700 sh × ~$132)** [6]:
    *   *Dividend income*: A dividend of **a163** (garbled/as spoken) per share [6] paid out **\$1,141** quarterly, translating to roughly **\$380 per month** [6].
    *   *The Shortfall*: To reach a **\$1,000 monthly goal**, the portfolio faced a **\$620 monthly shortfall** [6].
    *   *Premiums captured*: Selling 7 contracts yielded **\$665** in Month 1 (expiring worthless with UPS at **12855** [garbled/as spoken]) [2, 7], **\$644** in Month 2 (expiring worthless with UPS at **13125** [garbled/as spoken]) [4], and **\$784** in Month 3 (expiring worthless with UPS at **13405** [garbled/as spoken]) [4].
    *   *Total return*: The campaign generated a total of **\$3,234** in 3 months (premiums plus the dividend payment), averaging **\$1,078 per month** and successfully exceeding the monthly cash target [8].

### Caveats
*   **Upside Cap**: If the stock rallies dramatically past the call strike, the shares are called away, capping the stock's capital gains potential [8].
*   **Unprotected Downside**: If the underlying stock drops significantly, the capital loss on the stock will normally be much greater than the monthly income earned from selling calls [9].
*   **The Loss-Locking Trap**: If the stock drops too much, the investor might be forced to sell covered calls below their initial acquisition price to meet monthly income needs, exposing them to a realized capital loss if the stock rallies back above the strike [9].

***

### PART B — Spoken Numbers Table

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Portfolio Goal & Target** | Covered call & dividend campaign, cash income focus | Target cash income: **\$1,000 a month** or more [5, 6] |
| **Share Baseline & Sizing** | UPS stock shares owned as of August 1st close | August 1st close: **13.58** (garbled/as spoken) [1]; **700 shares** owned [6]; total value: **\$92,700 **⚠inferred** (transcript garbled: "worth $927"; 700 sh × ~$132)** [6]; raised dividend for **22 years** in a row [6]; dividend aristocrat benchmark: **at least 25 straight years** [6]; dividend issued May 10th: **a163** (garbled/as spoken) per share [6] |
| **Portfolio Cash Shortfall** | UPS stock quarterly dividend vs. monthly cash goal | Total quarterly dividend collected: **\$1,141** [6]; monthly average: **roughly \$380** per month [6]; monthly shortfall: **\$620** [6] |
| **Month 1 Covered Call Entry** | UPS Stock, covered call. Owned 700 shares, sold 7 calls at 136 strike. August 1st entry, August 30th expiry. | Price target: **at least 90** cents [2]; call priced at: **95** cents [2]; contract size: **100 shares** per contract [2]; sold: **seven** calls [2]; cash inflow: **\$665** [7]; monthly shortfall: **\$620** [7] |
| **Month 1 Expiration & P&L** | UPS Stock, covered call at August 30th expiration | Expiration close: **12855** (garbled/as spoken) [7]; calls expired worthless; net profit: **\$665** [7] |
| **Dividend Payment Event** | UPS stock quarterly dividend payout | Paid August 19th [3]; collected: **\$1,141** arising from **700 shares** [3] |
| **Month 2 Covered Call Entry** | UPS Stock, covered call. Owned 700 shares, sold 7 of the 136 calls expiring October 4th. | Oct 4th chain duration: **expires in 35 days** [3]; call premium priced at: **92** cents [4]; cash produced: **\$644** [4] |
| **Month 2 Expiration & P&L** | UPS Stock, covered call at October 4th expiration | Expiration close: **13125** (garbled/as spoken) [4]; calls expired worthless; net profit: **\$644** [4] |
| **Month 3 Covered Call Entry** | UPS Stock, covered call. Owned 700 shares, sold 7 of the 145 calls expiring November 1st. | November 1st chain duration: **expires in about 30 more days** [4]; call premium priced at: **a112** (garbled/as spoken) [4]; positive cash flow: **\$784** [4] |
| **Month 3 Expiration & P&L** | UPS Stock, covered call at November 1st expiration | Expiration close: **13405** (garbled/as spoken) [4]; calls expired worthless; net profit: **\$784** [4] |
| **3-Month Campaign Totals** | UPS Stock, total collected over 3 months | Total collected: **\$3,234** [8]; average monthly cash flow: **\$1,078 per month** [8] |

### [BPvBoQLupOQ] Huge Options Blunders: If I think A Stock Is Going Up, I’ll Just Buy A Call, It’s Cheaper (ep 8) (26,000 views)

PART A — handbook chapter content: "Huge Options Blunders: If I think A Stock Is Going Up, I’ll Just Buy A Call, It’s Cheaper (ep 8)"

### Setup
*   **Instruments**: Chipotle Mexican Grill (CMG) stock [1] (also illustrated with a hypothetical XYZ stock example) [2].
*   **Structure**: Long Call option (buying an out-of-the-money call option) [2, 3].
*   **Strikes/Deltas**: 
    *   *CMG*: **860 strike** call option, which is located **about 10 points** above CMG's all-time high [1]. 
    *   *XYZ*: **105 strike** call option, when the stock is trading at **100** [2].
    *   *Deltas*: Not explicitly stated in the transcript for this video.
*   **DTE (Days to Expiration)**: 
    *   *CMG*: Expiring in the first week of the new year on **January 3rd** [1]. 
    *   *XYZ*: Expiring **30 days out** [2].
*   **Entry Trigger**: Directional price confirmation. The trade is initiated when a speculator develops a highly bullish directional opinion that a stock will rally significantly and blast through its previous all-time highs [1].

### Management and Exit Rules
*   **Expiration worthless**: If the stock's closing price is at or below the call option strike price on expiration day, the option expires completely worthless [2]. The option seller pockets the premium, and the option buyer suffers a **100% loss of their premium capital** [3].
*   **In-the-Money Expiration Exercise**: If the stock closes above the short strike price on expiration day, the call option buyer is assigned the shares and can flip them immediately in the open market at the higher trading price to capture a profit [3, 4].
*   **The Profit Hurdle Rule**: To generate a net profit, the stock's closing price must exceed the strike price by **at least the cost of the option itself** [4]. If it does not, the speculator will lose money on the transaction even if they timed the move perfectly and correctly predicted the direction and magnitude of the stock's advance [2, 4].

### Stated Edge or Statistics
*   **The Leverage Illusion**: Speculating with long calls offers spectacular theoretical returns on small capital compared to buying equities outright [1, 3]. 
    *   *CMG Stock Purchase Return*: Buying **100 shares** of CMG at **810** requires an investment of roughly **81 thousand dollars** [1]. If the stock rallies to **900** by January 3rd, selling the shares yields a profit of **90 thousand dollars** (a **10.2 percent return**) [1].
    *   *CMG Call Option Return*: Buying the **860 strike call** for **666 dollars** [1]. If the stock rallies to **900**, exercising at 860 and flipping them "1 second later" for 900 yields a **\$40 per share** profit on **100 shares**—netting **\$4,000 in total** (over a **500 percent gain** on the option cost) [1].
*   **Net Selling Reality**: While buying calls can be used strategically at the right time, the team at SMB prefers acting as net options sellers who collect options time premium, taking advantage of the high probability that out-of-the-money options will decay to zero [5].

### Caveats
*   **The "Technical Genius" Trap**: It is a common blunder to brilliantly time the direction, magnitude, and timeframe of a stock move and still lose money on the option [2, 4]. For example, if CMG rallies to **865** (exceeding the **860 strike** target by **five points**), the trader is assigned and makes **500 dollars** on the share flip, but because they paid **666 dollars** (spoken as "paid 666 dollars for the shares"), they still realize a net loss on the trade [4].
*   **A Decaying Asset**: Unlike equities where a trader only has to be right about the stock's direction, options require being right about direction, magnitude, *and* timing before time decay erodes the option's value [4, 6].

***

PART B — Spoken Numbers Table

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Series Context** | Huge Options Trading Blunders series | Episode "**8**" (8th) in a "**10**" part series (contextual) [7] |
| **XYZ Baseline Stock** | XYZ Stock, purchase | Stock trading at "**100**" [2] |
| **XYZ Call Option Pricing** | XYZ Stock, Long Call, 105 strike, 30-day options chain | Option costs "**80 cents**" per share; total cost to buyer is "**\$80**" [2, 3]; represents the right to buy "**100**" shares; buy cost calculated as "**100**" times "**80 cents**" which is "**\$80**" [3] |
| **XYZ Option Expiration (Worthless)** | XYZ Stock, Long Call, 105 strike, 30 days to expiration | Option expires after "**30**" days; stock closes at "**105 or less**"; buyer loses "**\$80**"; seller pockets "**\$80**" [3] |
| **XYZ Option Expiration (In-the-Money)** | XYZ Stock, Long Call, 105 strike, 30 days to expiration | Stock trades up to "**107**"; seller required to sell shares to buyer for "**105**" even though trading at "**107**"; buyer paid "**80 cents**" for the option [3] |
| **Blunder #8 Definition** | Options vs. Equities structural comparison | Blunder "**8**" [2, 3]; buying a call is considered cheaper than buying "**100**" shares of stock [3] |
| **CMG Target speculation** | Chipotle Mexican Grill (CMG) stock or options, expiring January 3rd | Speculator targets stock to get to "**700**" (or "**900**") by "**January 3rd**" [1] |
| **CMG Option Setup** | CMG Stock, Long Call, 860 strike, expiring January 3rd | Option strike is "**860**", which is "**about 10 points**" above all-time highs; sold for "**six dollars and sixty six cents**" (\$6.66) per contract; total purchase cost is "**666 dollars**" to control "**100**" shares [1] |
| **CMG Stock Purchase Comparison** | CMG Stock, outright purchase of 100 shares held until January 3rd | Shelled out roughly "**81 thousand dollars**" for "**100**" shares; sell them for "**90 thousand dollars**" on "**January 3rd**"; return is "**10 point 2 percent**" if correct [1] |
| **CMG Best-Case Call Option Payoff** | CMG Stock, Long Call, 860 strike, expiring January 3rd | Option purchased for "**666 dollars**"; right to buy at "**860**" when trading at "**900 dollars**"; sell "**1 second**" later for "**900 dollars**" for a "**\$40**" per share profit on "**100**" shares; total profit: "**\$4,000**" (representing "**over a 500 percent**" gain) [1] |
| **CMG Actual Expiration & Options Loss** | CMG Stock, Long Call, 860 strike, expiring January 3rd | Stock exceeded target by "**five**" points (closing at 865); call entitles to "**100**" shares; flipped immediately for "**865 dollars per share**" after buying them for "**860 per share**"; made "**500 dollars**" from selling shares; paid "**666 dollars for the shares**" (spoken error for option premium); transaction resulted in a net loss [4] |

***

📊 I can turn this options pricing math into a custom visual payoff diagram comparing stock ownership to call options at expiration so you can easily analyze the exact breakeven curves.

### [KBWUtGD1kwk] The Hidden Key that Makes Options Trading Profitable (26,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: **Amazon (AMZN) stock**.
*   **Structure**: This strategy utilizes **implied volatility spikes** as the "secret sauce" to execute three core structures:
    1.  **Cash-Secured Put**: Selling a single out-of-the-money put at a multi-year low strike price.
    2.  **Put Credit Spread**: Selling a put option and simultaneously buying a protective put option at a lower strike price (e.g., five strikes lower) to define risk.
    3.  **Iron Condor**: Surrounding the market price by combining a put credit spread below the market and a call credit spread above the market (e.g., short strikes at 145 and 190).
*   **Strikes/Deltas**: 
    *   *Short Put strike*: Set deep out of the money at a multi-year low support level, specifically the **145 put** strike (when the stock is trading at 16732). 
    *   *Protective Put strike*: Set at the **120 put** strike.
    *   *Short Call strike*: Set above the market at the **190 call** strike.
*   **DTE (Days to Expiration)**: Long-term duration expiring "a little less than a year later," specifically **333 days later** (on March 20th, 2026).
*   **Entry Trigger**: A massive **spike in the VIX index** (the fear index). Professional traders enter these positions when fear pumps up options premiums to extreme overvalued levels, such as when VIX jumps to **33.82 82** (representing a **14% increase** in a single day) following major geopolitical trade war/tariff announcements.

### Management and Exit Rules
*   **Expiration Worthless**: Puts are only activated if the stock closes below the strike on expiration day. If the underlying stock remains above the short strike, the options expire completely worthless, and the seller retains the entire upfront positive cash flow as pure net profit.
*   **Capital Allocation**: For cash-secured puts, the trader must maintain sufficient cash in the account to purchase **100 shares of Amazon at 145** per contract sold (tying up **145** in capital).
*   **Spread Risk Definition**: By purchasing a protective put at a lower strike (e.g., 120 put), the trader defines their maximum loss. The broker recognizes this stop-loss protection, which drastically reduces the capital margin requirement to **\$1,877** instead of the full cash-secured requirement.
*   **Condor Range Management**: If the stock closes within the range of all options (between the short put 145 and short call 190), all four options expire worthless. The trader pockets the maximum gain of **\$1,385**.

### Stated Edge or Statistics
*   **Volatility Premium Edge**: Implied volatility tends to overestimate the actual realized movement of the stock. Spikes in fear allow premium sellers to collect dramatically higher credits.
*   **Yield Comparison (High vs. Low Volatility)**:
    *   *Cash-Secured Put*: In a high VIX environment (VIX of 33.82 82), selling the 145 put for **\$198** yields a **8.26%** return on capital. In a low VIX environment (VIX in the 15 to 20 range), the same 145 put sells for only **808**, significantly decreasing the yield.
    *   *Put Credit Spread*: Selling the 145 put and buying the 120 put for **120** in high volatility drops cash flow to **623** but yields a **33.1%** return on a small capital requirement of **\$1,877**.
    *   *Iron Condor*: Surrounding Amazon between 145 and 190 in high volatility generates **\$1,385** in premium for a best-case return of **124.2%** against a capital requirement of **,5** (garbled). In low volatility, the same condor yields only **\$1,158** in premium and a smaller **86.9%** potential return. The high-volatility condor offers a **42.9% better** potential return.

### Caveats
*   **Extreme Downside Exposure**: For cash-secured puts, a massive down move below the short strike forces the trader to buy the shares at the strike price, incurring significant unrealized paper losses on the equity.
*   **Defined Risk Expiration**: With spreads, if the market moves aggressively past the short strikes, the trade will realize a maximum loss, which can occur much faster if there is a rapid market drop before expiration.
*   **Increased Risk in Volatility**: High VIX environment premiums are inflated precisely because the market is pricing in a higher expectation of large, violent swings, making the probability of a strike being breached higher.

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Firm History** | N/A | Founded "since 2005" |
| **Volatility Context (Low Vol)** | N/A | VIX living in "15 to 20 range" for the first "two months of the year" |
| **Volatility Event (High Vol)** | S&P Index, April 21st | S&P closed at "5158.20" down "124 points"; VIX closed at "33.82 82" (representing a "14%" increase over Friday close) |
| **Asset Baseline (High Vol)** | Amazon (AMZN) Stock, April 21st | Amazon rallied from "145" in "early January of 2024"; closed at "16732" on April 21st |
| **Cash-Secured Put (High Vol)** | AMZN, Cash-Secured Put, 145 strike put, March 20th 2026 expiration | Option expiration "333 days later" (about a year); sold put at "price of \$198" collecting "\$1,198" or "1198 of cash flow"; capital requirement: must come up with "145" (if stock closes below 145); yield on capital: "8.26%" ("8.26% 26%") |
| **Cash-Secured Put (Low Vol)** | AMZN, Cash-Secured Put, 145 strike put, February 20th 2024 entry | Put option sold for "808" in lower volatility environment |
| **Put Credit Spread (High Vol)** | AMZN, Put Credit Spread. Short 145 put, Long 120 put, March 20th 2026 | Paid for protective put "120"; net cash flow "drops to 623"; required capital margin: "\$1,877" ("\$1877"); maximum potential return: "33.1%" |
| **Iron Condor (High Vol)** | AMZN, Iron Condor. Short range between 145 and 190 strikes, March 20th 2026 | Cash flow collected: "\$1,385"; return on required capital: "124.2%" against capital of ",5" (garbled) |
| **Iron Condor (Low Vol)** | AMZN, Iron Condor. Short range between 145 and 190 strikes, February 2024 entry | Net premium collected: "\$1,158"; potential return on trade: "86.9%" |
| **Volatility Yield Edge** | High Volatility vs. Low Volatility Iron Condor comparison | High volatility Condor yields "42.9% better" return potential than the low volatility trade |

### [cUfBqD03mTc] How to TRIPLE Your Options Income (Easily) (26,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: **SPY ETF** (S&P 500 ETF).
*   **Structure**: **Short Strangle** (selling an out-of-the-money call and an out-of-the-money put) written against an existing long stock position. This setup is designed to "get paid by the market" while waiting for shares sitting on large unrealized losses to recover.
*   **Strikes/Deltas**: 
    *   **Short Call**: Strike price set slightly above the original stock purchase cost basis, specifically the **330 call** (with original stock entry at **324** and the market trading at around **275**).
    *   **Short Put**: Strike price set below the lowest close of the market crash to ensure safety, specifically the **220 put** (where the lowest crash close was **222**).
*   **DTE (Days to Expiration)**: Approximately **six months out** (specifically utilizing the September options chain on a trade entered on April 13th).
*   **Entry Trigger**: Deployed after a major market crash (such as the bear market in the **first half of 2022** or the **beginning of 2020** crash) when a trader holds underwater shares and expects a consolidation or gradual recovery bounce.

### Management and Exit Rules
*   **Holding to Expiration (Full Recovery)**: If the market rallies past the short call strike at expiration (e.g., stock is over **334** on expiration day), the puts expire worthless. The shares are automatically assigned and called away at the short call strike of **330**. The trader collects the capped stock sale proceeds plus the entire strangle premium.
*   **Early Profit Take**: If the market bounces back rapidly near all-time highs (e.g., by **August 4th**), the trader can choose to exit the stock and options early to book a smaller, modest profit (e.g., taking a **600** dollar win) rather than holding to expiration.
*   **Wiggle Room / Sideways Resolution**: If the stock remains within the wide strangle boundaries (between **220 and 330**) at expiration, both the short call and the short put expire worthless. The trader retains the entire premium and can reload by selling a new strangle to continue generating income.

### Stated Edge or Statistics
*   **Triple Income Potential**: Owning the shares and allowing them to simply recover to the **330** level yields a profit of only **600** bucks. By contrast, writing the strangle yields a final profit of **1746 dollars in total**, which is **nearly three times** the profit of a simple unhedged stock sale.
*   **Significant Cash Flow Generation**: The strangle generates substantial positive cash flow upfront to finance the hold, collecting **238** for the call option and **908** dollars for the put option, for a **total positive cash flow of 1146**.

### Caveats
*   **Capped Upside**: Selling the call option caps the stock's appreciation potential. If the stock rallies significantly past the strike price (e.g., past 330 to **334**), the investor does not participate in the gains above the call strike.
*   **Downside Put Obligation**: If the market enters a secondary severe decline and breaks below the short put strike of **220**, the trader is obligated to buy more shares at that strike price, which could lead to additional paper losses if the stock continues to drop.

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Market Correction Context** | SPY ETF broad market performance | Down "**over 10 percent**" for this calendar year following the bear market of the "**first half of 2022**" |
| **Hedged Position Entry** | SPY ETF, 100 shares purchased in the "**beginning of 2020 before the crash**" | Original stock purchase price: "**324**"; stock price at hedge entry: "**around 275**" on "**april 13th late in the afternoon**" |
| **Strangle Call Leg** | SPY ETF, September options chain ("**about six months out**"). Sold short call up at 330 (which is "**about six points**" above the original stock buy price of 324) | Call option premium: "**2.38 cents**"; contract represents "**100**" shares; positive cash flow received: "**238**" |
| **Strangle Put Leg** | SPY ETF, September options chain ("**about six months out**"). Sold put at 220 (which is below the lowest close of the crash where SPY closed at "**222 on march 23rd**") | Put option premium: "**nine dollars and eight cents**"; contract represents "**100**" shares; positive cash flow received: "**908**" dollars |
| **Upfront Strangle Cash Flow** | SPY ETF, short strangle (330 call & 220 put) | Upfront "**total positive cash flow of 1146**" |
| **Early Stock Exit Scenario** | SPY ETF, unhedged 100 shares sold early on a market bounce | Exited on "**august 4th**"; stock trading back near all-time highs; cashing out at "**330**" strike; modest win: "**600**" bucks |
| **Strangle Expiration Outcome** | SPY ETF, 100 shares + short strangle held to expiration. Stock rallies past call strike. | Stock closes "**over 334**"; receive "**33 000**" for selling shares at the "**330**" strike; put "**220**" expires worthless; subtract out "**32-4**" (original share cost); total profit: "**1746 dollars in total**" (which is "**nearly three times**" the unhedged stock profit of "**600**" bucks) |

### [-wyjzl9zPfs] The Top 3 Options Trading Strategies That Anyone Can Learn (25,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: S&P 500 Index (SPX) [1, 2].
*   **Structure**: 
    *   *Strategy 1*: **Put Credit Spread** (selling a put close to the market and simultaneously buying a further out-of-the-money put) [1].
    *   *Strategy 2*: **Call Credit Spread** (selling a call close to the market and simultaneously buying a further out-of-the-money call) [3].
    *   *Strategy 3*: **Iron Condor** (a combination of a put credit spread below the market and a call credit spread above the market) [4].
*   **Strikes/Deltas**:
    *   *Put Credit Spread*: Short put at the **4750 strike** (selected as the closest strike to a **20 Delta**), protected by a long put at the **4700 put** strike (**50 points below**) [1].
    *   *Call Credit Spread*: Short call at the **6250 strike** (selected at an **18.9 Delta**, which is closest to a **20 Delta** and located **more than 160 points above** the index price); protected by a long call at the **6300 strike** (**50 points above**) [3].
    *   *Iron Condor*: The call side consists of the **6150 and 6200 calls** [2]. The put side is located **quite a bit below** the market [2]. Shorts are systematically located around **20 Deltas** [4].
*   **DTE (Days to Expiration)**: Approximately **one month** (e.g., September 6th options chain for the put spread [1]; December 2nd to January 3rd, 2025 for the call spread [3]; Iron Condor expiring in **just a month** [2]).
*   **Entry Trigger**: Directional and range-bound signals utilizing momentum indicators. A common trigger is the **RSI indicator** (RSI reading **under 30** indicates oversold conditions ripe for a bullish put credit spread [1, 5]; RSI reading **above 70** indicates overbought conditions ripe for a bearish call credit spread [3, 5]; listless, range-bound, or channeling market environments are ideal for the Iron Condor [4, 5]).

### Management and Exit Rules
*   **Expiration Worthless**: The primary objective is to allow all short options to expire out of the money. If the index settles below the call strikes or above the put strikes at expiration, the options expire worthless, allowing the trader to keep the entire initial premium as pure profit [2, 4].
*   **Risk Capping**: Buying the further out-of-the-money put (e.g., 4700 put) or call (e.g., 6300 call) serves as insurance to define the maximum loss before the trade is ever entered [1, 3].
*   **Margin Efficiency (Iron Condor Advantage)**: Because the market cannot simultaneously expire above the call strikes and below the put strikes, the broker requires less capital margin to hold an Iron Condor than the two credit spreads separately [2]. This reduction in the capital denominator dramatically increases the percentage return on capital [2].

### Stated Edge or Statistics
*   **Statistical Margin of Safety**: Locating short options at **20 Deltas** provides a very high mathematical probability of success, as there is an **80% statistical likelihood** that the options will expire completely worthless [1, 4].
*   **Strategy 2 Performance**: The December call credit spread yielded a net profit of **\$725** in initial cash flow, representing a **16.9% return** [4].
*   **Strategy 3 Performance**: The monthly Iron Condor achieved an impressive **46.4% return** when the SPX settled at **6061** at expiration, causing the 6150/6200 calls and the puts to all expire completely worthless [2].

### Caveats
*   **Complexity Misconception**: Traders are often falsely intimidated by options, believing they need a "doctorate degree" to execute these high-probability structures [6, 7].
*   **Capped Returns**: High-probability credit spreads trade off massive directional gains for consistent, capped income [2]. 
*   **Probability is Not Certainty**: High probability represents an edge over a large sample of trades, not a guarantee on any single trade [4].

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Firm History** | SMB Capital firm overview | Founded since **2005** |
| **Strategy General Scope** | Easiest option strategies for beginners | **Top 3** easiest option strategies |
| **Indicator Benchmarks** | RSI momentum indicator overbought/oversold levels | Overbought: **above 70**; Oversold: **under 30** |
| **Strategy 1: Put Credit Spread** | S&P 500 Index (SPX), Put Credit Spread, Sept 6th expiry (about a month out) | Short strike: **4750 put**; Short premium credit: **6965**; Long strike: **4700 put** (positioned **50 points below**); Long premium debit: **5975**; Target Delta: **20 Delta** (also spoken as **20 Deltas**) |
| **Strategy 2: Call Credit Spread Entry** | S&P 500 Index (SPX), Call Credit Spread, entered Dec 2nd 2024, expiring Jan 3rd 2025 | S&P 500 index close: **60 8649** (as spoken); Target Delta: **20 Delta**; Short strike: **6250 call** with a Delta of **18.9** (located **more than 160 points above** the index); Short premium credit: **1540**; Long strike: **6300 call** (positioned **50 points above**) |
| **Strategy 2: Call Credit Spread P&L** | S&P 500 Index (SPX), Call Credit Spread campaign outcome | Net profit / initial cash flow: **\$725**; Return on capital: **16.9% return**; Target Delta: **20 Deltas** |
| **Strategy 3: Iron Condor Expiration** | S&P 500 Index (SPX), Iron Condor expiring in **just a month**, entered shortly after Jan 6th | Call side options strikes: **6150 and 6200 calls**; SPX closing price: **6061**; Worthless options: **all four options**; Return on capital: **46.4% return** |

### [VDYG8LDIfGk] How to Generate Income With High Yield Stocks (Options Tutorial) (25,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: Altria (trading symbol: **MO**), a consistently high-yielding cigarette stock [1].
*   **Structure**: Covered call position, which involves buying shares of stock and simultaneously selling call options of the same stock [2].
*   **Strikes/Deltas**: 
    *   **Short Call Strike**: Set slightly above the stock price, specifically the **45 strike** for the initial trade [1].
    *   **March Roll Strike**: Short March calls set at the **45 strike** [3].
    *   **June Roll Strike**: Short June calls set at the **45 strike** [3].
    *   *Deltas*: Not explicitly stated in the transcript for this video.
*   **DTE (Days to Expiration)**: Expiring about **four months later** (specifically, the November options chain entered on **July 22nd, 2022**) [1].
*   **Entry Trigger**: Strategic cash generation on high-yield stocks in a falling interest rate environment, specifically when the Fed signals cutting interest rates and money market fund yields (previously over **5%** with close to no risk) are coming to an end [4]. It is deployed when a high-yielding dividend stock has experienced a pullback, such as when MO rallied to **57** in the first **five** months of 2022, but dropped to around **43** by July [1].

### Management and Exit Rules
*   **Dividend Collection**: Hold the underlying shares (1,000 shares) to collect the quarterly dividend of **94 cents** per share [1, 5].
*   **Assignment Protection Roll Rule**: If the stock trades above the call strike near expiration (e.g., MO trading around **46** just before March calls expire), execute a roll to prevent assignment and maintain the campaign [3]. Close the short March calls by buying them back at a price of **a122** (garbled/as written) and simultaneously sell calls expiring in June at the **45 strike** for **233** (garbled/as written) [3].
*   **Stock Ownership Requirement**: The short calls are fully covered by the physical ownership of **1,000 shares** of stock, with each contract representing **100** shares [2, 5].

### Stated Edge or Statistics
*   **Yield Supercharging**: Covered calls can boost returns to capture up to **24%** in a single year compared to low single-digit returns [6].
*   **Campaign Outperformance**: Over a one-year campaign, the traditional dividend collection approach (inclusive of capital gains) yielded a return of **11.3%** [7]. Under the covered call approach, the total return skyrockets to 10 points higher, achieving a fantastic **21.5%** return [7].
*   **Upfront Positive Cash Flow**: Entering the position brings in an upfront credit of **\$1,490** from selling 10 calls at **a149** (garbled/as written), offsetting the initial stock purchase cost of **\$42,988** (buying 1,000 shares at **42.98** per share) [1, 2, 5].

### Caveats
*   **Uncertain Interest Rate Regime**: Deployed specifically because of shifting yields as the Fed cuts interest rates, ending easy yield on cash [4].
*   **Capital Risk**: Buying shares of stock still carries standard equity downside risk, though partially buffered by the options premium [2].
*   **Clerical Discrepancies**: Transcribed values contain obvious numerical errors and garbles, such as stating a quarterly dividend payment of 94 cents per share on 1,000 shares resulted in a cash deposit of "94" (garbled/truncated) [5], and citing the total campaign profit of the covered call strategy as only "\$926" (garbled/truncated) for the entire campaign [7].

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Covered Call Annual Potential** | High-yield covered call campaign, 1-year duration | Return of up to **24%** in a single year [6] |
| **Proprietary Firm History** | Firm foundation and performance | Founded since **2005** [6]; developed "**seven**" and even "**e (garbled)**" figure per year traders [6] |
| **Interest Rate Baseline** | Money market fund interest rates | Get over **5%** with close to no risk [4] |
| **Asset Dividend Rate** | Altria (MO) quarterly dividend (2022) | Paying a dividend of **94 cents** a share every quarter [1] |
| **Stock Pullback Context** | Altria (MO) stock performance tracking (2022) | Rallied in the first "**five**" months [1]; reached as high as **57** at "**one**" point [1]; dropped to around **43** by July [1] |
| **Initial Stock Purchase** | Altria (MO) stock purchase, July 22nd | Bought "**1,000**" shares for **42.98** per share [1]; total cost: **\$42,988** [2] |
| **Initial Option Sale** | Altria (MO) short call, November expiration (about four months later), July 22nd | Sold "**10**" calls at the **45** strike price [1]; sold at a price of "**a149 (garbled)**" [1] / "**a do 49 (garbled)**" [2, 5]; contract represents **100** shares of stock [2, 5]; received total cash premium: **\$1,490** [2, 5] |
| **First Dividend Payout** | Altria (MO) stock quarterly dividend, paid October 11th | Paid **94 cents** (implied); resulted in a cash deposit of "**94 (garbled/truncated)**" [5] |
| **Second Dividend Payout** | Altria (MO) stock quarterly dividend, paid January 10th | Cash deposit of **\$940** [3] |
| **March Position Roll (Buyback)** | Altria (MO) short March call, closed near expiration | Stock trading at around **46** [3]; closed short March **45** calls [3]; buyback price: **a122 (garbled)** [3] |
| **March Position Roll (Sale)** | Altria (MO) short June call, opened near March expiration | Sold June **45** calls [3]; premium credit: **233 (garbled)** [3] |
| **Campaign Totals** | Altria (MO) covered call campaign total yield | Total of "**\$926 (garbled/truncated)**" for the entire campaign [7] |
| **Campaign Performance Compare** | Traditional dividend collection vs. Covered call approach, 1-year duration | Traditional return: **11.3%** [7]; covered call return: **21.5%** [7]; return skyrockets to **10** points higher [7] |
| **Workshop Training** | Webinar options strategies | Teaches **three** more option strategies [8] |

### [YVPcw-xIUhs] Before Trading Options You Need to Learn This (Greeks for Beginners) (25,000 views)

PART A — handbook chapter content

### Setup
*   **Instrument**: **Meta stock** [1, 2].
*   **Structure**: 
    *   **Long Call**: A bullish directional trade structured by buying an at-the-money call option [3, 4].
    *   **Cash-Secured Put**: A high-probability premium-selling strategy where a trader sells an out-of-the-money put option to collect premium, intending for it to expire worthless while maintaining the obligation to buy the shares at the strike price if it is breached [2].
*   **Strikes/Deltas**:
    *   *Long Call*: The at-the-money **680 call** strike (closest available option to a **60 Delta**, with an actual delta of **61.48**) [4].
    *   *Cash-Secured Put*: The out-of-the-money **470 put** strike (additionally referred to in context as the "**475 price**") selected at a **30 Delta** [2, 5].
*   **DTE (Days to Expiration)**:
    *   *Long Call*: Approximately **one year** (expires on **June 18th, 2026** on a trade entered on Monday, June 23rd) [1, 4].
    *   *Cash-Secured Put*: Entered on June 24th, 2024 (exact DTE to expiration not specified) [2].
*   **Entry Trigger**:
    *   *Long Call*: A highly bullish directional viewpoint where the trader expects the stock to rise [3].
    *   *Cash-Secured Put*: A bullish but conservative outlook where the trader wants a safety buffer ("room for error") [2]. The entry is made by choosing a **30 Delta** strike, which mathematically yields a high probability of expiring out-of-the-money [2, 5].

### Management and Exit Rules
*   **The Profit Hurdle for Buyers**: To realize a net profit on a long call, the underlying stock price must rise above the strike price by **at least the cost of the option premium** [3, 6]. Otherwise, options pricing variables can cause the trader to lose money on the call even if the stock goes up [3, 7].
*   **Put Expiration worthless**: If the stock closes above the short put strike at expiration, the put expires completely worthless, leaving the option seller with **100% of the upfront premium** as net profit [2, 5].
*   **Assignment Obligation**: If the stock closes below the put strike on expiration day, the put seller is assigned the shares and is obligated to purchase the stock at the strike price [2].
*   **Time Decay Capture**: Options income traders manage positions to capture **Theta (time decay)**, which is their "best friend" [8]. The core technique is to hold short options to profit as the premium decays and the option value falls over time [8].
*   **Gamma Monitoring**: Gamma acts as the "**gas pedal**" of Delta [5]. When Gamma is high, the option's Delta will increase or decrease quickly as the stock price moves, rapidly changing the trade's directional exposure [5].

### Stated Edge or Statistics
*   **Delta as Probability of Expiration**: Options Delta is mathematically utilized as a close approximation of the probability that the option will expire in-the-money [2].
    *   A **30 Delta option** possesses a **30% statistical chance** of expiring in-the-money, giving the put seller a **70% probability** that the option will expire completely worthless to secure a win [2, 5].
*   **Predictability of Theta**: Time decay is highly modeled and mathematically predictable [8]. For instance, Theta calculations predict that **7 days** passing at **21 cents a day** of decay will reduce an option's premium value by **\$147** (dropping a model-predicted price of **653** to an actual market price of **650**) [8].

### Caveats
*   **The Directional Option Trap**: Trading options purely based on a directional thesis without understanding the Greeks is highly dangerous [3, 9]. A trader can be correct on direction (the stock rises after buying a call, or falls after buying a put) and still lose money anyway due to the unchecked drag of time decay (Theta) or volatility changes (Vega) [3].
*   **Delta is Dynamic**: Delta is not a constant number [5]. It shifts continuously as the stock price moves—accelerated by Gamma—which means the trade's directional risk and probability of expiring in-the-money fluctuate constantly [5].

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Professional Performance** | SMB proprietary trading desk overview | Desk houses numerous "**seven**" and even "**eight**" figure per year traders [9] |
| **At-the-Money Long Call Entry** | Meta stock, Long Call, 680 strike, expires June 18th 2026. Entered Monday, June 23rd. | Meta stock open price: "**68030**" (spoken/as written); strike: "**680 call**" (at-the-money); target Delta: "**60 delta**"; actual Delta: "**61.48**"; call option premium price: "**10977**" (spoken/as written) [1, 4] |
| **Cash-Secured Put Entry** | Meta stock, Cash-Secured Put, 470 put strike (referred to as "475 price" as spoken). Entered June 24th 2024. | Meta stock trading price: "**50326**" (spoken/as written); strike: "**470 put**" with "**30 delta**"; "**475 price**" (as spoken) is "**more than 33 points**" below where Meta is trading; probability of expiring in-the-money: "**30% chance**"; probability of expiring worthless (win rate): "**70% chance**" [2, 5] |
| **Theta Decay Model** | Option time-decay prediction example (Theta) | Time elapsed: "**7 days**"; daily time decay rate: "**21 cents a day**"; total time decay value: "**\$147**"; model-predicted final price: "**653**"; actual final market price: "**650**" [8] |
| **Delta Movement Basis** | General option delta definition | Underlying stock price move of "**exactly one point**" [1] |
| **The Greeks Overview** | Four major Greeks | "**four major Greeks**" / "**big four Greeks**" (Delta, Gamma, Theta, Vega) [1, 8] |

***

📊 I can turn this options pricing math into a custom visual payoff diagram comparing stock ownership to call options at expiration so you can easily analyze the exact breakeven curves.

### [xDaCtZ9GMl0] Top 3 Options Strategies to Catch Reversals (25,000 views)

PART A — Handbook Chapter Content

### Setup
*   **Instrument**: Tech-heavy NASDAQ 100 Index (NDX).
*   **Structure**: This reversal strategy covers three distinct options structures:
    1.  **High-Probability Put Credit Spread**: A conservative defined-risk play consisting of a short out-of-the-money put and a lower-strike long protective put [1].
    2.  **Modified Risk Reversal**: A highly bullish, asymmetric structure combining a put credit spread below the market with a long out-of-the-money call option expiring in the same month [2, 3].
    3.  **Out-of-the-Money Long Call**: A simple, highly leveraged directional bet consisting of a single long out-of-the-money call option [4].
*   **Strikes/Deltas**:
    *   *High-Probability Put Credit Spread*: Short put at a **20 Delta** (specifically the **16200 put** strike), protected by a long put at the **16025 put** strike (positioned over 800 points below the index's trading level) [1].
    *   *Modified Risk Reversal*: Short put set near the money at a **44 Delta** (the **17325 strike**), a long protective put 150 points lower at the **1717 strike** (also referred to as **17175**), and a long call at the **19300 strike** (selected because its premium is slightly less than the credit generated by the put spread) [2, 3].
    *   *Simple Long Call*: Bought at a **20 Delta** (specifically the **18650 call** strike) [4].
*   **DTE (Days to Expiration)**: Entered approximately **two months out** (specifically utilizing the **June 21st** options chain) [1].
*   **Entry Trigger**: Technical chart oversold signal, specifically when the **RSI indicator hits 30 or below** on daily charts, indicating the intense tech sell-off is near its end [5, 6].

### Management and Exit Rules
*   **Holding to Expiration**: Positions are designed to run to expiration to capture full value decay or structural payoffs [7].
*   **High-Probability Credit Spread Resolution**: If the index closes above the short put strike at expiration, all options expire worthless, and the trader retains the net credit collected at entry [7].
*   **Modified Risk Reversal Multi-Scenario Outcomes**:
    *   *Sideways / Modest Move*: If the market consolidates and settles between the short put strike (**17375** / **17325**) and the long call strike (**19300**), all options expire completely worthless. The trader walks away keeping the net cash credit (e.g., **\$690**) [7].
    *   *Upside Reversal (Best-Case Payoff)*: If the index rallies aggressively past the long call strike, the puts expire worthless and the long call pays off in cash at a rate of **\$100 per point** above the **19300 strike** [7].
*   **Simple Long Call Resolution**: Hold the option to capture explosive upside. If the market fails to rally past the strike price, the call expires worthless, resulting in a **100% loss of the premium paid** [4].

### Stated Edge or Statistics
*   **Statistical Cushion**: Out-of-the-money options at **20 Delta** possess an **80% statistical chance** of expiring worthless, providing a very wide margin of safety [1, 4].
*   **Modified Risk Reversal Win Rate**: The near-the-money put spread leg starts with a **56% probability of success** based on the short put's **44 Delta** [2, 4].
*   **Leverage Squeeze**: Selecting high-delta options or combinations allows traders to replicate huge equity positions with massive capital efficiency. For example, the modified risk reversal yielded a massive **320% return on original capital** at expiration [7].

### Caveats
*   **Timing Difficulty**: Attempting to time the exact bottom of an intense sell-off is notoriously "very difficult" [8].
*   **Win Rate vs. Payoff Trade-Off**: The modified risk reversal has a lower statistical win probability (**56%**) compared to the **80% probability** of the 20 Delta put credit spread [2, 4].
*   **The Option Buyer's Decay Trap**: Buying out-of-the-money calls is a very low-probability trade with an **80% statistical chance of expiring completely worthless** and losing 100% of the invested premium [4].

***

PART B — Markdown Table of Spoken Numbers

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Market Sell-Off Duration** | Tech-heavy NASDAQ 100 Index (NDX) correction | Sell-off lasting for the last "**six weeks**" |
| **Correction Magnitude** | NASDAQ 100 Index (NDX) vs. Broader Market | NASDAQ 100 off "**13.6 6%**" from its highs in "**midFebruary**"; broader market off "**under 10%**" |
| **Strategy Presentation** | General overview of reversal options setups | "**three**" different strategies for playing the end of a sell-off |
| **Reversal Technical Signal** | RSI Indicator Oversold Benchmark | Reversal signaled when RSI indicator hits "**30 or below**"; occurred on "**March 10th**" |
| **Historical Reversal Baseline** | NASDAQ 100 Index (NDX) historical reference point | Entered trade "**almost a year ago**" on "**April 19th of 2024**"; index closed at "**1703765**" that day |
| **Strategy 1: Put Spread Setup** | NDX 20 Delta put credit spread, June 21st options chain | Entered "**about two months out**"; short put strike "**16200**" placed "**over 800 points below**" the index; sold short put for a price of "**\$20055**"; bought protective long put at "**16025**" strike for "**\$17,240**" (referred to as a "**20 delta**" put credit spread) |
| **Strategy 2: Put Spread Leg-In** | NDX modified risk reversal put credit spread, June expiration | Short put has a "**44 delta**" at the "**17325 strike price**"; long protective put is "**150 points below**" at the "**1717**" strike price (also referred to as "**17175**"); sold short put for "**51140**"; bought protective put for "**45270**"; trade has a "**56% chance of this trade winning**" |
| **Strategy 2: Call Option Leg-In** | NDX modified risk reversal long call, June expiration | Bought protective long call at "**19300**" strike for "**5180**" |
| **Strategy 2: Spread Cash Flow** | NDX modified risk reversal entry cash flow | Put credit spread brought in "**\$5,870**"; net credit after buying call is positive by "**\$690**" |
| **Strategy 2: Expiration Settlement** | NDX modified risk reversal expiration on June 20th | Options stopped trading on "**June 20th**"; index closed at "**1975270**" that day; index closed "**45230**" above the call's "**193**" (19300) strike price; short put strike referenced at "**17375**" |
| **Strategy 2: Expiration P&L** | NDX modified risk reversal final returns | Call payoff is "**45230* 100 or 45,230**"; total net profit is "**45,920**"; return of "**320%**" on original capital |
| **Strategy 3: Long Call Entry** | NDX long out-of-the-money call, June expiration | Bought "**20 delta call**" at the "**18650 call**" strike; "**20% likelihood**" of expiring with value; "**80% chance**" of expiring with no value |
| **Strategy 3: Long Call Expiration** | NDX long out-of-the-money call final payoff | Made "**770**"; return of "**662%**" off original risk |


## CHAPTER: NLM-extracted videos (hybrid pipeline — NotebookLM extraction, figure-gated)

> Extracted by NotebookLM from the verbatim transcript archives, then gated by `trial_verify_figures.py`: every figure below appears in the raw transcript unless marked **⚠unverified** (not found as digits or spoken words — treat as suspect until a human or Claude pass adjudicates it). Claude did not read these transcripts.

### [IedTDDpXFCw] What are realistic returns for options income trading? (24,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Russell 2000 index options [1]. The presenter explains that index options are preferred over equity options for income trading because they provide built-in diversification and do not carry the volatility risks associated with quarterly corporate earnings releases [1].
    *   **Structure**: Options income trading strategies designed to profit consistently and in a disciplined manner [1, 2].
    *   **Strikes/Deltas**: Not specifically defined in this video.
    *   **DTE (Days to Expiration)**: Not specifically defined in this video.
    *   **Entry Trigger**: Systematic and disciplined execution of backtested rules [1, 2]. The entry is not dependent on directional market prediction but is designed to trade regularly, especially in index options which remain tradable every month of the year (unlike equities, where earnings make one month out of every quarter untradable) [1].

*   **The Management and Exit Rules**:
    *   Trades must be executed strictly according to the guidelines of the backtested strategies [1].
    *   Unlike equities, options income trading on indexes avoids the risk of sudden gaps caused by individual company events (such as earnings releases or corporate governance issues) [1].
    *   The goal is consistent capital compounding by executing trades over a long-term time horizon rather than focusing on a single trade's outcome [1, 2].

*   **The Stated Edge or Statistics**:
    *   **Backtested Strategy Returns**: Based on full records from 2013 to 2018, four popular index options income strategies yielded annual returns ranging from **22% to 80% a year** [1].
    *   **Benchmark Performance**: These options returns are contrasted with the average **7% return** on equities and the "horrendously bad returns" offered by fixed-income securities [1].
    *   **Win Probability**: One of the proprietary strategies taught in the firm's workshop boasts a statistical **80% probability of profit** month in and month out [2].

*   **The Caveats the Presenter Gives**:
    *   The presenter labels the goal of making \$500 a week on a \$5,000 account (which requires a **10% weekly return**, compiling to **520% a year**) as "preposterous" [2, 3].
    *   Generating such outsized weekly returns is impossible on a consistent basis and would require taking an "enormous and irresponsible amount of risk" [2].
    *   Generally, there is a direct trade-off in options trading: the higher the potential return of a strategy, the more variable the actual results will be [1].
    *   Achieving consistent returns requires a trader to be highly "disciplined and knowledgeable" [2].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Presenter's market experience | General options desk | **10 years** (subject driving presenter crazy) [4] |
| Follower's weekly income goal | Unspecifiedoptions trade, \$5,000 account | **five hundred dollars** a week P&L [3] |
| Follower's target account size | Unspecified options trade | **five thousand dollar** trading account [3] |
| Implied daily target of follower | Unspecified options trade, \$5,000 account | **\$100** a day P&L [3] |
| Number of track-record strategies | Russell 2000 index options strategies | **four** strategies [1] |
| Track record duration | Russell 2000 index options | **five years** [1] |
| Track record calendar range | Russell 2000 index options | **2013 to 2018** [1] |
| Target index name | Russell 2000 index options | Russell **2000** index [1] |
| Equity earnings cycle | Individual stock options | every **three months** [1] |
| Equities untradable period | Individual stock options | **one month** the quarter [1] |
| Annual returns range (low end) | Russell 2000 index options strategies | **twenty two percent** a year return [1] |
| Annual returns range (high end) | Russell 2000 index options strategies | **80 percent** a year return [1] |
| Backtest time horizon | Russell 2000 index options | **five year** time horizon [1] |
| Baseline equity return benchmark | Standard equities buy-and-hold | average **7%** return on equities [1] |
| Workshop strategies count | General options income | **three** option strategies taught [2] |
| Workshop high-probability win rate | Statistical options income strategy | statistical **80 percent** probability of profit [2] |
| Follower's weekly percent return goal | Follower's \$500/week on \$5,000 account | **10%** a week return [2] |
| Follower's annualized return goal | Follower's \$500/week on \$5,000 account | **five hundred twenty percent** a year return [2] |
| Achievable returns range | SMB options desk strategies | **twenty two to eighty percent** returns [2] |

### [8y_bNYZgy1I] Stop Making Your Broker Rich Buying SPY Options (24,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 index options (SPX) instead of SPY ETF options [1, 2].
    *   **Structure**: Buying call or put options directly to express a long or bearish directional bet on the market, or buying call/put options to hedge large existing long or short stock positions [3, 4].
    *   **Strikes/Deltas**: The video does not discuss selecting strikes based on specific Deltas. For illustrative setups, the presenter uses:
        *   An SPX call option at the **3010** strike price when the SPX index is trading at **3000** [1].
        *   An SPX put option at the **2985** strike price when the SPX index is trading at **3000** [1].
    *   **DTE (Days to Expiration)**: Not explicitly defined for the setup, but the index option example describes options expiring [1, 2].
    *   **Entry Trigger**: Triggered when a day trader wants to make a long or bearish bet on the market or needs to hedge a large existing equity position [3, 4].
*   **The Management and Exit Rules**:
    *   Unlike equity options (such as SPY), index options do not involve physical share delivery; they are settled directly in cash at a rate of **\$100 per point** if they expire in-the-money [1].
    *   If the index closes at or below the strike price of a call option, or at or above the strike price of a put option, the option expires completely worthless [1].
    *   Traders can close the positions early by selling back the options rather than letting them expire [2].
*   **The Stated Edge or Statistics**:
    *   **The Commission Savings Edge**: Because the SPY ETF is worth exactly **1/10** of the point value of the SPX index, a trader can buy **1/10** of the number of SPX contracts to achieve the exact same point value and market exposure [2]. 
    *   By doing so, the trader pays only **1/10** of the round-trip commission costs compared to executing the equivalent size in SPY options [2].
*   **The Caveats the Presenter Gives**:
    *   This alternative is only logical "**as long as you're trading with enough size**" to be able to scale down the position contract count by dividing by 10 (as fractional SPX index contracts cannot be traded) [2].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Presenter's observation timeline | General options trading | **10 years** (subject driving presenter crazy) [5] |
| Free educational workshop strategies | General options income strategies | **3** solid real-world option strategies [4, 6]; statistical **80 percent** probability of profit [6, 7] |
| Equity options definition | SPY options | Represents **100** shares of stock [1] |
| Index options definition | S&P **500** index options (SPX) | Paid in cash **\$100** per point [1] |
| Hypothetical index call trade | SPX, Long Call, Strike **3010**, entered when SPX is at **3000** | SPX trading at **3000**; call strike **3010**; SPX goes to **3015**; receive **\$500** in account; call expires worthless at **3009** or lower [1] |
| Hypothetical index put trade | SPX, Long Put, Strike **2985**, entered when SPX is at **3000** | SPX trading at **3000**; put strike **2985**; market sells off to **2975**; profit of **\$1,000**; put expires worthless at **2985** or higher [1] |
| Trade value equivalence at expiration | SPY puts vs. SPX puts, expiring **for \$1 more than their worth in the market** | **for \$1 more than their worth in the market**; **100** spy puts; worth **\$10,000** at the end of the day; equivalent to **10** SPX put options; **100** spy put options (exact same value) [2] |
| SPX option round-trip commissions | 10 SPX put options | Round-trip commissions: **\$20** total; **\$10** to buy; **\$10** to sell; assuming **one dollar** per option commission [2] |
| SPY option round-trip commissions | 100 SPY put options | Round-trip commissions: **\$200** total; **100** spy options; assuming **one dollar** per option commission [2] |
| Value and commission ratio | SPY vs. SPX | SPY ETF usually worth **1/10** of the point value of the index; trade **1/10** of the number of SPX options; pay **1/10** of the commissions [2] |

### [n8BOGRwntF4] Inside an Elite Trading Firm: How to achieve 85% Accuracy (trading options) (23,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Major market index options (Seth explains that options traders have ways of trading the entire market through index options) [1].
    *   **Structure**: A systematic, rules-based options trading system based on options credit spreads (vertical spreads) [2-4]. 
    *   **Strikes/Deltas**: Not specified in this introductory video (the specific strike selection method is not disclosed in this part, although Seth notes that they do not base the system on deltas in the typical way) [2, 4, 5].
    *   **DTE (Days to Expiration)**: Not specified in this part [2].
    *   **Entry Trigger**: The IQ (InvestoQuant) adaptive ensemble signal [2, 5, 6]. This signal is a "signal of signals" developed in partnership with InvestoQuant (Scott Andrews' firm in North Carolina) [2, 3]. It is generated at the start of the cash market (9:30 AM) and predicts whether the S&P 500 will close above or below its opening price on a given day [3, 7]. The signal aligns a group of systems that analyze different market states and factors:
        *   Trend across diverse, non-optimized time horizons (including the past 3 days, 10 days, 100 days, and past year) [8].
        *   Momentum states (such as identifying strong momentum or hanging out near highs) [8].
        *   It only fires when multiple systems and indicators align [7].

*   **The Management and Exit Rules**:
    *   **No Optimization of Exits**: By design, the system excludes optimization of the exit (such as trying to optimize points, dollars, or ATR percentages for profit targets or stops based on historical performance) [8-10]. The trade simply predicts whether the market will close up or close down on a given day [8].
    *   **Performance State Adaptation**: The system employs performance inputs to dynamically adapt, ensuring the system only trades when specific market states remain profitable and meet strict performance criteria [7].
    *   **Built-in Risk Flooring**: Options credit spreads (vertical spreads) are used to build the stop automatically into the trade at initiation [11, 12]. The protective long option puts a floor on any loss and ensures the trader's drawdowns are mild [13]. This built-in stop prevents the trader from being prematurely stopped out during rapid intraday volatility before the market can revert in favor of the daily signal [12].

*   **The Stated Edge or Statistics**:
    *   **85% Accuracy**: The combined options credit spread trading system based on the IQ signal achieves an 85% win rate (highly accurate) [14-16].
    *   **Black Shirt Standard**: Earning a prestigious "black shirt" at SMB Capital requires a trader to generate over **\$2 million net** in trading profits within a single year [17, 18].
    *   **First Indicator Failure**: Seth's first coded signal (combining trend + momentum + Bollinger bands + RSI above 20%) failed miserably right out of the box in the real world despite backtesting incredibly well [19].
    *   **Rare Success Rate**: Only **1 in 100** people who try to code a signal or create a backtested system achieve long-term success [19].
    *   **Math Problem of Frequency**: Trade frequency and trade accuracy are at direct mathematical odds. Achieving high accuracy requires more context, which drastically reduces trade frequency [9].
    *   **Sample Size Limits**: Traditional indicator testing on rare setups often suffers from tiny, statistically insignificant sample sizes (such as only 100 opportunities over the past 20 years) [9].
    *   **Ensemble Development Time**: It took a couple of years to build the adaptive ensemble (a group of systems) and generate historical data for testing [20].
    *   **Seth's Live Capital Testing**: Before sharing the system with clients, it was tested on Seth's own capital ("out of sample walk forward") with "amazing success" [20].

*   **The Caveats the Presenter Gives**:
    *   **The Optimization Trap**: Relying on backtesting and optimization to identify the "best" moving average or exit target is a major trap [9, 10, 21]. These systems always fail eventually because they look backward, cherry-pick historical data, and fit curves to past noise rather than predicting forward [10, 21]. Optimization "grossly exaggerates" performance, often doubling the expected returns on paper compared to what is achievable in the real world [10].
    *   **Static Rules Shelf Life**: Coded trading rules are static by definition, meaning they have a shelf life [21, 22]. The moment rules are finalized, they begin aging and degrading because the market is not static and is always changing [22].
    *   **Edge Arbitrage**: Unlike static fields (such as medicine, where breast cancer is easily predicted using 20 stable factors), market opportunities change as soon as participants identify and trade them [22]. The edge gets "arbitraged out" over time as market behavior shifts [22].
    *   **Short-Term Data Randomness**: Testing with a small window (like six months of data) is highly susceptible to randomness [20]. Long-term backtesting and rigorous validation are required to verify a genuine edge [20].
    *   **Discretionary Trading Failure**: Discretionary trading alone, without tapping into technology, automation, alerts, and scripts, is extremely difficult, and even highly talented traders are unlikely to succeed without a technological edge [17, 23].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Target strategy win rate | Index options, IQ signal options credit spread strategy *(strikes, DTE, dates not specified)* | **85%** win rate (Accuracy) [14, 15, 24] |
| Prop firm trader earnings | Prop desk traders *(instrument, structure, strikes, DTE, dates not specified)* | **7 and 8** figure annual earnings [14, 15] |
| Video series part | Intro to the series | Part **one** [14] |
| Elite trader status milestone | SMB proprietary desk trader qualification | **\$2 million** net in trading profits for the year [17, 23] |
| Coded signal filter (Failed) | Trend, momentum, Bollinger bands, RSI indicator setup *(strikes, DTE, dates not specified)* | RSI was at a certain level above **20%** [19] |
| Signal developer population | General retail system/signal coders | **100** people [19] |
| Coder long-term success rate | General retail system/signal coders | **one** in a **100** might have some success [19] |
| Rare setup historical period | General context-heavy setup backtest | Past **20** years [9] |
| Rare setup opportunity sample size | General context-heavy setup backtest over 20 years | Sample size of **100** opportunities [9] |
| Breast cancer prediction factors | Medical diagnostic model (static baseline comparison) | **20** factors [22] |
| Intern's model validation steps | Intern's backtested system *(instrument, strikes, DTE, dates not specified)* | **two** layers behind a raw backtest [25] |
| Optimization return inflation | General over-optimized backtest setup | Can **double** (2x) the expectations on paper [10] |
| Adaptive Ensemble trend duration 1 | Trend state look-back horizon | Past **three** days [8] |
| Adaptive Ensemble trend duration 2 | Trend state look-back horizon | Past **10** days [8] |
| Adaptive Ensemble trend duration 3 | Trend state look-back horizon | Past **100** days [8] |
| Adaptive Ensemble trend duration 4 | Trend state look-back horizon | Past **year** (1 year) [8] |
| Stated signal focus frequency | IQ signal options credit spread execution | **a couple** of days a month [7] |
| Out-of-sample forward testing window | Out-of-sample test on Seth's own capital | **six** months of data [20] |
| Ensemble development duration | Building and gathering data for the group of systems | Took **a couple** years to build out [20] |

### [4P5LxIdOJXY] Options Strategies for Day Traders (23,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Google stock options (GOOG / Google) [1].
    *   **Structure**: A simple options spread (taught as part of the "Super Simple Spreads" program) [2].
    *   **Strikes/Deltas**: The hypothetical trade utilizes the **460** strike level [2]. Selection is based on the options market and pricing models predicting that there is **no more than a 10% chance** of the index or stock actually reaching that level [2]. 
    *   **DTE (Days to Expiration)**: Entered in the August monthly expiration, which expires on the **third Friday** of the month [1, 2].
    *   **Entry Trigger**: Not defined by technical indicators [1-5]. The trade is positioned as a portfolio diversification tool designed to be entered during low-movement market conditions when traditional equity day trading struggles [4].

*   **The Management and Exit Rules**:
    *   **Low Maintenance**: Because the underlying stock price is very far from the 460 strike level, the trade is highly passive and requires very little active management [2].
    *   **Peak Hour Avoidance**: Positions are managed primarily outside of peak equity day trading hours [4]. Day traders actively trade the open and the close, whereas options income traders observe the market and execute their trades **between those two periods of time** so as not to interfere with daily stock operations [1, 4].

*   **The Stated Edge or Statistics**:
    *   **Low Correlation**: Options income trading has a very low correlation with equity day trading, offering strong diversification benefits [4].
    *   **High Probability**: The trade is structured around options pricing models that estimate a **no more than 10% chance** of the 460 level being violated before August expiration [2].
    *   **Desk Validation**: The "Super Simple Spreads" strategy was developed by the firm's top options desk trader, John Locke, who has successfully traded these specific methods for **over seven years** [2].

*   **The Caveats the Presenter Gives**:
    *   The provided passages of this video do not contain any explicit caveats, risks, margin requirements, or downside scenarios [1-5].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | YouTube video metadata | **23000** views [3] |
| Proprietary firm performance rankings | SMB Capital daily trader lists | "**top ten**" traders list [4] |
| Monthly option expiration schedule | General options expiration frequency | "**third Friday** of each month" [1] |
| Option expiration probability model | Google, August monthly option spread, strike 460 | "**no more than a 10% chance**" [2] |
| Option spread strike selection | Google, August monthly option spread | "**460** level" [2] |
| Head trader strategy validation | John Locke options strategies | "**seven** years" [2] |

### [njoDkeNAs8E] You Can Win So Many Different Ways With This Weekly Options Strategy (23,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **Russell 2000 Index options (RUT)** `[1, 2]`. Seth Freudberg notes that index options work similarly to equity options but are settled directly in cash, avoiding physical share transactions `[2]`.
    *   **Structure**: The **weekly put broken wing butterfly strategy** `[3, 4]`. It is constructed by buying an out-of-the-money long put, selling two puts at a lower strike price, and buying one protective put at an even lower strike price `[4]`. The wing widths are unequal (broken wing) to ensure the position is entered for a net credit (positive cash flow) `[4, 5]`.
    *   **Strikes/Deltas**: 
        *   *Trade 1 (May 19th setup)*: Buying one **1250** put (almost **83** points below the market), selling two **1230** puts, and buying one protective **1180** put `[4]`.
        *   *Trade 2 (June 11th setup)*: Buying one **1340** long put, selling two puts (short strikes not spoken), and buying one protective **1270** put (located **86** points away) `[6]`.
        *   Specific Delta targets are not explicitly spoken for this strategy setup in this transcript.
    *   **DTE (Days to Expiration)**: **10** days to expiration `[4, 6]`.
    *   **Entry Trigger**: Entered as a bullish options income strategy, typically when the market is experiencing a strong bounce off its lows `[1, 3, 6]`.

*   **The Management and Exit Rules**:
    *   The trade is highly flexible and provides a range of prices over which the trader can win `[3]`.
    *   **Scenario 1 (Market rallies, stays flat, or drops slightly)**: If the index rises or trades sideways, all puts expire completely worthless well below the market price at expiration `[7]`. The trader does not owe any money to settle the contracts and simply pockets the net credit received at entry as profit `[7]`.
    *   **Scenario 2 (Orderly pullback / sell-off)**: If the market sells off gradually, the options closer to the money (specifically the upper long put) gain value rapidly while the further out short options decay, allowing the trader to close the trade early for a "bonus profit" `[6]`.
    *   Index options are settled automatically in cash at expiration at a rate of **\$100 per point**, avoiding physical stock delivery `[2, 4]`.

*   **The Stated Edge or Statistics**:
    *   **No Upside Risk**: Because the trade is initiated for a net credit, there is absolutely zero risk on the upside if the market continues to rally `[3-5]`.
    *   **Double Profit on Pullbacks**: If a sell-off occurs at the right time, the strategy yields a dramatic "bonus profit" that can be more than double the original credit (e.g., yielding **\$555**) `[6]`.
    *   **Time Decay harvesting**: The calendar spread mechanics harvest time premium, since the shorter-term sold options decay much faster than the longer-term bought options `[6]`.
    *   **High Probability Workshop Baseline**: The video mentions a prop-taught options income strategy that features a statistical **80%** (spoken as "eighty") probability of profit month in and month out `[5]`.

*   **The Caveats the Presenter Gives**:
    *   The presenter notes that pullbacks are inevitable even when the bull market is running wild `[6]`.
    *   The strategy does have a margin requirement, as the broker will require capital to be set aside to cover the worst-case scenario risk (e.g., **27.65** points for Trade 1) `[5]`.
    *   If the market sells off too aggressively beyond the lower wing protection, the trade can hit its worst-case maximum loss `[5, 6]`.

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video views metadata `[8]` | Video metadata | **23000** views |
| S&P 500 Index baseline `[1]` | S&P 500 Index (SPX) | **500** index |
| standard equity options contract size `[2]` | General Equity Option | represents **100** shares of a stock |
| Russell 2000 Index options cash settlement `[2]` | Russell 2000 Index (RUT) | **2000** index; paid in cash **\$100** per point |
| Trade 1 entry timing `[4]` | RUT Put Broken Wing Butterfly | May **19th** (entry date); May **29** options chain (expiration date); **10** days (DTE) |
| Trade 1 strike configuration `[4]` | RUT Put Broken Wing Butterfly (1250/1230/1180) | Bought 1250 put (almost **83** points below market); sold **two** of those 12 30 (1230) puts; bought **one** protective 1180 put |
| Trade 1 individual execution prices `[4]` | RUT Put Broken Wing Butterfly (1250/1230/1180) | Bought 1250 put for **14.25** premium (representing **100** per point, total cost of **1 425**); sold two 1230 puts for **10.75** premium each (brings in cash of **2015** (garbled/typo in transcript, physically representing 2150)); bought one protective 1180 put for **490** premium |
| Trade 1 net cash credit and margin `[5]` | RUT Put Broken Wing Butterfly (1250/1230/1180) | Received cash inflow of **235** into account; broker required capital of **27.65** (worst-case scenario risk, representing \$2,765) |
| Trade 1 expiration result `[7]` | RUT Put Broken Wing Butterfly (1250/1230/1180), expiring May 29th | Russell 2000 index closed at **13.94** (verbatim text, representing 1394); all puts expired worthless; kept **235** profit |
| Trade 2 strike parameters and market conditions `[6]` | RUT Put Broken Wing Butterfly, June 11th drop | June **11th** (date of the drop); "fairly high also **885**" (verbatim value of a leg or index price); **1340** long put strike; **1270** put strike (located another **86** points away) |
| Trade 2 close-out performance `[6]` | RUT Put Broken Wing Butterfly, closed June 11th | 1270 put going for **2.95** premium; net profit of **555** dollars (which is **more than double** the original credit); represents **more than a 20** return on capital (verbatim text, representing 20%) in **10** days |
| Workshop teaching duration `[5]` | General educational workshop | **two-hour** free intensive workshop |
| Workshop strategies count `[5]` | General educational workshop | teaches **three** of those strategies |
| Workshop high-probability win rate `[5]` | High-probability options income strategy | statistical **eighty** probability of profit (verbatim text, representing 80% probability) |

### [Wc-JbFF8x5o] High Probability Options Strategy (Best Time To Execute) (23,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Russell 2000 Index options (ticker symbol: RUT), representing a basket of small-cap US stocks [1, 2].
    *   **Structure**: The Bear Trap strategy, which is a specialized version of a put Condor strategy [3]. It involves:
        *   Buying a long put strike below the market price [2, 3].
        *   Selling a short put strike 10 points lower than the purchased put [2, 3].
        *   Selling another short put strike way down at a crucial historical support level [2, 3].
        *   Buying a final long put strike even lower down for tail risk protection [2, 3].
    *   **Strikes/Deltas**: 
        *   *Example 1*: Long 1910 puts (5 contracts), Short 1900 puts (5 contracts), Short 1650 puts (5 contracts), and Long 1600 puts (5 contracts) [2].
        *   *Example 2*: Long 181 puts (5 contracts; later referenced as the 1810 put), Short 1800 puts (5 contracts), Short 1650 put (5 contracts), and Long 1600 puts (5 contracts) [4, 5].
        *   *Deltas*: The video does not explicitly state specific Delta parameters for selecting the strikes.
    *   **DTE (Days to Expiration)**: Approximately 3 months to expiration [2, 4].
    *   **Entry Trigger**: Entered when the index has rallied to a major overhead resistance level and a bearish rollover is expected, while anticipating that any subsequent sell-off will likely find support and bounce where it has bounced twice in the past year (e.g., the 1650 support level) [1-4].
        *   *Example 1 Entry*: Entered on February 3, 2023, after RUT bounced off the 1650 level in June and October of 2022, rallied to 19855 3, and approached the crucial 2000 level where it rolled over in August 2022 [1, 2].
        *   *Example 2 Entry*: Entered on Wednesday December 13th 2023 (a Fed day), when the index had rallied since late October to 19475 and the bounce was deemed overdone [4].

*   **The Management and Exit Rules**:
    *   The trade is a "set and forget" style designed to be left alone and held to expiration [6].
    *   At expiration, the broker cash-settles the index contracts automatically at a rate of \$100 per point that the index closes below the put strike price [3, 6].
    *   **Winning Exit (Target Scenario)**: If the market rolls over and channels near the historical support level at expiration, the trade yields maximum profitability [4, 6].
    *   **Consolation Exit (Wrong Direction Scenario)**: If the market rallies instead of falling, all options expire completely worthless [5]. Because the trade is initiated for a net positive cash flow (credit), the trader retains the initial cash as their profit [5].

*   **The Stated Edge or Statistics**:
    *   **Positive Cash Flow Hedging**: Unlike standard portfolio hedges that cost premium, this strategy actually pays the trader a positive cash flow (credit) to enter [6].
    *   **Unconditional Profit Profile**: It is the only type of trading strategy that can provide a win even when the trader is flat-out wrong about the direction of the index [5, 7].
    *   **Diversification Edge**: Index options are used to design these longer-term hedges because they are protected from individual company risks [1, 8].

*   **The Caveats the Presenter Gives**:
    *   The trade carries a high broker capital/margin requirement (e.g., requiring at least 19,950 in the account for a 5-lot trade) [6].
    *   This required capital represents the trade's absolute worst-case scenario loss [6].
    *   If the stock/index collapses extremely far (i.e., drops deep below the protective lower long strike), the trade can become a loss [7].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Prop firm longevity [8] | General firm operations | Established since **2005** |
| Historical baseline year [1] | RUT index historical baseline | **February of 2023** |
| Target index name [1] | Russell **2000** Index | Russell **2000** Index |
| Preceding selloff period [1] | RUT index historical behavior | Most of **2022** |
| Support level [1] | RUT index support level | Bounced off that **1650** level |
| Trade entry RUT price [2] | RUT Bear Trap, Feb 3, 20123 / 2023 entry | Closing price of **19855 3** (Note: transcribed as 19855 3 in source text) |
| Trade entry date [2] | RUT Bear Trap entry date | **February 3rd 20123** (Note: transcribed as 20123 in source text) |
| Crucial resistance level [2] | RUT index resistance level | **2000** level |
| Historical rollover month [2] | RUT index historical rollover | **August of 2022** |
| Expiration time horizon [2] | RUT Bear Trap | about **3** months later |
| Expiration options chain [2] | RUT Bear Trap | April **28th** options chain |
| Upper long put strike [2] | RUT Bear Trap (April 28th, 2023) | **1910** put strike price |
| Upper long puts contract count [2] | RUT Bear Trap (April 28th, 2023) | bought **five** of those puts |
| Upper short puts contract count [2] | RUT Bear Trap (April 28th, 2023) | sold **five** puts |
| Upper short put strike [2] | RUT Bear Trap (April 28th, 2023) | Short puts at **1900** strike |
| Strike width [2] | RUT Bear Trap (April 28th, 2023) | **10** points lower (1910 put vs 1900 put) |
| Lower support level [2] | RUT Bear Trap (April 28th, 2023) | Crucial **1650** level |
| Historical bounce frequency [2] | RUT index support level | Bounced **twice** in the previous year |
| Lower short puts contract count [2] | RUT Bear Trap (April 28th, 2023) | sold **five** of those puts |
| Lower long puts contract count [2] | RUT Bear Trap (April 28th, 2023) | buy **five** puts |
| Lower long put strike [2] | RUT Bear Trap (April 28th, 2023) | Long puts at **1600** strike |
| Support level strike [3] | RUT Bear Trap (April 28th, 2023) | **1650** level |
| Short puts strike identification [3] | RUT Bear Trap (April 28th, 2023) | those **1900** puts |
| Short 1900 put sale price [3] | RUT Bear Trap (April 28th, 2023) | Received a price of **4355** (Note: representing \$43.55 **⚠unverified**) |
| Index point multiplier [3] | RUT Index option payoff | Rate of **\$100** per point |
| Multiplier factor [3] | General cash flow calculation | Multiply by **100** |
| Short 1900 puts contract count [3] | RUT Bear Trap (April 28th, 2023) | sold **five** of them |
| Short 1900 puts total credit [3] | RUT Bear Trap (April 28th, 2023) | Positive cash flow of **21,775** (Note: representing \$21,775 **⚠unverified**) |
| Short 1650 puts total credit [6] | RUT Bear Trap (April 28th, 2023) | Received **5,175** (Note: representing \$5,175) |
| Short put strike identification [6] | RUT Bear Trap (April 28th, 2023) | sold way down "**at650**" (Note: transcribed as at650 in source text) |
| Long put strike identification [6] | RUT Bear Trap (April 28th, 2023) | bought the **1910s** |
| Short put strike identification [6] | RUT Bear Trap (April 28th, 2023) | **1900s** we sold |
| Long 1910 puts total cost [6] | RUT Bear Trap (April 28th, 2023) | Cost of **\$23,200** |
| Long 1600 puts total cost [6] | RUT Bear Trap (April 28th, 2023) | Cost of **3875** (Note: representing \$3,875) |
| Net entry credit [6] | RUT Bear Trap (April 28th, 2023) | Net positive cash flow of **\$50** |
| Capital margin requirement [6] | RUT Bear Trap (April 28th, 2023) | broker will require at least **19,950** in your account |
| Max risk / worst case [6] | RUT Bear Trap (April 28th, 2023) | worst case scenario of **19,950** |
| Expiration timeline [6] | RUT Bear Trap | about **3** months later |
| Expiration date [6] | RUT Bear Trap | **April 28th 2023** |
| Crucial resistance level [6] | RUT index resistance level | same **2000** level |
| March/April channeling floor [6] | RUT index channeling range | channeling between **1700** a (Note: cut off as "1700 a" in source text) |
| Fed day RUT closing price [4] | RUT index price, Dec 13, 2023 | Rallying to **19475** (Note: representing 1947.5) |
| Second trade entry date [4] | Second RUT Bear Trap entry date | **Wednesday December 13th 2023** |
| Expiration timeline [4] | Second RUT Bear Trap | about **3** months later |
| Expiration date [4] | Second RUT Bear Trap | March **15th of 2024** |
| Upper long puts contract count [4] | Second RUT Bear Trap (March 15th, 2024) | bought **five** of those puts |
| Upper long put strike [4] | Second RUT Bear Trap (March 15th, 2024) | Long### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Russell 2000 Index options (ticker symbol: RUT) [1, 2].
    *   **Structure**: The Bear Trap strategy, which is a specialized version of the put Condor strategy [3]. It is constructed by buying a put option below the market price, selling a put 10 points lower, selling a second put further down at a historical bounce support level, and buying a final put even lower for tail risk protection [2, 3].
    *   **Strikes/Deltas**: 
        *   *Setup 1*: Long 1910 puts, Short 1900 puts, Short 1650 puts, and Long 1600 puts [2]. 
        *   *Setup 2*: Long 1810 puts (referred to on slide as 181 puts), Short 1800 puts, Short 1650 puts, and Long 1600 puts [4, 5].
        *   *Deltas*: The video does not select strikes based on specific Deltas.
    *   **DTE (Days to Expiration)**: Approximately 3 months to expiration [2, 4].
    *   **Entry Trigger**: Entered when the index bounces up to a key overhead resistance level (like the 2000 level) and a pullback is expected, with the thesis that the market will find support and bounce where it had bounced twice in the previous year (such as the 1650 level) [1-3].

*   **The Management and Exit Rules**:
    *   The trade is a passive hedge designed to be held until expiration [6].
    *   If the index rolls over as expected and channels above the lower support strike, the trade achieves its maximum profit potential [4, 6].
    *   If the trader is flat-out wrong and the index rallies, all four puts expire completely worthless [5]. Because the trade was entered for a credit, the trader keeps the initial cash flow as a "consolation prize" [5, 7].
    *   No active intra-trade management or adjustments are mentioned for this strategy.

*   **The Stated Edge or Statistics**:
    *   **Positive Cash Flow**: Unlike traditional hedges that cost premium, this strategy actually pays the trader a net credit to enter [6, 7].
    *   **High Flexibility**: It is the only type of trading strategy that can provide a win even when the directional thesis is completely wrong [5, 7].

*   **The Caveats the Presenter Gives**:
    *   The strategy has a high capital requirement, as the broker requires significant margin to execute the trade [6].
    *   This margin represents the trade's absolute worst-case scenario maximum loss (e.g., \$19,950 for a 5-lot) [6].
    *   If the market completely falls apart and collapses below the lowest protective strike, a maximum loss is incurred [2, 6, 7].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Proprietary firm longevity | General firm history | Established since **2005** [8] |
| Trade 1 entry date | RUT Bear Trap, Feb 3, 2023 | Entered on **February 3rd 20123** (Note: transcribed as 20123 in source) [2]; RUT closed at **19855 3** (Note: transcribed as 19855 3 in source) [2] |
| Historical bounce support | RUT Index historical support | Bounced twice off the **1650** level [1, 2] |
| Historical rollover resistance | RUT Index resistance | Rolled over at the crucial **2000** level in **August of 2022** [2] |
| Trade 1 setup | RUT Bear Trap, April 28th expiration | Expires about **3** months later [2]; April **28th** options chain [2] |
| Trade 1 strikes & sizing | RUT, 5-lot Bear Trap | Bought **five** 1910 puts [2], sold **five** 1900 puts (**10** points lower) [2], sold **five** 1650 puts [2], bought **five** 1600 puts [2] |
| Option contract multiplier | RUT Index cash-settlement multiplier | Pays off at a rate of **\$100** per point [3]; values must be multiplied by **100** [3] |
| Option contract pricing | RUT, individual leg premium values | Short 1900 puts priced at **4355** [3]; Long 1910 puts cost **\$23,200** [6]; Short 1650 puts priced at **5,175** [6]; Long 1600 puts cost **3875** [6] |
| Trade 1 cash flow | RUT, 5-lot Bear Trap credit | Short 1900 puts generated positive cash flow of **21,775** [3]; net trade positive cash flow of **\$50** [6] |
| Trade 1 capital requirements | RUT, 5-lot Bear Trap margin | Broker requires at least **19,950** in account [6]; trade's worst-case scenario is **19,950** [6] |
| Trade 1 expiration outcome | RUT, 5-lot Bear Trap, April 28, 2023 | RUT expired about **3** months later [6] on **April 28th 2023** [6]; channeled between **1700** a (Note: transcribed as "1700 a" in source) [6] |
| Trade 2 entry date | RUT Bear Trap, Dec 13, 2023 | Entered on **Wednesday December 13th 2023** [4]; RUT closed at **19475** [4] |
| Trade 2 setup | RUT Bear Trap, March 15th expiration | Expires about **3** months later [4]; March **15th of 2024** options chain [4] |
| Trade 2 strikes & sizing | RUT, 5-lot Bear Trap | Bought **five** of the **181** puts (Note: 1810 on slide) [4, 5], sold **five** of the 1800 puts [4], sold **five** of the 1650 puts [4], bought **five** of the 1600 puts [4] |
| Trade 2 expiration outcome | RUT, 5-lot Bear Trap, March 15, 2024 | RUT expired on **March 15 2024** [4]; rallied above **2,000** to **23932** [5]; highest put expired over **129** points below index close [5] |
| Trade 2 wrong-way P&L | RUT, 5-lot Bear Trap expired worthless | Consolation prize of **\$75** for being wrong [5] |

### [STQOppV45ZQ] Covered Calls: How to Create an INCOME MACHINE (Easily) (23,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Exxon stock (ticker symbol: XOM), or more generally any dividend-paying stock (which pays an average dividend yield of 1.74% [1]) or non-dividend stock (which constitutes 25% of all stocks [2]).
    *   **Structure**: A covered call campaign. This involves owning 100 shares of stock and selling one call option for each 100 shares owned [1, 3].
    *   **Strikes/Deltas**: 
        *   *First Month (September)*: Sold the 100 strike price call option (located about six dollars above XOM's current price) [3].
        *   *Second Month (October)*: Sold the 105 strike price call option [4].
        *   *Third Month (November)*: Sold the November covered call [5].
        *   *Selection Rule*: The strategy selects a call option "as far above exxon's current price as possible while at the same time having the value of around a dollar" [3].
    *   **DTE (Days to Expiration)**: Approximately one month to expiration (monthly options chain) [3].
    *   **Entry Trigger**: Triggered when a trader owns or acquires shares of a high-quality stock (such as Exxon) after it has pulled back to some extent but is still considered a solid long-term investment [3]. XOM was bought on August 19, 2022, at 94.06 after pulling back from 105 in June to as low as 80 in the summer [3].

*   **The Management and Exit Rules**:
    *   **Outcome 1 (Stock closes below the call strike price at expiration)**: The call option expires completely worthless (value of zero) [4]. The trader pockets the initial premium as pure trade profit and immediately "reloads" by selling a fresh call option expiring a month later (e.g., after XOM closed at 93.21 on September 16, the 100 call expired worthless, and the trader sold the October 105 call) [4].
    *   **Outcome 2 (Stock closes above the call strike price at expiration)**: The shares owned are automatically sold ("called away") to the option buyer at the strike price (a process called "assignment") [5]. To continue the campaign, the trader must purchase a fresh 100 shares of stock in the open market in order to write the next monthly covered call (e.g., after XOM closed at 105.86 at October expiration, the shares were sold at 105, requiring the trader to buy a fresh 100 shares of XOM to sell the November call) [5].
    *   **Duration**: The campaign is systematically managed month-by-month over a six-month period [6].

*   **The Stated Edge or Statistics**:
    *   **Yield Multiplication**: Over a six-month period, the covered call campaign on Exxon generated a total income of 677 dollars, nearly quadrupling the 182 dollars in dividend-only income that would have been received by simply holding the shares [2, 5].
    *   **Comparison to Fixed Income**: Prior to the last 12 months, bond yields or certificates of deposit (CDs) paid literally less than a full percentage point [7].
    *   **Turn Non-Dividend Stocks Into Yield Generators**: Covered calls allow traders to multiply yield on dividend stocks and basically turn the 25% of all stocks that pay zero dividends into income-generating assets [2].

*   **The Caveats the Presenter Gives**:
    *   The campaign can be hands-on, requiring the trader to actively manage assignment by re-buying shares at potentially higher open-market prices if the stock rallies above the strike price [5].
    *   Only the first month's covered call income is known for sure at the outset of the campaign; subsequent monthly premiums vary depending on market conditions (e.g., XOM September call brought in 126, October brought in 72, November brought in 103) [4-6].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Prop firm longevity | General firm history | numerous "seven" (7) and even "eight" (8) figure per year Traders [7] |
| Historical bond yield timeline | CD / bond yields benchmark | "prior to the last 12 months" (12) [7] |
| CD/Bond yield benchmark | CDs or bond yields | "literally less than a full percentage point" (less than 1%) [7] |
| Average equity dividend yield | S&P 500 equities buy-and-hold | "on average 1.74" (1.74%) dividend yield [1] |
| Sizing of call option contract | General stock option structure | entitles the buyer to buy "100" shares of stock [1] |
| Exxon historical pullback | Exxon stock (XOM), June/Summer 2022 | Pulled back "six months ago" (6) from a June high of "105" to "as low as 80" [3] |
| XOM campaign entry | XOM stock purchase, August 19, 2022 | Bought "100" shares at "9406" (representing \$94.06 **⚠unverified** per share) on "August 19 2022" (and "August 19th") [3] |
| XOM September call strike | XOM, Short September Call, August 19, 2022 | Strike price "100" (located "six dollars" above current price); target option value "around a dollar" [3] |
| XOM September call sale price | XOM, Short September Call, August 19, 2022 | sold for "a dollar twenty six" (representing \$1.26 per share, or \$126 total credit) [3] |
| Campaign planned duration | XOM covered call campaign | "every month for six months" (6 months) [6] |
| October call planned price | XOM, Short October Call, August 19, 2022 | "about a dollar" [6] |
| Exxon dividend metrics | XOM stock quarterly dividend | pays "91 cents per share" quarterly; yields "91 dollars per quarter" on 100 shares [6] |
| September call cash flow | XOM, Short September Call total credit | received cash of "126 dollars"; calculated by multiplying the "1.26" number by "100" shares [6] |
| Exxon dividend schedule | XOM stock dividends on 100 shares | pays "91 dollars" in both "November and February" [6] |
| September call expiration date | XOM, September Call | "September 16th" [4] |
| September expiration XOM price | XOM, September Call expiration | XOM closed at "93.21"; short "100" call expired with a value of "zero"; trader kept "126 dollars" [4] |
| October call entry | XOM, Short October Call, September 16, 2022 | sold the "105" strike call; received "72 dollars" [4] |
| October call expiration date | XOM, October Call | XOM closed at "105.86"; sold shares at strike of "105" (assignment) [5] |
| November campaign reload | XOM, Short November Call, October expiration | bought fresh "100" shares of XOM; sold November call for "103 dollars"; received November dividend of "ninety one dollars" [5] |
| Total campaign performance | XOM covered call campaign, 6-month period | total income over "six month period" ending "mid-February" was "677 dollars" [5] |
| Dividend-only baseline comparison | XOM stock buy-and-hold (no options), 6-month period | would have made "182 dollars that being the 291 dollar dividends" (verbatim text, representing two \$91 dividends) over "six-month period" [2] |
| Performance multiplier | XOM covered call vs. buy-and-hold | "nearly quadrupled" (quadrupled / ~3.72x) dividend income [2, 5] |
| Traditional dividend frequency | General dividend stocks | receive a dividend every "90 days" [2] |
| Non-dividend stocks proportion | General equities market | "25 percent" of all stocks [2] |
| Target return enhancement | Covered call campaign potential | "triple your income" / "more than triple the amount of income" (3x) [7, 8] |

### [4gON-kdleCM] Using options to profit if the stock market goes up or down (22,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX index) [1].
    *   **Structure**: Iron Condor strategy. This consists of selling options closer to the index price (both calls and puts) and buying protective options further away from the market on both sides [2, 3].
    *   **Strikes/Deltas**: 
        *   Short Call strike: **5100** (located **500** points above where the index is trading) [2].
        *   Short Put strike: **4100** (located **500** points below the index price) [2].
        *   Long Call (for protection): **5150** strike (located **50** points above the short calls) [2].
        *   Long Put (for protection): **4050** strike (located **50** points below the short puts) [2].
        *   *Deltas*: The video does not specify any Delta targets or metrics for strike selection [1-8].
    *   **DTE (Days to Expiration)**: Approximately five months to expiration. Entered on the morning of **July 27th**, 2023, and expiring at the very end of the year on **December 29th, 2023** [1, 2].
    *   **Entry Trigger**: Positioned at a market inflection point when the S&P 500 Index tests previous highs and there is high uncertainty as to whether it will break out to the upside or fail and break down [5, 6]. In this case, it was entered on July 27, 2023, when the index rallied back up to the key **4600** level, which was a key resistance level where a previous bounce had failed in March of 2022 [1].

*   **The Management and Exit Rules**:
    *   The trade is a "set and forget" range-bound trade [7, 8].
    *   **Winning Exit (Range Bound)**: As long as the index closes below the lowest call (**5100**) and above the highest put (**4100**) at expiration, all four options expire worthless [8]. The trader has no further settlement obligations and pockets 100% of the net cash credit as pure profit [8].
    *   The range of profitability is **1,000** points wide (between 4,100 and 5,100), representing practically **20%** of the entire index's value [8].
    *   Index options are cash-settled, meaning calls only have value if the index closes above the strike price, and puts only have value if the index closes below the strike price [8].
    *   **Losing Exit / Worst-Case Scenario**: If the market moves violently outside of the boundaries, the maximum loss is defined by the width of the spread minus the net credit received [7]. The maximum risk/loss is strictly capped at the broker's capital requirement [7].

*   **The Stated Edge or Statistics**:
    *   Savvy traders use this strategy to profit whether the market goes up, goes down, or stays sideways within a broad range of prices [3, 4].
    *   **Positive Cash Flow**: Entering the trade yields a net credit upfront, resulting in positive cash flow of **\$8,400** at the outset of the trade for a 10-lot [7].
    *   Allows traders to capture a handsome return without being forced to predict the exact direction of the market breakout [3, 6].

*   **The Caveats the Presenter Gives**:
    *   The trade carries a high capital requirement, as the broker requires a margin of at least **41,600** in the account to execute a 10-lot trade, which also represents the trade's absolute worst-case scenario loss [7].
    *   If the account size is too small to support this capital requirement, the trader must scale down the lot size (e.g., to five lots or two lots) [7].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video views metadata | YouTube video metadata [4] | **22000** views |
| Target year for Federal Reserve monetary policy easing | General S&P 500 index market environment [5] | **2024** |
| Date of S&P 500 Index previous all-time highs | S&P 500 Index [5] | **early 2022** |
| Duration of S&P 500 Index sell-off | S&P 500 Index [5] | **full year** |
| S&P 500 Index bounce year | S&P 500 Index [5] | **2023** |
| Month and year S&P 500 Index returned to all-time highs | S&P 500 Index [5] | **January of 2024** |
| Date of S&P 500 breakout after covid crash | S&P 500 Index [5] | **late 2020** |
| Year S&P 500 failed at all-time highs | S&P 500 Index [6] | **2015** |
| Number of times S&P 500 retested highs in 2015 | S&P 500 Index [6] | **three** |
| Contextual year of historical failure level | SPX Index [1] | **March of 2022** |
| Contextual year of S&P 500 all-time highs | SPX Index [1] | **January of 2022** |
| Timeframe of S&P index key level rally | SPX Index [1] | **Late July 2023** (also "**July of 2023**") |
| SPX Index key level tested in July 2023 | SPX Index [1] | **4600** |
| Trade entry date | SPX Iron Condor entry [1] | morning of **July 27th** |
| Option contract expiration date | SPX Iron Condor [2] | **December 29th 2023** |
| Distance of short call above index price | SPX Long/Short Call [2] | **500** points |
| Strike price of short call options | SPX Long/Short Call [2] | **5,100** |
| Number of short call option contracts sold | SPX Long/Short Call [2] | **10** |
| Sale price of short call options | SPX Long/Short Call [2] | price of **16.40** (representing \$16.40 per share) |
| Distance of short put below index price | SPX Long/Short Put [2] | **500** points |
| Strike price of short put options | SPX Long/Short Put [2] | **4100** |
| Number of short put option contracts sold | SPX Long/Short Put [2] | **10** |
| Sale price of short put options | SPX Long/Short Put [2] | **\$415** (quoted as \$415 in transcript; representing \$4.15 per share) |
| Number of protective long call options bought | SPX Long/Short Call [2] | bought **10** |
| Strike price of long protective call options | SPX Long/Short Call [2] | **5150** calls |
| Distance of protective calls above short calls | SPX Long/Short Call [2] | **50** points |
| Price paid for protective long call options | SPX Long/Short Call [2] | price of **\$12** (representing \$12.00 **⚠unverified** or \$1.20) |
| Total cost of protective long call options | SPX Long/Short Call [7] | cost of **\$1,050** |
| Number of protective long put options bought | SPX Long/Short Put [2] | bought **10** |
| Strike price of long protective put options | SPX Long/Short Put [2] | **4050** puts |
| Price paid for protective long put options | SPX Long/Short Put [2] | price of **\$375** (representing \$375 or \$3.75) |
| Total cost of protective long put options | SPX Long/Short Put [7] | cost of **37,50** (garbled/typo in transcript, representing \$3,750) |
| Initial net positive cash flow credit received | SPX Iron Condor, 10-lot setup [7] | positive cash flow of **\$8,400** |
| Required broker capital / maximum risk margin | SPX Iron Condor, 10-lot setup [7] | at least **41,600** in capital (worst case scenario loss) |
| Scaled-down trade lot sizes | SPX Iron Condor scaled setups [7] | **five** Lots or **two** lots |
| Approximate index bottoming level during initial sell-off | SPX Index movement [7] | **4...** (garbled/truncated in transcript) |
| Lower boundary of profit zone (short put strike) | SPX Index [8] | **4100** |
| Upper boundary of profit zone (short call strike) | SPX Index [8] | **5100** |
| Number of total options in iron condor | SPX Index [8] | all **four** options |
| Width of the range of profitability | SPX Index [8] | **1,000** Point range |
| Floor of profitability range | SPX Index [8] | **4,100** |
| Ceiling of profitability range | SPX Index [8] | **5100** |
| Percentage of entire index's value represented by range | SPX Index [8] | practically **20%** |
| Additional options strategies taught in workshop | Workshop promotion [3] | **three** |

### [0lzwuAhX16U] How to Profit From a Market Meltdown: A Guide to Options Trading During a Crash (22,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Cash-settled S&P 500 Index options (SPX) [1-3]. 
    *   **Structure**: At-the-money (ATM) put credit spread [1]. This involves selling an at-the-money put option right below where the S&P 500 index is currently trading, and simultaneously purchasing a protective put option 50 points lower [1, 4].
    *   **Strikes/Deltas**: The short put is placed right below the current index price [4, 5], and the long put is purchased exactly 50 points below the short strike [1, 5]. Explicit Delta parameters are not spoken, but the position is entered "at the money" to capture maximum premium [1].
    *   **DTE (Days to Expiration)**: Approximately 6 months (half a year) to expiration [2, 4, 5].
    *   **Entry Trigger**: Triggered when the VIX index spikes and blows through the **40 level** intraday during a market crash or period of massive uncertainty [4-6]. This is a rare, high-fear event that has occurred on average only once every two years over the last decade [6, 7].

*   **The Management and Exit Rules**:
    *   **Trade Management**: The trade is executed as a "set and forget" credit spread [1, 2, 7]. There is no active management or adjustment mentioned; the options are held all the way to expiration [2, 7].
    *   **Winning Exit**: If the S&P 500 index recovers or flatlines and closes above the short put strike on expiration day, both put options expire completely worthless [2, 5]. The trader has no further settlement obligations and pockets 100% of the upfront net cash credit as pure profit [2, 5].
    *   **Losing Exit**: If the index collapses and closes below the lower protective long put, the maximum loss is strictly capped at the 50-point spread width (multiplied by \$100 per point, or \$5,000 **⚠unverified** per contract) minus the initial credit received [1, 7].

*   **The Stated Edge or Statistics**:
    *   **100% Demonstrable Win Rate**: Over the last 10 years, this exact strategy has successfully yielded a winning trade in all 5 historical instances where the VIX popped above the 40 level [2, 3].
    *   **Asymmetric Profit Returns**: The total profit across the 5 historical VIX-spiked days was **\$40,575**, which represents more than twice the capital at risk for any single trade [3]. A trader could have lost one or even two of these trades and still come out net profitable [3].
    *   **Volatility Pricing Edge**: During extreme VIX spikes, option sellers are paid significantly higher premiums than in normal market conditions [7]. Because the maximum loss of a credit spread is defined by the strike width minus the credit received, collecting a massive upfront credit automatically shrinks the capital required (margin/risk) while drastically multiplying the potential reward [7].

*   **The Caveats the Presenter Gives**:
    *   **Risk of Outlier Loss**: The presenter explicitly warns that there is no such thing as a guaranteed win in trading: "That's not to say that this trade or any trade that we've covered on our channel won't lose. In fact every trade I've ever covered in these videos has not only the risk of losing but they actually lose" [7].
    *   **Position Sizing**: Because a losing trade is inevitable at some point, traders must only make "responsibly-sized" trades and maintain appropriate risk controls [7].
    *   **Edge over Perfection**: Professional traders must accept that perfection is impossible, focusing instead on identifying high-probability edge trades backed by a demonstrable historical track record and logical rules [7, 8].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Prop firm history | General operations | Co-founded in **2005** |
| Video views metadata | Video statistics | **22000** views |
| Index bear market signal | S&P 500 Index intraday drop, April 7th | Dropped below **4,900** before bouncing intraday |
| VIX spike threshold | VIX Index, April 4th | VIX blew through the **40** level; only happened a handful of times in the last **10 years** |
| VIX spike frequency | General market conditions | Occurs on average every **two years** over the last **10 years** |
| Trade 1 entry conditions | SPX, August 24th, 2015 entry | August of **2015** (just under **10 years** ago); market opened down for the **fifth** straight day; VIX spiked over **40**; entered on morning of **August 24th** of that year; options chain expiring **January 25th 2016** (about a half year later) |
| Trade 1 strikes and contract size | SPX ATM put credit spread | Sold **five** short puts right below the market at the **\$1875** strike; bought **five** protective puts **50** points lower at **1825** strike |
| Trade 1 execution prices | SPX put credit spread, August 24th, 2015 | Sold short puts for a price of **1840** (Note: transcribed as `price of1840` in Passage 131, representing \$18.40 **⚠unverified**) and bought protective puts for **99.50** |
| Index multiplier | SPX Index option payoff structure | Index option pays off at a rate of **\$100** per point |
| Trade 1 total credit and pricing | SPX put credit spread, August 24th, 2015 | Verbatim short put price: **\$11840** (Passage 132); received **\$59,200** in cash for short puts |
| Trade 1 performance results | SPX put credit spread, expiring Jan 25th, 2016 | Pocketed initial cash flow of **9450** as trade profit (representing \$9,450 net credit); return of **64.5%** against original risk of **15,550** on the trade |
| Trade 2 entry conditions | SPX, February 6th, 2018 entry | VIX hit rare **40** level intraday; S&P closed at **269514** (Note: transcribed as `269514` in text, representing 2695.14); options chain expiring about **6** months later; entered on **February 6th 2018** |
| Trade 2 strikes and sizing | SPX ATM put credit spread | Sold **five** short puts right below market at **2675**; bought **five** puts **50** points lower at **2625** |
| Trade 2 execution prices | SPX put credit spread, February 6th, 2018 | Sold short puts for **\$113.75**; bought protective puts for **97.95** |
| Trade 2 performance results | SPX put credit spread | Produces positive cash flow in the amount of **\$7,900** |
| Trade 3 entry conditions | SPX, February 28th, 2020 entry | **February 28th** entry (initial COVID crash); options chain expiring about **6** months later (August 21st, 2020) |
| Trade 3 strikes and sizing | SPX ATM put credit spread | Sold **five** short puts at **2950**; bought **five** puts **50** points lower at **2900** |
| Trade 3 performance results | SPX put credit spread, expiring August 21st, 2020 | Net cash flow credit: **8925** (representing \$8,925); capital required / amount at risk: **\$16,75** (Note: transcribed as `$16,75` in Passage 134, representing \$16,075 **⚠unverified**); S&P closed at new all-time high of **339716** (Note: transcribed as `339716` in text, representing 3397.16); pocketed **8925**; return of **55.5%** win |
| Trade 4 performance results | SPX, June of 2020 VIX follow-up | Entered in **June of 2020**; short puts strike was **3,000**; index closed more than **500** points higher **6** months later; resulted in a win of **9275** (representing \$9,275) |
| Trade 5 performance results | SPX, August 5th, 2024 VIX spike | Entered on **August 5th 2024** (Japanese yen carry trade unwinding in **August of 2024**); VIX spiked through **40** level; index closed over **6,000** on expiration day; resulted in a win of **\$5,025** |
| Cumulative strategy results | Combined 5-day performance | Total profit of **\$40,575** for just those **five** days out of the last **10 years**; profit is more than **twice** the risk of any **one** of those trades; could have lost **one** or maybe even **two** of those trades and still come out ahead |
| Strategic educational workshops | General program offerings | Teaches **three** more option strategies; statistical **80 percent** probability of profit month in and month out |

### [q4lILcbWKJ0] The Gamma Squeeze Trading Strategy (in $AMC) (22,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Common stock of AMC (ticker symbol: AMC) [1-3].
    *   **Structure**: Day trading long positions in common stock [3-5]. No options positions were traded by the desk trader in this specific setup [5]; rather, options are discussed as the market-wide driver of the stock's volume [3].
    *   **Strikes/Deltas**: None selected for this trade [5]. The strategy relies on identifying when retail traders are buying out-of-the-money weekly call options to force market makers into delta-hedging [3, 6].
    *   **DTE (Days to Expiration)**: None specified for this trade, though near-expiration weekly options are identified as the catalyst for the squeeze [3, 6].
    *   **Entry Trigger**:
        *   **Wedge Breakout**: Stock breaking out of a larger timeframe wedge on increased volume, pulling back into its weekly range on decreased volume, and moving back over the highs on increasing daily volume [7, 8].
        *   **Pre-Market Pullback / Gap Down**: A morning gap down on low volume (acting as a short trap) that holds pre-market levels and pre-market trend [9].
        *   **Opening Range Range-Play**: A range is developed in the first 15 minutes of the open [9]. If a false breakdown occurs but is quickly bid back up, it signals strong buyers or squeezed-out short sellers [9].
        *   **The Pull-in Setup (Primary Entry)**: The stock pulls into a key support level on decreasing volume [4, 10]. In the detailed trade, the stock pulled into the 18/18.42 level (confluence of the pre-market trend and the previous day's level) on decreasing volume [11]. Bids stacked up at 18.60 and 18.55, and once 18.70 lifted, tape speed and volume expanded to confirm the entry [11, 12].
        *   **Opening Range Breakout**: A breakout of the 15-minute or 30-minute range confirmed by strong, consistent buying volume [5, 10].
        *   **The "See It" Moment (Irrational Support)**: When a stock is up massively and should decline, but drops below intraday support (like 39.50) and fails to trade lower, testing support (like 38.80) multiple times without breaking [13, 14]. This failure to drop indicates that something irrational is happening and the stock is highly likely to trade much higher [14].

*   **The Management and Exit Rules**:
    *   **Stop Loss / Risk Level**: Stop loss must be determined before execution [15]. In the \$18 setup, the stop was placed below the wick low of 18.55 (rather than the low of the day, which was a shakeout) [11, 12].
    *   **Exit Indicators / Selling Rules**:
        *   Decreasing volume as the stock pulls into support [4].
        *   Selling into breakouts of new daily highs or into a sharp price extension (selling into strength) to capture optimal exit prices [4].
        *   Reasons to sell include the stock falling below VWAP, a negative change in character on the tape, a reversal candle, breaking EMAs, a lower high, or a breaking trend [4].
    *   **Scale-Out Technique**: Scale out of the position in pieces (e.g., selling 2/3 of the size) into sharp upward spikes [159 (actually 156, 159)], and stair-step the stop up along the way as price action and volume develop [5]. The trade was scaled out over 21 and into 22.50 into strength, with the final small size exited on a trend break [5, 16].
    *   **Active Sizing**: Use 15% to 30% of total size to add on dips and sell on rips, trading around a core position to maximize risk/reward [16].

*   **The Stated Edge or Statistics**:
    *   **Social Media Sentiment Edge**: Tracking positive/negative sentiment, overall activity, and trending tickers on popular forums like Wall Street Bets using sentiment scanners (like Swaggy Stocks) [17]. AMC climbing to the top three of the trending list signaled massive retail volume [17]. A 20% increase in sentiment and activity caught the trader's attention and signaled a massive retail imbalance [3, 17].
    *   **The Gamma Squeeze Cycle**: Massive retail buying of out-of-the-money weekly calls near expiration forces market makers (the call sellers) to delta hedge by buying the common stock, creating a parabolic buying loop as the stock price rises [3].
    *   **Short Float Coverage**: High short interest/short float (AMC had a 23% short float) adds intense buying pressure as short sellers are forced to buy back stock to cover their losses [3, 18].
    *   **Volume Characteristics**: Volume increases on upticks and decreases on downticks, indicating buyers are in control [10].
    *   **Tape Speed**: The tape speeds up and volume pours in as key levels lift, validating the move [12].

*   **The Caveats the Presenter Gives**:
    *   **Short Bias Danger**: Many elite traders on the desk got into serious trouble by trading a short thesis with too much size because they stubbornly believed the stock "had no business being up in the 40s" or was "only worth six bucks" [19, 20]. Stubborness, arrogance, and trading on emotions rather than price action can lead to catastrophic losses [16, 20].
    *   **Extreme Volatility and "Whippiness"**: AMC is not a "clean trader"; it frequently wicks out at various points, blowing through common stop points to shake traders out of position before continuing its move [157, 158 (actually 157)].
    *   **Regime Shift / Retail Dominance Uncertainty**: No one knows how long the new market regime (where retail traders run stocks and dictate price) will last, so traders must remain open-minded and patient to adjust [21].
    *   **Perfectionism Trap**: Perfectionism is ego-driven; a trader will never have perfect exits. The goal is to minimize the gap between exiting too early and too late by focusing on the setup and developing variables [16].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video views metadata | Video statistics | **22000** views |
| Timing of setup | AMC stock | **about a week ago** |
| Trading book classic | Book title reference | **one** good trade |
| Weekly volatility standard | Volatile stocks (GME, AMC, Triple B Y) | **over 15 percent** range in a week |
| Open interest timeline | Option chain scan | **past two days** |
| Additional setups taught | Free webinar curriculum | Teaches **three** real-world setups |
| Elite trader milestone | Prop firm trader earnings | **seven figure** big money earner |
| Webinar training duration | Free intensive workshop | **a couple of hours** |
| Online educational background | General options education | **years** of online education |
| Squeeze participants | Squeeze mechanics | **three** major players |
| Social media sentiment spike | Ticker sentiment increase on Wall Street Bets | **20** increase in AMC ticker sediment (sentiment activity; note: represents 20%) |
| Sentiment comparison timeline | AMC forum sentiment | **past few months** |
| Short interest float | AMC stock | **23** short float (short float percentage; note: represents 23%) |
| Sentiment tracker rank | Swaggy Stocks trending list | **top three** of that list |
| Sentiment activity spike | Ticker activity increase on Swaggy Stocks | **20** increase in activity in AMC (activity percentage; note: represents 20%) |
| Breakout timeline | AMC daily breakout | **four days prior** |
| Wedge breakout consolidation level | AMC stock | **13** range |
| Progression of price acceleration | AMC stock | **sixteens** (16s), **18s** (18s), **1850** (18.50), up near in the **60s** |
| Chart timeframe | AMC intraday analysis | opening **15** minutes |
| Pre-market chart timeframe | AMC pre-market zoom | **one** minute |
| Breakout timeline | AMC 30-minute range breakout | **30** more minutes into the day |
| Support pullback level | AMC stock day trade | **1850** range |
| Intraday breakout range | AMC chart timeframe | **30** minute range |
| Consolidation period | AMC stock consolidation before second leg | **two hours** |
| Trade session day | Day trade timeline | **day one** |
| Pullback entry inflection point | AMC stock day trade | **18** like **18 1842** level (representing 18.00 - 18.42) |
| Planned risk cut-off level | AMC stock day trade | **1850** level (representing 18.50) |
| Tape reading support levels | AMC stock day trade | **1860** to **1855** level; bids stacked at **1860** and **18.55** |
| Tape acceleration breakthrough points | AMC stock day trade | above **86** (garbled; representing 18.60), **1870** (representing 18.70) |
| Wick low risk point | AMC stock day trade | **18.55** |
| Immediate target price | AMC stock day trade | sell it at **70** |
| Post-trade session peak | AMC stock day trade | traded up to **76** |
| Time elapsed post-trade | AMC stock day trade | **couple** of sessions later |
| Subsequent session price action | AMC stock day trade | traded down this morning into the **40s**; currently trading above **60** |
| Yesterday's volatility range | AMC stock day trade | **yesterday**; range was **42** to **39.50** |
| Support failure test levels | AMC stock day trade | got below **39.50**; couldn't trade below **38.80** |
| Irrelevant stock valuation level | AMC stock | no business being up in the **40s** |
| Target price expectation | AMC stock | go to **100** |
| Squeeze price range magnitude | AMC stock | run from the **teens** to the **40s** |
| Yesterday's see-it moment run | AMC stock day trade | **38 80ish** level (entry point); went to **76** yesterday; closed in the **60s** |
| fundamental asset value vs price | AMC stock day trade | worth **six** (6) bucks; currently at **18** |
| Stock price levels traded through | AMC stock | being at **18**; **42**; **60** dollars |
| Bullish trade execution timeframe | AMC stock day trade | opening **15-minute** range |
| Scale-out price points | AMC stock long | sold over **21**; sold more into **2250** |
| Sizing rules | AMC stock long (trading around core) | **15 to 30 percent** of my size |

### [btgyiIKAqeA] Directional Options Strategies (22,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Google stock options (ticker: GOOG) [1, 2].
    *   **Structure**: Bullish vertical put credit spread. This involves selling a December put option closer to the market price and buying a cheaper December put option at a lower strike price for protection [2, 3].
    *   **Strikes/Deltas**: 
        *   *Initial Setup*: Selling the 620 put option and buying the 615 put option for protection [2].
        *   *Strike Selection Logic*: The short strike is selected by using options analysis software to locate a level 1 standard deviation move downwards (which represents a 64% to 65% statistical probability of the stock staying within that range over the two-month trade duration) [3]. 
        *   *Deltas*: The video does not list specific Delta targets for the initial setup, though it notes the position begins with a relatively flat Delta entry [4] and has a statistical 85% probability of profit [5].
    *   **DTE (Days to Expiration)**: Approximately 2 months to expiration [3]. The November options chain is explicitly avoided because its 3-week duration is "pretty fast" and does not offer enough time premium [3].
    *   **Entry Trigger**: Triggered when a trader has an absolute bullish directional opinion on a stock that has experienced a steep sell-off (such as a 50-point drop in a day on earnings) and has begun to consolidate and channel around a key support level (the 680 area) for several days [1, 6].

*   **The Management and Exit Rules**:
    *   **Winning Exit (Standard Scenario)**: If Google stock rallies, trades sideways, or even sells off slightly but remains above the short 620 strike price at December expiration, all options expire completely worthless [7]. The trader has no further settlement obligations and pockets the initial cash credit as pure profit [7].
    *   **Max Loss Stop-Loss Rule**: The maximum risk management rule is strictly capped at 150% of the initial credit received [5, 8]. If the position's unrealized loss reaches this threshold, the trade must be exited immediately to preserve capital [8].
    *   **Defensive Adjustment (Rolling Down)**: If the stock moves against the trade and breaks key support levels, the trader can roll the position down to a safer strike level [9, 10]. For example, when Google broke its 660 support and dropped to 655/658.50, the trader closed out the initial 620/615 spread (locking in a loss of \$3,800 to \$4,100) and rolled the spread down 15 points to the 605/600 strikes [10, 11].
    *   **Sizing Adjustment on Roll**: When rolling down, there is less time premium remaining in the options chain [11]. To make back the locked-in loss, a directional bullish trader can judiciously increase their contract lot size slightly (e.g., by 25%) when re-establishing the position [11]. Bumping the lot size must be done conservatively and only if the trader remains directionally bullish [11, 12].
    *   **Single Adjustment Limit**: The strategy permits adjusting the trade only *once* [12]. Doing a second adjustment is highly dangerous because there will be almost no premium left near expiration, and if the market moves against you twice, the directional thesis is simply wrong [12].
    *   **Final Week Position Closing Decision**: Near expiration, if the short options have decayed to a very low price (e.g., 3 cents, which represents \$375 for the position), the trader faces a decision [13]. While most traders let them expire worthless to capture the last few dollars, a conservative trader will pay to close the short options to completely remove the massive tail risk (such as a \$54,000 loss exposure on a catastrophic 100-point gap down) [13].

*   **The Stated Edge or Statistics**:
    *   **High Statistical Probability**: Because the short options are located 1 standard deviation away from the market price, the strategy has an 85% statistical probability of profit [5, 7].
    *   **Extreme Wiggle Room (Forgiveness Edge)**: Unlike stock trading where being wrong immediately loses money, a credit spread allows a trader to be "wrong, wrong, wrong" and still win [14]. Even if the trader never adjusted the initial 620/615 spread, they would have won 100% of their initial credit because Google (entered at 677) never breached the 620 short put strike before expiration [14].
    *   **Volatility and Time Decay Edge**: Gradually rising stock prices cause option implied volatility to contract and premiums to melt away, which benefits the options seller [15]. Time decay (Theta) also accelerates as expiration approaches, bleeding value out of the short options much faster than the protective long options [16, 17].

*   **The Caveats the Presenter Gives**:
    *   **High Margin/Capital Requirements**: Credit spreads require significant capital or margin in the broker account (e.g., \$43,000 of risk margin for the initial 620/615 setup) [7].
    *   **Whippiness and Overnight Gap Risk**: Volatile stocks carry rapid drawdown risks [5]. If Google dropped to 620 the day after entry, the trade would quickly run into a \$16,000 paper loss, making risk discipline and adherence to stop-losses paramount over technical charts [5, 18].
    *   **No Free Lunch**: The high probability of winning is directly paid for by capping the maximum reward to the initial premium collected, while accepting a lopsided maximum loss profile if the trade is unmanaged [19].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Background market news feed [20] | News ticker background audio overlay | **3.17 billion EUR** revenue; **4.2%** year-over-year; **4.8%** third quarter sales; down about **a%** (verbatim) on the day; **4 pennies** |
| Google earnings selloff [1] | GOOG Stock historical chart (October 2012) | **50p point** (verbatim, representing 50-point) drop in a day; **680** area |
| Google support target [21] | GOOG Stock historical chart | **670** support level |
| Timeframe avoidance [3] | GOOG Options, November chain | **3 weeks** |
| Statistical range calculation [3] | GOOG Options, 1 standard deviation | **6 65%** (garbled/verbatim) chance; **64 65%** chance |
| Volatility calculation [3] | GOOG Options volatility input | **21.7** volatility |
| Period of trade [3] | GOOG Options trade duration | next **two months** |
| 1 Standard deviation downside limit [2] | GOOG Options, December chain | down to **62140** (representing 621.40); **minus one** (-1) standard deviation |
| 2 Standard deviation safety target [2] | GOOG Options, December chain | **two** standard deviations out; price level of **569** |
| Spread entry timing [2] | GOOG Put Credit Spread | **4:00** regular trading session close |
| Initial trade setup [2] | GOOG Put Credit Spread, December | **620** and **615** strikes |
| Short option premium [2] | GOOG Put Credit Spread (620 short) | price of **five \$5.90** (garbled/verbatim, representing \$5.90) |
| Initial protective capital requirement [2] | GOOG Put Credit Spread (unprotected hypothetical naked risk) | paid **\$59,000** as protection (representing naked option capital obligation) |
| Sinking margin hazard [2] | GOOG Put Credit Spread | drop down into **570** |
| Total naked cash collection [7] | GOOG Put Credit Spread (unprotected hypothetical naked credit) | take home **\$59,000** |
| Initial credit spread net premium [7] | GOOG December 620/615 Put Credit Spread | paid initially **\$6,350** for selling the 620s and buying the 615s; got my **6350** |
| Total capital risk of initial spread [7] | GOOG December 620/615 Put Credit Spread | took exactly **\$443,000** of risk (garbled/verbatim, representing \$43,000) |
| Baseline stock price at entry [7] | GOOG December 620/615 Put Credit Spread | trading at **677** |
| Initial probability of profit [5, 7] | GOOG December 620/615 Put Credit Spread | **78%** probability of profit; corrected to **85%** probability of profit |
| Strategy risk-reward baseline [7] | GOOG December 620/615 Put Credit Spread | reward of **6,000** bucks; risk of **43** (representing \$43,000 margin) |
| Required expiration threshold [5] | GOOG December 620/615 Put Credit Spread | at least **\$620 in one cent** |
| Gap down risk scenario [5] | GOOG December 620/615 Put Credit Spread | out about **\$16,000** if it dropped to 620 the next day |
| Strategy adjustment threshold [5, 8] | GOOG December 620/615 Put Credit Spread | maximum loss is **150%** of our credit; credit of **6300** / **6,300**; maximum loss number is **\$99,500 roughly** (garbled/verbatim, representing \$9,500); at **9500** I am out |
| November 19 review details [8, 15] | GOOG December 620/615 Put Credit Spread | checked at **12:30 on the 19th of November**; Google at **687** on **November 1st**; up **\$2,300** on the trade |
| November 8 support break details [9, 22] | GOOG December 620/615 Put Credit Spread | checked on **November 8th** at **12:30**; Google trading at **65850**; second to bottom gain/loss line only down **3,300** / down **\$3,300** |
| Max stop comparison [9] | GOOG December 620/615 Put Credit Spread | stop level of **9500 bucks** |
| Roll calculation variables [10, 23] | GOOG Put Credit Spread Roll | calculated at **130** (1:30 PM); Google trading at **655** / support at **660**; initial short strike at **620**; market moved down **17 points** |
| Adjusted 1 standard deviation target [10] | GOOG Put Credit Spread Roll | new level **605**; new standard deviation move from this point is **65** (garbled/verbatim, representing 605) |
| Rolled trade strikes [10] | GOOG December 605/600 Put Credit Spread | moved down **15 points** to the **605 600** strikes |
| Lot size roll bump [11] | GOOG December 605/600 Put Credit Spread | bumped size **25%**; locked in **3,800** / **4,100** loss on the closed 620/615 spread |
| New adjusted max profit [11] | GOOG December 605/600 Put Credit Spread | best we can now do is **4,138** / **4,100** |
| Original profit target [11] | GOOG December 620/615 Put Credit Spread | target closer to **4700** |
| Settle in place scenario [24] | GOOG December 620/615 Put Credit Spread | market at **660**; position at **620** (**40 points** below market); keep entire **60 6350** (garbled/verbatim) / **6350**; take **third** less potential profit |
| Pre-expiration rally check [16] | Adjusted GOOG Put Credit Spread | market at **682**; **15 days to go**; up **30 325** (garbled/verbatim) / **3325**; max adjusted profit limit **4138** |
| Final week pricing decay [13] | Adjusted GOOG Put Credit Spread | short option at **65 cents**; credit worth **three cents** |
| Catastrophic tail risk [13] | Adjusted GOOG Put Credit Spread | **554,000** of risk (garbled/verbatim) / **\$54,000** of risk / **59 sorry uh \$54,000** of risk (garbatim/verbatim) if Google drops **100 points** in the **next four days** |
| Position buyback cash value [13] | Adjusted GOOG Put Credit Spread | **3 cents times 12,500** contracts / **375** / **additional 375** |
| Consolation wrong-way win [14] | GOOG December 620/615 Put Credit Spread | if Google fell to **630** (entered at 677); still win **\$6,300** / **63 50** |
| Probability score [25] | GOOG December Put Credit Spread | win probability is **85%** |

### [avvWq9V95AQ] The Short Risk Reversal Options Strategy (16,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

#### The Setup
*   **Instrument**: Common stock options of Nvidia (ticker symbol: nvidia) [1].
*   **Structure**: A modified version of a short risk reversal trade [2]. The structure combines selling an out-of-the-money put option, buying a protective put option further out of the money, and buying an out-of-the-money call option [2, 3].
*   **Strikes/Deltas**: 
    *   **Short Put**: **185** strike [3].
    *   **Long Put (Protection)**: **110** strike (located exactly **75** points below the short put strike) [3].
    *   **Long Call**: **205** strike at initial setup [3] (later referred to in the cash flow math and losing consolidation scenarios as the **210** strike call [2, 4], and during the winning exit walkthrough as the **185** strike call [5]).
    *   *Deltas*: Specific Delta numbers for the strikes are not spoken, though the setup is styled as a bullish directional trade [2, 3].
*   **DTE (Days to Expiration)**: Approximately **three** months to expiration [3].
*   **Entry Trigger**: Entered on **August 18th** when Nvidia is trading around **192** [3]. The trigger is based on a bullish thesis over a short time horizon [6]. Nvidia had rallied off its COVID-19 crash lows below **50** all the way up to **190**, alternately rallying and consolidating [1]. During the summer of 2021, the stock consolidated and channeled between **175** and a little over **200** [1, 6]. The entry is triggered by the technical expectation that the stock is consolidating around its highs and is highly likely to break out of this summer consolidation channel [6].

#### The Management and Exit Rules
*   **Trade Management**: The trade is managed passively as a defined-risk spread held to November monthly expiration [3, 5].
*   **Winning Exit Scenario (Breakout/Rally)**: If the stock rallies strongly (e.g., breakout to **252** on October 26th [5] and running all the way to **329.85** on November 19th expiration [5]):
    *   Both the short and long puts expire worthless since the stock closed well above both strikes [5].
    *   The long call is exercised at its strike price (exercised at **185** in the presenter's walkthrough), costing **18,500** to buy 100 shares [5, 7].
    *   The shares are simultaneously sold in the open market at the **329.85** price, yielding proceeds of **32,985** [7].
    *   This walkthrough results in a total net profit of **14,593** dollars and **85** cents [7].
*   **Neutral/Wrong Scenario (Stock Stagnates/Drops Slightly)**: If the stock doesn't rally and instead closes at **186** at expiration, all three options expire worthless [4].
    *   Both the 185 and 110 puts expire worthless because the stock closed above both strikes, and the long call also expires worthless [4].
    *   In this scenario, the trader still pockets the original cash flow credit of **108** dollars as profit [4].
*   **Losing Exit Scenario**: If the stock collapses below the protective long put (110 strike), the maximum loss is strictly capped at the required capital level, as the protective put puts a floor on the trade and prevents further drawdowns [2, 8].

#### The Stated Edge or Statistics
*   **Upfront Positive Cash Flow**: Entering the trade generates an immediate positive cash flow credit of **108** dollars deposited directly into the trader's account [2].
*   **Highly Capital Efficient**: Executing the options trade requires at least **7,392** (or **7,400**) in account capital to support the transaction [2, 7], which is far less than the **in excess of 19,000** required to buy 100 shares of Nvidia outright at entry [7].
*   **Room to be Wrong (Forgiveness Edge)**: Unlike a common stock purchase—which would lose **638** dollars if the stock dropped from entry to 186 [4]—the modified risk reversal trade still yields a profit of **108** dollars in the same scenario [4].
*   **Leveraged Explosive Return**: Yields a **197** percent return on original capital if the bullish thesis is correct [7].

#### The Caveats the Presenter Gives
*   The required capital of **7,392** (or **7,400**) represents the trade's absolute worst-case scenario maximum loss [2, 7].
*   Options trading carries risks, and traders must use intelligently structured defined-risk strategies to avoid taking excessive risk [8].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistic [9] | Nvidia, modified risk reversal trade, November expiration | **16000** views |
| Stock prior historical crash lows [1] | Nvidia common stock | below **50** |
| Stock prior historical rally peak [1] | Nvidia common stock | all the way up to **190** |
| Consolidation period year [6] | Nvidia, summer consolidation | **2021** |
| Consolidation channel lower boundary [6] | Nvidia, summer consolidation | **175** |
| Consolidation channel upper boundary [6] | Nvidia, summer consolidation | a little bit over **200** |
| Strategies count in workshop [6] | General options income workshop | **three** more option strategies |
| Call option contract multiplier [10] | General stock call option | purchase **100** shares |
| Put option contract multiplier [10] | General stock put option | sell **100** shares |
| Entry date of trade [3] | Nvidia, modified risk reversal | **august 18th** |
| Stock price at entry [3] | Nvidia stock price on August 18th | trading around **192** that day |
| Expiration month [3] | Nvidia, modified risk reversal | expires in **november** |
| Options expiration duration [3] | Nvidia, modified risk reversal | about **three** months out |
| Short put strike price [3] | Nvidia, November short put | strike of **185** |
| Short put premium credit [3] | Nvidia, November short put | sold for **11.** and **30** cents (receive **11.30**) |
| Distance between put strikes [3] | Nvidia, put credit spread component | **75** points below |
| Long protective put strike price [3] | Nvidia, November long put | strike of **110** |
| Long protective put premium cost [3] | Nvidia, November long put | cost of **52** cents |
| Long call strike price (initial setup) [3] | Nvidia, November long call | strike of **205** |
| Long call premium cost (initial setup) [3] | Nvidia, November long call | cost of **9.73** |
| Total short put credit received [2] | Nvidia, November 185 short put | total cash inflow of **1 130** |
| Total long put cost paid [2] | Nvidia, November 110 long put | cost of **52** dollars |
| Long call strike price (math calculation context) [2] | Nvidia, November long call | strike of **210** |
| Long call premium cost (math calculation context) [2] | Nvidia, November long call | cost of **9.73** |
| Net entry cash flow credit received [2] | Nvidia, November modified risk reversal | positive **108** dollars net credit |
| Required broker account capital / worst-case risk [2] | Nvidia, November modified risk reversal | at least **7 392** dollars (worst case scenario) |
| Breakout date of stock [5] | Nvidia common stock | **october 26th** |
| Stock price on breakout date [5] | Nvidia common stock on October 26th | all-time high of **252** dollars |
| Options expiration date [5] | Nvidia, November modified risk reversal | **november 19th** |
| Stock price at options expiration [5] | Nvidia, November modified risk reversal expiration | run all the way to **329.85** |
| Expiration put options boundary threshold [5] | Nvidia, November short/long puts | trading up over **300** |
| Long call strike price (winning exit exercise context) [5] | Nvidia, November long call exercise | **185** call that we bought (Note: verbal slip/discrepancy by presenter) |
| Capital cost to exercise call option [7] | Nvidia, November 185 long call exercise (100 shares) | cost of **18 500** |
| Share sale proceeds at expiration [7] | Nvidia, November long call exercise share sale | proceeds of **32985** (Note: written as `32985.` in transcript) |
| Winning trade net profit [7] | Nvidia, November modified risk reversal | profit of **14 593** dollars and **85** cents |
| Winning trade return percentage on capital [7] | Nvidia, November modified risk reversal | return of **197** percent |
| Winning trade original capital laid out [7] | Nvidia, November modified risk reversal | capital of **7400** |
| Capital cost to buy shares outright at entry [7] | Nvidia stock purchase of 100 shares at entry | in excess of **19 000** |
| Stock close in hypothetical losing timing scenario [4] | Nvidia common stock at expiration | closed at **186** |
| Puts expiration state in losing timing scenario [4] | Nvidia, November 185 short put & 110 long put | both puts expire worthless below **186** |
| Call expiration state in losing timing scenario [4] | Nvidia, November 210 long call | call expires worthless |
| Options net profit in losing timing scenario [4] | Nvidia, November modified risk reversal | original **108** dollars in cash flow profit |
| Outright shares purchase count [4] | Nvidia common stock bought at entry | buying **100** shares of nvidia |
| Outright shares loss in losing timing scenario [4] | Nvidia stock purchase of 100 shares at entry | lost **638** |

### [D4sAWnZIohg] You Can Only Be A Successful Options Trader If You DO THIS! (16,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX index) [1, 2].
    *   **Structure**: Bullish vertical call debit spread (buying a call option at a lower strike price and simultaneously selling a call option at a higher strike price) [1].
    *   **Strikes/Deltas**: 
        *   Long Call Strike: **2980** (transcribed as "the 2980 call" and "29 80 call") [2, 3].
        *   Short Call Strike: **2990** [1, 2].
        *   *Deltas*: Specific Delta selection targets are not explicitly discussed in the provided passages of this video.
    *   **DTE (Days to Expiration)**: Not explicitly defined for the setup, but the detailed walkthrough represents a trade held up to the final day of expiration [1, 3].
    *   **Entry Trigger**: Not defined by indicators. Triggered when a day or swing trader has a bullish directional thesis and wants to express it using a defined-risk option surrogate instead of trading underlying index contracts [1, 4].

*   **The Management and Exit Rules**:
    *   **The 90% Profit Target Rule (Primary Exit)**: A professional options trader must remain focused on risk-reward relationships and close a credit or debit spread when it has achieved **90 percent** of its maximum profit potential [3, 5].
    *   **Intraday Profit-Taking (Close-out)**: On the final day of the trade at around **1:00 p.m.**, if the SPX index is trading at **30 15** (well above the **2990** short strike), the debit spread can be closed early for a mid price of **\$9.50** [2]. The trader sells the long 2980 call for **36 55** and buys back the short 2990 call for **2705** [2]. Subtracting the original **\$400** cost, this locks in a **\$550** profit [2].
    *   **The Risk of Holding to Expiration**: If the trader remains unhedged and greedy to squeeze out the remaining **50** of profit, the risk-reward relationship shifts unfavorably. The trader begins risking **\$950** (the **\$550** paper profit plus the **\$400** original cost) to win a meager **50** [2].
    *   **Unmanaged Expiration Outcome (Losing Exit)**: If the index pulls back on the final afternoon and closes at **29 80 40**, the short call expires worthless and the long 2980 call is worth only **\$40** [3]. This leaves the amateur trader with a net loss of **\$360** (after subtracting the **\$400** cost) [3].
    *   **GTC Limit Order Automation**: To maintain discipline and prevent greed, traders should place a Good-to-Cancel (GTC) limit order to sell the spread at **\$9.50** (or **\$9 and 50 cent**) immediately after paying **\$400** for it at entry [5]. The broker will then fill the order automatically when the market hits the target price [5].

*   **The Stated Edge or Statistics**:
    *   **Risk-Reward Efficiency**: Closing the trade at 1:00 p.m. yields a **\$550** profit, whereas holding to expiration yields a **\$360** loss, resulting in a net difference of **9:10** (representing \$910 **⚠unverified**) between the two outcomes [3, 5].
    *   **Defined, Capped Risk**: The maximum loss is strictly defined and capped at the original debit paid (e.g., **\$400**) [1, 2].
    *   **High Probability Webinar Baseline**: The video highlights a prop-taught options income strategy that features a statistical **80 percent** probability of profit month in and month out [1].

*   **The Caveats the Presenter Gives**:
    *   **Risk-Reward Shift**: Risk-reward ratios do not remain static and must be actively monitored. Holding a spread for the last remaining premium destroys the edge and skews the math of long-term trading expectancy [2, 5].
    *   **Emotional Accepting of Losses**: Beginners must learn that losses are a normal part of options trading and avoid getting emotionally despondent when trades fail [5].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Target audience potential earnings | General firm traders | "**seven** and even **eight** figure per year traders" [6] |
| Hypothetical max profit ceiling | SPX Bull Call Debit Spread, 2980/2990 strikes | maximum profit of **\$600** (regardless of how high index rises) [1] |
| Runaway index price point | SPX Bull Call Debit Spread, 2980/2990 strikes | index goes to **4,000 even** [1] |
| Spread width profit calculation | SPX Bull Call Debit Spread, 2980/2990 strikes | short call caps long call gains at **\$1,000** less than payout [1] |
| Long call gain in runaway scenario | SPX, Long 2980 Call, expiring at 4,000 | makes **\$12,000** on the long call [1] |
| Short call liability in runaway scenario | SPX, Short 2990 Call, expiring at 4,000 | pay out **\$11,000** on the short call [1] |
| Spread entry debit cost | SPX Bull Call Debit Spread, 2980/2990 strikes | original cost will always be **400** / **\$400** / **400 dollar** [1, 2, 5] |
| Expiration profit-taking price floor | SPX Bull Call Debit Spread, 2980/2990 strikes | index closed at any price above **2990** on expiration [1] |
| Spread strike width points | SPX Bull Call Debit Spread, 2980/2990 strikes | **10** points in the money on long call at 2990 [1] |
| Long call value at short strike expiration | SPX, Long 2980 Call at 2990 index close | worth **\$1000** [1] |
| Short call strike price | SPX, Short Call | **2990** call [1] |
| Promoted intensive workshop duration | General Options Income Strategies | "**2** our" (garbled/typo for 2 hour) free intensive workshop [1] |
| Promoted intensive workshop strategies count | General Options Income Strategies | Teaches **three** of those strategies [1] |
| Workshop high-probability win rate | High-probability options income strategy | statistical **80 percent** probability of profit [1] |
| Trade check-in time of day | SPX Bull Call Debit Spread, final day | reviewed at around **1:00 p.m.** [2] |
| SPX index price level at check-in | SPX Bull Call Debit Spread, 1:00 p.m. | trading at **30 15** [2] |
| Maximum profit short strike target | SPX Bull Call Debit Spread | maximum profit level of **2990** [2] |
| Spread market value at 1:00 p.m. | SPX Bull Call Debit Spread | worth **\$9.50** [2] |
| Long call market price at 1:00 p.m. | SPX, Long 2980 Call, 1:00 p.m. | trading at **36 55** [2] |
| Short call market price at 1:00 p.m. | SPX, Short 2990 Call, 1:00 p.m. | trading at **2705** [2] |
| Open paper profit at check-in | SPX Bull Call Debit Spread, 1:00 p.m. | paper profit would be **\$550** / up **550** [2] |
| Remaining potential profit | SPX Bull Call Debit Spread, 1:00 p.m. | remaining profit is **50** extra bucks / **50** / **50 dollars** [2] |
| Downside support level break | SPX Bull Call Debit Spread | sells off down below **29 80** / **28 980** (garbled/typo) [2] |
| Total capital risk of holding at 1:00 p.m. | SPX Bull Call Debit Spread, 1:00 p.m. | new risk is **950 dollars** of risk [2] |
| Re-calculated risk reward reward target | SPX Bull Call Debit Spread, 1:00 p.m. | reward of **50 dollars** [2] |
| Extreme downward gap level | SPX Bull Call Debit Spread | sells off to below **20 980** (garbled/typo) [2] |
| Closed profit percentage | SPX Bull Call Debit Spread | attained **90 percent** of maximum profit potential [3] |
| SPX index closing price at expiration | SPX Bull Call Debit Spread, 4:00 p.m. close | closed at **29 80 40** (representing 2980.40) [3] |
| Long call strike price | SPX, Long Call | long call at **29 80** [3] |
| Long call closing value at expiration | SPX, Long 2980 Call, close | worth **\$40** [3] |
| Unmanaged trade expiration net loss | SPX Bull Call Debit Spread, held to close | loss of **\$360** on the trade [3] |
| Outcome P&L difference | Professional vs. Amateur | difference of **9:10** (representing \$910 **⚠unverified**) between outcomes [5] |
| Automated order sell limit price | SPX Bull Call Debit Spread | GTC order right at **\$9.50** / **\$9 and 50 cent** [5] |

### [yHOAgcUIR0k] Easy, Repeatable Options Trades (How to Find Them) (15,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: QQQ ETF (the exchange-traded fund that mirrors the NASDAQ 100 index) [1, 2].
    *   **Structure**: Iron Butterfly options strategy [3].
    *   **Strikes/Deltas**: 
        *   Short call strike: **286** [4].
        *   Long call strike: **293** [4].
        *   Short put strike: **286** [4].
        *   Long put strike: Not explicitly named as a specific strike number in the transcript, though both puts are described as expiring below the market price [4].
        *   *Deltas*: No specific Delta metrics are spoken in the transcript.
    *   **DTE (Days to Expiration)**: Initiated on the **Wednesday before Thanksgiving** and closed on the **Friday after Thanksgiving** (a **two-day** trade duration) [3, 4].
    *   **Entry Trigger**: A seasonal holiday-based pattern where the trader enters the trade on the Wednesday before Thanksgiving when the market is expected to remain quiet [3, 5].

*   **The Management and Exit Rules**:
    *   The trade is designed to be closed out on the **next trading day around 1 pm on Friday**, which is a half-day market session [3].
    *   **Exit Execution**: The long calls (293 strike), the short puts (286 strike), and the protective long puts all expire with no value at expiration (with QQQ closing at 286.92) [4]. The trader buys back the short 286 calls right before they close for **about 92 cents** to fully exit the position [4].

*   **The Stated Edge or Statistics**:
    *   **High Short-Term Yield**: The case study trade produced a **71 percent return** in just **two trading days** [4].
    *   **Collaborative Edge**: Developed through systematic ideas shared within the "options tribe trading team," which is a group of **about 50 options traders** who communicate in Slack and present trade plans **every Tuesday** [4, 6].
    *   **Low Volatility Harvesting**: The trade capitalizes on the market going extremely quiet and range-bound during the Thanksgiving holiday period [3].

*   **The Caveats the Presenter Gives**:
    *   **Historical Drawdowns**: Backtests show that the strategy is subject to some "first few rough years" and has occasional large drawdown potential [5].
    *   **Strict Capital Limits**: Because of the potential for large drawdowns, the presenter strongly advises students never to commit large amounts of capital to the strategy, but rather to treat it as a smaller, non-core component of an overall trading portfolio [5].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | QQQ Thanksgiving Iron Butterfly | **15000** views [7] |
| Prop firm trader earnings milestones | General firm context | "**seven** and even **eight** figure per year Traders" [8] |
| QQQ ETF underlying index | QQQ ETF target | S&P 500 ETF (SPY) vs. QQQ which tracks the NASDAQ **100** index [1, 2] |
| Equity options standard sizing | General options review | entitles the buyer to buy or sell **100** shares [2] |
| Trade exit timing | QQQ Iron Butterfly, Thanksgiving | "**next trading day around 1 pm on Friday**" (which is a half day Market session) [3] |
| QQQ index price at expiration | QQQ Iron Butterfly, closed Friday after Thanksgiving | closed at **286.92** [4] |
| Initial credit received | QQQ Iron Butterfly, Thanksgiving | "**original 8675 of cash flow**" [4] |
| Option contract components count | QQQ Iron Butterfly, Thanksgiving | "**three of the four options** expired with no value" [4] |
| Upper long call strike | QQQ Iron Butterfly, Thanksgiving | long calls up at **293** [4] |
| Short call strike price | QQQ Iron Butterfly, Thanksgiving | short calls of **286** [4] |
| Short call buyback price | QQQ Iron Butterfly, Thanksgiving | buy back right before close for "**about 92 cents**" [4] |
| Trade return percentage on investment | QQQ Iron Butterfly, Thanksgiving | "**71 percent** return" [4] |
| Trade holding duration | QQQ Iron Butterfly, Thanksgiving | "**two** trading days" [4] |
| Options tribe collaborative team size | General options tribe | group of "**about 50 options traders**" [4] |
| Options tribe presentation schedule | General options tribe | "**every Tuesday**" [6] |
| Backtested drawdown timeline | QQQ Thanksgiving Iron Butterfly | "**first few rough years**" [5] |
| Ideal seasonal strategy basket | General seasonal strategy playbook | "**four or five** other short-term seasonal trades" [5, 9] |

### [2qIkQUHUmJM] How I Buy Stocks At Huge Discounts (with Options) (15,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Deep in the money call options on stocks you love (like Tesla or Caterpillar), acting as stock surrogates [1, 2].
    *   **Structure**: A synthetic stock position or stock surrogate created by buying deep in the money call options instead of outright stock shares [1, 2].
    *   **Strikes/Deltas**: 
        *   *Tesla setup*: Buying a **75** strike call when the stock trades at **12315** (approx. \$123.15 **⚠unverified** per share) [1]. The strike is selected deep in the money such that the option is priced at "about half the stock price" [1]. Specific Deltas are not explicitly defined in the video, but the high delta of deep in the money calls allows them to move "almost like 300 shares of stock" proportionately [3].
    *   **DTE (Days to Expiration)**: Approximately one year to expiration (e.g., expiring on **December 15th** when entered on **December 23rd**) [1].
    *   **Entry Trigger**: Activated when high-quality stocks that are solid long-term investments experience "oversold conditions" (such as the weekly chart RSI closing **below 30**) [1] or during major market-wide crashes (such as the beginning of "CO 19" in **March of 2020** when most stocks were crashing) [3].

*   **The Management and Exit Rules**:
    *   **Holding Period**: The trade is held passively to allow the stock to undergo its anticipated long-term bounce and recovery [3].
    *   **Winning Exit**: If the stock rallies sufficiently, the call options capture almost all of the stock's absolute upward dollar move, but on less than half the capital, resulting in a significantly higher percentage return (e.g., the Tesla call yielded a **191%** return) [3].
    *   **Losing Exit**: If the trade thesis fails and the stock drops further, the maximum possible loss is strictly defined and capped at the initial premium paid for the calls, which is less than half the capital required for outright share purchases [1, 3].
    *   No active rolls or adjustments are detailed in this specific transcript [1, 2].

*   **The Stated Edge or Statistics**:
    *   **Massive Capital Efficiency**: Buying deep in the money call options allows a trader to control the same quantity of shares for less than half the cash outlay compared to stock shares (e.g., **\$6,113** for the Tesla call vs. **\$12,315** for 100 shares of stock) [1, 3].
    *   **Outsized Percentage Returns**: The leverage of deep in the money calls causes them to "blow the returns on the shares away in almost all cases" during a rally (e.g., a **191%** return on the Tesla call, and "very nearly double" the profit on two Caterpillar calls compared to shares) [2, 3].
    *   **Massive Risk Reduction**: Tying up less than half of the stock's capital shields the trader from extreme downside exposure compared to outright stock ownership [1, 3].

*   **The Caveats the Presenter Gives**:
    *   The strategy requires the stock to rally sufficiently for these stellar returns to emerge [3].
    *   The absolute dollar profit of the calls can be slightly less than outright stock ownership (e.g., **11,697** on the Tesla call vs. slightly higher on stock) [3].
    *   If the stock completely collapses, the option premium paid will be entirely lost [1].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistic | `[2qIkQUHUmJM]` title card [4] | **15000** views |
| Call surrogate purchase discount | Tesla / Caterpillar deep ITM call setup [5] | up to a **50%** discount |
| Proprietary desk trader earnings milestones | General firm context [5] | **seven** and even **eight** figures per year |
| Market bounce portion | S&P 500 Index behavior [5] | regaining about **half** of what it lost |
| Target entry RSI oversold trigger level | Tesla, Deep ITM Call [1] | closing below **30** |
| Trade entry date | Tesla, Deep ITM Call [1] | **December 23rd** |
| Stock price at entry | Tesla, Deep ITM Call [1] | **12315** (representing \$123.15 **⚠unverified** per share) |
| Expiration date of options contract | Tesla, Deep ITM Call [1] | **December 15th** (almost exactly a year later) |
| Sizing ratio of option premium | Tesla, Deep ITM Call [1] | priced about **half** the stock price; a little less than **50%** of the price of the shares themselves |
| Strike price of the call option | Tesla, Deep ITM Call [1] | **75** call |
| Option contract price / premium | Tesla, Deep ITM Call [1] | priced at **6113** |
| Sizing / share count multiplier | Tesla, Deep ITM Call [1] | represents the right to buy **100** shares |
| Capital cost of outright share purchase | Tesla, 100 shares [1] | **12,315** |
| Total capital cost / premium of call option | Tesla, 75 strike call [1] | **\$6,113** |
| Option capital required fraction | Tesla, 75 strike call [1] | cost less than **half** of that |
| Strike price identification | Tesla, Deep ITM Call [1] | at **75** |
| Option contract multiplier factor | Tesla, Deep ITM Call options pricing math [1] | So the price is **multiplied by 10** (verbatim) |
| Call option absolute dollar profit | Tesla, Deep ITM Call performance [3] | **11,697** |
| Call option capital outlay fraction | Tesla, Deep ITM Call performance [3] | **less than half** |
| Call option return percentage on capital | Tesla, Deep ITM Call performance [3] | a fantastic **191%** |
| Target stock timing indicator | Caterpillar, Deep ITM Call [3] | beginning of CO **19** (verbatim) in **March of 2020** |
| Caterpillar trade overall profit | Caterpillar, Deep ITM Call [2] | over **\$23,000** in profit |
| Caterpillar outright share profit | Caterpillar stock purchase benchmark [2] | **12,565** profit |
| Caterpillar calls contract count | Caterpillar, Deep ITM Call [2] | **two** calls |
| Caterpillar call trade profit | Caterpillar, Deep ITM Call [2] | **24,960** |
| Caterpillar calls profit ratio | Caterpillar, Deep ITM Call [2] | very nearly **double** |
| General promo option strategies | Intensive workshop curriculum [2] | **three** more option strategies |

### [H_2YWD0dUFM] An effective technique for turning losing options trades into winners (14,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX index) [1, 2].
    *   **Structure**: **Iron Butterfly** options strategy [2, 3].
    *   **Strikes/Deltas**: 
        *   *Center/Short strike*: Sold both the short call and the short put at the money at **31.35** (also referred to as **3135**) [2, 4, 5].
        *   *Initial Long Put*: Long put at the **3110** strike [5, 6].
        *   *Initial Long Call*: Long call at the **thirty one fifty five** (3155) strike [2, 6].
        *   *Deltas*: No specific Delta targets or values are spoken in this transcript.
    *   **DTE (Days to Expiration)**: A short-term or same-day trade ("what options traders call a one-day trade") designed to expire "at the end of the day" [1, 2].
    *   **Entry Trigger**: Entered on sleepy, slow trading days, typically in the middle of the summer when regular day traders struggle to find opportunities, expecting the market to consolidate and remain in a tight range [1, 3].

*   **The Management and Exit Rules**:
    *   **Prudent Risk Management / Defensive Adjustment**: If the market moves aggressively in one direction and breaks out of the range (specifically dropping below the lower downside boundary of **31.15** around **3:30 PM**), the trader performs an adjustment instead of being a "sitting duck" [4-6].
    *   **Adjustment Action (Put Side Butterfly)**: The trader buys a put-side butterfly to repair the trade [5]. This is executed by:
        *   Buying back the short **3135 put** to negate and close the short position [5].
        *   Selling **two** puts at the **3110 strike** (which closes the original long 3110 put and sells a new 3110 put) [5].
        *   This rolls the short put position out of harm's way from 3135 down to 3110 [6].
    *   **Unadjusted Trade Outcome**: If left unmanaged, the calls expire worthless, but the short 3135 put closes **21.60 in the money**, requiring a payout of **2160** [6]. After subtracting the initial **two thousand dollars** credit, this results in a net loss of **160** dollars [6].
    *   **Adjusted Trade Outcome**: By rolling the short put down to 3110, both puts expire completely worthless since the index closes above 3110 (at 3113.40) [6]. This preserves the trade and turns a losing position into a net profit of **582 dollars** [6].

*   **The Stated Edge or Statistics**:
    *   **Wiggle Room and Safety**: The initial range of profitability spans **20 points** above or below 31.35 (from 31.15 to 31.55) [2, 4].
    *   **Turning Losers into Winners**: Prudent adjustments allow options traders to defend their range and repair a trade that goes south [3, 7].
    *   **Time Decay harvesting**: Options income trading strategies benefit from time premium decay [1, 7].
    *   **Workshop Promoted Edge**: Teaches three professional options strategies, including one with a statistical **eighty percent** probability of profit month in and month out [8].

*   **The Caveats the Presenter Gives**:
    *   **Binary/Double-Sided Risk**: At the end of the day, except for a rare fluke closing precisely at the center strike, the trader will always owe money under either the short call or short put because it is binary (market must close either above or below 31.35) [4].
    *   **Risk of No Action**: If the market makes a significant move outside of the range and the trader does not adjust, they are a "sitting duck" and will lose money on the trade [3, 4, 6].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | General video metadata | **14000** views [9] |
| Equity options contract size explanation | General Equity Options | purchase or sell **100** shares [1] |
| Promoted intensive workshop duration | General Options Income Strategies | "**two-hour** free intensive workshop" [8] |
| Promoted intensive workshop strategies count | General Options Income Strategies | Teaches **three** of those strategies [8] |
| Workshop high-probability win rate | High-probability options income strategy | statistical **eighty percent** probability of profit [8] |
| Initial Iron Butterfly center / short strike | SPX Iron Butterfly | opening price of **31.35** (also referred to as **3135** or **3135 put**) [2, 5, 6] |
| Initial Iron Butterfly range of profitability | SPX Iron Butterfly | **31.15** to **thirty one fifty five** (3155) [2] |
| Win likelihood in unmanaged Iron Butterfly | SPX Iron Butterfly | in more than **ninety nine percent** of the cases [2] |
| Profitability range width | SPX Iron Butterfly | **20** points above or below 31.35 [4] |
| Check-in/Adjustment time of day | SPX Iron Butterfly | "**3 30** that day" (representing 3:30 PM) [5] |
| Adjustment put contract sale sizing | SPX Put Side Butterfly Adjustment | sold **two** of those 3110 puts [5] |
| Long put strike in initial trade & sold in adjustment | SPX Iron Butterfly | **3110** strike / **3110** put [5, 6] |
| Profit on adjusted trade | SPX Iron Butterfly (Adjusted) | profit of **582** dollars / **582** dollars [6, 7] |
| Extent of short put in-the-money at expiration | SPX Iron Butterfly (Unadjusted) | closed **21.60** in the money [6] |
| Payout settlement required on unadjusted short put | SPX Iron Butterfly (Unadjusted) | pay to settle that option which comes to **2160** [6] |
| Initial credit collected at trade entry | SPX Iron Butterfly | collected **two thousand** dollars [6] |
| Loss on unadjusted trade | SPX Iron Butterfly (Unadjusted) | loss of **160** [6] |
| Typos/Garbled words in transcript | SPX Put Side Butterfly Adjustment | "**3135 foot**" (garbled/typo for 3135 put) [6] |

### [e9lTVDaDBOk] SMB Options Tribe - The Triple Butterfly (14,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Russell 2000 index options [1].
    *   **Structure**: The triple butterfly strategy, which is a classic options income trade [2].
    *   **Strikes/Deltas**: The strategy is initiated by placing an at-the-money butterfly centered at **1150** (with the Russell 2000 index trading around 1150) [1]. If rolled, the lowest butterfly (original 1150) is rolled up to the **1210** strike [3]. No specific Deltas are spoken in these passages [1-8].
    *   **DTE (Days to Expiration)**: The trade is entered at the beginning of the March expiration cycle, moving back about **30** days [1].
    *   **Entry Trigger**: Not defined by technical indicators. It is entered strictly at the money, starting wherever the market is currently trading, and "allowing the market to tell you what to do next as opposed to anticipating" [2].

*   **The Management and Exit Rules**:
    *   **Upward Trend Adjustments**:
        *   If the market rallies strongly, the trader adds a second butterfly above the first one (referred to as a "nuclear power plant look") [1, 5]. This requires the trader to "keep your powder dry" and have additional capital set aside for adjustments [1].
        *   If the market continues to rally further, a third butterfly is added (creating the "triple butterfly" formation) [5].
        *   "Once we've added three butterflies then we don't add a fourth" [5]. Instead, roll the butterflies farthest from the market further up without adding a lot of additional capital [3, 5].
        *   On March 4th, during a very large rally, the trader rolled out of the original 1150 butterfly and rolled up to the 1210 strike [3].
    *   **Defensive Exits and Expiration**:
        *   The trade depends on the market eventually stalling, slowing down, or channeling near the end of the expiration period [3, 6].
        *   On St. Patrick's Day (Monday, March 17th), the trade turned quite profitable [6].
        *   On Wednesday, March 19th, the trade was up over **\$11,000** and was allowed to be exited [7].
        *   The time decay of the short options handles the rest of the work as the trade nears expiration [7].

*   **The Stated Edge or Statistics**:
    *   **Market Neutral Reactivity**: Unlike directional day trading, this options income style does not require you to predict where the stock or index is heading; instead, you simply react to what the market does [1, 2].
    *   **Time Decay (Theta) Forgiveness**: The natural properties of short options decay provide profitability [7]. As Seth notes, "with options income trading time heals most if not all wounds" [6].
    *   **High Profit Recovery**: Even when challenged by an aggressive, radical up move in the Russell 2000 index, the strategy was resilient enough to recover and reach an open profit of over **\$11,000** on March 19th [3, 7].

*   **The Caveats the Presenter Gives**:
    *   **High Complexity**: The trade is "a little bit complicated" and contains many subtle nuances [2].
    *   **Explicit Warnings**: Seth heavily warns the audience, "don't try this at home" and "I really don't recommend your running out and trying one of these in the real market without a lot of experience and education" [2, 7].
    *   **Upward Trend Threat**: A massive, relentless one-sided up trend is a "challenging month for a strategy like this" [5].
    *   **Capital Reservation**: Traders must maintain capital reserves ("powder dry") specifically to fund subsequent adjustments (adding butterflies) [1, 7].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[e9lTVDaDBOk]` title card | **14000** views [4] |
| Trade duration baseline | Russell 2000 index (RUT) triple butterfly, March expiration cycle | initiated "**about 30 days**" back [1] |
| Underlying index identifier | RUT index | Russell "**2000**" index [1] |
| Initial butterfly center strike | RUT at-the-money butterfly | centered at "**1150**" [1] |
| Strong rally timeline | RUT triple butterfly, March expiration | "**late February and early March**" [1] |
| First butterfly adjustment | RUT, addition of second butterfly | "**second** butterfly" [1] |
| Second butterfly adjustment | RUT, addition of third butterfly | "**third** butterfly" / "**three** butterflies" [5] |
| Maximum butterfly configuration | RUT triple butterfly strategy | do not add a "**fourth**" butterfly [5] |
| Aggressive rally date | RUT triple butterfly adjustments | "**March 4th**" [3] |
| Adjustment roll strike levels | RUT, put/call roll adjustments | rolled out of original "**1150**" strike to new "**1210**" strike [3] |
| Sideways consolidation timeframe | RUT, triple butterfly post-rally consolidation | last "**30** days" / "**a week** later" [6] |
| Initial profit turn date | RUT, triple butterfly campaign | St. Patrick's Day (Monday, "**March 17th**") [6] |
| Mid-week peak performance date | RUT, triple butterfly campaign | Wednesday, "**March 19th**" [7] |
| Realized open profit level | RUT, triple butterfly open position on March 19th | up over "**\$11,000**" [7] |
| Options Tribe webinar history | Options Tribe webinars | hosted since "**May of 2011**" [8] |

### [5dUqJWT_Uf8] How To Profit From  A Recession: A Guide to Trading Options During A Crash (14,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: QQQ ETF (referred to as "the Q's"), which represents a basket of stocks tracking the tech-heavy NASDAQ 100 index [1].
    *   **Structure**: Put broken wing butterfly options strategy [2, 3].
    *   **Strikes/Deltas**: 
        *   *Long Put*: Bought 1 contract of the at-the-money **510** put [3].
        *   *Short Puts*: Sold 2 contracts of the **485** puts (set at key support) [3].
        *   *Long Put (Protection)*: Bought 1 contract of the out-of-the-money **365** put to manage capital/margin requirements [3, 4].
        *   *Deltas*: No specific Delta selection parameters are spoken in the transcript [1-10].
    *   **DTE (Days to Expiration)**: Approximately three months (entered on January 2nd, 2025, and expiring at the end of the first quarter on March 31st, 2025) [1, 3].
    *   **Entry Trigger**: Activated when a high-performing stock or index has experienced an aggressive rally (such as QQQ rallying 25% in 2024 to close at 510.23 on January 2nd, 2025), making an outright long share purchase highly risky [1]. The trader uses the strategy to profit from an anticipated near-term pullback and acquire the shares at a much cheaper price on the subsequent bounce [1, 2, 6].
        *   *Technical Support*: The short strikes are placed at **485** because the index bounced from that level at the end of October and established support there multiple times in September and October [3].

*   **The Management and Exit Rules**:
    *   **Scenario 1: Market never pulls back and rallies instead (Thesis is completely wrong)**: If the index rallies straight up (e.g., to 521.22), all three options expire worthless because they are at or below the 510 strike [9]. The trader has no further settlement obligations and simply pockets the initial net credit of **\$150** as a "consolation prize" [4, 9].
    *   **Scenario 2: Market pulls back as expected and triggers assignment (Correct Thesis)**: 
        *   If the index sells off below the short strike on expiration (e.g., closing at **468.92** on March 31st), the long 510 put is in-the-money and the short 485 puts are assigned [4, 8].
        *   The options portion of the trade is closed/settled on March 31st, netting an options profit of **\$2,572** [8].
        *   The trader is assigned and now owns 100 shares of the Q's at the **485** strike price [8].
        *   The trader holds the assigned stock through any further temporary selling (e.g., dropping as low as **402** at one point) until the anticipated bounce occurs [8].
        *   Once the stock recovers and rallies back near its highs (e.g., reaching **521.22** on May 27th), the trader sells the 100 shares to realize the capital gain [8].
        *   Combining the options settlement profit of **\$2,572** and the stock rebound gain, the total realized trade profit is **\$6,194** [8].

*   **The Stated Edge or Statistics**:
    *   **Monetizing the Sell-off**: The broken wing butterfly generates a substantial cash profit during a crash (\$2,572 in options profit), which heavily subsidizes the entry cost of the assigned stock shares [8].
    *   **Absolute Downside Protection**: Buying the protective lower wing (365 strike put) places a hard floor on the options portion of the trade and prevents broker margin requirements from blowing up [3, 4].
    *   **Unconditional Profit Profile**: It allows traders to extract a positive return from the market even if their directional thesis is flat-out wrong [9].

*   **The Caveats the Presenter Gives**:
    *   The trade requires the trader to have a clearly identified support target backed by historical chart behavior [1, 3].
    *   The strategy has a significant capital requirement, as the broker requires a margin of at least **\$9,350** to execute the trade [4].
    *   The trader must be comfortable accepting physical share assignment and riding out high intraday volatility (such as the index dropping from the 485 assignment level down to 402 before bouncing back to 521.22) [8].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Prop firm trader earnings | Prop desk traders | "**seven** and even **8** figure per year" |
| Free workshop duration | Workshop promotion | "**two**-hour free intensive workshop" |
| Free workshop strategies | Workshop promotion | teaches "**three** of those strategies" |
| Workshop high-probability win rate | High-probability options income strategy | statistical "**eighty percent** probability of profit" |
| QQQ performance baseline | QQQ Index, buy-and-hold | staged an impressive "**25%** rally in 2024" |
| QQQ baseline entry price | QQQ Put Broken Wing Butterfly (January 2nd, 2025) | closed on first trading day of 2025 at "**51023**" (representing \$510.23 **⚠unverified**) |
| Target entry date | QQQ Put Broken Wing Butterfly | "**January 2nd 2025**" (also "**January 2nd**") |
| Expiration options chain | QQQ Put Broken Wing Butterfly | "**March 31st**" (end of the first quarter) |
| Historical support levels | QQQ Index historical support | "**485**" |
| Short put strikes | QQQ Put Broken Wing Butterfly (1 long 510 / 2 short 485 / 1 long 365) | sold "**two** of those 485 puts" |
| Short put premium credit | QQQ Put Broken Wing Butterfly (485 short) | sold for a price of "**997**" (representing \$9.97 per share, or \$997 each) |
| At-the-money long put strike | QQQ Put Broken Wing Butterfly (1 long 510) | "**510** put" |
| At-the-money long put contract count | QQQ Put Broken Wing Butterfly (1 long 510) | bought "**one**" |
| At-the-money long put premium cost | QQQ Put Broken Wing Butterfly (510 long) | bought for "**1749**" (representing \$17.49 **⚠unverified** per share, or \$1,749) |
| Out-of-the-money protective strike | QQQ Put Broken Wing Butterfly (1 long 365) | "**365** put" |
| Options credit collected at entry | QQQ Put Broken Wing Butterfly | collected "**\$150**" |
| Required broker margin capital | QQQ Put Broken Wing Butterfly | require "**\$9,350** in your account" |
| QQQ price at options expiration | QQQ Put Broken Wing Butterfly | dropped below "**500**" and trading at "**46892**" (representing \$468.92 **⚠unverified**) |
| Upper long put strike identifier | QQQ Put Broken Wing Butterfly | "**510** put" |
| Short put strike identifier | QQQ Put Broken Wing Butterfly | "**485** puts" |
| Protective put strike (split text) | QQQ Put Broken Wing Butterfly | "**36**" (split text segment; note: representing the 365 put) |
| Realized options profit at expiration | QQQ Put Broken Wing Butterfly | profit of "**\$2572**" |
| Assigned QQQ share contract sizing | QQQ share assignment | own "**100** shares" |
| Assigned QQQ share strike price | QQQ share assignment | assigned at "**485**" (representing \$48,500 **⚠unverified** total) |
| Post-expiration drop bottoming level | QQQ Index post-assignment drop | down as low as "**402** actually at one point" |
| Stock exit / sell-off recovery date | QQQ share exit | "**May 27th**" |
| QQQ recovery rebound exit price | QQQ share exit | rallied all the way up to "**52122**" (representing \$521.22 **⚠unverified**) |
| Total share sale proceeds | QQQ share exit | brought in "**\$52,122**" |
| Combined total trade profit | QQQ share exit + options profit | total profit comes to "**\$6,194**" |
| Consolation profit if wrong (no pullback) | QQQ Put Broken Wing Butterfly, straight rally | still make "**\$150**" (also "**150**" and "**150 dollars**") |
| Straight rally QQQ threshold | QQQ Put Broken Wing Butterfly, straight rally | rallied straight to "**521-22**" |
| Option strikes threshold for worthless expiration | QQQ Put Broken Wing Butterfly, straight rally | strike price of "**510** or lower" |
| General promo option strategies | Intensive workshop curriculum | "**three** more option strategies" |

### [5QZUDprprlU] How to Construct an Options Trade With a Really Wide Profit Zone (14,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Real options on an unnamed stock [1].
    *   **Structure**: Iron Condor options strategy [2].
    *   **Strikes/Deltas**: 
        *   *Put Side*: Short put option strike of **1 000** protected by a long put strike of **9.75** [1].
        *   *Call Side*: Short call option strike of **11 25** (also spoken as **11.25**) protected by a long call strike of **11.50** [1].
        *   *Sizing*: Four contracts are utilized for each leg (selling four puts at **one thousand**, buying four protective **975** puts, selling four **eleven twenty five** calls, and buying four **eleven fifty** protective calls) [1].
        *   *Deltas*: Specific Delta selection targets are not explicitly stated in the provided passages of this video.
    *   **DTE (Days to Expiration)**: **Fifty one** days to expiration at entry, expiring in **January** [1].
    *   **Entry Trigger**: Positioned as a rangebound options income strategy that profits from sideways movement [2]. It is entered on a real stock trading "at about 10.60 on november first" [1].

*   **The Management and Exit Rules**:
    *   **The 5-Point Trigger Rule**: If the market price of the stock gets within **five points** of either of the short strikes (**1000** put or **11:25** call), the trader must execute a defensive adjustment [3].
    *   **Adjustment Execution (Condor Roll)**: The short and long options on the challenged side of the trade are closed out and re-established further from the market price to widen the profit zone [3]. 
        *   *Adjustment Roll Down Example*: On **November 20th** (**nineteen days** into the trade), when the stock trades at **1003** (within **three points** of the short **1000** puts), the put side is rolled down **50 points** [3]. 
        *   *Action*: The trader buys back the short 1000 puts (costing **15,000 780**) and sells the long 975 puts (receiving **11,000 980**), then simultaneously sells four **950** puts (receiving **eight thousand six hundred forty**) and buys four protective **925** puts (costing **six thousand five hundred sixty dollars**) [3].
        *   *Adjusted Settle-In Zone*: Widens the overall profit area from **125 points** to **175 points** (boundaries of **950 and 1125**) [3, 4]. The total net cost of this roll is **1720 dollars**, reducing the maximum potential profit to **three thousand three hundred and eighty dollars** [3].
    *   **Holding to Expiration**: If the stock closes within the range boundaries on expiration day, all puts and calls expire worthless [1, 4].
        *   *Adjusted Winning Exit*: On January expiration, the stock closed at **980** (below the original short **1000 a** put strike) [4]. Because the put side was rolled down, all adjusted options expired worthless, netting the trader **three thousand three hundred eighty dollars** in options premium [4].
        *   *Unadjusted Sitting Duck Outcome*: If left unadjusted, the trade would have been severely damaged ("killed") because the stock closed well below the original **1000** short puts [4].

*   **The Stated Edge or Statistics**:
    *   **Multi-Scenario Winning Profile**: Unlike traditional stock trading where you must predict the exact direction, this range-bound options strategy allows the trader to win on expiration across a whole range of circumstances (whether the market goes up, down, or sideways) [5].
    *   **Adjustability Edge**: Options income trading provides incredible flexibility. Traders do not have to be sitting ducks; they can cleverly roll their positions out of trouble multiple times and still retain a profitable credit [6].
    *   **Workshop Promoted Statistics**: Teaches three professional options strategies, including an options trading strategy that boasts an **80 percent** statistical probability of profit month in and month out [6].

*   **The Caveats the Presenter Gives**:
    *   **Adjustments are Costly**: Adjusting the trade is not free; rolling the spreads closer to safety consumes a portion of the original credit and reduces the total maximum payout [3, 4].
    *   **Adverse Breakout Risk**: If the market runs aggressively in an adverse direction past the adjusted boundaries, the trade can still result in a loss [6].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Options income win spectrum [5] | Hypothetical options trade | wins in more than **one** circumstance |
| Rangebound baseline stock [5] | Hypothetical options trade | stock trading at say **300** a share |
| Predefined profit zone [5] | Hypothetical options trade | wins if stock closes anywhere between **250 and 350** |
| Real stock entry price [1] | Unnamed Stock, Iron Condor, November 1st | trading at about **10.60** on **november first** |
| Target profit range [1] | Unnamed Stock, Iron Condor, January expiration | win anywhere between the prices of **1 000** on the low side and **11.25** on the high side |
| Iron Condor strike setup [1] | Unnamed Stock, Iron Condor, January expiration | Short call at **11 25**; long protective call at **11.50**; short put at **1 000**; long protective put at **9.75** |
| Puts sizing and duration [1] | Unnamed Stock, put credit spread, January expiration | sold **four** puts at **one thousand**; **fifty one** days out from expiration |
| Put individual sale premium [1] | Unnamed Stock, short put, January expiration | received **19.45 cents** for each option |
| Contract multiplier [1] | Stock options contract size multiplier | represents **100** shares |
| Short puts cash inflow [1] | Unnamed Stock, 4-lot short puts, January expiration | total cash received was actually **seven thousand seven hundred eighty dollars** |
| Sizing of protective puts [1] | Unnamed Stock, long protective puts, January expiration | purchased **four** of those protective **975** puts |
| Protective puts total cost [1] | Unnamed Stock, long protective puts, January expiration | costing as you can see **fifty seven hundred** |
| Sizing of short calls [1] | Unnamed Stock, short calls, January expiration | sold **four** of the **eleven twenty five** calls |
| Short call individual premium [1] | Unnamed Stock, short calls, January expiration | priced at **twenty one eighty five** |
| Short calls cash inflow [1] | Unnamed Stock, 4-lot short calls, January expiration | generated **eight thousand seven hundred forty dollars** |
| Sizing of protective calls [1] | Unnamed Stock, long protective calls, January expiration | purchased **four** **eleven fifty** protective calls |
| Protective call individual cost [1] | Unnamed Stock, long protective calls, January expiration | priced at **fourteen dollars and thirty cents** |
| Protective calls total cost [1] | Unnamed Stock, long protective calls, January expiration | costing us **five thousand seven hundred twenty dollars** |
| Total net entry cash flow credit [1] | Unnamed Stock, 4-contract Iron Condor (Jan expiration) | netted out a cash flow of **five thousand one hundred dollars** |
| Profit zone boundaries [1] | Unnamed Stock, Jan expiration | if stock closes between **one thousand** and **1125** |
| Adjustment trigger distance [3] | Unnamed Stock, Iron Condor adjustment | gets within **five** points of either the **1000** put or the **11:25** call |
| Adjustment roll timing [3] | Unnamed Stock, Put roll adjustment | moving to **November 20th** which is **nineteen** days later |
| Stock price at adjustment [3] | Unnamed Stock, Put roll adjustment | market on this stock actually got to **1003** |
| Distance from short puts [3] | Unnamed Stock, Put roll adjustment | within **three** points of our short puts located at **1000** |
| Rolldown distance [3] | Unnamed Stock, Put roll adjustment | roll our position down **50** points |
| New adjusted put strikes [3] | Unnamed Stock, adjusted put credit spread | short **four** of the **950** puts; long **four** for the **925** puts (transcribed as "**925 place**") |
| Cost to close short puts [3] | Unnamed Stock, closing short 1000 puts | buy back the **1000** puts to close that position, need to pay **15,000 780** |
| Cash from closing long puts [3] | Unnamed Stock, closing long 975 puts | closing long **975** actually gives us cash of **11,000 980** |
| Cash from new short puts [3] | Unnamed Stock, selling short 950 puts | sold those **950** puts for total cash of **8,000 640** |
| Cost of new long puts [3] | Unnamed Stock, buying long 925 puts | paid **six thousand five hundred sixty dollars** for the **925** puts (transcribed as "**925 foots**") |
| Net cost of roll [3] | Unnamed Stock, put side Condor roll down | total cost of rolling those **1,000** puts (verbatim) was **1720 dollars** |
| Profit zone range width [3] | Unnamed Stock, adjusted Iron Condor | profit area expanded from **125** points to **175** points |
| Net adjusted trade max profit [3, 4] | Unnamed Stock, adjusted Iron Condor | profit down to **three thousand three hundred and eighty dollars** / **three thousand three hundred eighty dollars** |
| Adjusted profit range boundaries [4] | Unnamed Stock, adjusted Iron Condor | stock closes anywhere between **9 50** and **11 25** (also written as **950 and 1125**) |
| Stock closing price at expiration [4] | Unnamed Stock, adjusted Iron Condor | stock did close at **980** |
| Original put strike at risk [4] | Unnamed Stock, original short put | original **1000** put (transcribed as "**1000 a**") |
| Workshop promo strategies [6] | Options class promo | teaches **three** more real-world option strategies |
| High probability options edge [6] | Options class promo | statistical **80** percent profit month in and month out (verbatim "**80 percent profit**") |

### [KAapuE02EOw] How to Grow a Small Options Account (quickly) (14,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Broad stock or exchange-traded fund (ETF) options (such as SPY, Tesla, CMG, or Costco) [1-3].
    *   **Structure**: Vertical spreads—specifically bull put credit spreads and call debit spreads—are utilized as systematic risk-management tools in lieu of outright option buying [1, 4].
    *   **Strikes/Deltas**: 
        *   *Bull Put Credit Spread baseline*: Selling the **100 put** and buying the **95 long put** [4]. 
        *   *Zero DTE Option Spread example*: Selling at the **19 delta** and buying a protective leg **25 points** below, buying the **7330** (verbatim) [2].
        *   *30-day Option Spread example*: Selling the **7100 strike** and buying the protective **7075 strike** [5].
    *   **DTE (Days to Expiration)**: Zero DTE (0 DTE) vs. 30 to 45 days [6].
    *   **Entry Trigger**: Executed strictly based on a pre-planned market thesis, selecting strike parameters according to a systematic, probability-based framework rather than emotional "feel" [3, 7].

*   **The Management and Exit Rules**:
    *   **Pre-Calculated Risk Profile**: Both the maximum potential gain and worst-case loss are clearly calculated and known before entering the trade [1, 4].
    *   **Margin & Capital Locking**: For bull put credit spreads, the total broker margin needed is the strike wing width multiplied by 100 minus the net upfront credit [4].
    *   **Time and Gamma Management**: Zero DTE spreads are subject to high gamma risk (**negative 1.81 gamma**), making them highly sensitive to sudden adverse market moves (e.g., losing 10% on a 10-point move down) [2]. To protect capital, traders are instructed to trade further out in time (e.g., 30-day spreads with **0.04 gamma**, which drops less than 2% on an equivalent 10-point move) [5].
    *   **Short Leg Roll Obligation**: Short options should not be ignored or allowed to expire unmanaged near expiration due to heightened assignment and gamma risk [3]. Short options should be rolled as expiration nears, with entries kept at **21DTE plus** [3].

*   **The Stated Edge or Statistics**:
    *   **Capital Protection**: Capital preservation is the core rule that allows small accounts to survive long enough for statistical probabilities to work in their favor [1, 6].
    *   **Capital Efficiency**: Spreads require significantly lower capital outlays compared to buying single options outright [4, 6].
    *   **Risk Diversification**: The capital efficiency of vertical spreads allows small accounts to spread risk across multiple simultaneous trades (different stocks, different sectors, and different expiration cycles), which reduces reliance on any single trade and lets probability play out [5].
    *   **Statistical Repeatability**: The edge is derived from probability over a large sample of trades rather than trying to perfectly predict market direction [3, 7].

*   **The Caveats the Presenter Gives**:
    *   **Uncontrolled Sizing Risks**: Most small accounts do not fail because of bad market conditions, but rather because of uncontrolled risk and oversized trades where one bad loss erases weeks of gains [6].
    *   **Chasing Premium**: Selling spreads too close to the money to grab larger upfront credits ignores the heavily elevated directional risk [3].
    *   **Confusing Probability with Certainty**: High probability is a long-term mathematical edge, not a guaranteed win on any individual trade [3].
    *   **Gamma Near Expiration**: Spreads traded too close to expiration can move against the trader faster than they can respond [3].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistic | `[KAapuE02EOw]` title card | **14000** views [8] |
| Risk scenario baseline | Multiple traders risk test | **10** traders [1] |
| Timeframe risk comparison | Option spread DTE comparison | **zero** DTE (0 DTE) vs. **30 to 45** days; **20** delta spread vs. **20** delta spread [6] |
| Small account foundation rule | General risk management | **one** rule (protecting capital first) [6] |
| Spread execution structure | General options spread order | entered as **one** order [4] |
| Credit spread strikes | Bull put credit spread | sold the **100** put; bought the **95** long put [4] |
| Credit spread pricing math multiplier | Bull put credit spread multiplier | wing width multiplied by **100** [4] |
| Credit spread initial cash requirement | Bull put credit spread (100/95 strikes) | took in a **\$100** credit; total needed in account is **\$400** [4] |
| Credit spread breakeven price | Bull put credit spread (100/95 strikes) | break even on this trade is **\$99 \$1** (garbled) [4] |
| Zero DTE option spread delta | Option Explorer credit spread | selling at the **19** delta [2] |
| Zero DTE spread strike separation | Option Explorer credit spread | went down and sold below **25** points to cap risk [2] |
| Zero DTE long call option reference | Option Explorer credit spread | buying the **7330** (garbled) [2] |
| Zero DTE spread credit collected | Option Explorer credit spread, 10 contracts | collecting **\$2580** [2] |
| Zero DTE spread required margin | Option Explorer credit spread, 10 contracts | total margin taken out of our account is **\$22,240** [2] |
| Zero DTE spread contract size | Option Explorer credit spread | selling **10** contracts [2] |
| Zero DTE spread gamma metrics | Option Explorer credit spread, 10 contracts | negative **1.81** gamma; deltas change by **1.81** [2] |
| Zero DTE market move down drawdown 1 | Option Explorer credit spread, 10 contracts | down **10%** on a **20**point (20-point) move [2] |
| Zero DTE market move down drawdown 2 | Option Explorer credit spread, 10 contracts | down on a **10**point (10-point) move down [2] |
| 30-day spread contract sizing | Option Explorer credit spread, 30-day DTE | selling the same **10** contracts [2] |
| 30-day spread short strike | Option Explorer credit spread, 30-day DTE | going to **7100** [5] |
| 30-day spread long protective strike | Option Explorer credit spread, 30-day DTE | going down to **7075** to buy protection [5] |
| 30-day spread gamma metrics | Option Explorer credit spread, 30-day DTE | gamma is **0.04**; roughly **40** times less than going **zero** DTE [5] |
| 30-day spread market move down drawdown | Option Explorer credit spread, 30-day DTE | less than **2%** down on a **10**-point move in the market [5] |
| Common credit spread mistakes | General options trading errors | **four** common mistakes (including number **one**, **two**, and **three**) [3] |
| Entry DTE safety threshold | Credit spread short strike | keep short at **21DTE** plus at entry [3] |
| Single trade performance limit | General vertical spreads | **one** single trade [5]; **one** big winner [7]; **one** mistake [7] |
| Promoted workshop option strategies | General intensive workshop promotion | **three** more option strategies [9] |

### [tG5zTqOITkM] SMB Options Tribe - The Heart Friendly Butterfly (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX) [1]. (The presenter notes that while other instruments might be fine, they must be backtested first due to the unique peculiarities of each index or ETF [1]).
    *   **Structure**: The "Heart Friendly Butterfly" is a double butterfly options strategy [2].
    *   **Strikes/Deltas**:
        *   The center of the double butterfly is placed **at the money** [1].
        *   The wings of the butterfly are set at a distance of **one standard deviation out** based on 7 days to expiration [1].
        *   The wings must be set **no less than 75 points** from the center of the butterfly [1].
        *   *Deltas*: The strategy is designed to aggressively control the position's Delta (the tendency of a trade's P&L to be affected by the movement in price) [3].
    *   **DTE (Days to Expiration)**: The trade is initiated about **5 weeks out** from expiration [1].
    *   **Entry Trigger**: Not indicator-driven. The position is established about 5 weeks out, placing the center at the money, and "allowing the market to tell you what to do next as opposed to anticipating" [1, 2].

*   **The Management and Exit Rules**:
    *   **Active Delta Control**: The trade is managed to aggressively control and stay on top of the Deltas [2, 3]. This tight control minimizes the impact of price movement on the trade's P&L [3].
    *   **Theta Decay Harvesting**: The butterfly is an at-the-money Theta trade that leverages maximum time decay [1]. The trade capitalizes on the fact that at-the-money options start to accelerate their time decay and bleed out from 5 weeks down to Day Zero [4].
    *   **Adjustment Philosophy**: The style involves reacting to the market and adjusting to what it is doing rather than trying to predict where the stock or index is heading [5].
    *   Specific adjustment triggers or exit targets are not provided in this excerpt of the video.

*   **The Stated Edge or Statistics**:
    *   **Peace of Mind Edge**: Aggressive Delta risk management removes the fear and large P&L swings typical of options trading, making it "heart friendly" [3].
    *   **Range-Bound Winning Profile**: Typically produces a very nice profit if the stock or index trades within a range, without requiring the trader to predict direction [6, 7].
    *   **Time Decay Edge**: The passage of time is the options income trader's best friend, eroding option value to generate consistent income [1, 6].

*   **The Caveats the Presenter Gives**:
    *   **Capped Returns**: Controlling Deltas aggressively sacrifices potential return. Traders must accept that they will not make "50 60 70% return on your capital" [3].
    *   **Personality and Comfort Zone**: The conservative nature of this strategy fits a risk-averse personality. Traders must trade within their comfort zone to succeed [8].
    *   **Underlying Peculiarities**: Other underlying vehicles (like RUT) have their own peculiarities and must be backtested rather than assuming they will perform identical to SPX [1].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| News ticker background audio overlay | Background market news feed | **3.17 billion EUR** revenue; **4.2%** year year (verbatim); **4.8%** third quarter sales; down about **a perent** (garbled/verbatim for "a percent") on the day; **four pennies** (little more than) |
| Simplified options income example stock | Google common stock, May 22nd 2013 | trading around **900** |
| Simplified options income example premium | Google Iron Condor, entered in May | collected **\$1,380** (ours to keep) |
| Simplified options income range target | Google Iron Condor, entered in May | stays between **two** very wide points |
| Options Foundation program sizes | Options Foundation Program | **20 part** video curriculum; over **12** hours of recorded videos; **500** PowerPoint slides |
| Options Foundation program price | Options Foundation Program | cost is **1950** |
| Elite Mentoring Package structure | Elite Mentoring Package | **three** private one-on-one sessions; approximately **one** hour (per session); **3-month** period; **three** times a month student meetings; **nine** total student meetings; **three** one-on-one mentoring sessions |
| Mentoring program meeting archive | Options Tribe student meeting archive | goes back to the middle of **2011** |
| Options Tribe webinar history | Options Tribe webinars | hosted since May of **2011** |
| Presenter options career start | Seth Freudberg options trading | started options trading back in **2006** |
| Heart Friendly Butterfly structure | SPX "Heart Friendly Butterfly" | **double** butterfly trade |
| Heart Friendly Butterfly sacrificed returns | SPX double butterfly, 5 weeks out | will not make **50** (percent), **60** (percent), or **70%** return on your capital |
| Heart Friendly Butterfly wing settings | SPX double butterfly, 5 weeks out | **one** standard deviation out; **7** days to expiration; no less than **75** points from the center |
| Heart Friendly Butterfly DTE entry | SPX double butterfly, 5 weeks out | initiate the trade about **5** weeks out |
| Time decay acceleration curve | SPX double butterfly, 5 weeks out | bleed out time Decay from **5** weeks down to Day **Zero**; Day **Zero** |

### [6BLrentthYQ] How Short Term Traders Can Survive Unprecedented Volatility (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Broad-market index exchange-traded funds (such as SPY and QQQ), medium-term bond ETFs (TLT), and volatility ETFs (VXX) [1-4].
    *   **Structure**: Intraday range-bound and momentum swing trading using underlying shares [1, 3]. Additionally, short-term, defined-risk long put options (e.g., next-week options) are utilized to express highly leveraged bearish positions without the open-ended risk of shorting common stock [4, 5].
    *   **Strikes/Deltas**:
        *   *TLT Put Options Play*: Next week's **160** strike puts are purchased cheap to capture downstream bond price pullbacks [4]. 
        *   *Deltas*: No specific delta targets are discussed for this setup, but technical execution targets are determined strictly by calculating support and resistance levels across multiple timeframes [6, 7].
    *   **DTE (Days to Expiration)**: Short-term weekly options (e.g., expiring the next week) are preferred for directional leverage [4].
    *   **Entry Trigger**:
        *   **Chart Level Setup**: Drawing three distinct timeframes—intraday (pre-market and post-market), 30-minute two-week, and daily charts—to identify prior buyer support and supply/resistance levels [7, 8].
        *   **Pre-Market Resistance Failure**: Pre-market volatility indexes (VXX) topping out at a key level (e.g., **32**) and failing on the open [9].
        *   **Inflection Open**: The underlying ETF (e.g., QQQ) opening cleanly above its pre-determined inflection price point (e.g., **204**) to signal a gap-and-go rally [10].
        *   **Support Hold Pullback**: Index pulling back on low volume to test established intraday support (such as SPY pulling back to hold S1 at **292** or QQQ pulling back to test its **204** inflection point) [11, 12].
        *   **Pre-Market Gaps**: Underlying asset gapping up significantly (e.g., **four or five dollars**) into a zone with no nearby technical levels, indicating an overextended gap-and-fail or sell-the-news opportunity [4, 13].

*   **The Management and Exit Rules**:
    *   **Strict Risk-Budget / Sizing Rule**: When intraday ranges expand heavily (e.g., SPY moving in \$14-\$16 daily ranges), traders must dynamically reduce their position sizes by half (e.g., cutting a standard 1,000-share tier size down to 500 shares, scaling up to 2,000 instead of 4,000) to withstand volatile whipsaws [3].
    *   **Stop Loss / Risk Capping**: Stops must be determined before entry. (e.g., QQQ stop set below **203 70** on a 204 breakout entry, risking 30 cents) [10]; AMD stop set below **46 50** on a 47 entry [14]. Trailing stops are managed on runners as momentum slows [12].
    *   **Profit-Taking & Scaling**: 
        *   For breakout plays, sell half of the position into the initial morning momentum spike and trail the remainder [12].
        *   For short positions (e.g., TLT short common), cover **50% to 75%** of the position as it drops into S1 support (e.g., **164**) [13].
        *   **Hit and Run rule**: Rather than swing-trading to hold positions for full days, trade "move to move." In extreme volatility, sharp reversals occur in the first few hours; traders should scale out of positions within 15 to 20 minutes to book quick profits [15].

*   **The Stated Edge or Statistics**:
    *   **Implied Volatility/Fear Bid Edge**: During market panics, heightened fear heavily bids up put options. Options buyers seeking overnight protection pay inflated premiums. A trader can acquire puts cheap on morning spikes (e.g., paying **70 cents** on the open), and watch their value inflate in the afternoon (e.g., trading at **220 or 230**) even if the underlying stock remains completely flat, cashing in purely on the surge in fear bid [4, 13].
    *   **Relative Strength / Weakness Edge**: Stacking edges by looking at market leaders (Apple, Microsoft, Netflix) and individual stocks (such as AMD) that hold up better than the broader index (SPY). Buying AMD at support (e.g., **47**) if it shows relative strength ensures a massive move (to **49** or **50**) if the broader market experiences even a mild bounce off support [14, 16].
    *   **Predetermined Intraday Ranges**: Financial markets operate under repeatable human patterns where institutions accumulate or sell positions against intraday VWAP, providing high-probability zones for mean reversion [8].

*   **The Caveats the Presenter Gives**:
    *   **Severe Overnight Gap Risk**: Intraday swing traders are highly vulnerable to overnight macro headlines (e.g., Syria, trade wars, Trump investigation) that can trigger catastrophic open gaps, instantly blowing past stops before traders can react [17].
    *   **Emotional Micromanagement**: High volatility creates massive "whippiness" and intraday reversals that easily shake out traders who use tight, undisciplined stops or oversized positions [15, 18].
    *   **The Experience Warning**: If a trader has been active for less than a couple of years, the presenter issues a blunt caveat to "sit this one out" and paper trade [19]. Traders must build their risk tolerance slowly before trading in highly volatile markets [20].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Pre-market routine timeline | Trader preparation routine | "**5:30**" morning wake up; at the office by "**7:30**" |
| Unprecedented volatility timeline | Broad market volatility frequency | occurs once every "**two** or "**three**" years |
| Game plan date | Daily morning game plan notes | "**March sixth**" |
| Volatility tracking timeline | VXX ETF tracking period | "**thirty** days" |
| Yield rate decline milestones | Ten-year bond yield crash | "**ten**-year bond"; yield below "**one** percent"; heading down towards "**half** a percent" |
| Historical index bounce benchmark | SPY bounce, preceding week | bounced from "**last Friday**" from "**286**" to above "**312**" |
| Pre-market VXX resistance | VXX pre-market short setup | pre-market resistance at "**32**"; s1 at "**31**"; s2 at "**30**"; retrace alerts at "**30 180**", "**3185**", "**3190**", "**32**" |
| VXX afternoon trend target | VXX intraday short | ended up going down to below "**\$30**" (also "**\$30** a share") |
| SPY pre-market game plan levels | SPY daily range boundaries | r1 to "**295**"; R2 to "**292 98**"; R3 "**three 300s**"; S1 "**one to 92**"; S2 "**s two to 90**" |
| SPY open execution sequence | SPY morning scalp | opened below "**292**"; went up to almost s1 (support/resistance); pulled back to "**292**"; move to R1 (transcribed "**2 or 1**"); R2 to "**298**" |
| Active execution timing | SPY intraday trade | moved over after "**10 o'clock**" |
| SPY final run magnitude | SPY final afternoon rally | ripped up "**seven** dollars" in the final "**30** minutes" |
| Level selection preparation | Technical analysis chart setup | spent "**30** minutes" explaining; "**two** hour" free workshop; "**three**" time frames; "**30-minute**" two-week chart; "**two-week**" chart; "**daily**" chart; premarket on "**Monday**" reference level "**298**"; bounce from "**290**" to "**310**" |
| Sizing reduction rule | SPY shares risk control sizing | normally trade "**thousand** shares" down to "**500**"; build from "**500** into "**2,000**" instead of "**four thousand**" |
| SPY range compression stats | SPY daily ranges | range today was at "**\$7**" (also "**seven** today"); yesterday's "**eight**"; Wed "**nine**" (transcribed as "**\$9 to two**"); few days ago "**14** or "**16**" dollar range; "**third**" day in a row |
| QQQ inflection entry | QQQ breakout, open | opened above "**204**"; went straight to "**206**"; stop below "**2 or 3 70**" (representing 203.70); risk of "**30** cents"; target "**dollar** or "**two**" |
| QQQ pullback entry alerts | QQQ long re-entry, 9:45 AM | alert at "**204 2204 10 204**"; pulls back at "**9:45**"; pop high target "**206**"; sell "**half**"; rest at "**208**"; hold last "**25%**" (trailing quarter) |
| TLT pre-market levels | TLT short common setup | gapping up to "**166**"; sold pre-market at "**166 65**"; pops "**dollar**" or "**dollar 50**" on the open to "**168**" |
| TLT long put options hedge | TLT next-week options purchase | bought next week "**160**" puts; premium paid "**70** cents"; afternoon value "**220**" or "**230**"; TLT trading at "**166 and a half**", "**167**" |
| TLT short position exit | TLT short common cover | gaps up/down "**four**" or "**five**" dollars; sold "**10%**"; expected drop "**ten** percent" or "**five** percent"; cover target comes into "**64**" (representing 164); cover "**50** to "**75** percent" of the position |
| TLT top execution range | TLT short common entry | topped at least "**167 and a half**"; put size on between "**67 67 and a half**" |
| Market average move standard | Index intraday volatility | moving "**two**" or "**three**" percent (also written as "**two three percent**") |
| AMD relative strength play | AMD long, SPY support alignment | get long AMD by "**47**"; stop below "**46 50**"; target "**49** or "**\$50**" |
| US coronavirus weekend gap scenario | Weekend macro threat projection | US baseline "**200** cases" to "**8,000** cases"; spies gap down "**three** or "**four**" dollars; spies heading to "**280 to 2 7**"; upside bounce hold above "**295**"; close target "**305**" |
| Target profit goals | Firm trader incentive targets | normal target "**twenty thousand** dollars" (also "**20**" and "**twenty**"); achieved "**50,000**" for the month; "**double**" the goal; "**triple**" the goal |

### [oPgTwTvc6Bk] A simple 3 day options strategy with surprising potential (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Digital World Acquisition Corporation (DWAC / SPAC) options, which represent the SPAC that announced a merger agreement with Trump Media and Technology Group [1].
    *   **Structure**: Calendar spread of call options [2, 3].
    *   **Strikes/Deltas**: The exact strike prices and Delta parameters are not specified in the provided passages of this transcript, but the strategy is established by selling a shorter-dated call option and buying a longer-dated call option at the same strike price [3].
    *   **DTE (Days to Expiration)**: A quick three-day option strategy [2]. Front week options (expiring earlier and decaying quicker) are sold, and back week options (expiring later and decaying slower) are purchased [4].
    *   **Entry Trigger**: Triggered when a stock with extreme price movement (such as DWAC, which skyrocketed from single digits to as high as 175) goes quiet and flatlines into a tight range for a short period of time [1, 5].

*   **The Management and Exit Rules**:
    *   **Trade Duration**: The trade is held over a very short period of just a few days [4].
    *   **Expiration Management**: At the end of the day when the short front-week options expire, the trade is closed out [3].
    *   **Cost of Close-out**: Closing out the trade costs **980** [3].
    *   **Profit Generation**: Because the short options decay faster than the long options, a relative difference in price is created, resulting in a net profit upon exit [3, 4].

*   **The Stated Edge or Statistics**:
    *   **Time Decay Advantage**: Calendar spreads exploit the relative difference in time decay between front week options and back week options [4]. In a flat market, options expiring earlier lose their value much faster than those expiring later [3].
    *   **High Short-Term Yield**: In the case study, the calendar spread produced an extraordinary profit of **eleven hundred seventy dollars** (a **forty six percent** return) on a **twenty five hundred dollars** original trade cost in just three days [3].
    *   **Defensive Edge**: During the quiet consolidation period, the short options lost **three dollars and forty seven cents** in value while the long options only lost **two dollars and thirty cents** in value, working exactly in the trader's favor [3, 4].

*   **The Caveats the Presenter Gives**:
    *   The provided passages of this video do not contain any explicit caveats, risks, margin requirements, or downside scenarios.

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | DWAC call calendar spread | **13000** views [6] |
| SPAC price baseline | DWAC common stock | "**single** digits" [5] |
| SPAC peak rally price | DWAC common stock | "**175**" at "**one** point" [5] |
| Free workshop promotions | General options educational seminar | teaches "**three**" more option strategies [2] |
| High probability options edge | Options class promotions | statistical "**eighty** percent" / "**80**" probability of profit [2, 7] |
| Trade duration | DWAC call calendar spread | "**three**-day" / "**three** days" option strategy [2, 3] |
| Expiration close-out cost | DWAC call calendar spread, end of day | cost of "**980**" [3] |
| Original trade cost | DWAC call calendar spread | originally spent "**2500**" / "**twenty five hundred** dollars" to enter [3] |
| Final trade profit | DWAC call calendar spread | profit of "**eleven hundred seventy** dollars" [3] |
| Trade return percentage on capital | DWAC call calendar spread | return of "**over forty six** percent" [3] |
| Front-week short options decay | DWAC call calendar spread | short options lost "**three dollars and forty seven cents**" in value [3] |
| Back-week long options decay | DWAC call calendar spread | long options lost "**two dollars and thirty cents**" in value [3] |

### [VNouUypRNYg] How to Own a FREE Put Option (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX index) [1].
    *   **Structure**: Put calendar spread campaign [2, 3]. This consists of purchasing longer-dated put options (the "anchor" hedge) and systematically selling shorter-dated puts against them at the same strike price to continually reduce the cost of the protection [3-5].
    *   **Strikes/Deltas**: 
        *   Put strike price: **2600** [4]. This specific level is selected because the 2600 level had established itself as a highly reliable support area tested multiple times throughout the year [4].
        *   *Deltas*: No specific Delta targets or values are spoken in this transcript.
    *   **DTE (Days to Expiration)**: The long put options are purchased with **four months** to expiration, expiring on **December 21st** [4]. The short-term short puts are sold across successive monthly options chains (such as October and November expirations) [2, 5].
    *   **Entry Trigger**: Positioned as a defensive portfolio hedge initiated after a prolonged, aggressive market-wide rally (such as an **11** percent run-up in the index over several months, as in early April to late August 2018 when the SPX rose to the **28.74** / **2875** area near its all-time highs) [1, 4]. The trader enters the calendar spread expecting an eventual market pullback to test key support [1, 4].

*   **The Management and Exit Rules**:
    *   **Defensive Roll Campaign**: The trade is managed dynamically by cashing in or rolling the short-term puts as expiration approaches [3, 5].
    *   **October Close-out / November Roll**: 
        *   On **October 11th** (the day before the October options expire), if the index has pulled back, the short October puts will have gained value and are bought back to close at **12 and 87 cents** per option [5].
        *   To fund this buyback, the trader simultaneously rolls the short put position by selling the next monthly options cycle puts (**November 2600 puts**) for a premium of **31 and 60 cents** [5].
        *   This roll generates a net positive cash flow of **sixty dollars** (**60**), which completely covers the remaining cost basis of the long December puts, rendering them entirely "free" to hold with a guaranteed minimum profit [2].
    *   **November Expiration**: If the index rallies up (e.g., closing at **27.81** on November expiration), the short November puts expire completely worthless [2]. The trader now holds the **five** December 2600 puts for free, carrying zero further risk and keeping the guaranteed **sixty dollars** of cash flow [2].
    *   **December Expiration (The Winning Exit)**: If a massive, violent market sell-off finally materializes in the final month of the trade, the "free" long December puts skyrocket in value. If the puts swell to **127 dollars and 21 cents** in value, cashing them out before expiration delivers a spectacular final profit of **over sixty three thousand dollars** [3].

*   **The Stated Edge or Statistics**:
    *   **Zero-Cost Protection**: By using a calendar spread campaign, the short-term premium decay fully subsidizes the cost of the protective long puts. If managed correctly, the hedge can be acquired for "free," removing the binary "cost vs. protection" dilemma of portfolio insurance [3, 6].
    *   **Triple-Outcome Winning Profile**: The trader can win if the market pulls back severely (options profits offset equity losses), stays completely still, or even rallies back to all-time highs (keeping the net credit as a "consolation prize" while long equities thrive) [2, 3].
    *   **Workshop Promoted Edge**: Teaches three professional options strategies, including an options strategy that boasts a statistical **80** percent probability of profit month in and month out [7].

*   **The Caveats the Presenter Gives**:
    *   This strategy is not a simple "buy-and-hold" play; it is an active campaign that requires systematic monthly management and options rolling knowledge to successfully eliminate the debit risk [3, 5].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video metadata | **13000** views [8] |
| Historical market rally duration | SPX Index macro trend, 2018 | early April through late August [1] |
| Historical market rally magnitude | SPX Index macro trend, 2018 | rose about **11** [1] (representing 11%) |
| Historical market rally peak date | SPX Index macro trend, 2018 | August of **24th** of that year [1] |
| SPX index level at rally peak | SPX Index, August 24th, 2018 | run up to **28.74** [1] (representing 2874) |
| Promoted free intensive workshop duration | General Options Income strategies | **two-hour** free intensive workshop [7] |
| Workshop strategies count | General Options Income strategies | teaches **three** of those strategies [6, 7] |
| Workshop strategy high probability win rate | High-probability options income strategy | statistical **80** probability of profit [7] (representing 80%) |
| Standard equity options contract size | General options mechanics | purchase or sell **100** shares of stock [9] |
| Historical underlying support level | SPX Index support zone | **2600** level [4] |
| Historical market rally index area | SPX Index | **2875** area [4] |
| Long put option contract sizing | SPX Put Calendar Spread | purchased **five** puts [4] |
| Long put option strike price | SPX December 2600 puts | **2600** puts [4] |
| Long put option price per contract | SPX December 2600 puts | priced at **23.78** [4] |
| Long put expiration date | SPX December 2600 puts | expiring on **december 21st** [4] |
| Long put expiration duration | SPX December 2600 puts | **four** months from now [4] |
| Index option cash settlement point value | SPX index options contract sizing | pays off at a rate of **100** per point [4] |
| Garbled/typo segment in transcript | Transcript anomaly | "**w thousand dollars to 93.05**" (garbled) [5] |
| October check-in roll date | SPX Put Calendar Spread | **october 11th** (a day before the October's expired) [5] |
| October short put buyback price | SPX October 2600 short puts | buy those back for **12 and 87 cents** for each option [5] |
| Short put strike price rolled to November | SPX November 2600 short puts | **november 2600** puts [5] |
| November short put sale price | SPX November 2600 short puts | sell those for **31 and 60 cents** [5] |
| November short put credit baseline | SPX November 2600 short puts | over **31** dollars [5] |
| Rolled calendar spread net cash credit | SPX Put Calendar Spread, November roll | positive cash flow on the trade of **sixty** dollars [2] |
| SPX index level at November expiration | SPX Index, November monthly close | index had rallied up to **27.81** [2] (representing 2781) |
| Rolled calendar spread cash gain | SPX Put Calendar Spread, November roll | collected **sixty** dollars [2] |
| Long put contracts owned for free | SPX December 2600 puts, November close | own those **five** puts for free [2] |
| Short put cash credit guaranteed floor | SPX Put Calendar Spread | guaranteed a **60** gain [2] (also "**60** of cash flow") |
| December puts peak value | SPX December 2600 puts, sell-off peak | skyrocketed to **127** dollars and **21** cents in value [3] |
| Final long put contracts sold | SPX December 2600 puts, final month | cost of those **five** puts [3] |
| Spectacular campaign net profit | SPX Put Calendar Spread, December close | final outcome of over **sixty three thousand** dollars [3] |

### [_mfnkltO5DE] You'll be surprised how quickly the profits can come in with this options strategy (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **FedEx common stock options** [1].
    *   **Structure**: **Iron Condor** options strategy [2].
    *   **Strikes/Deltas**: 
        *   *Short Call Strike*: **300** strike (located **35 points** above the entry price of 264) [3].
        *   *Long Call Strike (Protection)*: **330** strike (positioned **30 points** farther away, acting as a defensive wing **70 points** from the stock price) [2-4].
        *   *Short Put Strike*: **230** strike (positioned **34 points** below the entry price of 264, described as "35 points below") [3].
        *   *Long Put Strike (Protection)*: **200** strike (positioned **30 points** further out of the money) [2].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in this transcript.
    *   **DTE (Days to Expiration)**: **1 day** (options entered **30 minutes** before earnings and expiring the **next day**) [1, 3].
    *   **Entry Trigger**: Entered exactly **30 minutes before the scheduled quarterly earnings announcement** on March **18th** when the stock is trading up around **264** [1]. The short strikes are placed at or around the prices equivalent to the stock's largest recent historical moves after earnings [3].

*   **The Management and Exit Rules**:
    *   **Trade Management**: Managed as an overnight, "set-and-forget" or expirations-based earnings play with no active intra-day adjustments or rolling rules described [1, 3].
    *   **Winning Exit**: If the stock settles between the short strikes at expiration (closing below the short **300** call and above the short **230** put), all four options expire worthless [1, 3]. The trader pockets the entire net cash flow credit of **\$520** as net profit [5].
    *   **Losing Exit**: If the stock acts out of character and goes completely haywire, the maximum possible loss is strictly defined and capped by the protective long options at **330** and **200** (the wings) [2].

*   **The Stated Edge or Statistics**:
    *   **Implied Volatility Inflation Edge**: Imminent earnings announcements heavily inflate options time premium right before the release [4]. Instead of collecting a normal **two or three cents** for out-of-the-money options, the short call went for **48 cents** and the short puts went for **16 cents** [4].
    *   **The Volatility Crush ("Vol Crush") Edge**: Once the earnings report is released, the uncertainty is resolved and volatility immediately collapses to normal levels [4, 6]. This allows the short options to lose their value rapidly and expire worthless the next day [4].
    *   **Prudent Historical Buffer**: The short strikes are placed conservatively based on the largest historical moves the stock has made in recent history. FedEx tends to move less than **15 percent** (with research suggesting a **40-point** move was an extreme "as bad as it could get" limit) [3, 4]. Although FedEx experienced a large **16-point** move after earnings, it was well within the **35-point** distance to the short strikes, allowing all options to expire completely worthless for a 100% win rate [3, 4].

*   **The Caveats the Presenter Gives**:
    *   The trade is not a shortcut; it requires "putting in the homework" on historical moves before trading [6, 7].
    *   The stock can act out of character and go completely haywire, which is why protective long options (the wings) must always be purchased [2].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video metadata | **13000** views |
| Promoted free intensive workshop duration | General options income workshop | **two-hour** free intensive workshop |
| Workshop strategies count | General options income workshop | teaches **three** of those strategies |
| Entry timing | FedEx Iron Condor | **30 minutes** before earnings |
| Entry date | FedEx Iron Condor | March **18th** |
| Stock price at entry | FedEx stock options | trading up around **264** |
| FedEx historical move ceiling | FedEx stock options | tends to move less than **15 percent** after earnings are released |
| Short strikes distance | FedEx Iron Condor | **35 points** above and below the stock price of 264 |
| Short call strike | FedEx short call, expiring next day | **300** calls |
| Expiration | FedEx Iron Condor | expiring the **next day** |
| Short put strike | FedEx short put, expiring next day | **230** puts |
| Protective long call strike | FedEx protective long call, expiring next day | **330** calls |
| Protective long put strike | FedEx protective long put, expiring next day | **200** puts |
| Protective strikes distance | FedEx protective long options, expiring next day | **30 points** farther away from the stock price in both cases |
| Option contract multiplier | General stock options contract sizing | represents **100** shares |
| Call options contract sizing | FedEx short 300 calls, expiring next day | sold **10** of those calls |
| Short call premium price | FedEx short 300 calls, expiring next day | cost **48 cents** per share |
| Short call cash inflow | FedEx short 300 calls, expiring next day | brought in **480** in cash |
| Long call cost | FedEx long 330 calls, expiring next day | cost us **80 bucks** |
| Short put cash inflow | FedEx short 230 puts, expiring next day | brought in **160** in cash |
| Long put cost | FedEx long 200 puts, expiring next day | cost us **40 bucks** |
| Iron Condor total net credit | FedEx Iron Condor, 10-contract setup | total cash flow from the iron condor trade of **520** |
| Normal options value | General non-earnings options comparison | **two or three cents** |
| Put options premium price | FedEx short 230 puts, expiring next day | went for **16 cents** |
| Long call distance | FedEx long 330 calls, expiring next day | **70 points** from the stock price |
| Historical extreme move ceiling | FedEx historical earnings research | suggested more like **40 points** was about as bad as it could get |
| Post-earnings stock actual move | FedEx stock after earnings release | **16 points** is a very large move |
| Approximate stock trading price | FedEx stock trading price context | stock trading around **265** |

### [LG6iH1tac6U] The Best Breakout Strategy With Options (Must Know) (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **Russell 2000 Index options (RUT)** [1].
    *   **Structure**: A **modified version of the risk reversal trade** [1]. This bullish structure is established by purchasing an out-of-the-money long call option and simultaneously selling a put credit spread [1].
    *   **Strikes/Deltas**: 
        *   *Long Call Strike*: **20110** (verbatim transcript typo, representing the **2010** call strike), located approximately **90 points** above the index's closing price [1].
        *   *Short Put Strike*: **1910** put, sold right below where the index is trading [1].
        *   *Long Put Strike (Protection)*: **1650** put, purchased further down the options chain [1].
        *   *Deltas*: No specific Delta targets or metrics are explicitly mentioned in this transcript.
    *   **DTE (Days to Expiration)**: A little less than **three months** (Friday, **July 18th** expiration) [1].
    *   **Entry Trigger**: Triggered when a major market-wide catalyst signals a powerful market breakout [1]. The case study trade was executed on **April 23rd**, a few weeks after the administration announced plans to extend the deadline for tariff negotiations by **90 days** (which had sparked a massive market rally on **April 9th**) [1]. The Russell 2000 index gapped up **two and a half percent** to **1938** before consolidating to close at **1919 14** (representing 1919.14) on the entry day [1].

*   **The Management and Exit Rules**:
    *   **Best-Case Outcome (Rally/Breakout)**: If the index rallies strongly and closes above the long call strike at expiration (e.g., closing at **2240.01** on July 18th), both puts in the put credit spread expire completely worthless, and the long call is cashed in for a massive profit (resulting in **over \$23,000** in net profit) [1-3].
    *   **Range-Bound Outcome (Breakout Fizzles)**: If the breakout fails to materialize and the index closes in the **100-point range** between the short put strike (**1910**) and the long call strike (**2010**), all four options expire worthless [2, 3]. The trader simply keeps the original positive cash flow credit of **\$395** as a guaranteed minimum profit [1-3].
    *   **Downside Protection**: If the index collapses, the maximum loss is strictly defined and capped at the required capital level [1, 2]. The protective long put at **1650** puts an absolute floor on the trade's downside risk [1, 2].
    *   **Capital Optimization**: Because the trade is initiated for a net positive cash flow credit (no cash outlay), the trader can invest their capital in short-term instruments like money market funds (paying **over 4%**) while waiting for the trade to resolve, boosting the overall yield [2, 3].

*   **The Stated Edge or Statistics**:
    *   **Zero Cash Outflow**: The trade can be structured so that there is never any cash outflow from the account during the entire trade, allowing the trader to earn interest in a money market fund while the trade plays out [2, 3].
    *   **Triple-Outcome Profit Zone**: Unlike futures or stock trading where you lose money immediately if your directional bias is wrong, this options strategy allows you to win if the market rallies as expected, does nothing, or even sells off mildly [1-3].
    *   **Innovative Workshop Standard**: The video promotes a proprietary options income strategy that boasts an **80 percent** statistical probability of profit month in and month out [4].

*   **The Caveats the Presenter Gives**:
    *   **Catastrophic Downside Risk**: If the breakout prediction is completely wrong and the market sells off hard, the trade can hit its worst-case scenario maximum loss [1].
    *   **High Margin/Capital Requirements**: The broker requires a significant capital buffer (at least **25,65** in your account, representing the margin requirement/worst-case loss) to execute the put credit spread portion of the trade [1].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics [5] | Russell 2000 breakout modified risk reversal trade | **13000** views |
| Tariff negotiations deadline extension [1] | QQQ/RUT macro environment | **90** days |
| Date of initial tariff rally [1] | QQQ/RUT macro environment | April **9th** |
| Date of trade entry [1] | Russell 2000 Index, April 23rd | April **23rd** |
| Index opening gap-up percentage [1] | Russell 2000 Index | **two and a half%** |
| Index gap-up level [1] | Russell 2000 Index | **1938** |
| Index closing level at entry [1] | Russell 2000 Index, April 23rd | **1919 14** (representing 1919.14) |
| Options expiration duration [1] | Russell 2000 Index options chain | a little less than **three** months |
| Options expiration Friday date [1] | Russell 2000 Index options chain | Friday July **18th** |
| Long call option strike price [1] | Russell 2000 Index, July 18th long call | **20110** (verbatim transcript typo for the **2010** call strike) |
| Call strike distance above index [1] | Russell 2000 Index, July 18th long call | about **90** points |
| Call option price [1] | Russell 2000 Index, July 18th long call | trading for **6340** (representing 63.40 or \$6,340) |
| Short put option strike price [1] | Russell 2000 Index, July 18th short put | **1910** put |
| Short put option price [1] | Russell 2000 Index, July 18th short put | price of **92.40** (also referred to as **9240** in same passage) |
| Long protective put strike price [1] | Russell 2000 Index, July 18th long put | **1650** put |
| Long protective put option price [1] | Russell 2000 Index, July 18th long put | price of **255** (representing 2.55 or \$255) |
| Options multiplier factor [1] | General Index Options multiplier | rate of **\$100** per point; multiply that price by **100** |
| Put options contract sizing [1] | Russell 2000 Index, July 18th puts | sold **five** of them |
| Net entry positive cash flow credit [1] | Russell 2000 Index modified risk reversal | positive cash flow of **\$395** |
| Required broker account capital [1] | Russell 2000 Index modified risk reversal | at least **25,65** in your account (representing margin requirement/worst-case loss) |
| Index closing level at expiration [1] | Russell 2000 Index, July 18th close | closing at **2240.01** |
| Trade net profit at expiration [2] | Russell 2000 Index modified risk reversal | made over **\$23,000** on the trade |
| Money market fund yield [2] | Capital optimization benchmark | paying over **4%** |
| Potential outcome count [2] | Russell 2000 Index modified risk reversal | only ever really **three** potential outcomes |
| Range-bound zone width [2] | Russell 2000 Index modified risk reversal | **100** point range |
| Range-bound zone lower boundary [2] | Russell 2000 Index modified risk reversal | between **1** (garbled/truncated in transcript) |
| Workshop promoted strategies [4] | General Options Income Workshop | teaches **three** more option strategies |
| Workshop strategy statistical win rate [4] | High-probability options income strategy | statistical **80** (representing 80 percent) probability of profit |
| Free workshop duration [4] | General Options Income Workshop | **two-hour** (also written as **two hour**) free intensive workshop |

***

*   *Would you like to explore how this breakout strategy performs under high-volatility environments compared to a low-volatility baseline?* 📈

### [V_fvAxB7vgw] How to Buy an Options Contract for FREE (13,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **SPY ETF (S&P 500 ETF options)** [1, 2].
    *   **Structure**: **Risk reversal trade** [3]. This bullish structure is constructed by purchasing an out-of-the-money long call option and simultaneously selling an out-of-the-money short put option in the same expiration cycle [3]. This combination is designed to acquire the long call for "free" (with no upfront cash outlay) because the premium received from selling the put offsets the cost of the call [1, 3, 4].
    *   **Strikes/Deltas**: 
        *   Long Call Strike: **380** strike, located approximately **17 points** above where the market was trading [3].
        *   Short Put Strike: **348** strike (also spoken as "**three forty eight**") [3].
        *   *Deltas*: No specific Delta targets are explicitly spoken in the transcript for this trade.
    *   **DTE (Days to Expiration)**: Approximately **one month** to expiration, expiring on **November 18th** [3].
    *   **Entry Trigger**: Executed during a classic market pattern consisting of very strong sell-offs in SPY followed by a mild rally making a lower high [1]. The trade is initiated around **noon** on a day when SPY pulls back to test a key support level where the market had bounced earlier that morning (specifically the **348** level) [3].

*   **The Management and Exit Rules**:
    *   **Scenario 1: Market rallies past the long call strike (Best-Case Outcome)**: If SPY rallies aggressively past **380** before expiration, the calls gain tremendous value [5]. The short puts expire completely worthless, and the trader is able to cash in the long calls for an incredible profit [5].
    *   **Scenario 2: Market is range-bound / flat**: If the market closes between the short put (**348**) and long call (**380**) strikes on expiration day, all options expire completely worthless [5]. The trader simply pockets the initial credit collected at entry as their "bare minimum profit" [5].
    *   **Scenario 3: Market drops below the short put strike (Least Favorable Outcome)**: If the market breaks support and drops below **348** at expiration, the trader is assigned and obligated to buy the shares of SPY at **348** [5]. 

*   **The Stated Edge or Statistics**:
    *   **FREE Long Option**: By selling the downside put, the premium entirely funds the upside call, giving the trader unlimited upside potential with **no upfront cash outlay** [1, 3, 4].
    *   **Win-Win Profile**: Even when the best-case rally scenario does not emerge, the trader "basically wins in every other scenario" because they either pocket the initial credit or buy the S&P 500 ETF at a massive discount [5].
    *   **Unrivaled Markdown Entry**: If assigned shares at **348**, the trader acquires SPY at a **27.5 percent markdown** (or **27 and a half percent**) below its historical all-time high, which serves as a highly profitable long-term investment entry point [5].
    *   **Workshop Baseline Probability**: Teaches three professional options strategies, including a high-probability strategy that boasts an **eighty percent** statistical probability of profit month in and month out [6].

*   **The Caveats the Presenter Gives**:
    *   **Long-Term Holding/Patience**: In the least favorable scenario where the market closes below the short put strike and the trader is assigned SPY shares at 348, the trader must have the patience to hold the shares over a longer time frame for the ultimate recovery and profit to materialize [5].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics [4] | Video metadata | **13000** views |
| Baseline market sell-off year [1] | SPY ETF historical pattern | early **2020** |
| Promoted free intensive workshop duration [6] | General options income workshop | **two-hour** free intensive workshop |
| Workshop strategies count [6] | General options income workshop | teaches **three** of those strategies |
| Workshop high-probability win rate [6] | High-probability options income strategy | statistical **eighty** percent probability of profit |
| Option contract sizing multiplier [2] | General Equity option review | entitles the buyer to purchase **100** shares |
| Long call option strike [3] | SPY Risk Reversal, expiring November 18th | bought **five** calls at **380** strike |
| Call strike distance above market [3] | SPY Risk Reversal, expiring November 18th | about **17** points above where the market was trading |
| Short put option strike [3] | SPY Risk Reversal, expiring November 18th | sold **five** puts at **348** strike (also spoken as "**three forty eight** puts") |
| Short put execution premium [3] | SPY Risk Reversal, expiring November 18th | received a **7.12** price per option |
| Short put contract sizing multiplier [3] | SPY Risk Reversal, expiring November 18th | represents **100** shares of stock per option |
| Partial truncated put contract sale [3] | SPY Risk Reversal, expiring November 18th | "**sold fi...**" (garbled/truncated) |
| Assignment stock purchase price [5] | SPY assigned shares | buy the shares of spy at **348** |
| High-value markdown discount [5] | SPY assigned shares | **27.5** (also spoken as "**27 and a half percent**") below all-time highs |
| Outcome scenario count [5] | SPY Risk Reversal | least favorable outcome of the **five** |
| Promoted workshop strategies (final mention) [7] | General options class promotion | details of **three** real world options strategies |

***

*   *Would you like to analyze how this "free" risk reversal trade compares to a simple long call strategy when the underlying asset experiences a high-volatility sideways chop?* 📊

### [Usr6o69kTH8] Turning a Huge Misconception About Options Into a Big Opportunity (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Netflix (NFLX) common stock options [1].
    *   **Structure**: A professional Iron Butterfly options strategy (constructed by selling an at-the-money straddle and buying out-of-the-money protective wings) [2, 3]. This structure turns a common retail losing strategy (buying long straddles right before earnings) into a high-probability professional opportunity [1-3].
    *   **Strikes/Deltas**:
        *   *Short Strikes*: Selling both the at-the-money call option and the at-the-money put option (establishing a short straddle at the money) [2].
        *   *Long Protective Strikes*: Purchasing a protective call option **40 points** above the market and a protective put option **40 points** below the market [2].
        *   *Deltas*: Specific Delta selection targets are not explicitly spoken in the transcript passages for this strategy [1-6].
    *   **DTE (Days to Expiration)**: Short-term options expiring shortly after the earnings release to capture maximum volatility decay [1, 6].
    *   **Entry Trigger**: Executed right before a scheduled quarterly earnings announcement, when option premiums are heavily inflated due to high market uncertainty and rising implied volatility [1, 6].

*   **The Management and Exit Rules**:
    *   **Risk Mitigation (Wings)**: The presenter stresses that selling a naked straddle outright is never advocated [2]. To control risk and margin requirements, traders must buy protective wings (the long call at +40 points and long put at -40 points) [2].
    *   **Exit Execution (Volatility Crush)**: The position is exited (bought back) shortly after the earnings report is released [3, 6].
    *   **Trade Resolution**: When the earnings report is released, the uncertainty is resolved, causing an immediate "volatility crush" that collapses the value of the options [3, 6]. The trader buys back the short options for a fraction of their entry price [6].
    *   **Settle P&L**: The trade is closed by paying a debit of **six hundred twenty six dollars** [6]. Subtracting this from the upfront credit collected of **two thousand three hundred twenty seven dollars** leaves a net profit of **seventeen hundred and one dollars** [6].

*   **The Stated Edge or Statistics**:
    *   **Overestimation of Earnings Move**: The options market has a historical tendency to overestimate the potential post-earnings move of a stock, resulting in overcharged premiums for straddles [2].
    *   **Implied Volatility Decay (Theta/Vega Edge)**: Imminent earnings cause options prices to pump up right before the release [6]. Once the earnings are announced, the volatility crush collapses these inflated premiums, allowing sellers to capture rapid decay [3, 6].
    *   **Flipping the Misconception**: Turning a retail losing trade (buying straddles, which lose **nineteen hundred ten dollars** in this Netflix case due to overpricing and vol crush) into a professional winning trade (gaining **nineteen hundred ten dollars** as the seller, or pocketing a protected **seventeen hundred and one dollars**) [2, 6].
    *   **Workshop Stated Probability**: Teaches three professional options strategies, including a high-probability strategy that boasts a statistical **eighty percent** (also written as **80%**) probability of profit month in and month out [1, 2].

*   **The Caveats the Presenter Gives**:
    *   **Naked Selling Danger**: Selling short straddles outright without protective wings is an "unlimitedly dangerous activity" because a stock can move much more than expected on earnings, leading to massive losses [2, 3].
    *   **The Danger of Buying Pre-Earnings Options**: Retail traders often buy options (like long straddles) expecting explosive moves, but they get "really hurt" because they do not understand that price is not the only moving part; the post-earnings volatility crush will wipe out options value even if the stock moves up or down [1, 6].

---

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[Usr6o69kTH8]` metadata | **12000** views [4] |
| Free workshop duration | General Options Income Workshop | **two-hour** free intensive workshop [1] |
| Free workshop options strategies | General Options Income Workshop | teaches **three** of those strategies [1] / **three** real-world option strategies [3] |
| Workshop high-probability win rate | High-probability options income strategy | statistical **eighty percent** probability of profit [1] / statistical **80%** probability of profit [2] |
| Netflix long straddle performance (misconception) | Netflix, Long Straddle, entered pre-earnings | loss of **nineteen hundred ten dollars** [2] |
| Netflix short straddle performance (unprotected) | Netflix, Short Straddle, entered pre-earnings | gain of **nineteen hundred ten dollars** [2] |
| Netflix Iron Butterfly protective call wing | Netflix Iron Butterfly, long call leg | strike located **40** points above the market; cost of **a hundred 10** bucks [2] |
| Netflix Iron Butterfly protective put wing | Netflix Iron Butterfly, long put leg | strike located **40** points below the market; cost of **a hundred six** bucks [2] |
| Netflix Iron Butterfly entry cash credit | Netflix Iron Butterfly (at-the-money short straddle, 40-point wings) | brought in **two thousand three hundred twenty seven** dollars in cash [6] |
| Netflix Iron Butterfly close-out debit | Netflix Iron Butterfly, closed post-earnings | paid out **six hundred twenty six** dollars to close the trade [6] |
| Netflix Iron Butterfly final net profit | Netflix Iron Butterfly campaign | pocketed **seventeen hundred and one** dollars [6] |
| Key takeaways from the video | General options educational lesson | **two** things [6] |

### [IMl-Zg17M7w] How to Triple Your Dividend Income (With Covered Calls) (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: iShares 20-year Treasury Bond ETF (ticker: TLT), directly tied to the yield on 20-year treasury bonds [1, 2].
    *   **Structure**: **Covered Call** option strategy [3, 4]. This involves owning shares of stock (or an ETF) and selling call options against those shares on a one-to-one basis (selling one call option for each 100 shares owned) [1].
    *   **Strikes/Deltas**: 
        *   *Initial Setup*: Owned **1,000 shares** of TLT and sold **10** of the **91 strike price calls** [1].
        *   *Deltas*: No specific Delta targets are spoken in this transcript, though the short strike is set slightly out-of-the-money above the entry value.
    *   **DTE (Days to Expiration)**: A **one-year (12-month)** duration trade expiring on **September 20th, 2024** (entered in **2023**) [1, 5].
    *   **Entry Trigger**: Triggered when macro monetary policy shifts and the Federal Reserve begins aggressively slashing interest rates (such as cutting rates by **50 basis points** in a single meeting [3, 4]). This lower interest rate environment drives down standard fixed-income yields, prompting the trader to sell covered calls on high-yielding ETFs like TLT to supplement and supercharge cash flow [2-4].

*   **The Management and Exit Rules**:
    *   **Upfront Premium Collection**: Entering the trade generates an immediate cash inflow of option premium paid by the call buyer directly into the seller's account [1].
    *   **Dividend Harvesting**: The trader continues to hold the underlying shares and collects all monthly dividend payments throughout the 12-month campaign [5].
    *   **Winning Exit / Share Assignment (At Expiration)**: If the stock rallies and closes above the short call strike price at expiration (e.g., closing at **98.88** / spoken as **98.8** and **8%** across a passage split [1, 5]), the shares are automatically called away at the strike price (**91**) [5]. 
    *   The trader pockets the upfront option premium, collects the 12 monthly dividend payments, and realizes a small capital appreciation profit on the shares up to the 91 strike price, settling out the campaign for a massive total profit [5].

*   **The Stated Edge or Statistics**:
    *   **Income Multiplier Edge**: Intelligently writing covered calls more than triples the income compared to a passive "buy-and-hold" dividend collection approach. In this campaign, the covered call structure yielded a total return of **over 12%**, compared to the much lower passive yield [5].
    *   **Falling Yield Immunity**: It shields retirees and income-seeking investors from dropping bond yields as the Fed cuts rates, creating a highly predictable cash-generating machine [2-4].

*   **The Caveats the Presenter Gives**:
    *   **Capped Gains**: Selling call options caps the maximum capital appreciation potential. If the underlying ETF rallies far beyond the short strike price, the trader is forced to sell their shares at the strike, missing out on additional gains [1, 5].
    *   **Stable Asset Target**: This strategy requires using stable, solid stocks or index ETFs where the underlying asset isn't at risk of a catastrophic devaluation that would erase the premium and dividend gains [2].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video metadata | **12000** views |
| Proprietary desk establishment year | S&B Capital desk history | New York City since **2005**, now Miami as well |
| Proprietary trader earnings milestones | S&B Capital desk history | "**seven** and even **eight** figure per year" |
| Fed rate easing trigger | Federal Reserve FOMC rate cut | cutting rates **50** basis points |
| TLT baseline annual dividend yield | TLT underlying ETF yield, January 2025 | translates into **\$33.36** per year; **3.7%** annualized yield |
| TLT covered call share setup | TLT Covered Call, 2023 entry | owned **1,000** shares of TLT; worth **\$90,700** on that date; initiated in **2023** |
| TLT covered call option strikes | TLT Covered Call, expiring September 20, 2024 | sold **10** of the **91** strike price calls; expiring a year later on **September 20th 2024** |
| TLT option individual premium price | TLT Covered Call, expiring September 20, 2024 | priced at **\$7.7**; each option contract represents **100** shares; sold **10** of them |
| Stated upfront credit cash flow | TLT Covered Call, expiring September 20, 2024 | positive cash flow of **\$770** (Passage 511 verbatim); corrected as collected **\$7,700** initially (Passage 512 verbatim) |
| TLT closing price at expiration | TLT Covered Call expiration | closed at **98.8** (Passage 511 end) and **8%** (Passage 512 start) (together representing **98.88%** or **98.88**) |
| TLT campaign dividend payments | TLT Covered Call (October 2023 through September 2024) | paid total of **\$3,618** over a **12**-month period (**12** dividend payments) |
| Assigned share sell price | TLT Covered Call expiration | called away at **\$91** per share |
| Stated campaign total return P&L | TLT Covered Call campaign final results | total return is **\$10 \$1,978** (verbatim transcript typo representing **\$10,978 **⚠unverified****); return of over **12%** |
| Underlying bond maturity benchmark | TLT ETF tracking index | **20**-year treasury bonds |
| Promoted workshop option strategies | General options class promo | teaches **three** more option strategies |
| Workshop strategy statistical win rate | High-probability options income strategy | statistical **80** probability of profit (representing 80% **⚠unverified**) |

### [QfjqqzJC4ew] How Proprietary Traders Use Options (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Broad-market indexes and index tracking exchange-traded funds such as **SPX** and **SPY** [1], as well as highly volatile, high-priced individual equities like **Tesla** [2].
    *   **Structure**: 
        1.  *Put Credit Spreads*: A bullish directional trade structured by selling a put closer to the money and buying a lower strike put option for protection [3-5].
        2.  *Short Strangles*: A market-neutral trade structured by selling a call option way above the market and a put option way below the market [4, 6].
        3.  *Iron Condors*: A short strangle flanked with protective wings, consisting of a long call option above the short call, and a long put option below the short put [6].
        4.  *Put Broken Wing Butterflies*: A bearishly located structural play that can still make money if the market sells off gradually or rallies aggressively instead [7].
    *   **Strikes/Deltas**: 
        *   *For the Tesla earnings strangle play*: Short call strike located **400 points above** the market and short put strike located **400 points below** the market [2].
        *   *Deltas*: No specific Delta targets are spoken in the transcript for the standard setups; strike placement for the daily credit spread is determined by a specific proprietary technique rather than simple delta metrics [1, 3].
    *   **DTE (Days to Expiration)**:
        *   *Weekly Options Income Machine*: Same-day expiration / **1-day trades** (zero DTE) [1].
        *   *Standard swing/income campaigns*: Typically monthly contracts [8].
    *   **Entry Trigger**:
        *   *Weekly Options Income Machine*: Triggered by a "one-day signal" developed by North Carolina partner Investiquant [3]. Based entirely on overnight trading of **e-mini futures**, the signal outputs whether the market is likely to close higher than the open, lower than the open, or if it is too close to call ("we don't know") [3]. The signal fires off **two to three times a month**, specifically on **Mondays, Wednesdays, and Fridays** [1, 3].
        *   *Monday Sell-off Setup*: Selling put credit spreads into a severe Monday morning sell-off to capture rich premium fueled by fear-driven implied volatility [5].

*   **The Management and Exit Rules**:
    *   **Set and Forget**: The 1-day signals (Weekly Options Income Machine) do not require active intraday risk management or adjustments; they are placed in the morning and allowed to expire worthless at the close, trusting the statistical edge [4].
    *   **Active Range Defense (Strangle/Condor Rolls)**: For non-directional range trades, if the market breaks out of the expected range, the trader does not sit like a "**sitting duck**" [9]. Instead, they execute **adjustments** by moving or expanding the range [9].
    *   **Roll Up Call Spread**: If a short call (such as a **4360** call) is threatened by a market rally, the trader rolls the call strike further up [10]. This adjustment costs capital (reducing max profit) but preserves safety [10].
    *   **Hit Out Stops**: If the market goes severely against the directional guess, traders must admit they are wrong and hit out of the trade to limit losses rather than risking unlimited drawdown [11].

*   **The Stated Edge or Statistics**:
    *   **Statistical Forgiveness Edge**: Options income trading has an incredible forgiveness edge [11]. While day/swing traders lose money immediately if their directional prediction is slightly wrong, credit spread traders can still pocket maximum profit if the market goes in their favor, does nothing (sideways consolidation), or even moves slightly against them [11, 12].
    *   **Time Decay (Theta) Edge**: Options are a decaying asset [13]. While time immediately works against the options buyer (under which **75% of options expire worthless**), time decay is the options seller's best friend [8, 13]. Premium erodes continuously until the option goes to **zero**, generating consistent income [13].
    *   **Extremely High Win Rates**: By selling strangle strikes twice the stock's worst post-earnings move (e.g. 400 points away on Tesla), a trader can capture a ridiculous **95% win rate** [2, 14].

*   **The Caveats the Presenter Gives**:
    *   **Catastrophic Naked Risk**: Selling naked options is an "unlimitedly dangerous activity" [13]. If a trader does not buy protective options (wings) to define risk, an adverse market crash can cause total bankruptcy [4, 13].
    *   **Earnings Surprise Volatility**: Earnings are highly erratic, and there is no law stating a stock cannot break past its historical worst-case post-earnings moves, exposing unhedged traders to severe drawdown [15].
    *   **The Trap of High Win Rates (Negative Expectancy)**: High win rate is only a small part of the expectancy calculation [16]. If a trader goes too far out to achieve high win rates, they collect very small premiums, and a single outlier loss can wipe out all previous profits [17]. The magnitude of wins and losses is just as critical as the win rate [17].
    *   **Ego and Discipline**: Traders must not have their egos so invested that they refuse to accept when they are wrong [11]. If they are super wrong, they must hit out and take the loss rather than staying in a trade that will destroy their account [11].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `QfjqqzJC4ew` video card metadata | **12000** views [18] |
| Day and swing trading constraints | Day trading baseline directionality check | only can make money if **one** thing happens [12] |
| Weekly Options Income Machine signal frequency | SPX Index options, Put Credit Spread | **one** day signal [3], **two** to **three** times a month [3], **two** **three** times a month (verbatim) [1] |
| Weekly Options Income Machine expiration cycle | SPX Index options (derivative of spy), Put Credit Spread | expiring on **monday**, **wednesday** and **friday** [1], **one-day** trades [1], **one-day** signal [1], prediction for **one** day [1] |
| Spy 2 derivative reference | Spy ETF option tracking SPX index options | **spy 2** (verbatim) [1] |
| Hypothetical put credit spread math | SPX Put Credit Spread (Hypothetical) | sold the short put for **1500** [4], bought the long put for **500** [4], pocketed **thousand** dollars / **thousand** dollars (net profit) [4] |
| Neutral trade strangle structure | Index Options Strangle | stay between those **two** points [6] |
| Options strategies mentioned in promo | Options class workshop promotion | **three** option strategies [6, 7] |
| Options income forgiveness example | Put credit spread forgiveness benchmark | **one** example [11] |
| Options trading scenario outcomes | Put credit spread forgiveness benchmark | **one** you lose [11] |
| Golf range bound analogy | Options income range-bound analogy | **six** yard or **six** foot um circle [9], **six** foot circle [9] |
| Challenged call spread strike reference | Index/Stock Call Spread | short call strike at **4360** [10] |
| Forensic handwriting analyst trader profile | General options tribe trading team profile | **72** year old lady [10] |
| Tesla earnings post-announcement bounds | Tesla options earnings strangle setup | historical move never more than **200** points [2] |
| Tesla earnings strangle strikes | Tesla options earnings strangle setup | sold call **400** points away [2], sold put **400** points below the market [2], call **400** points above the market and a put **400** points below the market [2] |
| Tesla earnings worst case multiplier | Tesla options earnings strangle setup | **twice** the worst historical move ever [2] |
| Forensic analyst win rate | Tesla options earnings strangle setup | win rate of **95** [14, 15] |
| Forensic analyst historical lookback | Tesla options earnings strangle setup | **five** years [15] |
| Roulette wheel probability comparison | Roulette wheel analogy | **one** particular number [17] |
| All options expiration benchmark | General option buyer baseline | **75** of all options expire worthless [8], **75** out of **100** options expire worthless [13], **75** percent chance of that happening [13] |
| Speculative option buying windfall | Unnamed bought options play | **one** guy in **10** minutes made a **million** dollars [13] |
| Long call out of the money worthless target | General long call options baseline | call goes to **zero** if stock doesn't reach strike [13] |

### [124LSnWB2n0] How Pro Traders Use Weekly Options To Trade AMC (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: AMC Entertainment common stock options (meme stock) [1, 2].
    *   **Structure**: Purchasing same-day expiring put options to trade an intraday breakdown, then executing a defensive "roll" into cheaper, further out-of-the-money put options [1, 3, 4].
    *   **Strikes/Deltas**: 
        *   *First Phase (Initial Entry)*: Long **29** put options [4, 5].
        *   *Second Phase (Speculative Roll)*: Long **25** puts and **26** puts [3, 4].
        *   *Deltas*: Specific entry delta targets are not stated, but the initial position begins with low deltas (speculative out-of-the-money puts) that expand rapidly (nearly tripling per contract) as the stock capitulates toward the short strikes [3, 5, 6].
    *   **DTE (Days to Expiration)**: Expiring the very same day the trade is executed (0 DTE weekly options) [1, 5, 7].
    *   **Entry Trigger**: Triggered when a highly volatile stock has experienced an overextended rally, specifically gapping up for the **third straight day** (having started the week around **13 bucks**) [8]. The tactical trigger occurs when the stock consolidates near its highs [9] and then breaks down below its Volume Weighted Average Price (VWAP), with "holding under view up" confirming "a change in character" in the stock [7].

*   **The Management and Exit Rules**:
    *   **Phase 1 (The Initial Scalp)**: When the initial puts (**29** strike puts) appreciate significantly during a sharp drop, close them out to secure profits and remove initial trade risk [4].
    *   **Phase 2 (Establishing the Risk-Free Play)**: Simultaneously reinvest a portion of those proceeds into further out-of-the-money puts (buying **25** and **26** puts) [4]. Because the cost of these cheaper puts is fully covered by the profit of the first phase, the trade becomes entirely "risk-free" with a guaranteed minimum profit floor [10, 11].
    *   **Phase 3 (Scaling Out)**: As the stock capitulates further toward the daily Average True Range (ATR) target, scale out of the remaining rolled puts [3, 12]. Close the positions completely once momentum slows or when the stock hits prior daily support [6, 7, 12].
    *   **Timing Risk Control**: If the breakdown fails and the stock grinds back up towards VWAP, close the positions immediately [3, 9]. Because same-day options expire at the closing bell, holding them through a rally will result in a rapid, complete **100%** loss of the premium due to extreme time decay and implied volatility collapse [3, 6, 9].

*   **The Stated Edge or Statistics**:
    *   **Premium as Absolute Stop Loss**: Trading high-volatility meme stocks with common stock shares is dangerous because they frequently "wick out" (spiking through standard stop-loss points to trigger stops before reversing back down) [7, 13]. By using options, the premium paid acts as the absolute maximum risk (the stop-loss), allowing the trader to weather whipsaws without being forced out [13].
    *   **Convexity and Volatility (Vega) Squeeze**: Buying cheap same-day puts provides explosive leverage [5, 14]. When a stock capitulates rapidly, the expansion of delta and a massive spike in implied volatility (Vega) completely overwhelm the time decay of the options, creating multi-bagger returns in hours [3, 6].
    *   **The Zero-Risk Growth Engine**: Cashing out the initial puts and rolling into cheaper strikes guarantees a profit floor while keeping speculative exposure alive for a larger windfall if the drop continues [10, 15].

*   **The Caveats the Presenter Gives**:
    *   **No Room for Error**: Same-day expiring options have aggressive time decay [3, 6]. If the stock moves sideways or rallies, the options will quickly lose all value and expire worthless [3, 6, 9].
    *   **Intense Execution Focus**: Near expiration, options lose their remaining time premium and trade near parity [16]. Traders must keep an extremely close eye on the stock price and tape to calculate exact intrinsic value and get filled efficiently [6, 7].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity | AMC same-day puts campaign | **12000** views [17] |
| Weekly starting price | AMC common stock | around **13 bucks** [8] |
| Stock prior gapping streak | AMC common stock | **third** straight day [8] |
| Option contract sizing multiplier | Standard equity options mechanics | **100** [2, 4] |
| Initial put option strike | AMC same-day puts | strike price of **29** / **29** puts / **29s** [4, 5, 9] |
| Put entry premium | AMC same-day 29 puts | a price of **a dollar fifteen** [5] / **a dollar fifteen** [4] / **a dollar 15** [11] |
| Introductory contract size | AMC same-day 29 puts | **10** puts [5] |
| Introductory total trade cost | AMC same-day 29 puts | total cost of **1 150 dollars** [5] |
| Puts gain spectrum | AMC same-day puts campaign | around **100** or **200** gain (representing percentage) [3] |
| Stock closing price | AMC common stock | a little bit above **26** [3, 10] |
| Option strikes rolled to | AMC same-day puts campaign | **25s** and **26s** / **25** and **26** / **25** to **26s** [3, 4, 12] |
| Stock average true range (ATR) | AMC daily volatility range | somewhere in like the **five** to a **seven** range / **one** atr [12] |
| Phase 1 roll out profit | AMC same-day 29 puts | basically a **75** profit (representing 75 cents per contract) [12] |
| Phase 2 puts sale price | AMC same-day 25s and 26s puts | sold for **100** each (representing 100 cents per contract) [12] |
| Support level at prior day close | AMC common stock support | above **25** [7] |
| Expiration cycle duration | AMC same-day puts campaign | **one** day [7] |
| Actual campaign puts size | AMC same-day 29 puts | **100** of those puts / **100** of them [4] |
| Actual campaign entry cost | AMC same-day 29 puts | **11 500** in the first phase of the trade [4] |
| Phase 1 appreciation price | AMC same-day 29 puts | around **two** dollars [4] / **two** dollars [11] |
| Phase 1 exit proceeds | AMC same-day 29 puts | **twenty thousand** dollars [4] |
| Phase 1 locked-in profit | AMC same-day 29 puts | **8 500** profit / **8 500** profit [4, 11] |
| Phase 2 contract size | AMC same-day 25s and 26s puts | **50** of each / **50** contracts [4, 10] |
| Phase 2 26 put premium cost | AMC same-day 26 puts | around **50** cents [10] |
| Phase 2 26 put total cost | AMC same-day 26 puts | **2500** [10] |
| Phase 2 25 put premium cost | AMC same-day 25 puts | **30** cents [10] |
| Phase 2 25 put total cost | AMC same-day 25 puts | **fifteen hundred** dollars [10] |
| Roll campaign profit floor | AMC same-day puts campaign | gain of **4 500** [10] / **forty five hundred** dollars [11, 14] |
| Phase 2 exit price multiplier | AMC same-day 25s and 26s puts | **twice** what we paid [11] |
| Phase 2 26 puts proceeds | AMC same-day 26 puts | **five thousand** dollars [11] |
| Phase 2 25 puts proceeds | AMC same-day 25 puts | **three thousand** dollars [11] |
| Total campaign profits | AMC puts campaign | **twelve thousand five hundred** dollars [11, 14] |

### [4DAONEGmoX8] The 14 Day Asymmetrical Iron Condor (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Russell 2000 Index (RUT) options, or other liquid underlyings like index ETFs (such as IWM or SPX/SPY ETFs) that bring in decent premiums [1-3].
    *   **Structure**: **Asymmetrical Iron Condor (AIC)**, which is also referred to as the **"weird R"** or **"weird or"** [4, 5].
    *   **Strikes/Deltas**: The strategy combines credit spreads and debit spreads (specifically, a ratio of ten put credit spreads to one put debit spread) [6, 7]. At entry, the trade is market neutral, but the Delta is always designed to be slightly long [8, 9]. It features a flat T+0 line similar to a butterfly trade to remain highly risk-averse and avoid dealing with costly upside adjustments [1, 10]. 
    *   **DTE (Days to Expiration)**: Entered close to expiration, specifically between **30 to 35 days** [6, 11].
    *   **Entry Trigger**: Weekly strategy put on once a week [12]. Because the strategy is market neutral, the trader does not guess direction [8]. The trader typically picks a day near the end of the week and enters in the morning to get it out of the way [13]. If there is a volatility spike on a down day, that is an ideal but not mandatory entry condition [13].

*   **The Management and Exit Rules**:
    *   **Holding Period Limit**: Designed for quick profits; the holding period is strictly **14 days or less** [6, 14].
    *   **Profit Target**: Exit immediately ("if I hit that I'm gone") upon reaching a profit of **2% to 4%** (or **2% to 3%** as frequently referenced) of the Reg T margin [15-17].
    *   **Stop Loss / Risk Capping**: Losses are kept small, strictly smaller than **5%** most of the time [15]. The trader can exit early at under a **1%** loss if a large move makes recovery unlikely [18, 19].
    *   **Downside Moves / Adjustments**: Downside adjustments are triggered on technical index point drops (such as RUT dropping about 20 points or making an intraday drop of 33 points) [20]. The trader rolls the positions to flatten out Deltas under the profit tent [20]. Because the trade is closer to expiration, there is very little time to recover from multiple adjustments, so the presenter advises taking a small loss early rather than aggressively defending a badly challenged position [6, 19].
    *   **Upside Risk Management**: The upside risk can be completely removed if managed properly [2].
    *   **Exit Discipline**: The trader evaluates risk versus reward, exiting the trade if there is not enough remaining reward for the risk taken [17].
    *   **Main Profit Engine**: Put credit spreads represent the main profit driver; the trader should focus on getting fills close to the mid-price for the put credit spreads [7].

*   **The Stated Edge or Statistics**:
    *   **83% Win Rate**: Win-loss expectancy is about **83 percent** (representing **ten wins to two losses**) [15].
    *   **Smooth Capital Growth**: Small drawdowns combined with a high win-loss expectancy produce a smooth equity growth curve that protects capital [8].
    *   **Capital Efficiency**: Cuts margin/capital requirements in half compared to the monthly version while targeting the same annual return [4, 16, 21]. For example, a monthly strategy with two units risks \$36,000, whereas trading one unit of the 14-day AIC every other week risks only \$18,000 at any one time on \$20,000 planned capital [16, 21].
    *   **Time Diversification Edge**: Placing trades on a weekly cycle spreads risk across diverse market regimes, allowing the trader to bypass specific bad periods (such as market crashes or vertical rallies) and capture profit [16, 22, 23].
    *   **Consistent Returns**: Generates steady monthly/yearly growth (averaging 52% per year on \$20,000 planned capital when entering every other week) [16]. It also features highly efficient margin requirements that remain stable throughout the trade, regardless of adjustments [2, 13].

*   **The Caveats the Presenter Gives**:
    *   **Shorter Recovery Window**: The main risk is that the closer the trade gets to expiration, the less time there is to recover from large adverse moves or downside adjustments [6, 19].
    *   **Vol Crush / Gamma / Assignment Risk**: Closer to expiration, Gamma risk and assignment risk accelerate, meaning the trade must be watched and managed with tighter discipline [6, 17].
    *   **Liquidity Requirements**: Weekly option chains have less liquidity than monthly chains. Thus, the strategy works best on smaller sizing (e.g., 1 to 25 tranches), whereas trading massive size (e.g., 100 tranches) should be kept in the monthly cycles [3].
    *   **Margin Buffering**: While the margin per tranche is \$17,000 to \$18,000, the trader must maintain at least a \$20,000 minimum account size to have a buffer ("wiggle room") in case the first trade is a loss [9].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | QQQ Thanksgiving Iron Butterfly | **12000** views [4] |
| Strategy name duration | 14-Day Asymmetrical Iron Condor | **14** day [4], **14-day** [4, 6, 24], **14** days or less [6, 14] |
| Expected win rate | 14-Day Asymmetrical Iron Condor | about **83%** [15] |
| Win/loss outcomes count ratio | 14-Day Asymmetrical Iron Condor | **ten** wins to **two** losses [15] |
| Target profit percentage range per trade | 14-Day Asymmetrical Iron Condor | **two to four percent** [15] |
| Target profit percentage range (shooting for / average) | 14-Day Asymmetrical Iron Condor | **two to three percent** [17, 23], **between 2 and 3%** [16], **2%** per trade [16] |
| Target profit (Neil's question) | Weekly AIC, per tranche | **four to five hundred dollars** [23] |
| Max loss target limit | 14-Day Asymmetrical Iron Condor | smaller than **5%** [15], under **5%** [19] |
| Max loss target (Trade 4b result) | Weekly AIC, closed at a loss | less than a **1%** loss [18] |
| DTE at entry (monthly AIC) | Monthly Asymmetrical Iron Condor | **forty to fifty** days [12] |
| Average holding time (monthly AIC) | Monthly Asymmetrical Iron Condor | around **30** days [12], **30 to 40** days [12], about **30** days [12] |
| Monthly AIC exit target DTE | Monthly Asymmetrical Iron Condor | **14** days to expiration [12] |
| Monthly AIC trade count per year | Monthly Asymmetrical Iron Condor | **twelve** trades per year [21] |
| Weekly AIC trade count per year | 14-Day Asymmetrical Iron Condor | up to **52** trade opportunities per year [21] |
| Non-overlapping weekly AIC trade count | 14-Day Asymmetrical Iron Condor | **26** trade opportunities [16] |
| Opportunities per month | 14-Day Asymmetrical Iron Condor | **four** opportunities per month [16] |
| Monthly AIC average return per trade | Monthly Asymmetrical Iron Condor | **three or four percent** [21] |
| Monthly AIC annual return (with \$40k capital) | Monthly Asymmetrical Iron Condor, 2 tranches | **24 to 48 percent** per year [21] |
| 14-day AIC annual return (every other week, \$20k capital) | 14-Day Asymmetrical Iron Condor, 1 tranche | **52 percent** per year [16] |
| Sizing capital (monthly AIC, 2 tranches) | Monthly Asymmetrical Iron Condor, 2 tranches | **forty thousand dollars** [16, 21] |
| Risked capital (monthly AIC, 2 tranches) | Monthly Asymmetrical Iron Condor, 2 tranches | about **thirty six thousand** [21] |
| Margin per tranche (Reg T margin) | Asymmetrical Iron Condor, per tranche | somewhere between **seventeen and eighteen thousand dollars** [17], usually around **17** but **eighteen thousand dollars** [9], **18,000** [16], somewhere around **\$17,000** [25], **seventeen and eighteen thousand dollars** [17] |
| Minimum account size / planned capital | Asymmetrical Iron Condor, per tranche | **twenty thousand** [9, 25], **twenty thousand dollars** [25], **\$20,000** [16] |
| Sizing capital (monthly AIC, 2 tranches) | Monthly Asymmetrical Iron Condor | **forty thousand dollars** [16, 21] |
| Live trading experience (monthly AIC) | Monthly Asymmetrical Iron Condor | multiple year [26], about **four years** now [26], **four or five years** now [26], **four years** [3] |
| Live trading experience (14-day AIC style) | 14-Day Asymmetrical Iron Condor | a few months [26], **a few months** live [3] |
| Maximum size limit for weeklies tranches | 14-Day Asymmetrical Iron Condor | **twenty five** tranches is fine, but a **hundred** is too large [3] |
| Size limit for single/double tranches | 14-Day Asymmetrical Iron Condor | **one or two** tranches [3] |
| Historical backtest timeframe | 14-Day Asymmetrical Iron Condor | **January 2017 through February 2018** [25] |
| Historical backtest total trades count | 14-Day Asymmetrical Iron Condor | **54** total trades [25] |
| Historical backtest average holding duration | 14-Day Asymmetrical Iron Condor | only **8** days [25] |
| Historical backtest win/loss outcome count | 14-Day Asymmetrical Iron Condor | **46** winds to a La Russaes (garbled) [25] |
| Historical backtest average win amount | 14-Day Asymmetrical Iron Condor | **\$369** [25] |
| Historical backtest average loss amount | 14-Day Asymmetrical Iron Condor | **315** [25], **\$315** [25] |
| Historical backtest largest win amount | 14-Day Asymmetrical Iron Condor | **\$669** [25] |
| Historical backtest largest loss amount | 14-Day Asymmetrical Iron Condor | **735 dollars** [25] |
| Trade 1 launch date | RUT Asymmetrical Iron Condor | the **fourth** of the month [22], **5 4 2 17** [27] |
| Trade 1 entry index price | RUT Asymmetrical Iron Condor | **1384** [22] |
| Trade 1 check-in time | RUT Asymmetrical Iron Condor | day **six** [22], **six** days [27] |
| Trade 1 profit return | RUT Asymmetrical Iron Condor | **2.9 percent** [22, 28], **2.76 percent** [27] |
| Trade 2 launch date | RUT Asymmetrical Iron Condor | **5 11 17** [29] |
| Trade 2 entry index price | RUT Asymmetrical Iron Condor | **thirteen ninety** [29] |
| Trade 2 check-in time | RUT Asymmetrical Iron Condor | day **five** [29], **five** days [27] |
| Trade 2 early exit profit return | RUT Asymmetrical Iron Condor | **2.6%** [29], **2.43 percent** [27] |
| Trade 2b holding time (continuation) | RUT Asymmetrical Iron Condor | day **six** [20, 30] |
| Trade 2b index drop to trigger first adjustment | RUT Asymmetrical Iron Condor | down about **twenty** points [20] |
| Trade 2b first adjustment index price | RUT Asymmetrical Iron Condor | **thirteen seventy four** [20] |
| Trade 2b same day end drop | RUT Asymmetrical Iron Condor | about **thirty three** points [20] |
| Trade 2b continuation drop from first adjustment | RUT Asymmetrical Iron Condor | another **thirteen or fourteen** points [20] |
| Trade 2b paper loss at day six close | RUT Asymmetrical Iron Condor | down about **three percent** [30] |
| Trade 2b day 8 index price | RUT Asymmetrical Iron Condor | **thirteen sixty six** [30] |
| Trade 2b day 12 index price | RUT Asymmetrical Iron Condor | **thirteen seventy two** [27] |
| Trade 2b day 12 distance lower than start | RUT Asymmetrical Iron Condor | about **twenty** points lower than where I started [27] |
| Trade 2b final profit return | RUT Asymmetrical Iron Condor | about **one point one percent** [27], just under **ten** just under **one percent** (garbled) [27] |
| Trade 2b total holding duration | RUT Asymmetrical Iron Condor | additional **seven** days [27], **twelve** days total [27] |
| Trade 3 duration | RUT Asymmetrical Iron Condor | **four** days [18] |
| Trade 3 profit return | RUT Asymmetrical Iron Condor | **2.6%** [18] |
| Trade 4 duration | RUT Asymmetrical Iron Condor | **8** days [18] |
| Trade 4 loss | RUT Asymmetrical Iron Condor | less than a **1%** loss [18] |
| Four trades monthly total return | RUT Asymmetrical Iron Condor | somewhere around **seven point one three percent** [31] |
| Four trades monthly total return if Trade 2 held | RUT Asymmetrical Iron Condor | **five point six three percent** [31] |
| Trade 4 (February correction) DTE durations | RUT Asymmetrical Iron Condor | **12** days **8** days **15** and **11** [19] |
| Trade 4 (February correction) duration | RUT Asymmetrical Iron Condor | **four** days [19] |
| Trade 4b (February correction) duration | RUT Asymmetrical Iron Condor | only in it for **a day** [23] |
| Wing contracts ratio | RUT Asymmetrical Iron Condor | **ten** put credit spreads to **one** put debit spread [7] |
| Spread exit slippage cost | RUT Asymmetrical Iron Condor | extra **nickel or a dime** [7] |
| Q&A duration | RUT Asymmetrical Iron Condor | **ten** minutes [23] |

***

📊 *I could put together a structural comparison between the 14-day AIC and a standard at-the-money butterfly spread to visualize the difference in profit zone boundaries if that sounds useful!*

### [qpZr4V5NAaY] How to Safely Ride Out a Market Crash With This Easy (and cheap) Options Strategy (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX index) [1].
    *   **Structure**: Put calendar spread campaign that is converted into a put debit spread once a pullback occurs [2].
    *   **Strikes/Deltas**: 
        *   *Long Put Strike*: **4480 put** [2].
        *   *Short Put Strike*: **43.60 put** (representing the 4360 strike) [2, 3].
        *   *Deltas*: No specific Delta targets or values are spoken in the provided passages of this video.
    *   **DTE (Days to Expiration)**: Entered when the options are almost **two months** away from expiration [2].
    *   **Entry Trigger**: Positioned as a defensive hedge for an equity portfolio. The trader initiates the long put after a prolonged market rally (such as the hard rally in **2021** [1]) to anticipate an inevitable market pullback, particularly heading into historically volatile periods like **October** [1].

*   **The Management and Exit Rules**:
    *   **Initial Entry**: Purchase the long 4480 put option when the market is elevated [2].
    *   **Conversion to Put Debit Spread**: If the market experiences a sharp sell-off soon after entry (e.g., selling off back down to **4 400**), the October options gain substantial value [2]. The trader then sells the **43.60 put** to convert the trade into a put debit spread [2].
    *   **Free Protection Rule**: By selling the 43.60 put for **103.87**, which is a higher price than what was initially paid for the long put, the cost of the hedge is completely removed [2, 3]. From that point on, the hedge is "for free" with zero downside risk [3].
    *   **Winning Exit (Market Crash)**: In the bearish scenario the trader is worried about, the put debit spread can yield a spectacular profit of up to **twelve thousand three hundred fifty dollars** [3].
    *   **Consolation Exit (Market Rallies)**: If the market does not sell off further and instead rallies, all options expire worthless, but the trader still locks in a profit (the net credit from converting the spread) as their guaranteed minimum profit [3].

*   **The Stated Edge or Statistics**:
    *   **Elimination of Hedge Cost**: The strategy exploits early pullbacks to finance the long put option. Converting it into a put debit spread can eliminate the cost entirely, turning a typical portfolio drag (hedging cost) into a free position with a guaranteed profit [3].
    *   **Historical Precedent**: The presenter cites **2018** when the SPX rallied from a low of **2553** (beginning of the **second** quarter) to a high of **29.40** (end of the **third** quarter—a **15 percent** gain) before giving it all back in **October** by dropping to **2605** [1]. This historical volatility represents the type of market meltdown the cheap hedge protects against [1].
    *   **Workshop Stated Probability**: Teaches three professional options strategies, including a high-probability strategy that boasts an **eighty percent** statistical probability of profit month in and month out [4].

*   **The Caveats the Presenter Gives**:
    *   The strategy is not guaranteed; it requires "a little bit of luck with your initial entry" to get a reasonable-sized pullback shortly after entering the trade to successfully convert it to a free position [3].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[qpZr4V5NAaY]` metadata | **12000** views [5] |
| Historical SPX correction (Low) | SPX Index, Q2 2018 | **2553** low [1] |
| Historical SPX correction (Quarter of low) | SPX Index, Q2 2018 | **second** quarter [1] |
| Historical SPX correction (High) | SPX Index, Q3 2018 | **29.40** high (representing 2940) [1] |
| Historical SPX correction (Quarter of high) | SPX Index, Q3 2018 | **third** quarter [1] |
| Historical SPX correction (Rally magnitude) | SPX Index, Q2-Q3 2018 | gain of **15 percent** [1] |
| Historical SPX correction (Pullback low) | SPX Index, October 2018 | dropped down to **2605** (at **one** point) [1] |
| Strong market rally timeline | SPX Index macro trend | Year **2021** [1] |
| Multi-month timing projection | SPX Option Spread, October expiration | next **two** months [4] |
| Promoted workshop strategies | General options class promo | teaches **three** options strategies [4] |
| Promoted workshop win rate | High-probability options strategy | statistical **eighty percent** probability of profit [4] |
| SPX pullback level after entry | SPX Put Debit Spread | sold off back down to **4 400** [2] |
| DTE at spread conversion | SPX Put Debit Spread, October chain | almost **two** months away [2] |
| Long put strike price | SPX Put Debit Spread | **4480** put [2] |
| Short put strike price | SPX Put Debit Spread | **43.60** put (representing 4360) [2] |
| Short put premium collected | SPX Put Debit Spread | received **103.87** [2] |
| Index options multiplier | SPX Index Option contract mechanics | **one hundred** dollars per point [2] |
| Short put strike price segment (garbled/split) | SPX Put Debit Spread | **forty th** (garbled/truncated split) [2] |
| Short put strike price segment (garbled/split cont.) | SPX Put Debit Spread | **rty three sixty** (garbled/verbatim split) [3] |
| Maximum profit of free hedge | SPX Put Debit Spread | profit up to **twelve thousand three hundred fifty** dollars [3] |

### [97HFwhb_wxI] You Can REACT to the Market Instead of Predicting It With This 1 Day Options Strategy (12,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: S&P 500 Index options (SPX index options, which are cash-settled contracts) [1, 2].
    *   **Structure**: **Iron Butterfly** options strategy [3].
    *   **Strikes/Deltas**: 
        *   *Short Strikes*: Sold 5 calls and 5 puts at the same strike: **3215** (the at-the-money strike, transcribed as "**30 32 15**" or "**32 15**" strike) [3, 4].
        *   *Long Call Strike*: Bought 5 calls 50 points above the short calls at **3265** (transcribed as "**thirty to sixty five**") [3, 4].
        *   *Long Put Strike*: Bought 5 puts 50 points below the short puts at **3165** (transcribed as "**thirty 165**") [3, 4].
        *   *Deltas*: Specific Delta selection targets are not explicitly stated in the transcript, but the trade is centered strictly "at the money" at entry [3].
    *   **DTE (Days to Expiration)**: Same-day expiration / **1-day trades** (zero DTE options) [1, 3].
    *   **Entry Trigger**: Positioned as a rangebound options income strategy that allows a trader to react to market behavior rather than predicting direction [1, 5]. It is entered at the market open on **June 10th** when the S&P 500 index is trading at about **3215** (transcribed as "**32 fifteen**") [2, 3].

*   **The Management and Exit Rules**:
    *   **Unmanaged Profit Zone**: If the trade is left alone and not managed, it will make a profit if SPX closes anywhere between **3190 and 3240** (boundaries transcribed as "**thirty one ninety and thirty to forty**") on the expiration day [6].
    *   **Defensive Adjustment (The Condor Roll)**: If the market moves outside of the unmanaged profit zone during the day, the trader executes a defensive adjustment to expand the range [5, 6].
        *   *Adjustment Trigger*: When SPX drops to **3190** (transcribed as "**thirty 190**") at **10:30 AM** (transcribed as "**ten thirty**")—testing the bottom edge of the profit zone [6].
        *   *Adjustment Action (Condor Roll)*: The trader rolls both put options down **35 points** [6]. 
            *   Buy back the 5 short puts at **3215** (transcribed as "**30 to 15**") to close them [6].
            *   Sell the 5 original long puts at **3165** (transcribed as "**30 165**") to close them [6].
            *   Sell 5 new short puts further out of the money at **3180** (transcribed as "**30 180**" or "**3184**") [6].
            *   Buy 5 new protective long puts further out of the money at **3130** (transcribed as "**31 30**") [6].
            *   This Condor roll leaves the short calls at their original position and establishes the short puts 35 points lower at **3180** (transcribed as "**30 180**") [6].
    *   **Adjusted Profit Zone**: The put roll expands the profit range, creating a **55-point zone** (transcribed as "**55 points own**" / "**55**") between the adjusted short put (3180) and the original short call (3215) [5].
    *   **Winning Exit (At Settlement)**: On the final afternoon close, SPX sells off and closes at **3190** (transcribed as "**30 190**") [7]. Because this is above the short 3180 put strike and below the short 3215 call strike, all options expire completely worthless at the **4:00 PM** (transcribed as "**4:00 p.m.**") close [5, 7]. The trader pockets the remaining credit after paying the net cost of the Condor roll [5].

*   **The Stated Edge or Statistics**:
    *   **Reactivity Over Prediction**: The strategy does not require predicting the market's direction [1]. Instead, options allow the trader to shape the trade dynamically around what the market is actually doing [5].
    *   **Wide Profit Boundaries**: By adjusting the put or call side, the trader creates a wide zone of safety to capture decay on sleepy or choppy trading days [5].
    *   **Workshop Promoted Edge**: Teaches three professional options strategies, including an options income strategy that boasts an **80 percent** (transcribed as "**eighty percent**") statistical probability of profit month in and month out [4].

*   **The Caveats the Presenter Gives**:
    *   **Cost of Adjustments**: Moving options is not free; rolling the condor wings closer to safety consumes a portion of the original credit and reduces the total potential profit of the trade [5].
    *   **Extreme Gap/Move Risk**: If left completely unmanaged, or if the market has an extreme move beyond the expanded boundaries, the trade can still suffer losses up to its defined maximum risk of **\$11,915** (transcribed as "**eleven thousand nine hundred fifteen dollars**") [4].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[97HFwhb_wxI]` video metadata | "**12000** views" [1] |
| S&P 500 entry index level | SPX Index, June 10th | "**32 fifteen**" [1, 2] |
| Options expiration duration | SPX Iron Butterfly | "**one**-day" [1, 2] |
| Entry date | SPX Iron Butterfly | "June **10th**" [2, 3] |
| Standard equity options multiplier | General stock options contract sizing | "**100** shares" [2] |
| Index option point value multiplier | Index option contract mechanics | "**\$100** per point" [2] |
| Short options contract sizing | SPX Iron Butterfly | sold "**five** calls" [3] and "**five** puts" [3] |
| At-the-money short strike price | SPX Iron Butterfly | "**30 32 15** strike" [3] |
| Long call strike price | SPX Iron Butterfly, June 10th long call | "**thirty to sixty five**" [3] / "**thirty to sixty five** call" [4] |
| Long put strike price | SPX Iron Butterfly, June 10th long put | "**thirty 165**" [3] / "**thirty 165** puts" [4] |
| Call credit spread wing width | SPX Iron Butterfly call wing | "**50** points above the short calls" [3] |
| Put credit spread wing width | SPX Iron Butterfly put wing | "**50** points under the short pussy" (transcribed puts typo) [3] |
| Long call purchase premium price | SPX long 3265 call | bought for "**a dollar 73**" [4] |
| Total long calls purchase cost | SPX long 3265 calls, 5 contracts | "**eight hundred sixty-five** dollars" [4] |
| Short call strike price | SPX short 3215 call | "**thirty fifteen** call" [4] |
| Short call sale premium price | SPX short 3215 call | sold for "**15 76**" (transcribed as "**415 76**") [4] |
| Total short calls credit cash received | SPX short 3215 calls, 5 contracts | "**78 80**" [4] |
| Short put contracts sold | SPX short 3215 put | sold "**five** puts" [4] |
| Short put strike price | SPX short 3215 put | "**32 15**" [4] |
| Total short puts credit cash received | SPX short 3215 puts, 5 contracts | brought in "**74 45**" [4] |
| Long puts purchased count | SPX long 3165 put | bought "**five**" [4] |
| Total long puts purchase cost | SPX long 3165 puts, 5 contracts | costing "**1375**" [4] |
| Netted out initial cash credit inflow | SPX Iron Butterfly | "**thirteen thousand and eighty five** dollars" [4] |
| Required broker margin capital / max risk | SPX Iron Butterfly | "**eleven thousand nine hundred fifteen** dollars" [4] |
| Workshop promotion strategy count | General options income workshop | teaches "**three** of those strategies" [4, 8] |
| High-probability options win rate | High-probability options strategy | statistical "**eighty percent**" probability of profit [4, 8] |
| Unmanaged trade profit zone boundaries | SPX Iron Butterfly, unmanaged | profit at anywhere between "**thirty one ninety** and "**thirty to forty**" [6] |
| Check-in/Adjustment time of day | SPX Iron Butterfly, Condor Roll | "**ten thirty**" [6] |
| Index level at adjustment time | SPX Index, 10:30 AM | dropped to "**thirty 190**" [6] |
| Put options roll down distance | SPX Put Condor Roll | move both put options down "**35** points" [6] |
| Rolled short put strike price | SPX Put Condor Roll | "**3184**" (representing 3180 for, transcribed short puts strike) [6] |
| Rolled short put contracts count | SPX Put Condor Roll | "**five** short put options" [6] |
| Rolled long protective puts strike price | SPX Put Condor Roll | "**31 30**" [6] |
| Rolled long puts contracts count | SPX Put Condor Roll | "**five** long put options" [6] |
| Original short puts strike price bought back | SPX Put Condor Roll | buy back the short puts at "**30 to 15**" [6] |
| New short puts sold count | SPX Put Condor Roll | selling "**five** puts" [6] |
| New short puts strike price sold | SPX Put Condor Roll | puts at "**30 180**" [6] |
| Original long puts strike price sold | SPX Put Condor Roll | selling the original long puts down at "**30 165**" [6] |
| New long puts bought count | SPX Put Condor Roll | buying the "**five** new foots" (transcribed puts typo) [6] |
| New adjusted short put strike price | SPX Put Condor Roll | short puts at "**30 180**" [6] |
| Original cash received reference | SPX Iron Butterfly credit | originally received cash of about "**\$13,000**" [6] |
| Index closing price at expiration | SPX Index, 4:00 PM close | ended up back down at "**30 190**" (representing 3190 close) [7] |
| Index options close settlement time | SPX expiration day close | settlement at "**4:00 p.m.**" [7] |
| Long call strike price at expiration | SPX long call | "**3285** calls" (representing 3265, transcribed long call strike) [7] |
| Adjusted profit zone width | SPX Put Condor Roll | "**55** points own" (representing 35 point zone, transcribed zone) [5] |
| Workshop promotion duration | General options income workshop | "**two** hour" / "**two** hour free intensive workshop" [4, 8] |

### [vM1dt9PIKjw] If you use this simple options strategy you're win rate HAS to improve, probably dramatically (12,000 views)

PART A — HANDBOOK CHAPTER CONTENT

#### The Setup
*   **Instrument**: SPY ETF (the exchange-traded fund that holds a basket of stocks mimicking the S&P 500 Index) [1].
*   **Structure**: Put credit spreads [2, 3].
*   **Strikes/Deltas**: The short put option is located below the market when entering the trade [4]. No specific Delta numbers are spoken for the credit spread setup in this video.
*   **DTE (Days to Expiration)**: Same-day expiration / **1-day trades** (zero DTE) [1, 5].
*   **Entry Trigger**: Triggered by a rules-based trading system/program that generates buy or sell signals on Mondays, Wednesdays, or Fridays (the days SPY options expire) [1, 6]. The study analyzed signals generated since **January 1st, 2018** [1].

#### The Management and Exit Rules
*   **Set and Forget**: The trade is managed passively; positions are put on in the morning and allowed to expire at the close, letting the broker settle the contracts [1, 4]. 
*   **Winning Exit**: If the market moves in favor of the signal, or even if it moves against the signal by **one dollar or less**, the put credit spread expires worthless, allowing the trader to pocket 100% of the premium as a win [3, 4].
*   **Losing Exit**: If the market collapses strongly against the directional signal, the trade hits its defined risk. However, the protective long put option places a hard floor on the position to keep losses defined and prevent catastrophic drawdowns [4].

#### The Stated Edge or Statistics
*   **High Probability Optimization**: The raw signal trading SPY shares outright yields a win rate of **52.2 percent** (237 wins vs. 214 losses out of 451 cases since 2018) [1, 5].
*   **The Small-Loss Flip**: Fully **24 percent** of all trades (nearly half of the losing trades) experienced a loss of **one dollar or less** [5, 7].
*   **Spread Transformation**: By utilizing a put credit spread, all of these "one dollar or less" losing trades are converted into outright wins [3, 4]. 
*   **Win Rate Supercharging**: This flip dramatically rockets the win rate to **76.7 percent** (and drops the loss rate to **23.3 percent**), which is a **25 point** improvement in both directions [3].
*   **Wiggle Room Edge**: The cushion of selling puts below the market allows the trader to be temporarily or slightly wrong on direction but still walk away with a profitable trade [4, 8].

#### The Caveats the Presenter Gives
*   The presenter cautions that this dramatic win rate boost does "not necessarily result in a stronger profit result in every single case of using option spreads versus outright buying and selling shares with signals." [3]
*   Rules-based systematic trading can be emotionally difficult; "some traders find it hard to swallow" when they experience losses [9].

***

PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[vM1dt9PIKjw]` metadata | **12000** views [10] |
| Free workshop promotions | General options class | teaches **three** real-world option strategies [7, 8] |
| Rules-based system win probability baseline | General rules-based trading system | wins as low as **52** times out of **100** [9] |
| Rules-based system loss probability baseline | General rules-based trading system | losing **48** of the time [9] |
| Historical study start date | SPY rules-based system study | **january 1st 2018** [1] |
| Historical study sample size | SPY rules-based system study | **451** cases since **2018** [1, 4] |
| Outright share trading wins | SPY rules-based system study | won **237** times [5] |
| Outright share trading losses | SPY rules-based system study | lost **214** times [5] |
| Outright share win rate percentage | SPY rules-based system study | win rate of **52.2 percent** [5] |
| Outright share loss rate percentage | SPY rules-based system study | losing about **47.8 percent** of the time [5] |
| Outright share large win threshold | SPY rules-based system study | SPY moved at least **five dollars** [5] |
| Outright share large wins proportion | SPY rules-based system study | **four percent** of the wins [5] |
| Outright share small loss threshold | SPY rules-based system study | under **one dollar** / **one dollar** or less category [4, 7] |
| Small loss category proportion | SPY rules-based system study | represented fully **24** (representing 24 percent of all trades) [7] |
| Standard equity options contract sizing | General options contract multiplier | entitles the buyer to purchase **100** shares [11] |
| Case study execution date | SPY put credit spread case study | **wednesday june 3rd 2019** [2] |
| SPY entry trading price | SPY put credit spread case study | trading at around **275** [2] |
| Outright share transaction sizing | SPY put credit spread case study | bought **1 000** shares of spy [2] |
| Outright share transaction entry price | SPY put credit spread case study | bought at **275 dollars and five cents** [2] |
| Outright share transaction exit price | SPY put credit spread case study | sold off down to **274.57** [2] |
| Discrepant entry price mentioned by presenter | SPY put credit spread case study | bought the shares for **275 and 50** [2] |
| Outright share transaction loss | SPY put credit spread case study | loss of **480** on the trade [2] |
| Total flipped trades percentage | SPY put credit spread study | all **24 percent** of those trades flipping from losers to winners [3] |
| Put credit spread win rate | SPY put credit spread study | win rate skyrocket to **76.7 percent** [3] |
| Put credit spread loss rate | SPY put credit spread study | loss rate drops to **23.3 percent** [3] |
| Win/loss rate percentage gain | SPY put credit spread study | a **25** point improvement in both cases [3] |

### [CLywU1I3YB4] How to Profit From a Pullback on TSLA with Options (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **Tesla (TSLA) common stock options** [1, 2].
    *   **Structure**: **Iron Condor** options strategy, constructed by combining a call credit spread on the call side and a put credit spread on the put side [3, 4].
    *   **Strikes/Deltas**: 
        *   *Short Call Strike*: Sold 10 of the **810** calls [3].
        *   *Long Call Strike (Protection)*: Bought 10 of the **830** calls [4].
        *   *Short Put Strike*: Sold 10 of the **600** puts [3].
        *   *Long Put Strike (Protection)*: Bought 10 of the **580** puts [4].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in this transcript, though the strikes are positioned relative to market support and resistance [5].
    *   **DTE (Days to Expiration)**: Entered with options that expire "**a few months out**" [3] (specifically **March 19th, 2021**, entered on **January 7th, 2021** [3, 6], which represents **a little over two months** [7]).
    *   **Entry Trigger**: Triggered when a highly volatile stock (Tesla) has undergone an explosive, overextended rally and is anticipated to undergo a profit-taking pullback [2, 8]. Specifically, TSLA had rallied hugely, up over **55 percent** from October 1st to November 1st [2], pushing up over **1200** for a short period of time in less than **two weeks** [2]. A historical analogy was also drawn from **2020** when Tesla rallied almost **eight-fold** during the year [3].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (The Winning Exit)**: If the stock closes within the defined profit range of the short strikes (above the puts and below the calls) at expiration, all options expire completely worthless [7, 9]. 
        *   In the case study, TSLA closed at **652** on March 19th, 2021 [6]. Because this closing price was well below the short 810 call strike and above the short 600 put strike [6], all options expired worthless [9]. 
        *   The trader simply pocketed the full initial cash credit of **eleven thousand seven hundred ninety dollars** (\$11,790) as net profit [9].
    *   **Wide Profit Range Forgiveness**: The trade does not require a perfect directional prediction. The trader wins the entire initial credit if the stock closes anywhere between **600 and 810** [6, 9], and even at any price above **580** and below **830** (since the options expire worthless as long as they are not violated) [7, 9]. Specifically, if TSLA closes at **600 and 1 cent** on expiration day, both the 600 and 580 puts still expire completely worthless [7]. 

*   **The Stated Edge or Statistics**:
    *   **Wide Margin of Error**: Unlike directional stock trading, this options strategy allows a trader to succeed by simply defining a broad range of future prices. In this case study, the profitable pullback zone was **over 200 points wide** [5].
    *   **Exceptional Yield**: In the case study, the Iron Condor yielded a return of **over 143 percent** in a little over two months on the capital required to execute the trade [7].
    *   **Win When "Flat Out Wrong"**: This strategy provides a win even when the trader is flat out wrong about the direction of the underlying stock, as long as it remains within the wide profit range at expiration [7].

*   **The Caveats the Presenter Gives**:
    *   **Broker Margin/Worst-case Loss**: Executing the trade requires a substantial capital buffer. The broker requires the trader to have **at least 80 to 10** (spoken exactly as "80 to 10", representing the margin requirement/worst-case loss) in their account to enter the trade [6].
    *   **Capped Returns**: The maximum possible reward of this trade is strictly capped and limited to the upfront credit collected (**eleven thousand seven hundred ninety dollars**) [7, 9].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video card metadata | **11000** views |
| Tesla stock rally magnitude | Tesla common stock, Oct 1st to Nov 1st | up over **55 percent** / up over **55** |
| Tesla stock rally peak | Tesla common stock, post-earnings rally | over **1200** |
| Tesla stock rally duration | Tesla common stock, post-earnings rally | less than **two weeks** |
| Analogy year for Tesla rally | Tesla common stock rally historical analogy | Year **2020** |
| Tesla 2020 rally magnitude | Tesla common stock historical analogy | rallied almost **eight-fold** |
| Case study entry date | Tesla Iron Condor campaign | **january 7th** (first week in january of **2021**) |
| Options expiration date | Tesla Iron Condor campaign | **march 19th** (**march 19 2021**) |
| Put credit spread short contracts size | Tesla Iron Condor, March 19th expiration | sell **10** of those |
| Call credit spread short contracts size | Tesla Iron Condor, March 19th expiration | sell **10** of those |
| Short call option strike | Tesla short call | **810** calls / "**a10** calls" (verbatim transcription typo) |
| Short put option strike | Tesla short put | **600** puts |
| Quantity of protective long calls | Tesla Iron Condor | buy **10** |
| Quantity of protective long puts | Tesla Iron Condor | buy **10** |
| Long call option strike | Tesla long protective calls | **830** calls |
| Long put option strike | Tesla long protective puts | **580** puts |
| Stated profit zone short strikes range | Tesla Iron Condor | **600 to 810** range |
| Short call individual premium | Tesla short 810 calls | priced at **104.65** |
| Option contract sizing multiplier | General options contract specs | represents **100** shares of tesla stock |
| Quantity of contracts multiplier | General options contract specs | multiply that by **100** and we sold **10** |
| Total cash credit from short calls | Tesla short 810 calls | **one hundred four thousand six hundred fifty dollars** |
| Long call individual cost | Tesla long 830 calls | paid **ninety six dollars and forty eight cents** |
| Total cost of long protective calls | Tesla long 830 calls | cost us **96 480** |
| Total credit from short puts | Tesla short 600 puts | brought in **22 450** |
| Total cost of long protective puts | Tesla long 580 puts | pay back out **18 830** |
| Net entry cash credit inflow | Tesla Iron Condor campaign | total cash inflow of **11 790** |
| Required broker capital / worst-case risk | Tesla Iron Condor campaign | have at least **80 to 10** in your account / worst loss possible |
| Options campaign duration | Tesla Iron Condor campaign | expiring about **3** months later / a little over **two** months |
| High stock price peak in January | Tesla common stock, January 2021 | initial rally up to **900** in january |
| Stock closing price at expiration | Tesla common stock, March 19th, 2021 | closed at **6 52** / **652** |
| Closing distance from short calls | Tesla Iron Condor calls at expiration | expired **158 and 178 points** respectively above closing |
| Expiration puts strike reference | Tesla Iron Condor puts at expiration | puts down at **600 and 580** |
| Stated campaign net profit | Tesla Iron Condor campaign final result | profit of exactly **eleven thousand seven hundred ninety dollars** |
| Trade annualized return on margin | Tesla Iron Condor campaign final result | return of over **143 percent** |
| Spoken range boundaries for same outcome | Tesla Iron Condor same outcome zone | any price between **680 and 810** (verbatim speaking slip/typo) |
| Outer strike call boundaries | Tesla Iron Condor call side expiration | close on expiration day at **7.99 and 99 cents** unless they're over **800** |
| Outer strike put boundaries | Tesla Iron Condor put side expiration | closes at **600 and 1 cent** |
| Put credit spread short put strike | Tesla Iron Condor put side expiration | **600** puts |
| Put credit spread long put strike | Tesla Iron Condor put side expiration | **580** puts |
| Expanded profit zone width | Tesla Iron Condor campaign | over **200 points wide** |
| Promoted workshop option strategies | General options class promo | teaches **three** option strategies |
| Promoted workshop win rate | High-probability options strategy | statistical **eighty percent** probability of profit |

***

📊 *Would you like me to construct a visual P&L risk graph comparing this Tesla Iron Condor setup to a simple long stock position to clearly illustrate the difference in drawdown profiles?*

### [ofFaU56ynsk] How You Can Own Call Options For Free (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Tesla (TSLA) common stock options [1].
    *   **Structure**: **Synthetic Covered Call** (or "own call options for free" strategy) established by buying a long call option and subsequently selling a higher strike call option against it [2-4].
    *   **Strikes/Deltas**: 
        *   *Long Call Strike*: **1150** calls (verbatim transcript also references "**1500** calls" as the original cost basis in a subsequent passage, representing a speaking slip/transcript discrepancy) [5, 6].
        *   *Short Call Strike*: **1200** calls [5].
        *   *Deltas*: No specific Delta targets or values are spoken in this transcript.
    *   **DTE (Days to Expiration)**: Entered with **10** days to expiration on the long calls [5].
    *   **Entry Trigger**: Executed after a prolonged market sell-off (such as in **2022**) when the market begins an inevitable, rapid bounce [2]. The tactical trigger is based on a bullish belief that a strong stock (Tesla) is undergoing a secondary breakout to push higher than its previous consolidation level [5].

*   **The Management and Exit Rules**:
    *   **Initial Entry**: Buy the lower strike call option (the 1150 calls) at the market open when the stock is trading around **10.68** [5].
    *   **Downside/Unfavorable Outcome (Stock Closes at 1150 or Lower)**: If the stock fails to rally and remains below the long call strike, both options expire completely worthless [6, 7]. However, because the short calls were sold for more than the long calls cost, the trader still pockets the net positive cash flow of **56.88** (also spoken as **56.88 of cash flow**) as a guaranteed minimum profit [6, 7].
    *   **Winning/Explosive Outcome (Stock Closes above 1200)**: If the stock rallies aggressively as anticipated (crossing over **1200** on November 1st), the trader sells **three** of the **1200** calls [5]. This roll immediately sucks all risk out of the trade [7]. 
    *   At expiration, the short calls create a markdown of **22.9 cents per share** (translated to a total cash outflow of **6627** on the short position) [7]. However, adding back the **5688** positive cash flow credit results in a spectacular final net trade profit of **20 688** [7].

*   **The Stated Edge or Statistics**:
    *   **Risk-Free Protection**: By utilizing the momentum of a post-entry rally to write a higher strike option for more than the original cost of the long option, the trader completely eliminates downside risk [6, 7].
    *   **The Power of Bounces**: The presenter notes that market bounces are historically very powerful, citing a period where the S&P 500 index lost **35 percent** of its value and then rallied more than **40 percent** off its lows in less than **two and a half months** [8].

*   **The Caveats the Presenter Gives**:
    *   The strategy requires the stock to make a strong directional move shortly after entry so that the long options appreciate enough to sell the higher strike calls for a credit that exceeds the original purchase cost [3]. If the stock flatlines immediately after buying the long call, time decay will quickly erode the option value before the risk-free roll can be established.

---

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | General video metadata | **11000** views [9] |
| Historical index crash magnitude | S&P 500 Index | lost **35 percent** of its value [8] |
| Historical index recovery magnitude | S&P 500 Index | rallied more than **40 percent** off of its lows [8] |
| Historical index bounce timeline | S&P 500 Index | less than **two and a half months** [8] |
| Long call contracts count | TSLA synthetic covered call (Phase 1) | bought **three** [5] |
| Long call strike price | TSLA synthetic covered call (Phase 1) | **1150** calls [5] |
| Options duration on entry | TSLA synthetic covered call (Phase 1) | expiring in **10** days [5] |
| Stock price at entry | TSLA common stock | trading at about **10.68** [5] |
| Long call option individual premium | TSLA synthetic covered call (Phase 1) | paid **1558** [5] |
| Equity options standard sizing | Standard options contract multiplier | represents **100** shares [5] |
| Long call trade total cost | TSLA synthetic covered call (Phase 1) | total initial cost of the trade is **4674** [5] |
| Stock milestone price | TSLA common stock | over **1200** [5] |
| Short call strike price | TSLA synthetic covered call (Phase 2) | **1200** calls [5] |
| Short call contracts count | TSLA synthetic covered call (Phase 2) | sold **three** of the 1200 calls [5] |
| Short option per-share markdown | TSLA short 1200 calls (expiration) | hit in value of **22.9 cents** per share [7] |
| Short option per-share markdown | TSLA short 1200 calls (expiration) | forced to sell them **22.9 cents** below market [7] |
| Short option total account markdown | TSLA short 1200 calls (expiration) | cash outflow of **6627** [7] |
| Net entry cash credit | TSLA synthetic covered call | **5688** of positive cash flow [7] |
| Slip/Discrepancy strike spoken | TSLA synthetic covered call (Phase 2) | bought the **1500s** for (speaking slip/transcript typo for 1150s) [7] |
| Final campaign net profit | TSLA synthetic covered call | overall trade profit of **20 688** [7] |
| Expiration stock boundary | TSLA common stock | **11.50** or lower (verbatim representation of 1150) [6] |
| Minimum guaranteed campaign cash | TSLA synthetic covered call (worthless expire) | cash flow of **56.88** [6] |
| Minimum guaranteed campaign profit | TSLA synthetic covered call (worthless expire) | minimum we can make on the trade is that **56.88** [6] |
| Minimum guaranteed campaign profit | TSLA synthetic covered call (worthless expire) | make at least **56.88** [6] |
| Slip/Discrepancy strike spoken | TSLA synthetic covered call (original strike) | original cost basis on the **1500** calls (speaking slip/transcript typo for 1150s) [6] |

***

*   *Would you like to compare this "free call option" setup with a bearishly tilted put calendar spread to see how they perform on a volatile market consolidation?* 📉

### [0xzuGAUVqRM] Huge Options Trading Blunder #11: Market Orders on Options Spreads (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Amazon (AMZN) common stock options.
    *   **Structure**: Butterfly options strategy (specifically a call butterfly, constructed by selling an at-the-money call spread and buying an out-of-the-money call spread).
    *   **Strikes/Deltas**:
        *   *Short Strike*: Sold **20** calls at the **33 30** strike (the at-the-money strike where Amazon is trading).
        *   *Long Strike (Downside Wing)*: Bought **10** calls at the **32.60** strike (representing **3260**, also referred to as "**30 to 60**").
        *   *Long Strike (Upside Wing)*: Bought **10** calls at the **3 400** strike (representing **3400**).
        *   *Deltas*: No specific Delta targets are spoken in this transcript, though the position is centered "right where the market is trading."
    *   **DTE (Days to Expiration)**: Expiring in **June** (the exact days are not specified, though monthly options are used).
    *   **Entry Trigger**: Not indicator-driven. The trade is initiated when Amazon is trading right at around **33 30** under a specific trading plan (details of why the trader enters are not covered in this transcript, though it is used to capture a range-bound consolidation).

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (The Winning Exit)**: If Amazon's stock price closes anywhere between **3265 and 33.95** (representing **3395**) on expiration day, the options decay and expire, allowing the trader to make money.
    *   **Execution Rule (Midpoint Limit Orders)**: To enter the butterfly, the trader must execute the position as a single complex order using a **limit order** set exactly at the **midpoint** of the bid and ask prices of each option. 
    *   **catastrophic Execution Error**: Fledgling options traders frequently make the blunder of executing spreads via **market orders**. Because market makers fill market orders by forcing you to pay the ask price on buys and accept the bid price on sells, this blunder incurs devastating slippage across all **40** options in the spread, completely destroying the trade's economics.

*   **The Stated Edge or Statistics**:
    *   **Midpoint Fills**: Because of split-difference bidding mechanics, a patient trader can get filled at the midpoint price—or very close to it—the majority of the time.
    *   **Multi-legged Capital Efficiency**: If filled at the midpoint, the total cost of the **10-contract Amazon butterfly** is just **4 200** (representing **\$4,200**), which is extremely capital-efficient for controlling **20** short and **20** long contracts.

*   **The Caveats the Presenter Gives**:
    *   **Catastrophic Slippage Danger**: Bid-ask spreads on high-priced stocks (like Amazon) are exceptionally wide. If you use a market order, you get "crushed" on all **40** options, inflating the trade cost to **seventy five hundred** dollars—which is **thirty three hundred** dollars (or **seventy eight** percent) more expensive than the limit order.
    *   **Narrow Profit Zone**: The cheaper the butterfly can be purchased, the wider your profitable range of outcomes. Paying too much for a butterfly due to sloppy market order execution narrows the profit zone to a dangerously thin range.

---

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video metadata | **11000** views |
| Options trading blunder number | General options education | blunder number **11** |
| Amazon butterfly short strike level | AMZN Call Butterfly (June expiration) | **33 30** (representing **3330**) |
| Short contracts sizing | AMZN Call Butterfly (June expiration) | sold **20** Amazon call options / **20** short calls |
| Distance of wings from short strike | AMZN Call Butterfly (June expiration) | **70** points in this example |
| Upside wing strike price | AMZN Call Butterfly (June expiration) | **3 400** (representing **3400**) |
| Downside wing strike price | AMZN Call Butterfly (June expiration) | **32.60** (representing **3260**) |
| Long contracts sizing (Downside wing) | AMZN Call Butterfly (June expiration) | bought **10** calls at 32.60 |
| Long contracts sizing (Upside wing) | AMZN Call Butterfly (June expiration) | bought **10** calls at 3 400 / **20** long calls |
| Promoted workshop option strategies | General options class | teaches **three** additional option strategies |
| Promoted workshop duration | General options class | **two-hour** free intensive workshop |
| Butterfly range of profitable outcomes | AMZN Call Butterfly (June expiration) | anywhere between **3265** and **33.95** (representing **3395**) |
| Total cost of 3400 calls (midpoint) | AMZN 3400 calls (10 contracts) | bought for **122.38** each / total cost is **122 380** |
| Option contract sizing multiplier | General options contract specs | represents **100** shares of Amazon |
| Total credit received from short calls (midpoint) | AMZN 3330 calls (20 contracts) | brought in **310 hundred six** (garbled/transcribed) / before sold those for **310 560** |
| Downside wing strike price (slip/garbled) | AMZN Call Butterfly (June expiration) | buying those **30 to 60** calls (garbled/transcribed for 3260) |
| Total cost of 3260 calls (midpoint) | AMZN 3260 calls (10 contracts) | cost of **192 380** |
| Total net cost of limit order spread | AMZN Call Butterfly (June expiration) | modest cost of **4 200** |
| Bid price of 3400 call | AMZN 3400 calls | bid for the 3400 call is **121.75** |
| Ask price of 3400 call | AMZN 3400 calls | ask is **123** |
| Midpoint price of 3400 call | AMZN 3400 calls | midpoint rounds to **122.38** |
| Midpoint price of 3330 call | AMZN 3330 calls | midpoint of the 3330 is **155 28** |
| Midpoint price of 3260 call | AMZN 3260 calls | midpoint of the 3260 is **192.38** |
| Total options contracts in spread | AMZN Call Butterfly (June expiration) | **40** options / **20** you bought and the **20** you sold |
| Ask price of 3400 calls paid (market order) | AMZN 3400 calls (10 contracts) | paid ask of **123** / total of **123 000** / increase of **620** dollars |
| Bid price of 3330 calls received (market order) | AMZN 3330 calls (20 contracts) | receive **1540** (representing **154.00**) / total of **308 800** / **1 760** less received |
| Ask price of 3260 calls paid (market order) | AMZN 3260 calls (10 contracts) | pay **193.30** / paid **193.3** / paid **192 380** (midpoint reference) / additional **920** more |
| Total cost of market order entry | AMZN Call Butterfly (June expiration) | total cost is **seventy five hundred** dollars |
| Added cost of market order over limit order | AMZN Call Butterfly (June expiration) | **thirty three hundred** dollars more |
| Percentage increase of market order cost | AMZN Call Butterfly (June expiration) | full **seventy eight** percent greater |

### [c2YKd2TT-2I] You Can Supercharge Your Options Trades With THIS technique (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **Chipotle Mexican Grill (CMG) stock options** [1].
    *   **Structure**: Bullish options strategy initially established by purchasing a long call option [2]. To supercharge the trade's odds of success and manage downside risk, a **put credit spread** is strategically added to the position [3].
    *   **Strikes/Deltas**:
        *   *Long Call Strike*: **1045** strike [2]. This strike is placed about **20 points** above the current stock price of **10.27** at entry [2].
        *   *Deltas*: No specific Delta selection parameters or targets are mentioned in this transcript.
    *   **DTE (Days to Expiration)**: Approximately **one month** (options expire on **July 10th**, exactly one month after entry) [2].
    *   **Entry Trigger**: Executed on **June 10th** when the Relative Strength Index (RSI), a momentum indicator, crosses down below **30** into oversold territory, signaling an imminent market bounce [1, 2, 4].

*   **The Management and Exit Rules**:
    *   **Initial Entry**: Buy the slightly out-of-the-money 1045 call option on June 10th for **40.30**, which requires a total cash outlay of **four thousand and thirty dollars** per contract [2].
    *   **Put Credit Spread Addition**: A put credit spread is executed alongside the long call to inject defensive profit capability into the trade [3].
    *   **Exit / Expiration Management**: Unlike standard long calls which fail if the underlying asset declines, the addition of the put credit spread allows the trade to remain resilient during market corrections [3]. If the stock drops to **one thousand** the next day, and continues falling down **to 950**, the combination still secures a **pretty nice profit in 12 days** [2, 3]. This allows the trader to profit from their bullish thesis even if the stock sells off from the initial entry [3].

*   **The Stated Edge or Statistics**:
    *   **Squeezing Profit on Negative Moves**: The put credit spread adds an indispensable layer of profitability that a standalone long call cannot provide [3]. It enables a bullish trade to be profitable even if the underlying market drops, giving options traders an exceptional margin of error [3].
    *   **Workshop Stated Probability**: Teaches three options strategies, including a high-probability strategy that features a statistical **80** percent probability of profit month in and month out [4, 5].

*   **The Caveats the Presenter Gives**:
    *   The provided passages of this video do not contain any explicit caveats, risks, margin requirements, or downside scenarios other than pointing out that a long call alone is structurally disadvantaged during market sell-offs [3].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity [6] | `[c2YKd2TT-2I]` video card metadata | **11000** views |
| RSI overbought boundary [1] | General RSI indicator setup | readings over **70** |
| RSI oversold boundary [1, 2, 4] | General RSI indicator setup | readings under **30** / dropped below **30** |
| Free workshop duration [4] | General options income workshop | **two-hour** free intensive workshop |
| Workshop strategies count [3, 4] | General options income workshop | teaches **three** of those strategies / **three** real world options strategies |
| Workshop strategy win rate [5] | High-probability options income strategy | statistical **80** probability of profit |
| Option contract multiplier [2, 7] | General equity options contract sizing | represents **100** shares / entitles the buyer to purchase **100** shares |
| Entry date [2] | CMG Long Call + Put Credit Spread | June **10th** |
| Expiration date [2] | CMG Long Call + Put Credit Spread | **july 10th** |
| Expiration duration [2] | CMG Long Call + Put Credit Spread | about **a month** / exactly **a month** |
| Long call strike [2] | CMG Long Call option | **1045** strike |
| Call strike distance above market [2] | CMG Long Call option | about **20** points above |
| Underlying stock price at entry [2] | CMG stock on June 10th | current cmg price of **10.27** (verbatim speaking slip/typo representing 1027) |
| Call option price [2] | CMG July 10th 1045 Call | priced at **40.30** |
| Long call total trade cash outlay [2] | CMG July 10th 1045 Call | **four thousand and thirty** dollars |
| Stock price on Day 2 [2] | CMG stock drop | dropped down to **one thousand** (representing 1000) |
| Stock price drop magnitude on Day 2 [2] | CMG stock drop | another **27** points below the initiation of the call purchases |
| Stock price at trade close [3] | CMG stock decline | drop to **950** (representing 950) |
| Trade holding period / profit timeline [3] | CMG Long Call + Put Credit Spread | **12** days |

### [SqKhVuOYNNQ] Weekly Options Strategies Can Yield Outstanding Returns (Especially When the Market is Volatile) (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **NDX (Nasdaq 100 Index) options** [1].
    *   **Structure**: **Iron Condor** options strategy (referred to as the "April condor" or "January condor") [1, 2].
    *   **Strikes/Deltas**: 
        *   *January Condor*: Set at strike prices located **250 points above the index price** and **300 points below the index price** [3].
        *   *April Condor*: The exact strike levels or Deltas are not explicitly named in this transcript, though the put contracts are described as being "way below the market" at expiration [3].
    *   **DTE (Days to Expiration)**: A short-term **four-day** trade ("starts and finishes in four days") [3, 4].
    *   **Entry Trigger**: Continuous high volatility and radical market moves occurring almost every day for **more than three months** during the **COVID-19 pandemic** [5, 6]. This massive uncertainty heavily inflates options premiums due to fear, creating highly favorable conditions for range-bound credit sellers [4, 6].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (The Winning Exit)**: The position is held to expiration on **May 1st** [1]. If the index closes within the range of the short strikes, **all four options** expire completely worthless with no settlement value [3]. 
    *   The trader simply pockets and keeps the entire initial cash flow credit collected at entry as their net profit, and the options die with no further obligations [3].
    *   *No other active management, adjustments, or defensive rolling rules are discussed in this transcript excerpt.*

*   **The Stated Edge or Statistics**:
    *   **Volatility Premium Pump-up**: High-volatility environments force the options market to price in much wider ranges of safety, allowing sellers to collect significantly larger premiums while lowering their actual risk on the trade [2-4].
    *   **The Volatility Advantage**: The April Condor trade yielded a spectacular **68 percent actual return** in just **four days** on the risk capital deployed [3, 4].
    *   **Low-Volatility Comparison**: In a quiet, "almost fearless" market (like in January), the exact same four-day trade layout only yielded a maximum return of **11 percent on risk** [3].
    *   **Workshop Baseline Probability**: Teaches options income strategies, including a high-probability strategy with a statistical **80 percent** (statistical 80) probability of profit month in and month out [2].

*   **The Caveats the Presenter Gives**:
    *   **Overnight Headline Risk**: Holding directional positions overnight is highly "nerve-wracking and dangerous" because unpredictable overnight headlines can instantly "destabilize the market and wreck your trade" [5]. This risk highlights the security of utilizing range-bound options strategies [5].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video card metadata | **11000** views [7] |
| Market high volatility duration | COVID-19 pandemic market environment | more than **three** months of continuous volatility [5] |
| COVID-19 pandemic identifier | Macro environment trigger | kovid **19** [6] |
| Day trader earnings acceleration | General day trading vs. options comparison | making in **one** month what normally takes a **full year** [6] |
| Promoted free workshop duration | General options seminar promotion | **two-hour** free intensive workshop [2] |
| Promoted workshop strategies count | General options seminar promotion | teaches **three** of those strategies [2] |
| Workshop strategy probability edge | High-probability options income strategy | statistical **80** probability of profit [2] |
| Options trade expiration date | April NDX Iron Condor | **may 1st** [1] |
| Tranche option contracts count | April NDX Iron Condor, expiring May 1st | **all four** options expired worthless [3] |
| April trade actual return | April NDX Iron Condor, 4 DTE | actual return of **68** / **68** return [3, 4] |
| January trade upper boundary | January NDX Iron Condor, 4 DTE | **250** points above the index price [3] |
| January trade lower boundary | January NDX Iron Condor, 4 DTE | **300** points below the index price [3] |
| Trade holding period | NDX Iron Condor (January and April versions) | **four** days / **four** day trade [3, 4] |
| January trade maximum profit | January NDX Iron Condor, 4 DTE | return of **11** of our risk [3] |

### [7ICrfxra46Y] Boost Your Dividends Through This Easy Options Technique (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **iShares 20-year Treasury Bond ETF (TLT)**, which acts as a proxy for the long-term United States Treasury bond market [1].
    *   **Structure**: **Covered Call** option strategy [2]. This is established by purchasing shares of stock or an ETF and simultaneously selling one call option for each 100 shares owned (selling 10 calls against 1,000 shares) [2].
    *   **Strikes/Deltas**: 
        *   The short call option is written at a strike price **slightly above** where the underlying asset is trading at entry (e.g., selling the 88 calls when TLT trades at 87.57, or 90 calls when TLT closed at 89.27) [2, 3].
        *   **The Cost Basis Floor Rule (July/August)**: If the underlying asset drops significantly below the initial purchase price (e.g., dropping to 85.35), the trader must adjust strike selection. Instead of selling the first call strike above the market (the 86 calls), the trader writes the **88 calls** (at or above their original acquisition price of 87.57) to prevent the shares from being assigned at a price that would lock in a realized capital loss [4].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in this transcript.
    *   **DTE (Days to Expiration)**: Approximately **one month** to expiration (e.g., entering the trade on January 2nd with options expiring 36 days later on February 7th) [1, 2].
    *   **Entry Trigger**: Executed during periods when the Federal Reserve is on a path to steadily reduce interest rates, which causes yields on bonds and money market funds to drop and prompts investors to seek superior income alternatives [5, 6]. The strategy is implemented on solid, long-term stocks or ETFs that have experienced steady sell-offs (such as TLT steadily selling off since September 2024 to close at 87.57 on January 2nd, 2025) to secure a lower share cost and capture rich premium due to market uncertainty [1].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (Hold to Expiration)**: If the stock closes below the call strike price at expiration (e.g., closing at 86.97 against the short 88 calls), the calls expire completely worthless with zero value [4, 7]. The trader simply pockets the initial credit premium and continues the campaign [2, 7].
    *   **Defensive Buybacks (Rolling Calls)**: If the stock rallies past the short strike at expiration (e.g., TLT closing at 90.01 against the short 90 calls, or 92.85 against the short 91 calls), the options are highly valuable to the owner [3, 8]. To avoid having the shares called away (assigned) at the strike price, the trader rolls the position [3]. This is done by buying back the short calls at market price (e.g., paying 13 cents / \$130 or \$187 / \$1,870 **⚠unverified**) and simultaneously writing the next month's covered calls at a higher strike price to collect a fresh credit (e.g. June 93 calls) [3, 8].
    *   **The Capital Loss Prevention Principle**: Never write covered calls at a strike price lower than the initial share acquisition cost basis (e.g., writing the 88 calls instead of the 86 calls when TLT drops to 85.35) so that if assigned, you do not lock in a realized loss on the underlying stock shares [4].

*   **The Stated Edge or Statistics**:
    *   **Yield Supercharging**: Covered call programs dramatically outperform passive dividend collection [9]. In this case study, the covered call campaign combined with dividends yielded **\$7,630** in total cash flow compared to only **\$2,230** from passively collecting dividends alone—more than tripling the cash return on the equity portfolio [9].
    *   **Effortless Return Boost**: The program delivers outstanding cash generation from large-cap, high-yield equities with very little additional effort compared to buy-and-hold approaches [9].

*   **The Caveats the Presenter Gives**:
    *   **Capped Upside**: If the stock rallies aggressively, your share gain is capped at the strike price [4].
    *   **Downside Risk**: Writing covered calls does not eliminate equity downside risk; if the stock collapses steadily, the capital loss on the underlying stock shares can outweigh the options credit and dividend income collected [4, 7].
    *   **Capital Loss Lock-in Risk**: If the stock collapses and you are forced to write calls below your original purchase price to grab premium, a sudden bounce can trigger assignment and lock in a realized loss [4].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | Video metadata | **11000** views |
| Baseline S&P 500 average dividend yield | S&P 500 Index benchmark | barely over **1%** |
| High-yield dividend stock benchmark | General high dividend stock/ETF yield | **three** or **4%** |
| Underlying definition | TLT bond maturity benchmark | **20**-year |
| Macro sell-off baseline timeline | TLT ETF macro trend | steadily since september of **2024** |
| Macro sell-off baseline date | TLT ETF trade entry day | **2025** january **2nd** |
| Underlying price at entry | TLT purchase price | closed at **8757** (representing \$87.57 **⚠unverified**) |
| Annualized dividend yield baseline | TLT ETF baseline yield | little bit above **4%** |
| Monthly dividend per share | TLT ETF monthly dividend estimate | neighborhood of **30** cents a share |
|Sizing of shares | TLT Covered Call, 2025 campaign | bought **1,000** shares |
|Sizing capital spent | TLT Covered Call, 2025 campaign | spent **\$87,570** (also referred to as `8757` price) |
| Call options expiration date | TLT short call, expiring month 1 | expiring about a month later on february **7th** |
| Call options strike price | TLT short call, expiring month 1 | **88** calls |
| Sizing of call options | TLT short call, expiring month 1 | sold **10** of them (representing **1,000** shares, **100** shares per option) |
| Option premium collected | TLT short call, expiring month 1 | sold for a price of **\$153** (transcribed as \$153) |
| Net cash flow month 1 (January) | TLT Covered Call scorecard | **\$570** (transcribed as `ownership is $570`) |
| Call options expiration date 2 | TLT short call, expiring month 2 | expiring on march **7th** |
| Call options strike price 2 | TLT short call, expiring month 2 | **90** calls (transcribed as `90 march 70th calls`) |
| Call option price 2 | TLT short call, expiring month 2 | trading for **110** (representing 1.10) |
| Initial credit cash collected | TLT short call, expiring month 2 | produce **\$1,100** of positive cash flow |
| Expiration day stock closing | TLT close on March 7th | closing at **901** (representing 90.01) |
| Call buyback cost | TLT short call buyback, March 7th | buy back for **13** cent price / deducting **\$130** |
| Sized dividend payout 2 | TLT monthly dividend, March 6th | dividend paid of **\$290** on march **6th** |
| Sized campaign total profit 2 | TLT Covered Call scorecard | positive cash flow on this options trade is now **\$1,830** |
| Call options strike price 3 | TLT short call, expiring month 3 | selling the **91** calls |
| Call option price 3 | TLT short call, expiring month 3 | premium of **a11** (transcribed as a11) |
| Initial credit cash collected 3 | TLT short call, expiring month 3 | positive cash flow of **\$1,110** |
| Expiration day date 3 | TLT expiration 3 | by april **4th** |
| Expiration day stock closing 3 | TLT close on April 4th | closing at **92.85** |
| Option price above strike | TLT close on April 4th | closed at **\$185** (transcribed as \$185) above strike |
| Call buyback cost 3 | TLT short call buyback, April 4th | pay **\$187** to close |
| Monthly dividend per share payout 3 | TLT monthly dividend, April 4th | **32** cent dividend paid on april **4th** |
| Sized campaign total profit 3 | TLT Covered Call scorecard | positive cash flow was **1410** |
| Call options strike price 4 | TLT short call, expiring month 4 | **93** calls |
| Call option price 4 | TLT short call, expiring month 4 | going for **181** (representing 1.81) |
| Initial credit cash collected 4 | TLT short call, expiring month 4 | collect **\$1810** |
| Post-May sell-off stock price | TLT close context | closed at **8535** |
| Call options strike price 5 | TLT short call, expiring month 5 | **88** june calls |
| Option price at expiration 5 | TLT short call, expiring month 5 | expired with **no value** |
| Credit cash collected 5 | TLT short call, expiring month 5 | **1730** of cash flow |
| Sized dividend payout 5 | TLT monthly dividend, June | **320** dividend |
| Sized campaign total profit 5 | TLT Covered Call scorecard | now up to **\$5,600** in total trade positive cash flow |
| July alternative strike | TLT Covered Call, July setup | selling the **86** calls |
| July alternative assignment price | TLT Covered Call, July setup | called away at a price of **86** |
| Original shares cost context | TLT original share cost | **8757** per share |
| July actual strike price | TLT Covered Call, July setup | sell the **88** calls |
| July option price | TLT Covered Call, July setup | sold for **43** cents |
| Initial credit cash collected 6 | TLT Covered Call, July setup | yielding us### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **iShares 20-year Treasury Bond ETF (TLT)**, which acts as a proxy for the long-term United States Treasury bond market [1].
    *   **Structure**: **Covered Call** option strategy [2]. This is established by purchasing shares of stock or an ETF and simultaneously selling one call option for each 100 shares owned (selling 10 calls against 1,000 shares) [2].
    *   **Strikes/Deltas**: 
        *   The short call option is written at a strike price **slightly above** where the underlying asset is trading at entry (e.g., selling the 88 calls when TLT trades at 87.57, or 90 calls when TLT closed at 89.27) [2, 3].
        *   **The Cost Basis Floor Rule**: If the underlying asset drops significantly below the initial purchase price (e.g., dropping to 85.35), the trader must adjust strike selection [4]. Instead of selling the first call strike below their purchase price (the 86 calls), the trader writes the **88 calls** (at or above their original acquisition price of 87.57) to prevent the shares from being assigned at a price that would lock in a realized capital loss [4].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in this transcript.
    *   **DTE (Days to Expiration)**: Approximately **one month** to expiration (e.g., entering the trade on January 2nd with options expiring 36 days later on February 7th) [1, 2].
    *   **Entry Trigger**: Executed during periods when the Federal Reserve is on a path to steadily reduce interest rates, which causes yields on bonds and money market funds to drop and prompts investors to seek superior income alternatives [5, 6]. The strategy is implemented on solid, long-term stocks or ETFs that have experienced steady sell-offs (such as TLT steadily selling off since September 2024 to close at 87.57 on January 2nd, 2025) to secure a lower share cost and capture rich premium due to market uncertainty [1].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (Hold to Expiration)**: If the stock closes below the call strike price at expiration (e.g., closing at 86.97 against the short 88 calls), the calls expire completely worthless with zero value [4, 7]. The trader simply pockets the initial credit premium and continues the campaign [2, 7].
    *   **Defensive Buybacks (Rolling Calls)**: If the stock rallies past the short strike at expiration (e.g., TLT closing at 90.01 against the short 90 calls, or 92.85 against the short 91 calls), the options are highly valuable to the owner [3, 8]. To avoid having the shares called away (assigned) at the strike price, the trader rolls the position [3]. This is done by buying back the short calls at market price (e.g., paying 13 cents / \$130 or \$187 / \$1,870 **⚠unverified**) and simultaneously writing the next month's covered calls at a higher strike price to collect a fresh credit (e.g., June 93 calls) [3, 8].
    *   **The Capital Loss Prevention Principle**: Never write covered calls at a strike price lower than the initial share acquisition cost basis (e.g., writing the 88 calls instead of the 86 calls when TLT drops to 85.35) so that if assigned, you do not lock in a realized loss on the underlying stock shares [4].

*   **The Stated Edge or Statistics**:
    *   **Yield Supercharging**: Covered call programs dramatically outperform passive dividend collection [9]. In this case study, the covered call campaign combined with dividends yielded **\$7,630** in total cash flow compared to only **\$2,230** from passively collecting dividends alone—more than tripling the cash return on the equity portfolio [9].
    *   **Effortless Return Boost**: The program delivers outstanding cash generation from large-cap, high-yield equities with very little additional effort compared to buy-and-hold approaches [9].

*   **The Caveats the Presenter Gives**:
    *   **Capped Upside**: If the stock rallies aggressively, your share gain is capped at the strike price [4].
    *   **Downside Risk**: Writing covered calls does not eliminate equity downside risk; if the stock collapses steadily, the capital loss on the underlying stock shares can outweigh the options credit and dividend income collected [4, 7].
    *   **Capital Loss Lock-in Risk**: If the stock collapses and you are forced to write calls below your original purchase price to grab premium, a sudden bounce can trigger assignment and lock in a realized loss [4].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[7ICrfxra46Y]` video card metadata | **11000** views |
| Baseline S&P 500 average dividend yield | S&P 500 Index benchmark | barely over **1%** |
| High-yield dividend stock benchmark | General high dividend stock/ETF yield | **three** or **4%** |
| Underlying definition | TLT bond maturity benchmark | **20**-year |
| Macro sell-off baseline timeline | TLT ETF macro trend | steadily since september of **2024** |
| Macro sell-off baseline date | TLT ETF trade entry day | **2025** january **2nd** |
| Underlying price at entry | TLT purchase price | closed at **8757** |
| Annualized dividend yield baseline | TLT ETF baseline yield | little bit above **4%** |
| Monthly dividend per share | TLT ETF monthly dividend estimate | neighborhood of **30** cents a share |
| Sizing of shares | TLT Covered Call, 2025 campaign | bought **1,000** shares |
| Sizing capital spent | TLT Covered Call, 2025 campaign | spent **\$87,570** |
| Call options expiration date | TLT short call, expiring month 1 | expiring about a month later on february **7th** |
| Call options strike price | TLT short call, expiring month 1 | **88** calls |
| Sizing of call options | TLT short call, expiring month 1 | sold **10** of them (representing **1,000** shares, **100** shares per option) |
| Option premium collected | TLT short call, expiring month 1 | sold for a price of **\$153** |
| Net cash flow month 1 (January) | TLT Covered Call scorecard | **\$570** |
| Call options expiration date 2 | TLT short call, expiring month 2 | expiring on march **7th** |
| Call options strike price 2 | TLT short call, expiring month 2 | **90** calls (transcribed as `90 march 70th calls`) |
| Call option price 2 | TLT short call, expiring month 2 | trading for **110** |
| Initial credit cash collected | TLT short call, expiring month 2 | produce **\$1,100** of positive cash flow |
| Expiration day stock closing | TLT close on March 7th | closing at **901** |
| Call buyback cost | TLT short call buyback, March 7th | buy back for **13** cent price / deducting **\$130** |
| Sized dividend payout 2 | TLT monthly dividend, March 6th | dividend paid of **\$290** on march **6th** |
| Sized campaign total profit 2 | TLT Covered Call scorecard | positive cash flow on this options trade is now **\$1,830** |
| Call options strike price 3 | TLT short call, expiring month 3 | selling the **91** calls |
| Call option price 3 | TLT short call, expiring month 3 | premium of **a11** |
| Initial credit cash collected 3 | TLT short call, expiring month 3 | positive cash flow of **\$1,110** |
| Expiration day date 3 | TLT expiration 3 | by april **4th** |
| Expiration day stock closing 3 | TLT close on April 4th | closing at **92.85** |
| Option price above strike | TLT close on April 4th | closed at **\$185** above strike |
| Call buyback cost 3 | TLT short call buyback, April 4th | pay **\$187** to close |
| Monthly dividend per share payout 3 | TLT monthly dividend, April 4th | **32** cent dividend paid on april **4th** |
| Sized campaign total profit 3 | TLT Covered Call scorecard | positive cash flow was **1410** |
| Call options strike price 4 | TLT short call, expiring month 4 | **93** calls |
| Call option price 4 | TLT short call, expiring month 4 | going for **181** |
| Initial credit cash collected 4 | TLT short call, expiring month 4 | collect **\$1810** |
| Post-May sell-off stock price | TLT close context | closed at **8535** |
| Call options strike price 5 | TLT short call, expiring month 5 | **88** june calls |
| Option price at expiration 5 | TLT short call, expiring month 5 | expired with **no value** |
| Credit cash collected 5 | TLT short call, expiring month 5 | **1730** of cash flow |
| Sized dividend payout 5 | TLT monthly dividend, June | **320** dividend |
| Sized campaign total profit 5 | TLT Covered Call scorecard | now up to **\$5,600** in total trade positive cash flow |
| July alternative strike | TLT Covered Call, July setup | selling the **86** calls |
| July alternative assignment price | TLT Covered Call, July setup | called away at a price of **86** |
| Original shares cost context | TLT original share cost | **8757** per share |
| July actual strike price | TLT Covered Call, July setup | sell the **88** calls |
| July option price | TLT Covered Call, July setupPART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **iShares 20-year Treasury Bond ETF (TLT)**, representing a proxy for the long-term United States Treasury bond market [1].
    *   **Structure**: **Covered Call** option strategy [2]. This is established by purchasing shares of stock or an ETF and simultaneously selling one call option for each 100 shares owned (selling 10 calls against 1,000 shares) [2].
    *   **Strikes/Deltas**: 
        *   The short call option is written at a strike price **slightly above** where the underlying asset is trading at entry (e.g., selling the 88 calls when TLT trades at 87.57, or 90 calls when TLT closed at 89.27) [2, 3].
        *   **The Cost Basis Floor Rule**: If the underlying asset drops significantly below the initial purchase price (e.g., dropping to 85.35), the trader must adjust strike selection [4]. Instead of selling the first call strike below their purchase price (the 86 calls), the trader writes the **88 calls** (at or above their original acquisition price of 87.57) to prevent the shares from being assigned at a price that would lock in a realized capital loss [4].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in this transcript.
    *   **DTE (Days to Expiration)**: Approximately **one month** to expiration (e.g., entering the trade on January 2nd with options expiring 36 days later on February 7th) [1, 2].
    *   **Entry Trigger**: Executed during periods when the Federal Reserve is on a path to steadily reduce interest rates, which causes yields on bonds and money market funds to drop and prompts investors to seek superior income alternatives [5, 6]. The strategy is implemented on solid, long-term stocks or ETFs that have experienced steady sell-offs (such as TLT steadily selling off since September 2024 to close at 87.57 on January 2nd, 2025) to secure a lower share cost and capture rich premium due to market uncertainty [1].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (Hold to Expiration)**: If the stock closes below the call strike price at expiration (e.g., closing at 86.97 against the short 88 calls), the calls expire completely worthless with zero value [4, 7]. The trader simply pockets the initial credit premium and continues the campaign [2, 7].
    *   **Defensive Buybacks (Rolling Calls)**: If the stock rallies past the short strike at expiration (e.g., TLT closing at 90.01 against the short 90 calls, or 92.85 against the short 91 calls), the options are highly valuable to the owner [3, 8]. To avoid having the shares called away (assigned) at the strike price, the trader rolls the position [3]. This is done by buying back the short calls at market price (e.g., paying 13 cents / \$130 or \$187 / \$1,870 **⚠unverified**) and simultaneously writing the next month's covered calls at a higher strike price to collect a fresh credit (e.g., June 93 calls) [3, 8].
    *   **The Capital Loss Prevention Principle**: Never write covered calls at a strike price lower than the initial share acquisition cost basis (e.g., writing the 88 calls instead of the 86 calls when TLT drops to 85.35) so that if assigned, you do not lock in a realized loss on the underlying stock shares [4].

*   **The Stated Edge or Statistics**:
    *   **Yield Supercharging**: Covered call programs dramatically outperform passive dividend collection [9]. In this case study, the covered call campaign combined with dividends yielded **\$7,630** in total cash flow compared to only **\$2,230** from passively collecting dividends alone—more than tripling the cash return on the equity portfolio [9].
    *   **Effortless Return Boost**: The program delivers outstanding cash generation from large-cap, high-yield equities with very little additional effort compared to buy-and-hold approaches [9].

*   **The Caveats the Presenter Gives**:
    *   **Capped Upside**: If the stock rallies aggressively, your share gain is capped at the strike price [4].
    *   **Downside Risk**: Writing covered calls does not eliminate equity downside risk; if the stock collapses steadily, the capital loss on the underlying stock shares can outweigh the options credit and dividend income collected [4, 7].
    *   **Capital Loss Lock-in Risk**: If the stock collapses and you are forced to write calls below your original purchase price to grab premium, a sudden bounce can trigger assignment and lock in a realized loss [4].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[7ICrfxra46Y]` video card metadata | **11000** views [10] |
| Baseline S&P 500 average dividend yield | S&P 500 Index benchmark | barely over **1%** [5] |
| High-yield dividend stock benchmark | General high dividend stock/ETF yield | **three** or **4%** [6] |
| Underlying definition | TLT bond maturity benchmark | **20**-year [1] |
| Macro sell-off baseline timeline | TLT ETF macro trend | steadily since september of **2024** [1] |
| Macro sell-off baseline date | TLT ETF trade entry day | **2025** january **2nd** [1] |
| Underlying price at entry | TLT purchase price | closed at **8757** [1] |
| Annualized dividend yield baseline | TLT ETF baseline yield | little bit above **4%** [1] |
| Monthly dividend per share | TLT ETF monthly dividend estimate | neighborhood of **30** cents a share [1] |
| Sizing of shares | TLT Covered Call, 2025 campaign | bought **1,000** shares [1] |
| Sizing capital spent | TLT Covered Call, 2025 campaign | spent **\$87,570** [2] |
| Call options expiration date | TLT short call, expiring month 1 | expiring about a month later on february **7th** [2] |
| Call options strike price | TLT short call, expiring month 1 | **88** calls [2] |
| Sizing of call options | TLT short call, expiring month 1 | sold **10** of them [2] |
| Option contract sizing multiplier | General options contract multiplier | represents **100** shares [2] |
| Option premium collected | TLT short call, expiring month 1 | sold for a price of **\$153** [2] |
| Net cash flow month 1 (January) | TLT Covered Call scorecard | **\$570** [3] |
| Call options expiration date 2 | TLT short call, expiring month 2 | expiring on march **7th** [3] |
| March entry closing price | TLT close context | closed at **8927** [3] |
| Call options strike price 2 | TLT short call, expiring month 2 | **90** march 70th calls (verbatim typo for 7th) [3] |
| Call option price 2 | TLT short call, expiring month 2 | trading for **110** [3] |
| Initial credit cash collected | TLT short call, expiring month 2 | produce **\$1,100** of positive cash flow [3] |
| Expiration day stock closing | TLT close on March 7th | closing at **901** [3] |
| Call buyback price | TLT short call buyback, March 7th | buy back for **13** cent price [3] |
| Sized dividend payout 2 | TLT monthly dividend, March 6th | dividend paid of **\$290** on march **6th** [3] |
| Call buyback total | TLT short call buyback, March 7th | deducting **\$130** [3] |
| Sized campaign total profit 2 | TLT Covered Call scorecard | positive cash flow on this options trade is now **\$1,830** [3] |
| Call options strike price 3 | TLT short call, expiring month 3 | selling the **91** calls [8] |
| Call option price 3 | TLT short call, expiring month 3 | premium of **a11** (verbatim) [8] |
| Initial credit cash collected 3 | TLT short call, expiring month 3 | positive cash flow of **\$1,110** [8] |
| Expiration day date 3 | TLT expiration 3 | by april **4th** [8] |
| Expiration day stock closing 3 | TLT close on April 4th | closing at **92.85** [8] |
| Option price above strike | TLT close on April 4th | closed at **\$185** (verbatim) above strike [8] |
| Call buyback cost 3 | TLT short call buyback, April 4th | pay **\$187** (verbatim) to close [8] |
| Monthly dividend per share payout 3 | TLT monthly dividend, April 4th | **32** cent dividend paid on april **4th** [8] |
| Sized campaign total profit 3 | TLT Covered Call scorecard | positive cash flow was **1410** [8] |
| Call options strike price 4 | TLT short call, expiring month 4 | **93** calls [8] |
| Call option price 4 | TLT short call, expiring month 4 | going for **181** [8] |
| Initial credit cash collected 4 | TLT short call, expiring month 4 | collect **\$1810** [8] |
| Post-May sell-off stock price | TLT close context | closed at **8535** [4] |
| Call options strike price 5 | TLT short call, expiring month 5 | **88** june calls [4] |
| Option price at expiration 5 | TLT short call, expiring month 5 | expired with **no value** [4] |
| Credit cash collected 5 | TLT short call, expiring month 5 | **1730** of cash flow [4] |
| Sized dividend payout 5 | TLT monthly dividend, June | **320** dividend [4] |
| Sized campaign total profit 5 | TLT Covered Call scorecard | now up to **\$PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **iShares 20-year Treasury Bond ETF (TLT)**, which acts as a proxy for the long-term United States Treasury bond market [1].
    *   **Structure**: **Covered Call** option strategy [2]. This is established by purchasing shares of stock or an ETF and simultaneously selling one call option for each 100 shares owned (selling 10 calls against 1,000 shares) [2].
    *   **Strikes/Deltas**: 
        *   The short call option is written at a strike price **slightly above** where the underlying asset is trading at entry (e.g., selling the 88 calls when TLT trades at 87.57, or 90 calls when TLT closed at 89.27) [2, 3].
        *   **The Cost Basis Floor Rule**: If the underlying asset drops significantly below the initial purchase price (e.g., dropping to 85.35), the trader must adjust strike selection [4]. Instead of selling the first call strike below their purchase price (the 86 calls), the trader writes the **88 calls** (at or above their original acquisition price of 87.57) to prevent the shares from being assigned at a price that would lock in a realized capital loss [4].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in this transcript.
    *   **DTE (Days to Expiration)**: Approximately **one month** to expiration (e.g., entering the trade on January 2nd with options expiring 36 days later on February 7th) [1, 2].
    *   **Entry Trigger**: Executed during periods when the Federal Reserve is on a path to steadily reduce interest rates, which causes yields on bonds and money market funds to drop and prompts investors to seek superior income alternatives [5, 6]. The strategy is implemented on solid, long-term stocks or ETFs that have experienced steady sell-offs (such as TLT steadily selling off since September 2024 to close at 87.57 on January 2nd, 2025) to secure a lower share cost and capture rich premium due to market uncertainty [1].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (Hold to Expiration)**: If the stock closes below the call strike price at expiration (e.g., closing at 86.97 against the short 88 calls), the calls expire completely worthless with zero value [4, 7]. The trader simply pockets the initial credit premium and continues the campaign [2, 7].
    *   **Defensive Buybacks (Rolling Calls)**: If the stock rallies past the short strike at expiration (e.g., TLT closing at 90.01 against the short 90 calls, or 92.85 against the short 91 calls), the options are highly valuable to the owner [3, 8]. To avoid having the shares called away (assigned) at the strike price, the trader rolls the position [3]. This is done by buying back the short calls at market price (e.g., paying 13 cents / $130 or $187 / $1,870 **⚠unverified**) and simultaneously writing the next month's covered calls at a higher strike price to collect a fresh credit (e.g., June 93 calls) [3, 8].
    *   **The Capital Loss Prevention Principle**: Never write covered calls at a strike price lower than the initial share acquisition cost basis (e.g., writing the 88 calls instead of the 86 calls when TLT drops to 85.35) so that if assigned, you do not lock in a realized loss on the underlying stock shares [4].

*   **The Stated Edge or Statistics**:
    *   **Yield Supercharging**: Covered call programs dramatically outperform passive dividend collection [9]. In this case study, the covered call campaign combined with dividends yielded **$7,630** in total cash flow compared to only **$2,230** from passively collecting dividends alone—more than tripling the cash return on the equity portfolio [9].
    *   **Effortless Return Boost**: The program delivers outstanding cash generation from large-cap, high-yield equities with very little additional effort compared to buy-and-hold approaches [9].

*   **The Caveats the Presenter Gives**:
    *   **Capped Upside**: If the stock rallies aggressively, your share gain is capped at the strike price [4].
    *   **Downside Risk**: Writing covered calls does not eliminate equity downside risk; if the stock collapses steadily, the capital loss on the underlying stock shares can outweigh the options credit and dividend income collected [4, 7].
    *   **Capital Loss Lock-in Risk**: If the stock collapses and you are forced to write calls below your original purchase price to grab premium, a sudden bounce can trigger assignment and lock in a realized loss [4].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Popularity of the video | `[7ICrfxra46Y]` video card statistics | **11000** views |
| Benchmark S&P index yield | Average market returns comparison | barely over **1%** |
| Alternate fixed income yield | CD investments | **three** or **4%** |
| Treasury duration tracking | TLT ETF structure benchmark | **20**-year |
| Macro sell-off onset timeline | TLT ETF chart trend | steadily since september of **2024** |
| Macro entry target date | TLT share purchase date | **2025** january **2nd** |
| Share cost on entry date | TLT share purchase price | closed at **8757** |
| Yield on entry date | TLT annualized dividend | little bit above **4%** |
| Projected monthly payout | TLT monthly dividend per share | neighborhood of **30** cents a share |
| Initial share campaign size | TLT Covered Call stock purchase | bought **1,000** shares |
| Total purchase capital spent | TLT Covered Call stock purchase | spending **\$87,570** |
| Campaign month 1 expiration | TLT Covered Call month 1 | expiring about a month later on february **7th** |
| Campaign month 1 call strikes | TLT Covered Call month 1 | **88** calls |
| Sizing of options contracts | TLT Covered Call month 1 | sold **10** of them |
| Contract multiplier rule | General stock options specs | represents rights related to **100** shares |
| Price collected per call contract | TLT Covered Call month 1 | sold for that price of **\$153** |
| Campaign net profit after month 1 | TLT Covered Call scorecard | ownership is **\$570** |
| Campaign month 2 expiration | TLT Covered Call month 2 | march **7th** |
| March entry share price | TLT Covered Call month 2 | closed at **8927** |
| Campaign month 2 call strikes | TLT Covered Call month 2 | **90** march 70th calls (verbatim typo) |
| Option contract price | TLT Covered Call month 2 | trading for **110** |
| Option credit collected | TLT Covered Call month 2 | positive cash flow of **\$1,100** |
| Underlying close price at expiration 2 | TLT close on March 7th | closing at **901** |
| Call option contract buyback price | TLT Covered Call roll, March 7th | buy back for that **13** cent price |
| Sized dividend payout 2 | TLT monthly dividend, March 6th | dividend paid of **\$290** on march **6th** |
| Sized buyback total cost | TLT Covered Call roll, March 7th | after deducting **\$130** |
| Scorecard total profit 2 | TLT Covered Call scorecard | positive cash flow on this options trade is now **\$1,830** |
| Campaign month 3 call strikes | TLT Covered Call month 3 | selling the **91** calls |
| Option price 3 | TLT Covered Call month 3 | premium of **a11** (verbatim) |
| Option credit collected 3 | TLT Covered Call month 3 | positive cash flow of **\$1,110** |
| Expiration date 3 | TLT Covered Call month 3 | by april **4th** |
| Expiration price 3 | TLT close on April 4th | closing at **92.85** |
| Price above strike | TLT close on April 4th | closed at a **\$185** (verbatim) above strike |
| Call buyback cost 3 | TLT short call buyback, April 4th | pay **\$187** (verbatim) to close |
| Sized dividend payout 3 | TLT monthly dividend, April 4th | **32** cent dividend paid on april **4th** |
| Scorecard total profit 3 | TLT Covered Call scorecard | positive cash flow was **1410** |
| Campaign month 4 call strikes | TLT Covered Call month 4 | **93** calls |
| Option price 4 | TLT Covered Call month 4 | going for **181** |
| Option credit collected 4 | TLT Covered Call month 4 | collect **\$1810** |
| Post-May sell-off price context | TLT close context | closed at **8535** |
| Campaign month 5 call strikes | TLT Covered Call month 5 | **88** june calls |
| Credit cash collected 5 | TLT Covered Call month 5 | **1730** of cash flow |
| Sized dividend payout 5 | TLT monthly dividend, June | **320** dividend |
| Scorecard total profit 5 | TLT Covered Call scorecard | now up to **\$5,600** in total trade positive cash flow |
| July alternative strike | TLT Covered Call, July setup | selling the **86** calls |
| Original purchase price basis | TLT original cost | **8757** per share |
| July actual strike price | TLT Covered Call, July setup | sell the **88** calls |
| July actual option price | TLT Covered Call, July setup | sold for **43** cents |
| Initial credit cash collected 6 | TLT Covered Call, July setup | yielding us **\$430** in cash flow |
| July close price | TLT close on expiration 6 | closing at **86.97** |
| Scorecard total profit 6 | TLT Covered Call scorecard | total is now up to **6360** |
| August actual strike price | TLT Covered Call### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: **iShares 20-year Treasury Bond ETF (TLT)**, which tracks the long-term United States Treasury bond market [1].
    *   **Structure**: **Covered Call** option strategy [2]. This is constructed by buying shares of a high-yield asset and simultaneously selling one call option for every 100 shares owned (selling 10 calls against 1,000 shares) [2].
    *   **Strikes/Deltas**:
        *   *Standard Strike Selection*: Call options are written at a strike price **slightly above** the current trading price of the shares (e.g., selling 88 calls when TLT trades at 87.57, or 90 calls when TLT closed at 89.27) [2, 3].
        *   *The Cost Basis Floor Rule*: If the underlying asset drops significantly (e.g., dropping to 85.35), the trader must adjust strike selection [4]. Instead of writing a call below their original purchase price (the 86 calls), they must sell at the **88 strike** (at or above their original acquisition price of 87.57) [4]. This prevents the shares from being assigned at a price that would lock in a realized capital loss [4].
        *   *Deltas*: Specific Delta selection metrics or targets are not spoken in this transcript.
    *   **DTE (Days to Expiration)**: Approximately **one month** (e.g., entering on January 2nd with options expiring 36 days later on February 7th) [1, 2].
    *   **Entry Trigger**: Triggered when the Federal Reserve is on a path to steadily reduce interest rates, which lowers yields on bonds and money market funds and prompts investors to seek superior income alternatives [5, 6]. The strategy is implemented on solid, long-term stocks or ETFs that have experienced steady sell-offs (such as TLT steadily selling off since September 2024 to close at 87.57 on January 2nd, 2025) to capture rich premium fueled by market uncertainty [1].

*   **The Management and Exit Rules**:
    *   **Worthless Expiration (Hold to Expiration)**: If the stock closes below the call strike price at expiration (e.g., closing at 86.97 against the short 88 calls), the calls expire completely worthless [4, 7]. The trader simply pockets the initial credit premium and continues the campaign [2, 7].
    *   **Defensive Buybacks (Rolling Calls)**: If the stock rallies past the short strike at expiration (e.g., TLT closing at 90.01 against the short 90 calls, or 92.85 against the short 91 calls), the options are highly valuable to the owner [3, 8]. To avoid having the shares called away (assigned) at the strike price, the trader rolls the position [3]. This is done by buying back the short calls at market price (e.g., paying 13 cents / $130 or $187 / $1,870 **⚠unverified**) and simultaneously writing the next month's covered calls at a higher strike price to collect a fresh credit (e.g., June 93 calls) [3, 8].
    *   **The Capital Loss Prevention Principle**: Never write covered calls at a strike price lower than the initial share acquisition cost basis (e.g., writing the 88 calls instead of the 86 calls when TLT drops to 85.35) so that if assigned, you do not lock in a realized loss on the underlying stock shares [4].

*   **The Stated Edge or Statistics**:
    *   **Yield Supercharging**: Covered call programs dramatically outperform passive dividend collection [9]. In this case study, the covered call campaign combined with dividends yielded **$7,630** in total cash flow compared to only **$2,230** from passively collecting dividends alone—more than tripling the cash return on the equity portfolio [9].
    *   **Effortless Return Boost**: The program delivers outstanding cash generation from large-cap, high-yield equities with very little additional effort compared to buy-and-hold approaches [9].

*   **The Caveats the Presenter Gives**:
    *   **Capped Upside**: If the stock rallies aggressively, your share gain is capped at the strike price [4].
    *   **Downside Risk**: Writing covered calls does not eliminate equity downside risk; if the stock collapses steadily, the capital loss on the underlying stock shares can outweigh the options credit and dividend income collected [4, 7].
    *   **Capital Loss Lock-in Risk**: If the stock collapses and you are forced to write calls below your original purchase price to grab premium, a sudden bounce can trigger assignment and lock in a realized loss [4].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Popularity of the video | `[7ICrfxra46Y]` video card statistics | **11000** views |
| Benchmark S&P index yield | Average market returns comparison | barely over **1%** |
| Alternate fixed income yield | CD investments | **three** or **4%** |
| Treasury duration tracking | TLT ETF structure benchmark | **20**-year |
| Macro sell-off onset timeline | TLT ETF chart trend | steadily since september of **2024** |
| Macro entry target date | TLT share purchase date | **2025** january **2nd** |
| Share cost on entry date | TLT share purchase price | closed at **8757** |
| Yield on entry date | TLT annualized dividend | little bit above **4%** |
| Projected monthly payout | TLT monthly dividend per share | neighborhood of **30** cents a share |
| Initial share campaign size | TLT Covered Call stock purchase | bought **1,000** shares |
| Total purchase capital spent | TLT Covered Call stock purchase | spending **\$87,570** |
| Campaign month 1 expiration | TLT Covered Call month 1 | expiring about a month later on february **7th** |
| Campaign month 1 call strikes | TLT Covered Call month 1 | **88** calls |
| Sizing of options contracts | TLT Covered Call month 1 | sold **10** of them |
| Contract multiplier rule | General stock options specs | represents rights related to **100** shares |
| Price collected per call contract | TLT Covered Call month 1 | sold for that price of **\$153** |
| Campaign net profit after month 1 | TLT Covered Call scorecard | ownership is **\$570** |
| Campaign month 2 expiration | TLT Covered Call month 2 | march **7th** |
| March entry share price | TLT Covered Call month 2 | closed at **8927** |
| Campaign month 2 call strikes | TLT Covered Call month 2 | **90** march 70th calls (verbatim typo) |
| Option contract price | TLT Covered Call month 2 | trading for **110** |
| Option credit collected | TLT Covered Call month 2 | positive cash flow of **\$1,100** |
| Underlying close price at expiration 2 | TLT close on March 7th | closing at **901** |
| Call option contract buyback price | TLT Covered Call roll, March 7th | buy back for that **13** cent price |
| Sized dividend payout 2 | TLT monthly dividend, March 6th | dividend paid of **\$290** on march **6th** |
| Sized buyback total cost | TLT Covered Call roll, March 7th | after deducting **\$130** |
| Scorecard total profit 2 | TLT Covered Call scorecard | positive cash flow on this options trade is now **\$1,830** |
| Campaign month 3 call strikes | TLT Covered Call month 3 | selling the **91** calls |
| Option price 3 | TLT Covered Call month 3 | premium of **a11** (verbatim) |
| Option credit collected 3 | TLT Covered Call month 3 | positive cash flow of **\$1,110** |
| Expiration date 3 | TLT Covered Call month 3 | by april **4th** |
| Expiration price 3 | TLT close on April 4th | closing at **92.85** |
| Price above strike | TLT close on April 4th | closed at a **\$185** (verbatim) above strike |
| Call buyback cost 3 | TLT short call buyback, April 4th | pay **\$187** (verbatim) to close |
| Sized dividend payout 3 | TLT monthly dividend, April 4th | **32** cent dividend paid on april **4th** |
| Scorecard total profit 3 | TLT Covered Call scorecard | positive cash flow was **1410** |
| Campaign month 4 call strikes | TLT Covered Call month 4 | **93** calls |
| Option price 4 | TLT Covered Call month 4 | going for **181** |
| Option credit collected 4 | TLT Covered Call month 4 | collect **\$1810** |
| Post-May sell-off price context | TLT close context | closed at **8535** |
| Campaign month 5 call strikes | TLT Covered Call month 5 | **88** june calls |
| Credit cash collected 5 | TLT Covered Call month 5 | **1730** of cash flow |
| Sized dividend payout 5 | TLT monthly dividend, June | **320** dividend |
| Scorecard total profit 5 | TLT Covered Call scorecard | now up to **\$5,600** in total trade positive cash flow |
| July alternative strike | TLT Covered Call, July setup | selling the **86** calls |
| Original purchase price basis | TLT original cost | **8757** per share |
| July actual strike price | TLT Covered Call, July setup | sell the **88** calls |
| July actual option price | TLT Covered Call, July setup | sold for **43** cents |
| Initial credit cash collected 6 | TLT Covered Call, July setup | yielding us **\$430** in cash flow |
| July close price | TLT close on expiration 6 | closing at **86.97** |
| July scorecard total cash flow | TLT Covered Call scorecard | total is now up to **6360** |
| August actual

### [y_AW3Ahm954] How to Be Wrong and Still Make Money (Options for Beginners) (11,000 views)

### PART A — HANDBOOK CHAPTER CONTENT

*   **The Setup**:
    *   **Instrument**: Tesla (TSLA) common stock options [1].
    *   **Structure**: Iron Condor options strategy [2, 3].
    *   **Strikes/Deltas**: 
        *   *Initial Call Spreads*: Short calls at the **205** strike price and protective long calls at the **215** strike price [2].
        *   *Initial Put Spreads*: Short puts at the **170** strike price and protective long puts at the **160** strike price [3].
        *   *Deltas*: No specific Delta selection parameters or targets are spoken in the transcript.
    *   **DTE (Days to Expiration)**: Not explicitly spoken in the transcript.
    *   **Entry Trigger**: Positioned as a bearish play on a highly active stock (such as Tesla) during a period of volatility and weakness (such as investor concerns that Elon Musk was spending too much time on his Twitter acquisition and had lost focus on Tesla, causing the stock to sell off) [1].

*   **The Management and Exit Rules**:
    *   **Defensive Adjustment (The Call Condor Roll)**: If the stock rallies aggressively against the directional bearish thesis (such as Tesla stock rallying "further up over 200" [2]), the trader does not accept a maximum loss. Instead, they execute a defensive **call Condor roll** [2].
    *   **Roll Action**: The trader buys back the short **205** calls, sells off the long **215** calls, and rolls them up so that the new short calls are located at **220** and the protective long calls are located at **2 30** (both well above the market) [2].
    *   **Worthless Expiration (Winning Exit)**: If the stock consolidates and remains within the adjusted range at expiration (such as closing above the puts and below the adjusted short call strike, with the stock trading over **200**):
        *   All options on the call side (220/230) and the put side (170/160) expire completely worthless with zero value [3].
        *   The trader simply pockets the remaining cash credit of **three thousand seven hundred eighty dollars** (\$3,780) kept after the Condor roll as pure profit [3].

*   **The Stated Edge or Statistics**:
    *   **Dynamically Repairable Trades**: Options have a unique trait where trades can be modified or repaired in the midst of a campaign (such as the call Condor roll) if the initial thesis goes wrong, saving the position from a loss [3].
    *   **Win When Wrong**: Unlike stock trading, this options strategy allows a trader to be completely wrong about their directional thesis (expecting a sell-off but experiencing a massive rally instead) and still walk away with a highly profitable trade [3, 4].

*   **The Caveats the Presenter Gives**:
    *   **catastrophic Capital/Margin Risk**: The initial position carries a significant worst-case risk profile that requires a substantial capital buffer. The broker requires **nineteen thousand seven hundred forty dollars** in capital to execute the initial trade, which also represents the absolute worst-case scenario on the trade [2].

***

### PART B — CONCRETE NUMBERS SPOKEN

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| Video popularity statistics | `[y_AW3Ahm954]` video metadata | **11000** views [5] |
| Broker required capital / worst-case risk | Tesla Iron Condor (initial entry) | require **nineteen thousand seven hundred forty dollars** in capital / worst case scenario [2] |
| Underlying rally threshold | Tesla stock post-entry rally | rallied further up over **200** [2] |
| Initial short call strike price | Tesla Iron Condor (initial entry) | short calls at **205** [2] |
| Initial long protective call strike price | Tesla Iron Condor (initial entry) | long calls at **2 15** [2] |
| Adjusted short call strike price | Tesla Iron Condor (adjusted) | short calls at **220** [2] |
| Adjusted long protective call strike price | Tesla Iron Condor (adjusted) | long calls at **2 30** [2] |
| Put side short put strike price | Tesla Iron Condor (put side) | short puts at **170** [3] |
| Put side long protective put strike price | Tesla Iron Condor (put side) | long puts at **160** [3] |
| Expiration stock trading boundary | Tesla stock price at expiration | trading over **200** [3] |
| Final campaign net profit | Tesla adjusted Iron Condor | profit of **three thousand seven hundred eighty dollars** [3] |

## LEDGER OF DISTILLED VIDEOS

| id | title | views | chapters contributed to |
|---|---|---|---|
| MmryR1iu9dA | Options Trading Tips: Ten Things I Wish I Knew Before I Started Trading Options | 1,100,000 | Trading principles & risk management; The edge of selling options; Non-directional income strategies; Real numbers |
| hsPmj_6nl5E | Top 3 Options Trading Strategies for Small Accounts | 879,000 | Small-account strategies; Non-directional income strategies; Real numbers |
| U8gFC00kZ58 | How to Trade Covered Calls Properly (The 3 keys to Uncommon Profits) | 792,000 | Covered calls; Real numbers |
| w_BjFmbwbYA | The Only Options Trading Course a Beginner Will Ever Need (The Basics from A to Z) | 782,000 | Options basics & pricing; The edge of selling options & credit spreads; Covered calls; Non-directional income strategies; Getting started; Real numbers |
| mKQq33Rtdfo | The Psychology of Hedge Fund Traders (Insights from Elite Trading Psychologist) | 604,000 | Trader psychology & performance; Real numbers |
| 4d6qj5vtrBQ | Small Account Options Income Strategy (Easy) | 567,000 | Cash-secured puts & the wheel (low-capital wheel substitute); Weekly campaigns; Real numbers |
| 7a0BRIAufBA | You can TRIPLE your income from covered calls (simple tweak) | 512,000 | Covered calls (XOM campaign + synthetic); Real numbers |
| Qj8_3eybnaE | Is it Easy to Make Weekly Income Through Options Trading? (the answer may surprise you) | 471,000 | Weekly & monthly credit-spread income campaigns (broken-wing butterfly); Real numbers |
| UG4f752OXq8 | The Top 3 0 DTE Options Trading Strategies | 467,000 | 0-DTE strategies; Calendar spreads & overnight trades; Real numbers |
| Dl0O3z_5hB0 | Weekly Options Trading Earns Him $2,500 Every Week (but he's missing something huge) | 421,000 | Weekly campaigns (tail-risk math); Developing a strategy; Real numbers |
| nvJ_43579z8 | You'll Fail With Options Trading Until You Understand This ONE Thing | 359,000 | The edge of selling options (call-buying failure experiment); Real numbers |
| CP_euDwExN0 | The 5 Deadly Covered Call MISTAKES (which you may be making without knowing) | 322,000 | Covered calls (five mistakes); Real numbers |
| -h1mAx67OxA | If I wanted to make $1,000 a week trading options, this is exactly what I'd do | 305,000 | 0-DTE strategies (90-min iron butterfly); Developing a strategy (5 steps); Real numbers |
| i5JOd15b_w0 | The $200 Overnight Options Strategy for Small Accounts | 286,000 | Calendar spreads & overnight trades; Real numbers |
| TOc1XyCu83I | Top 3 Options Trading Strategies for Monthly Income | 271,000 | Cash-secured puts & the wheel; Covered calls; Real numbers |
| XQ9OSsOra5s | Covered Calls for Income: How To Effectively Generate Consistent Monthly Income | 239,000 | Covered calls (portfolio program); Real numbers |
| CeEksKNSGMQ | Top 3 Technical Analysis Indicators For 0DTE Options | 233,000 | Market internals & technical filters; Real numbers |
| tOMQNDXnczY | Are you bad at predicting market direction? Do THIS (With Options) | 211,000 | The edge of selling options; Non-directional income (index-option rationale, channel condor); Real numbers |
| 6VPPI-MNUDM | Credit Spread Options Strategies Explained (Top 3 Benefits) | 208,000 | The edge of selling options & credit spreads (three benefits); Real numbers |
| c49FJM6UDvo | 0DTE options trading strategy (Easy Fix for Losing Trades) | 207,000 | 0-DTE strategies (butterfly roll); Real numbers |
| Wpl3VI2FTio | The Secret to Turbocharging Your Covered Call Options Trades | 203,000 | Covered calls (SPY synthetic); Real numbers |
| WYya6HGDYYg | An Options Strategy That Can Return 100% Overnight | 183,000 | Earnings trades (post-earnings iron butterfly); Real numbers |
| RmtEzjn4Vh0 | Avoid This Deadly Covered Call Mistake (Guaranteed Loss) | 179,000 | Covered calls (NVDA basis rule); Real numbers |
| IkGV8x5uz_A | You Can Try This Surprisingly Simple Options Trading Strategy For Monthly Income | 179,000 | Earnings trades (pre-earnings straddle); Real numbers |
| Z4a5wkLfqlU | Simple 3-Indicator Setup for ODTE Options | 178,000 | Market internals & technical filters (momentum setup); Real numbers |
| xQfp8_5VsRU | How to Sell Put Credit Spreads for Weekly Passive Income | 170,000 | Weekly & monthly credit-spread income campaigns; Real numbers |
| xidgg27-yWU | How to Start Trading Options as a Beginner (Easy High Probability Strategy) | 168,000 | Weekly & monthly campaigns (10-delta PCS + roll); Real numbers |
| LWLFq1cMOdo | The Secret to Faster Cash Flow from Covered Calls (Easy Technique) | 168,000 | Covered calls (Key 1 buyback-at-10% — confirms garbled figures); Real numbers |
| m8R_564Kp6k | How To Start Options Trading (The Easy High Probability Way) | 160,000 | Non-directional income (5-delta 60-DTE iron condor campaign); Real numbers |
| bDhYEMCLm9k | Iron Condor Options Trading Strategy (Best Explanation) | 160,000 | Non-directional income (RUT channel condor); Real numbers |
| Ko9E9OFYsf8 | How to Use ChatGPT to Improve Your Options Trading | 153,000 | 0-DTE strategies (30Δ condor + AI calendar filter); Developing a strategy; Real numbers |
| Kg0ts5NGr0o | Cash Secured Puts To Generate Income (Step-by-Step Guide) | 153,000 | Cash-secured puts & the wheel (SPY wheel year); Real numbers |
| FhUcZZB3tmU | Huge Options Trading Blunders: I made 1000% return on an out of the money call! (episode 3) | 148,000 | The edge of selling options (far-OTM call blunder); Real numbers |
| oxNvLwZ0dGo | Super Simple Options Strategy You Can Trade Every Day (Powerful) | 145,000 | Calendar spreads & overnight trades; Real numbers |
| qPkolXAi4BM | How To Have a Killer Edge With 0 DTE Options | 144,000 | Market internals & technical filters (ETF filter, conviction-tiered trades); Real numbers |
| 7q7AJXYOq7s | A Simple, Effective Technique That Can Triple The Profit Potential Of Options Trades | 142,000 | Earnings trades (iron-butterfly wing-width lesson); Real numbers |
| Jniwt90PUS4 | The $100 New Options Strategy | 138,000 | Small-account strategies (XSP under-$100 ATM PCS); Options basics (XSP); Real numbers |
| vU64DYL3raU | The $SPX Broken Wing Butterfly Weekly Options Strategy: Q&A | 124,000 | Weekly & monthly campaigns (BWB windfall deep-dive); The edge of selling (75% stat, insurance analogies); Real numbers |
| kG0YKGa6kc0 | How to Buy Options at ZERO-COST (While Keeping BIG Profit Potential) | 117,000 | Legging into risk-free spreads (RUT zero-cost put); Real numbers |
| -Dfl8YyoP0E | 90% Win Rate (Possible Through Options) | 114,000 | Weekly & monthly campaigns (TSLA 10Δ 60-DTE campaign + delta-doubling roll); Real numbers |
| t6yuG7KKSKg | 0 DTE Options: How to Turn a Losing Trade Into a Winner | 114,000 | 0-DTE strategies (iron-condor threatened-side roll); Options basics (daily-expiry roster); Real numbers |
| aC-JCii8Vg8 | How To Start Options Trading with a $1,000 Account | 113,000 | Small-account strategies (daily 0-DTE iron butterfly 10%/20%); Real numbers |
| B9myhwUaSsQ | Super Accurate MACD Strategy for ODTE Options Trading | 108,000 | Market internals & technical filters (MACD 3/9/5 entry trigger, conviction tiers); Real numbers |
| Is9CVUBT9y0 | Options Blunders: I'll make money every month and pay my bills out of my options income (episode 4) | 104,000 | Trading principles (blunder #4: uneven income, 2–4%/mo, reserves); Real numbers |
| rHFJdAw4PtQ | An Effective One Day Options Strategy | 98,000 | 0-DTE strategies (expiration-day pinning iron condor); Real numbers |
| UrnFowunv-E | 3 Ways I Set Up a 70% Probability Options Trades | 97,000 | The edge of selling (delta-as-PoP, IC PoP formula); Real numbers |
| SmMsPFLFqc0 | Options Trading Blunders: I always win eventually if I keep rolling my short puts down, right? (#5) | 97,000 | Trading principles (blunder #5: martingale roll-down); Real numbers |
| t2hTAtI2OxY | How to Grow A Small Account With Options (3 Easy Steps) | 96,000 | Weekly & monthly campaigns (RSI-30 60-DTE ATM PCS); Real numbers |
| -gGvWxd_iXc | Top 3 Options Trading Strategies for Beginners | 96,000 | Legging into risk-free spreads (GOOG COVID leg-in; title mismatches content); Real numbers |
| Vm0qcsR5-E4 | The Right Way to Trade Covered Calls For Income | 96,000 | Covered calls (WMT income-goal vs price-target campaigns); Real numbers |
| hbkcV1ejzJw | The Simplest High Probability Options Technique for Beginners (with Zero experience) | 94,000 | Weekly & monthly campaigns (weekly 10Δ SPX PCS); The edge of selling (delta-as-PoP); Real numbers |
| fTbHswbCOls | How To Get A Funded Options Trading Account | 21,000 | Getting started (Andrew Falde's 5 steps to funding) |
| TpAPTwLMb44 | How to Maximize Options Profits | 20,000 | The edge of selling (velocity of capital); Real numbers |
| k-VJZ95j7ec | Covered Calls Strategy for Small Accounts | 20,000 | Covered calls (TLT quarterly + 30-lot synthetic); Real numbers |
| YKjnoiKNTLs | How to Earn Good Income With Options (Even with a Small Account) | 19,000 | The edge of selling (delta trade-off doctrine, expectancy, environment); Real numbers |
| pUD2sXdXHbI | How to DOUBLE & TRIPLE Your Potential Profits (with Options) | 19,000 | Directional swing trades (deep-ITM synthetic stock, AMZN); Real numbers |
| v_27P1SNZTU | Here's how you can use RSI with Options Strategies | 19,000 | Weekly & monthly campaigns (RSI-70 10Δ call credit spread); Real numbers |
| _7Ay68OHOTM | A Really Dopey Options Trading Concept | 19,000 | The edge of selling (cheap-OTM-call arithmetic, ADBE); Real numbers |
| f9pJ-V2vqww | An Easy (and safer) Way to Double Returns Using Options | 19,000 | Covered calls (SPY dividend-replication synthetic); Real numbers |
| dLZYl7kC468 | Huge Options Trading Blunders: I'll Find the Holy Grail Options Strategy and Just Trade That (ep10) | 19,000 | Trading principles (blunder #10: return chasing); Real numbers |
| cTX7BettDqk | How to Scalp Spikes in the $VIX | 19,000 | VIX trades (short puts at complacency support); Real numbers |
| EP6MBURnM-A | The Earnings Straddle Options Strategy | 18,000 | Earnings trades (IBM B-straddle playbook + backtests); Real numbers |
| rjHviGxmAKA | Why This Surprisingly Easy Options Strategy Works | 18,000 | Calendar spreads & overnight trades (1-month SPX ATM calendar); Real numbers |
| QsccAA3k_1o | How to Construct an Options Trade With a Really Wide Profit Zone | 17,000 | Non-directional income (iron condor 50-pt defensive roll); Real numbers |
| VsN4Ntw7onM | A Simple Options Strategy That Can Beat A Bearish Market | 17,000 | Cash-secured puts & the wheel (bear-market 10Δ put ladder); Real numbers |
| WO3fecu15dk | How Pro Traders Use Options | 17,000 | Directional swing trades (Max's AMZN breakout, phase-2 risk removal); Real numbers |
| y6NpvN0VLX0 | How to Own a Call Option Before Earnings For Free | 17,000 | Earnings trades (PCS-financed "free" call, BBBY); Real numbers |
| W1HJb-ST-6Q | Here's a cool options trade for a volatile market | 17,000 | Duplicate transcript of [-gGvWxd_iXc] (GOOG leg-in) — co-cited there; Real numbers |
| AtSAFHA2Hvc | Huge Options Trading Blunders: Your Back Test Proves That You're going To Get RICH (episode 9) | 17,000 | Transcript duplicates [Vm0qcsR5-E4] (WMT covered calls) — the titled blunder content is absent; co-cited in Covered calls |
| HpXE6fr-q4g | How to Be WRONG and Still Make Money (Beginner Options Trading) | 16,000 | Directional swing trades (XOM bearish put BWB on oil divergence); Real numbers |
| FNKIDMBPcaI | How to Trade the Butterfly - The Core Strategy of Our Trading Desk | 94,000 | Non-directional income (SPX 2815 iron butterfly, desk core setup); Real numbers |
| iwE_tI6foJs | The Small Account Options Strategy That Works | 91,000 | Covered calls (poor man's covered call, COST 2023 10Δ campaign); Real numbers |
| s1jRE-Kg4dQ | The Secret Momentum Indicators For 0 DTE options Trading Success | 87,000 | Market internals & technical filters (squeeze setup live on QQQ, intraday leg-in); Legging into risk-free spreads; Real numbers |
| PrsUnhNjF4Y | How to Roll Over Call Options for a Living | 86,000 | Covered calls (TLT call-diagonal monthly campaign); Real numbers |
| X5bFm3sWqkA | How to Turn Any Stock Into an Income Machine (Options Strategy) | 85,000 | Covered calls (BKNG 1%-per-month campaign); Real numbers |
| FYNpBJDuXhU | This Mistake Will DESTROY Your Options Trading Career (Watch Before You Start Trading) | 84,000 | Trading principles (8Δ RUT iron condor, scaling-on-a-streak blunder); Real numbers |
| 7Wwy58T83W0 | Options Strategies For Earnings Announcements | 84,000 | Earnings trades (GOOGL recency-bias pre-earnings put; IV-ramp numbers co-registered under [IkGV8x5uz_A]); Real numbers |
| -rwYS0Dq6Ro | Our Huge Options Trading Blunders Series (Episode 1) | 83,000 | Trading principles (blunder #1: $5k vs $500k sizing, risk-tolerance muscle); Real numbers |
| if0P_RU5zWc | Bull Call Spread Tutorial (Pro Options Strategy) | 82,000 | Directional swing trades (ITM bull call spread + roll-down/size-up rescue); Real numbers |
| kE0T8l-p9ko | Passive Income Through Options (Easiest Way to Profit for Beginners) | 81,000 | Cash-secured puts & the wheel (QQQ wheel May 2023–May 2024); Real numbers |
| CjbWjnWXXzQ | Simple Options Strategy That Made 500% While The Market Lost 4% | 81,000 | Weekly & monthly campaigns (2018 weekly PCS with 200-DMA filter); Real numbers |
| tVQY5bSDodk | How To Produce Consistent Monthly Cash Income With Options | 77,000 | Cash-secured puts & the wheel (MoneyShow SPY 2-lot wheel, AMZN CSP, pros/cons); Real numbers |
| 9j-MhX4j6cs | How to 10X Your Covered Call Returns (For Small Accounts) | 73,000 | Covered calls (SPY covered call vs 3-lot call debit spread); Real numbers |
| 25ej9CwzTGQ | Options Trading For a Living: You Can Become a Winning Options Trader If You Have These Qualities | 73,000 | Getting started (the ten traits / desk funding checklist, stress-period list); Trading principles (cross-ref); Real numbers |
| W5Gl_E2Sq-A | How I Would Start Trading Options With $3,000 | 71,000 | Small-account strategies (three trades under $3,000); Covered calls (PSX diagonal); Calendar spreads (UPS put calendar); Real numbers |
| t8VszTqb7iY | Weekly Options: Double Diagonal Options Strategy to Set Up A Potentially Risk Free Earnings Play | 71,000 | Earnings trades (CMG pre-earnings double diagonal roll campaign); Real numbers |
| YLrRxUUHl44 | The Most Consistently Profitable Options Trading Strategy (Step-by-Step Guide) | 70,000 | Non-directional income (TLT monthly double diagonal, 3-item checklist); Real numbers |
| IdbLc1JBYYI | One Day Trading Strategies Using Options Deltas | 67,000 | 0-DTE strategies (10Δ SPX iron condor template); Real numbers |
| 0M8oc0T66yk | How to Trade the Calendar Options Strategy | 66,000 | Calendar spreads (1-week/3-week SPX ATM calendar); Real numbers |
| F4d_OIVawns | Simplest Options Strategy for Beginners (with zero experience) | 66,000 | Non-directional income (RUT 10Δ 2-month iron condor, 50%-of-credit exit); Real numbers |
| N9mx7uz3vbw | SMB Options Tribe - The Weekly Broken Wing Butterfly Trade | 66,000 | Weekly & monthly campaigns (Options Tribe BWB guidelines, 16Δ, sell-off-day entry); Real numbers |
| PgghzkCugZ8 | Here's How A Simple Options Income Strategy Could Have Easily Beaten The 2019 Equity Markets | 66,000 | Weekly & monthly campaigns (2019 60-DTE 10Δ PCS with 200-DMA filter); Real numbers |
| 8KbV5QtKFCQ | Monthly Income Options Strategy (How to do it right & why most people screw it up) | 65,000 | Cash-secured puts & the wheel (TSLA 6-month wheel, three principles); Real numbers |
| AayABdqDKIc | High Accuracy Options Trading Strategy (That Actually Works) | 64,000 | Weekly & monthly campaigns (Bollinger+RSI → 20Δ credit spreads on QQQ); Real numbers |
| rnETl_NteAo | How I think (and trade) like a hedge fund | 62,000 | Trader psychology & performance (Steenbarger: ideas vs construction, themes, 4-quadrant environment grid); Real numbers |
| UOX2_YaAIRc | An Easy Options Strategy that Crushed The Market | 60,000 | Weekly & monthly campaigns (2017–18 70-day 10Δ PCS with 200-DMA filter, 2× stop); Real numbers |
| 6-Q6xjAX7aM | How to Fix a Losing 0 DTE Options Trade (and turn it into a winner) | 59,000 | 0-DTE strategies (iron-condor call butterfly roll, Dec 2024); Real numbers |
| MkWozp1MFmg | Top 7 Market Breadth Days for 0 DTE Options Trading | 59,000 | Market internals & technical filters (seven breadth-day types; neutral-day condor; trifecta risk reversal); Real numbers |
| mY0x0Mc8iqk | Swing Trading Strategies: You Can Boost Your Trading Returns With This Simple Options Technique | 59,000 | Directional swing trades (time-premium anatomy; converting a winning call to stock + target-strike strangle); Real numbers |
| ud2KQ-Di57Q | How to Expand the Profit Zone on Butterfly Trades | 59,000 | Non-directional income (iron butterfly → iron condor via call-side butterfly adjustment); Real numbers |
| zs4pK__ncCo | Top 3 Options Trading Mistakes You Must Avoid | 94,000 | NOT DISTILLED — harvested file is a copy of this volume, not a transcript (harvester captured the wrong NLM source); re-harvest required |
| vFTpvP8kwzY | Best Options Strategy for Bearish Markets | 58,000 | Directional swing trades (September-seasonality SPY put diagonal, 2021–23); Real numbers |
| WDbHqMeSCHA | Why, When & How to Roll a Covered Call (In-depth Guide) | 56,000 | Covered calls (WMT >80%-decay buyback + re-sell "double dip"); Real numbers |
| lRj741LUAFo | High Profit Short Options Strategy (With Step-by-Step Execution) | 56,000 | Directional swing trades (bearish SPY broken-wing butterfly + assignment into the bounce); Real numbers |
| 1HXDto7qXaU | Generate Weekly Passive Income with this Options Strategy | 56,000 | Cash-secured puts & the wheel (weekly SPY wheel, ≥$2.00 put rule, Q1 2023); Real numbers |
| RbWA61gJSa4 | A Very Effective Options Strategy Using the RSI Indicator | 56,000 | Weekly & monthly campaigns (RSI 70/30 on DIA → 1-SD two-week credit spreads); Real numbers |
| KPcDNIqd4OI | Options Secrets: It is possible to win 80% of your options trades | 55,000 | Non-directional income (10Δ 60-day SPX iron condor through 2022 + delta-doubling roll); Real numbers |
| Stfx1brjj0k | How To Make a Potential 2X Profit Overnight (With Options) | 53,000 | Earnings trades (NVDA Nov 2024 earnings iron butterfly; IV build vs V crush measured); Real numbers |
| 4iCQciAzjJY | Options Trading Blunders: Why should I waste money buying long options to protect my short options? | 53,000 | Non-directional income (blunder #7: NDX short strangle vs iron condor, capital efficiency); Real numbers |
| pW2ZZAAPVMI | How to Supercharge Your Trading Returns (Options Strategy) | 51,000 | Directional swing trades (SPX 2-month bullish risk reversal, Jul–Aug 2020); Real numbers |
| DQ6nTpng7MM | Do This Before Every Covered Call Trade | 50,000 | Covered calls (five-rule checklist, 2025 examples PSX/TSLA/QQQ/AMZN); Real numbers |
| ic24mZL9Fdk | Why Over 90% of Options Traders Lose Money | 49,000 | The edge of selling options (three hurdles of option buying: cheap deltas, premium hurdle, V crush); Real numbers |
| qm5ENAPUCEA | A Simple Weekly Options Strategy | 49,000 | Non-directional income (pre-election one-week SPX iron butterfly + put butterfly roll, Oct 2020); Real numbers |
| toMmfKHzQXU | A Weekly Options Strategy With Remarkable Potential | 49,000 | Weekly & monthly campaigns (weekly SPX double broken-wing butterfly); Real numbers |
| weUoHkMBL4A | How to Yield Consistent Income (Using Options) | 48,000 | Covered calls (monthly SPY buy-write at the ½%-of-price call, 2023–24); Real numbers |
| ipzry05eP00 | How to Win up to 80% of Your Trades (Easy Options Strategy) | 48,000 | Earnings trades (NVDA Feb 2024 pre-earnings 10Δ iron condor; earnings vs normal-day condor width); Real numbers |
| RP5xIYMrXKE | Weekly Options Strategies Around Earnings (Remarkable Potential for This 4 Day Trade in $AAPL) | 48,000 | Earnings trades (pre-earnings call calendar, AAPL Apr 2019); Real numbers |
| iJMkj24PHqs | Small Trading Account? Trade This Options Strategy | 46,000 | Small-account strategies (capital hogs: RUT iron condor vs iron butterfly); Real numbers |
| K6YVPHULzPA | The Wheel Options Strategy Explained (Step by Step) | 45,000 | Cash-secured puts & the wheel (QQQ Oct 2025–Feb 2026); Real numbers |
| 4dedQBgiZJA | The Secret to Finding High Probability Options Trades in Less than 3 Minutes | 45,000 | Weekly & monthly campaigns (10-delta credit spreads on RSI extremes, SPX 2024–25); Real numbers |
| oO5SfYblvio | The Easy Way to Grow a Small Account With Options | 45,000 | Small-account strategies ($5k SPY monthly put credit spread program 2023); Real numbers |
| xrCSOh4WEGY | How to Trade a Weekly Options Strategy with a Built in Lottery Ticket | 45,000 | Weekly & monthly campaigns (weekly SPX put broken-wing butterfly, 20-SMA filter); Real numbers |
| l7BHgd2PO6A | How to Turn Losing O DTE Options Trades Into Winners (Simple Fix) | 43,000 | 0-DTE strategies (iron condor call condor roll, Oct 31 2023); Real numbers |
| 8u89hMA2was | Options Income Trading: Why Do You Win So Frequently? | 43,000 | Non-directional income (AMZN 60-day 10Δ iron condor campaign 2019); Real numbers |
| qabKcPmwjEA | Weekly Options: The Keys to Success | 42,000 | Weekly & monthly campaigns (SMB × InvestiQuant one-day SPX credit-spread backtest, 2018–2020); Real numbers |
| LwZ9s2ud68s | Huge Options Trading Blunders: I'm switching to the options strategy that's CRUSHING it (episode 6) | 42,000 | Trading principles (blunder #6 strategy hopping; bearish butterfly vs Bull 2013–15); Real numbers |
| cSI1eXFW6Ms | Options Strategies for Regular Income: He won this trade through smart analysis & options knowledge | 42,000 | Non-directional income (GOOGL iron condor side-scalping, Oct–Dec 2019); Real numbers |
| dU3eKVXlKQE | How to Generate Consistent Monthly Income (Cash Secured Puts vs. Covered Calls) | 41,000 | Cash-secured puts & the wheel (CSP vs covered call doctrine, MSFT 2024–25); Real numbers |
| 8BjBWBuiEh8 | The Unique Overnight Options Trading Strategy | 41,000 | Calendar spreads & overnight trades (overnight 20Δ SPX iron condor, May 2025); Real numbers |
| tT08tJdsH_E | Huge Options Trading Blunders Series: Owning Long Options for "Free" (episode 2) | 41,000 | Trading principles (blunder #2 "free call" = naked put risk); Real numbers |
| 9q32G8yLxbM | Bollinger Band Options Trading Strategy (That Actually Works) | 40,000 | Weekly & monthly campaigns (Bollinger-band 1-σ credit spreads, RUT 2025); Real numbers |
| tXD17g377NY | Options Trading Secrets: How to Enter and Exit like a Pro | 40,000 | Weekly & monthly campaigns (50%-of-credit exit on 60-DTE 20Δ SPX put credit spreads, capital velocity); Real numbers |
| Mn5fYhFqxvs | An Easy One Day Options Strategy | 39,000 | 0-DTE strategies (iron condor on the overnight-futures support/resistance zones); Real numbers |
| 7IHCmruEZUk | How to Grow a Small Account (Using Options) | 39,000 | Small-account strategies (four steps: define risk with the condor, journal, backtest, compound); Real numbers |
| 66lbCWsfnyA | Improve Your Options Returns Hugely With This Simple Tweak (Counterintuitive) | 39,000 | The edge of selling options (spread width: tighter long strike = more lots, less capital, higher return); Real numbers |
| ygMHTNFIdbw | Put Ratio Spread Guide (Step by step) | 38,000 | Cash-secured puts & the wheel (TSLA put-ratio-spread accumulation campaign 2023–24); Real numbers |
| pyjOcisjrTU | Options Secret for Producing Smart Passive Income | 38,000 | Covered calls (PEP covered strangle, 1-year); Real numbers |
| lXtcZyC1Rks | Best Options Trading Strategy for Beginners (with Zero experience) | 37,000 | Cash-secured puts & the wheel (MSFT monthly CSPs until assignment); Real numbers |
| 5UNql894bD4 | Double Diagonal Options Strategy | 37,000 | Calendar spreads & overnight trades (SPX double diagonal rolled every 2–3 days, Nov 2020); Real numbers |
| LHx19knh8x4 | High Reward Low Risk Options Strategies | 36,000 | Directional swing trades (GS 5-wide call debit spread at the channel low); Real numbers |
| rpFL_mEFPSg | Trade Options Like a Casino (Consistent Profits) | 34,000 | Developing a strategy (casino edge, expectancy formula, 75Δ/25Δ put debit spread system); Real numbers |
| ftmEH4ikBy4 | The Worst Mistake Beginner Options Traders Make | 34,000 | Trading principles & risk management (10× size-up blowup; risk tolerance as a muscle); Real numbers |
| cSKJpuNX2lU | Scalping Options Trades is Easy and Smart | 34,000 | Non-directional income (scalping each condor side at ~80% of its own credit); Real numbers |
| FDpmRhFsp5s | How to Transition Into a Professional Options Trader | 34,000 | Getting started (Freudberg's path, desk hiring criteria, the Rhino, tooling, why traders fail); Real numbers |
| -huhEgn9TRg | How to Protect Your Stock Profits (With This Smart Options Strategy) | 34,000 | Directional swing trades (TSLA bear put spread financed by a covered call); Real numbers |
| qblhVcLltZQ | How to Trade Earnings with Options | 33,000 | Earnings trades (CRM double calendar exited before the report); Real numbers |
| LcqiRgKeGXg | An Easy Options Trade for a Small Account | 33,000 | Non-directional income (weekly SPY iron condor + put condor roll, Dec 2021); Real numbers |
| 7XBsrrQOdQU | You can crush earnings season with this options strategy | 33,000 | Earnings trades (AMZN double calendar, Jan–Feb 2021); Real numbers |
| j0laz0Ks5F8 | You'll never guess the best way to dramatically improve your risk and return on options spreads | 33,000 | The edge of selling options (spread width vs lot count on a fixed $2,000 gross risk); Real numbers |
| ASsnZOKLXGg | Iron Condor Options Strategy: 2 Easy Steps | 32,000 | Non-directional income (condor construction, breakeven past the short strike, delta probability dial); Real numbers |
| IsuWqXxvjeA | How to Profitably Trade Options in a Volatile Market (CHEAT SHEET) | 32,000 | The edge of selling options (same put credit spread in high vs normal VIX); Real numbers |
| i0h4_uVeDtY | The 5 Deadliest Mistakes Options Traders Make | 32,000 | Trading principles & risk management (sizing, market vs limit orders, strategy hopping, cheap OTM, backtest degradation); Real numbers |
| DGnUHMPbcJA | Weekly Options Trading For Income Workshop | 32,000 | Weekly & monthly campaigns (InvestiQuant Weekly Options Income Machine, full statistics); Real numbers |
| WP7JVyd6bjM | Super High Win Rate Options Strategy | 31,000 | Directional swing trades (TLT "win-win-win" modified risk reversal, Oct–Dec 2023); Real numbers |
| vfpqix1O30U | How to Profit BIG When Stocks Crash (with Options) | 31,000 | Directional swing trades (6-month 40Δ SPY put credit spreads into VIX>50 spikes); Real numbers |
| nMq1TZFBToE | Using Options For Swing Trading | 31,000 | Directional swing trades (Spencer's TSLA risk reversal hedged with short common, May 2019); Real numbers |
| Fet_MWkqemw | How To Profit From A Big Market Crash (With Options) | 30,000 | Directional swing trades (SPX modified risk reversal, Jul–Oct 2024); Real numbers |
| BY2qOpNoDdI | The Bear Trap Options Strategy (Powerful) | 30,000 | Directional swing trades (broken-wing put condor entered for a credit, Aug–Sep 2022); Real numbers |
| WSsXl8Nh3PM | The Easy Options Strategy That Can 2X Your Stock Returns | 29,000 | Small-account strategies (rolling deep-ITM NFLX LEAPS campaign 2019–2025); Real numbers |
| CNEYo3P-CRk | Options Secret to Trading Major Market Events (WITHOUT being in a trade during the event) | 28,000 | Calendar spreads & overnight trades (Brexit double calendar closed before the vote); Real numbers |
| 9pnSF-YE2DQ | You can supercharge your small account returns with this simple options strategy | 28,000 | Small-account strategies (deep-ITM 0-DTE SPY call instead of 300 shares); Real numbers |
| j2PxP-o-M1E | A Simple Options Strategy for Monthly Income | 27,000 | NLM-extracted (hybrid); Real numbers; 2 unverified figure(s) |
| goK0QOsQRvQ | If you want to win at Options trading, enter and exit like this | 27,000 | NLM-extracted (hybrid); Real numbers; 1 unverified figure(s) |
| EYA6mxeZmzg | How to Make $1,000/month owning certain dividend stocks (and options) | 27,000 | NLM-extracted (hybrid); Real numbers; 1 unverified figure(s) |
| BPvBoQLupOQ | Huge Options Blunders: If I think A Stock Is Going Up, I’ll Just Buy A Call, It’s Cheaper (ep 8) | 26,000 | NLM-extracted (hybrid); Real numbers |
| KBWUtGD1kwk | The Hidden Key that Makes Options Trading Profitable | 26,000 | NLM-extracted (hybrid); Real numbers |
| cUfBqD03mTc | How to TRIPLE Your Options Income (Easily) | 26,000 | NLM-extracted (hybrid); Real numbers |
| -wyjzl9zPfs | The Top 3 Options Trading Strategies That Anyone Can Learn | 25,000 | NLM-extracted (hybrid); Real numbers |
| VDYG8LDIfGk | How to Generate Income With High Yield Stocks (Options Tutorial) | 25,000 | NLM-extracted (hybrid); Real numbers |
| YVPcw-xIUhs | Before Trading Options You Need to Learn This (Greeks for Beginners) | 25,000 | NLM-extracted (hybrid); Real numbers |
| xDaCtZ9GMl0 | Top 3 Options Strategies to Catch Reversals | 25,000 | NLM-extracted (hybrid); Real numbers |
| IedTDDpXFCw | What are realistic returns for options income trading? | 24,000 | NLM-extracted (hybrid); Real numbers |
| 8y_bNYZgy1I | Stop Making Your Broker Rich Buying SPY Options | 24,000 | NLM-extracted (hybrid); Real numbers |
| n8BOGRwntF4 | Inside an Elite Trading Firm: How to achieve 85% Accuracy (trading options) | 23,000 | NLM-extracted (hybrid); Real numbers |
| 4P5LxIdOJXY | Options Strategies for Day Traders | 23,000 | NLM-extracted (hybrid); Real numbers |
| njoDkeNAs8E | You Can Win So Many Different Ways With This Weekly Options Strategy | 23,000 | NLM-extracted (hybrid); Real numbers |
| Wc-JbFF8x5o | High Probability Options Strategy (Best Time To Execute) | 23,000 | NLM-extracted (hybrid); Real numbers; 2 unverified figure(s) |
| STQOppV45ZQ | Covered Calls: How to Create an INCOME MACHINE (Easily) | 23,000 | NLM-extracted (hybrid); Real numbers; 1 unverified figure(s) |
| 4gON-kdleCM | Using options to profit if the stock market goes up or down | 22,000 | NLM-extracted (hybrid); Real numbers; 1 unverified figure(s) |
| 0lzwuAhX16U | How to Profit From a Market Meltdown: A Guide to Options Trading During a Crash | 22,000 | NLM-extracted (hybrid); Real numbers; 3 unverified figure(s) |
| q4lILcbWKJ0 | The Gamma Squeeze Trading Strategy (in $AMC) | 22,000 | NLM-extracted (hybrid); Real numbers |
| btgyiIKAqeA | Directional Options Strategies | 22,000 | NLM-extracted (hybrid); Real numbers |
| avvWq9V95AQ | The Short Risk Reversal Options Strategy | 16,000 | NLM-extracted (hybrid); Real numbers |
| D4sAWnZIohg | You Can Only Be A Successful Options Trader If You DO THIS! | 16,000 | NLM-extracted (hybrid); Real numbers; 1 unverified figure(s) |
| yHOAgcUIR0k | Easy, Repeatable Options Trades (How to Find Them) | 15,000 | NLM-extracted (hybrid); Real numbers |
| 2qIkQUHUmJM | How I Buy Stocks At Huge Discounts (with Options) | 15,000 | NLM-extracted (hybrid); Real numbers; 1 unverified figure(s) |
| H_2YWD0dUFM | An effective technique for turning losing options trades into winners | 14,000 | NLM-extracted (hybrid); Real numbers |
| e9lTVDaDBOk | SMB Options Tribe - The Triple Butterfly | 14,000 | NLM-extracted (hybrid); Real numbers |
| 5dUqJWT_Uf8 | How To Profit From  A Recession: A Guide to Trading Options During A Crash | 14,000 | NLM-extracted (hybrid); Real numbers; 5 unverified figure(s) |
| 5QZUDprprlU | How to Construct an Options Trade With a Really Wide Profit Zone | 14,000 | NLM-extracted (hybrid); Real numbers |
| KAapuE02EOw | How to Grow a Small Options Account (quickly) | 14,000 | NLM-extracted (hybrid); Real numbers |
| tG5zTqOITkM | SMB Options Tribe - The Heart Friendly Butterfly | 13,000 | NLM-extracted (hybrid); Real numbers |
| 6BLrentthYQ | How Short Term Traders Can Survive Unprecedented Volatility | 13,000 | NLM-extracted (hybrid); Real numbers |
| oPgTwTvc6Bk | A simple 3 day options strategy with surprising potential | 13,000 | NLM-extracted (hybrid); Real numbers |
| VNouUypRNYg | How to Own a FREE Put Option | 13,000 | NLM-extracted (hybrid); Real numbers |
| _mfnkltO5DE | You'll be surprised how quickly the profits can come in with this options strategy | 13,000 | NLM-extracted (hybrid); Real numbers |
| LG6iH1tac6U | The Best Breakout Strategy With Options (Must Know) | 13,000 | NLM-extracted (hybrid); Real numbers |
| V_fvAxB7vgw | How to Buy an Options Contract for FREE | 13,000 | NLM-extracted (hybrid); Real numbers |
| Usr6o69kTH8 | Turning a Huge Misconception About Options Into a Big Opportunity | 12,000 | NLM-extracted (hybrid); Real numbers |
| IMl-Zg17M7w | How to Triple Your Dividend Income (With Covered Calls) | 12,000 | NLM-extracted (hybrid); Real numbers; 2 unverified figure(s) |
| QfjqqzJC4ew | How Proprietary Traders Use Options | 12,000 | NLM-extracted (hybrid); Real numbers |
| 124LSnWB2n0 | How Pro Traders Use Weekly Options To Trade AMC | 12,000 | NLM-extracted (hybrid); Real numbers |
| 4DAONEGmoX8 | The 14 Day Asymmetrical Iron Condor | 12,000 | NLM-extracted (hybrid); Real numbers |
| qpZr4V5NAaY | How to Safely Ride Out a Market Crash With This Easy (and cheap) Options Strategy | 12,000 | NLM-extracted (hybrid); Real numbers |
| 97HFwhb_wxI | You Can REACT to the Market Instead of Predicting It With This 1 Day Options Strategy | 12,000 | NLM-extracted (hybrid); Real numbers |
| vM1dt9PIKjw | If you use this simple options strategy you're win rate HAS to improve, probably dramatically | 12,000 | NLM-extracted (hybrid); Real numbers |
| CLywU1I3YB4 | How to Profit From a Pullback on TSLA with Options | 11,000 | NLM-extracted (hybrid); Real numbers |
| ofFaU56ynsk | How You Can Own Call Options For Free | 11,000 | NLM-extracted (hybrid); Real numbers |
| 0xzuGAUVqRM | Huge Options Trading Blunder #11: Market Orders on Options Spreads | 11,000 | NLM-extracted (hybrid); Real numbers |
| c2YKd2TT-2I | You Can Supercharge Your Options Trades With THIS technique | 11,000 | NLM-extracted (hybrid); Real numbers |
| SqKhVuOYNNQ | Weekly Options Strategies Can Yield Outstanding Returns (Especially When the Market is Volatile) | 11,000 | NLM-extracted (hybrid); Real numbers |
| 7ICrfxra46Y | Boost Your Dividends Through This Easy Options Technique | 11,000 | NLM-extracted (hybrid); Real numbers; 2 unverified figure(s) |
| y_AW3Ahm954 | How to Be Wrong and Still Make Money (Options for Beginners) | 11,000 | NLM-extracted (hybrid); Real numbers |
