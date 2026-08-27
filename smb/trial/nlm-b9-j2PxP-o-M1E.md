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
| **June Trade Entry & Capital** | SPY cash-secured put. Sold 10 contracts at 400 strike expiring June 18th (third Friday in June). | Put option price: "**3.78**"; cash premium collected: "**37.80**" (representing \$3,780) |
| **June Trade Settlement** | SPY put expiration (June 18th) | SPY closed at "**right under 415**"; puts expired worthless; net profit kept: "**37.80**" (\$3,780) |
| **1-Year Campaign Totals** | SPY cash-secured put campaign (April 2021 to April, 12 months) | Won "**all 12 months**"; total cash profit: "**53 610**" dollars; average capital tied up: "**four hundred twenty two thousand five hundred dollars**" (\$422,500); return on capital: "**over twelve percent**" (12%); buy-and-hold SPY return baseline: "**4.92**" (options campaign return was "**more than two and a half times**" the stock return) |