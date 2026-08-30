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