PART A — handbook chapter content

**Setup**
*   **Instrument**: Tesla stock (TSLA) [1].
*   **Structure**: Put credit spread (selling a put higher up on the options chain and simultaneously buying a put lower down on that same options chain for protection) [2, 3].
*   **Strikes/Deltas**: The short put is selected at approximately the 10 Delta strike price (e.g., the 105 put when Tesla opened at 1581) [1, 4]. The protective long put is bought exactly five points lower than the short put [2]. 
*   **DTE (Days to Expiration)**: Approximately 60 days (two months) [1, 5].
*   **Entry Trigger**: Bullish directional bias on the stock [3, 6]. The strategy is run as an ongoing annual campaign where a new 60-day trade is entered continuously once capital is freed up from the previous trade's expiration [3].

**Management and Exit Rules**
*   **Holding to Expiration**: If the stock closing price is above the short put at expiration, both puts expire worthless and the trader simply walks away keeping the entire upfront positive cash flow as net trade profit [7, 8].
*   **Line in the Sand (Defensive Trigger)**: Actively monitor the Delta of the short puts [9]. If the stock pulls back and the short put's Delta doubles from its original 10 Delta to a 20 Delta, this serves as the "Line in the Sand" trigger to execute a defensive roll [10].
*   **Roll-Down Procedure**: Close the threatened put credit spread (buying back the short puts and selling off the protective long puts) and establish a new put credit spread further down the chain, targeting the current 10 Delta strike to restore safety [6]. This adjustment keeps the trade cash-flow positive, though at a significantly reduced net profit [6, 11].

**Stated Edge or Statistics**
*   **Statistical Probability**: 10 Delta options statistically have an approximate 90% chance of expiring worthless, giving the put credit spread a 90% chance of winning [3, 4].
*   **Historical Performance**: In a full-year TSLA campaign, the strategy won all six of the 60-day trades [12, 13].
*   **Campaign Returns**: The campaign produced a total of \$3,370 in collected premium on a peak capital requirement of 4,530, yielding a 74% return over 12 months [13].

**Caveats**
*   **Inevitability of Losses**: Despite the high 90% win rate, losses are statistically guaranteed to occur approximately 10% of the time when the underlying asset closes below the short put strike [13].
*   **Friction and Adjustment Cost**: Implementing defensive risk management (rolling down) has a "serious cost" that heavily degrades the trade's profit margins, as seen when the roll-down procedure reduced a \$600 potential gain down to only \$110 [6, 11].

***

PART B — a markdown table of every CONCRETE NUMBER spoken

| theme | trade (instrument, structure, strikes, DTE, dates) | numbers (premium/debit/credit, capital or max risk, P&L, win rate, percentages) |
| :--- | :--- | :--- |
| **Win-Rate Expectancy** | put credit spread, 10 Delta short options [3, 14] | "90% win rate" [3, 14]; "10% of the time" the stock closes below short strike causing a loss [13] |
| **February Expiration Trade** | Tesla (TSLA) stock, put credit spread. Sold 10 of the 105 puts, bought 10 of the 100 puts (Five Points below). Entered December 19, 2022. Expiration February 17, 2023 (60 days/two months later) [1, 2, 4]. | Tesla opened at "1581" (contextual "150 stock") [1, 4]; stock dropped "62% for the Year" [4]; short put "10.36" Delta (45 points below TSLA price) [4]; statistically "approximate 10% chance" of closing below 105 (90% chance of closing above 105) [4]; short puts sold for "\$2,930" [2]; long puts bought at "\$2.34" ("\$2,340" paid out) [2]; net positive cash flow "\$590" [2]; required capital/worst-case loss "\$4,410" [2]; Tesla rallied over "200" closing at "20831" [2, 7]; final trade profit "\$590" [2, 7]; short puts expired "more than 100 points" out-of-the-money [7]. |
| **April Expiration Trade (Unadjusted Baseline)** | Tesla (TSLA) stock, put credit spread. Sold 10 of the 145 puts, bought 10 of the 140s. Entered February 17th. Expired April 23rd (about two months later) [5]. | Short put Delta "10" [5]; initial positive cash flow "\$600" [5]; required capital "4,400" [5]; stock channeled between "165 and 210" [5]; closed at "1658" on expiration [5]; short puts "more than 20 points" below close [5]; long puts "25 points" below close [5]; trade win of "\$600" [5]. |
| **June Expiration Trade** | Tesla (TSLA) stock, put credit spread. Sold 10 of the 125 puts, bought 10 of the 120 puts. Expiration June 16th [15]. | Short put Delta closest to "10" [15]; short puts sold for "a buck 72" (\$1.72) [15]; long puts bought at "a125" (\$1.25) [15]; net positive cash flow "\$470" [15]; required capital "4530" [15]; Tesla closed at year-to-date high of "26054" [15]; short puts expired "over 135 points" below close [15]; long puts expired "140 points" below close [15]; trade win of "\$470" [15]. |
| **August Expiration Trade** | Tesla (TSLA) stock, put credit spread. Short 195 puts, bought 190 puts (Five Below) [16]. | Short put Delta "10" [16]; stock closed at "21549" [16]; trade profit "\$600" [16]. |
| **October Expiration Trade** | Tesla (TSLA) stock, put credit spread. Short 165 puts, bought 160 puts [12]. | Tesla closed at "to 1193" [12]; trade profit "590" [12]. |
| **December Expiration Trade** | Tesla (TSLA) stock, put credit spread. Short 165 puts, bought 160 puts [12]. | Tesla closed far above short and long puts; options expired worthless (trade profit is included in annual tally) [12]. |
| **Defensive Roll Procedure (April Trade Roll-Down)** | Tesla (TSLA) stock, put credit spread roll-down. original short 145 put / long 140 put rolled down to short 130 put / long 125 put [6]. Triggered on March 13th, expiring April 21st [6, 10]. | Tesla dropped from original "20831" to "17157" [10]; short 145 put Delta increased from "10" to "20" [10]; chance of not expiring worthless dropped to "80%" [10]; risk of closing below short strike doubled [10]; buyback of original short puts cash outflow "\$523" [6]; selling 140 long puts brought in "4,180" [6]; selling new short puts at 130 brought in "2620" [6]; buying new protective puts at 125 cost "2060" [6]; net positive cash flow after roll "\$110" [6]; Tesla closed at "16508" on April 21st [6]; both puts expired worthless; final roll profit only "\$110" [11]. |
| **Put Credit Spread Campaign (Full Year Statistics)** | Tesla (TSLA) stock, put credit spread campaign. Six 60-day trades completed over 12 months [12, 13]. | Statistically "about 90%" likely to expire worthless [13]; total premium collected "\$3,370" [13]; largest required capital "4,530" (during the June trade) [13]; return on capital "74% return in 12 months" [13]; won "all six" trades [12]. |