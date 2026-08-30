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
| Short 1900 put sale price [3] | RUT Bear Trap (April 28th, 2023) | Received a price of **4355** (Note: representing \$43.55) |
| Index point multiplier [3] | RUT Index option payoff | Rate of **\$100** per point |
| Multiplier factor [3] | General cash flow calculation | Multiply by **100** |
| Short 1900 puts contract count [3] | RUT Bear Trap (April 28th, 2023) | sold **five** of them |
| Short 1900 puts total credit [3] | RUT Bear Trap (April 28th, 2023) | Positive cash flow of **21,775** (Note: representing \$21,775) |
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