PART A — Handbook Chapter Content

### Setup
*   **Instrument**: S&P 500 Index (SPX) [1].
*   **Structure**: Iron Butterfly (selling at-the-money calls and puts, buying equidistant out-of-the-money protective long calls and puts) [2].
*   **Strikes/Deltas**: Sell the at-the-money (ATM) calls and puts directly where the market is trading in the morning (e.g., 5350 strikes when trading at 5350) [1, 2]. Buy protective long calls 75 to 80 points above the short strikes (e.g., 5430 strike) and buy protective long puts 75 to 80 points below the short strikes (e.g., 5270 strike) [2, 3].
*   **DTE (Days to Expiration)**: Zero DTE (same-day expiration) [1].
*   **Entry Trigger**: Entered in the morning [1]. (The specific times of day and granular entry rules are kept proprietary to the trader [1]).

### Management and Exit Rules
*   **Time-Based Close**: Automatically exit and close the position "about 90 minutes later" to capture rapid morning time decay as options quickly approach expiration [4].
*   **Defensive Exits**: Establish and follow predefined stop and target profit parameters rather than holding blindly [3].
*   **Platform Practice (Step 3)**: Use a paper trading account for "say a month" to practice finding and executing the pre-loaded complex order ticket on your broker platform without risking live capital [5, 6]. Stare at the paper losses and evaluate your psychological comfort with them [6].
*   **Scaling Sizing (Step 4 & 5)**: When transition to live capital is made, trade the "smallest possible lot size" ("one lot") first so that execution errors and predictable losses only cost a fraction of the full size [7, 8]. Gradually and slowly increase capital over time (checking in "every month or two") [9]. 

### Stated Edge or Statistics
*   **Example Trade S&P Performance**: A 6-lot ATM Iron Butterfly on June 6th captured a net profit of \$2,466 in 90 minutes on a broker-required capital margin of \$36,366 [3, 4].
*   **Historical Backtest (Full Year 2023)**: Running this strategy daily over the entire year of 2023 yielded an average return of "a little bit over \$1,200 average per week" [5].
*   **Distribution of Performance**: The strategy was profitable in most months of 2023, experiencing net monthly losses in only three specific months: February, April, and June [10]. 

### Caveats
*   **No ATM Illusion**: Options strategies are statistical; no setup acts as an automated "ATM machine," and every healthy system has inevitable losing weeks and months that must be budgeted for [10, 11].
*   **The Sizing Trap**: Sizing up too quickly after a winning streak is a fatal blunder. Scaling capital tenfold overnight exposes the trader to drawdowns they are psychologically unprepared to tolerate (e.g., a \$400 chump-change drawdown on a 1-lot becomes a \$40,000 drawdown on a 10-lot), leading to panic-selling at a massive loss and squandering the career [9, 12-14].
*   **Live Degradation**: Live trading often underperforms backtesting due to live execution friction and real-world execution errors caused by emotional nervousness [8].
*   **Discipline Failure**: Nervousness under live market conditions frequently causes traders to bail out of their systems at the worst times, missing subsequent recovery winning streaks [8, 9].

***

PART B — Markdown Table of Spoken Numbers

| Theme | Trade (Instrument, Structure, Strikes, DTE, Dates) | Numbers (Premium/Debit/Credit, Capital or Max Risk, P&L, Win Rate, Percentages) |
| :--- | :--- | :--- |
| **Prop Firm History** | N/A | NYC since "2005" [15]; developed "7even" and "eight figure per year" traders [15]. |
| **Weekly Income Target** | Unspecified Proposed Strategy | Average of "\$1,000 per week" [15]. |
| **Example Trade Entry** | SPX Index, 0-DTE Iron Butterfly. Sold 6 calls & 6 puts at 5350 strike (ATM). Bought 6 calls at 5430 strike & 6 puts at 5270 strike. Entered morning of June 6th. | SPX open: "all-time high of 53 5780" [1]; SPX level at entry: "5350" [1]; short call price: "1065 buy" [2]; index option payoff rate: "\$100 per Point" [2]; short calls premium: "\$ 6390" [4]; short puts premium: "\$54.90" [4]; protective calls cost: "\$48" [4]; protective puts cost: "\$198" [4]; net credit received: "\$ 11,644" [4]; broker required capital: "36,3 66" [4]. |
| **Example Trade Exit** | SPX Index, 0-DTE Iron Butterfly (June 6th) closed early. | Closed "about 90 minutes later" [4]; trade profit: "\$2,466" [3]. |
| **General Hypothesis Structure** | SPX Index, repeated daily. Sell 6 ATM calls & 6 ATM puts; buy 6 calls & 6 puts for protection. | Protective wings placed "about 75 80 points further away" [3]; closed "90 minutes later" [3]. |
| **Historical Backtest Stats** | SPX Index, repeated daily (Full Year 2023). | Strategy lost money in "three of them" (specifically "February, April and June" months) [10]; average weekly yield: "little bit over \$1,200 average per week" [5]. |
| **Paper Trading Practice** | Step 3: Paper simulation before live capital. | "say a month before" live deployment [5]. |
| **Live Money Sizing Control** | Step 4: Smallest lot size live execution vs. target 6-lot. | Execute a "one lot" instead of "six lot" [7]; yields and loses "about 16%" of the size of a six-lot [7]. |
| **Target Capital Sizing** | Step 5: Sizing up gradually to target. | Target size: "six slot" [9] to make "about \$1,000 a week on average" [9]; size-up checks "every month or two" [9]. |
| **Additional Strategies** | Free training workshop. | "three more option strategies" [16]. |