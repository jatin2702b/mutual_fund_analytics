# Mutual Fund Analytics Capstone 

An end-to-end data engineering and analytics project focused on processing, cleaning, storing, and analyzing mutual fund data. The project transforms raw financial datasets into a structured SQLite data warehouse and generates business insights through SQL analytics.

---

## 🚀 Project Overview

This project simulates a real-world mutual fund analytics workflow:

1. Data Ingestion from multiple CSV sources
2. Data Cleaning and Validation
3. Database Design using a Star Schema
4. Data Loading into SQLite
5. Analytical SQL Queries
6. Documentation and Version Control

The goal is to create a reliable analytics platform for evaluating fund performance, NAV trends, investor behavior, and Assets Under Management (AUM).

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- Jupyter Notebook
- Git & GitHub

---

## 📂 Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_final_analysis.ipynb
│
├── bluestock_mf.db
├── data_dictionary.md
├── requirements.txt
└── README.md
```

---

## 📥 Data Ingestion

Loaded and explored multiple mutual fund datasets, including:

- Fund Master Data
- NAV History
- AUM Data
- Monthly SIP Inflows
- Category Inflows
- Investor Transactions
- Scheme Performance
- Portfolio Holdings
- Benchmark Indices

---

## 🧹 Data Cleaning & Validation

### NAV History
- Converted dates to datetime format
- Removed duplicate records
- Validated NAV > 0
- Forward-filled missing NAV values
- Sorted by fund and date

### Investor Transactions
- Standardized transaction types
- Validated transaction amounts
- Converted dates to datetime format
- Verified KYC status values

### Scheme Performance
- Validated performance metrics
- Converted financial columns to numeric types
- Checked expense ratio ranges
- Removed invalid records

---

## 🏗️ Database Design

Implemented a SQLite Star Schema consisting of:

### Dimension Tables
- dim_fund
- dim_date

### Fact Tables
- fact_nav
- fact_transactions
- fact_performance
- fact_aum

This structure supports efficient analytical queries and reporting.

---

## 📊 SQL Analytics

Developed analytical queries to answer business questions such as:

- Top funds by AUM
- Average monthly NAV
- SIP vs Lumpsum transaction trends
- Transactions by state
- Top investors by investment amount
- Funds with low expense ratios
- Top-performing funds
- Risk vs Return analysis
- High-volatility funds
- Monthly transaction volume trends

---

## 📈 Key Outcomes

- Built a complete data pipeline from raw data to analytics
- Designed and implemented a financial data warehouse
- Generated actionable insights using SQL
- Applied data engineering and analytics best practices

---

## 🔄 Workflow

```text
Raw CSV Files
      ↓
Data Ingestion
      ↓
Data Cleaning & Validation
      ↓
SQLite Star Schema
      ↓
Data Warehouse
      ↓
SQL Analytics
      ↓
Business Insights
```

---

## 📚 Documentation

Detailed column descriptions and business definitions are available in:

```text
data_dictionary.md
```

---

## 👨‍💻 Author

**Jatin Bisht**

B.Tech Computer Science Engineering

Interested in Data Analytics, Data Engineering, Machine Learning, and Software Development.

---

## ⭐ Future Improvements

- Interactive dashboard using Power BI or Streamlit
- Automated ETL pipeline
- Advanced fund performance analysis
- Predictive analytics and forecasting
- Cloud database integration
