# 📊 Mutual Fund Analytics - Data Dictionary

## 1. dim_fund
Stores basic information about mutual fund schemes.

- amfi_code: Unique fund identifier
- scheme_name: Name of the mutual fund scheme
- fund_house: Asset management company
- category: Fund category (Equity, Debt, Hybrid)
- plan: Growth/Dividend plan type
- risk_grade: Risk classification of fund
- morningstar_rating: Rating given by Morningstar

---

## 2. dim_date
Calendar dimension for time-based analysis.

- date: Trading date
- year: Year extracted from date
- month: Month extracted from date
- day: Day of month
- quarter: Financial quarter

---

## 3. fact_nav
Daily NAV values for funds.

- amfi_code: Fund identifier
- date: NAV date
- nav: Net Asset Value

---

## 4. fact_transactions
Investor transaction records.

- investor_id: Unique investor ID
- transaction_date: Date of transaction
- amfi_code: Fund invested in
- transaction_type: SIP / Lumpsum / Redemption
- amount_inr: Transaction amount in INR
- state: Investor state
- city: Investor city
- city_tier: Tier classification of city
- age_group: Age bracket
- gender: Gender of investor
- annual_income_lakh: Annual income in lakhs
- payment_mode: Payment method
- kyc_status: KYC verification status

---

## 5. fact_performance
Fund performance metrics.

- amfi_code: Fund identifier
- return_1yr_pct: 1-year return (%)
- return_3yr_pct: 3-year return (%)
- return_5yr_pct: 5-year return (%)
- benchmark_3yr_pct: Benchmark return
- alpha: Excess return over benchmark
- beta: Market sensitivity
- sharpe_ratio: Risk-adjusted return
- sortino_ratio: Downside risk adjusted return
- std_dev_ann_pct: Volatility
- max_drawdown_pct: Maximum loss from peak
- expense_ratio_pct: Fund expense percentage

---

## 6. fact_aum
Assets under management data.

- amfi_code: Fund identifier
- aum_crore: AUM in crores