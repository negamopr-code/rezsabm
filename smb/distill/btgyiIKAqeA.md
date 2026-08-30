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