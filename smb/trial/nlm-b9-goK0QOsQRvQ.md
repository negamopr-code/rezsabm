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
*   **Managed Campaign**: Using the quartile profit matrix over the exact same period and asset produced a final profit of **\$3,050** [7].
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
| **Managed Campaign Totals & Contrast** | TLT ETF, Managed 6-trade campaign vs Unmanaged [7] | Managed campaign final profit of **\$3,050**; generated **25%** more profit than the unmanaged technique [7] |