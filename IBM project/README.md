# 🛒 Supermarket Sales Analysis Dashboard

**A B.Tech Data Science Project — Interactive Sales Dashboard built with Python & Streamlit**

---

## 📌 Project Title

**Supermarket Sales Analysis Dashboard using Python, Pandas, and Streamlit**

---

## 📖 Introduction

This project builds an interactive web-based dashboard to analyse supermarket sales data. The dashboard allows users to explore sales trends, product performance, branch comparisons, customer behaviour, and payment preferences — all through an easy-to-use interface with sidebar filters.

The project covers the complete data science workflow: from loading and cleaning raw data, to computing statistics, generating charts, and delivering business insights — entirely in Python without any hardcoded values.

---

## ❓ Problem Statement

Supermarkets generate large volumes of transactional data every day. Without proper analysis, this data sits unused. The challenge is to:

- Identify which products, branches, and categories drive the most revenue
- Understand customer behaviour across different segments
- Discover payment preferences and satisfaction trends
- Present all findings in a simple, interactive dashboard that any stakeholder can use

---

## 🎯 Objectives

1. Load and clean the supermarket sales dataset automatically
2. Handle missing values, duplicates, wrong data types, and invalid records
3. Display key performance indicators (KPIs) in metric cards
4. Provide interactive sidebar filters (Branch, City, Product, Customer Type, Gender, Payment, Date)
5. Perform detailed analysis across 7 categories: Product, Branch, Category, Payment, Customer Type, Gender, and Rating
6. Answer 6 live business questions dynamically from the filtered data
7. Generate data-backed business insights with no hardcoded results

---

## 📂 Dataset Description

| Property | Value |
|----------|-------|
| **File Name** | `supermarket_cleaned_500.csv` |
| **Total Records** | 500 transactions |
| **Total Columns** | 17 original + 1 calculated (`sales`) |
| **Date Range** | January 2019 – March 2019 |
| **Branches** | A (Yangon), B (Mandalay), C (Naypyitaw) |
| **Source** | Supermarket sales dataset (Myanmar) |

### Column Details

| Column | Type | Description |
|--------|------|-------------|
| `invoice_id` | String | Unique transaction identifier |
| `branch` | String | Branch code (A, B, or C) |
| `city` | String | City where the branch is located |
| `customer_type` | String | Member or Normal customer |
| `gender` | String | Customer gender (Male / Female) |
| `product_line` | String | Product category (6 types) |
| `unit_price` | Float | Price per product unit |
| `quantity` | Integer | Number of items purchased |
| `tax_5pct` | Float | 5% tax applied to the sale |
| `total` | Float | Final bill amount (cogs + tax) |
| `date` | Date | Transaction date |
| `time` | String | Transaction time |
| `payment` | String | Payment method (Cash / Ewallet / Credit card) |
| `cogs` | Float | Cost of goods sold (unit_price × quantity) |
| `gross_margin_percentage` | Float | Gross margin % (constant 4.762%) |
| `gross_income` | Float | Gross income (same as tax_5pct) |
| `rating` | Float | Customer satisfaction rating (1–10) |
| `sales` *(calculated)* | Float | Derived as `unit_price × quantity` |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web dashboard framework |
| **Pandas** | Data loading, cleaning, and analysis |
| **Plotly Express** | Interactive charts and visualisations |

---

## ✨ Project Features

### 🗂️ Data Management
- Automatic CSV loading with data type correction
- Missing value detection and imputation (median for numerics, mode for categoricals)
- Duplicate row removal
- Numeric validation (removes rows with invalid prices, quantities, ratings)
- Sales column calculated as `unit_price × quantity`
- Full cleaning audit log showing every step taken

### 📊 Dashboard & KPIs
- 5 primary KPI cards: Total Sales, Transactions, Quantity Sold, Avg Transaction Value, Avg Rating
- 4 secondary KPIs: Tax Collected, Gross Income, Avg Unit Price, Avg Items per Transaction
- KPI breakdown tables by Branch, Product Line, and Payment Method

### 🔽 Interactive Filters
- Multiselect filters: Branch, City, Product/Category, Customer Type, Gender, Payment Method
- Date range picker
- One-click Reset All Filters button
- All charts and KPIs update instantly when filters change

### 📈 Analysis Sections (7 total)
1. **Product Sales Analysis** — bar chart, donut chart, scatter plot
2. **Branch / Store Analysis** — bar, pie, rating bar, monthly trend line
3. **Category Sales Analysis** — horizontal bars, rating comparison
4. **Payment Method Analysis** — donut charts, avg transaction bar, branch breakdown
5. **Customer Type Analysis** — pie, grouped bars, product line comparison
6. **Gender Analysis** — pie, grouped bars, product line comparison
7. **Customer Rating Analysis** — histogram with mean line, by branch, product, payment, gender

### 🔎 Live Analysis
- Answers 6 business questions dynamically from the current filtered dataset
- Styled Q&A cards with supporting values
- Summary table and 6 mini-charts

### 💡 Business Insights
- 15+ insight cards in 5 categories: Product, Branch, Payment, Customer, Rating
- Green (positive), amber (warning), blue (neutral) colour coding
- Insight summary table at the bottom

---

## 🔬 Methodology

```
Raw CSV Data
     │
     ▼
1. Load Data        → pd.read_csv(), parse dates
     │
     ▼
2. Clean Data       → fix types, impute nulls, remove duplicates,
                       validate numerics, calculate sales column
     │
     ▼
3. Apply Filters    → sidebar selections → df_filtered
     │
     ▼
4. Compute KPIs     → groupby, agg, mean, sum, count
     │
     ▼
5. Visualise        → Plotly bar, pie, line, scatter, histogram charts
     │
     ▼
6. Live Analysis    → 6 dynamic Q&A from df_filtered
     │
     ▼
7. Business Insights → 15+ insight cards backed by calculated values
```

---

## 🔄 Project Workflow

```
supermarket_cleaned_500.csv
        │
        ├── app.py  (all logic, UI, charts, insights)
        │       ├── load_data()       — reads CSV, parses dates
        │       ├── clean_data()      — 5-step cleaning pipeline
        │       ├── Sidebar Filters   — interactive multiselects
        │       ├── df_filtered       — filtered working dataset
        │       ├── Dashboard         — KPI metrics
        │       ├── Dataset sections  — preview, info, missing, duplicates
        │       ├── Analysis sections — 7 deep-dive analyses
        │       ├── Live Analysis     — 6 Q&A cards + charts
        │       └── Business Insights — 15+ insight cards
        │
        ├── requirements.txt  (dependencies)
        └── README.md         (this file)
```

---

## ⚙️ How to Install

### Prerequisites
- Python 3.8 or higher
- pip

### Step 1 — Clone or download the project folder

Place these 4 files in the same folder:
```
IBM project/
├── app.py
├── requirements.txt
├── README.md
└── supermarket_cleaned_500.csv
```

### Step 2 — Install dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit >= 1.32.0`
- `pandas >= 2.0.0`
- `plotly >= 5.18.0`

---

## ▶️ How to Run

```bash
streamlit run app.py
```

The app will automatically open in your browser at:
```
http://localhost:8501
```

If it does not open automatically, copy the URL from the terminal and paste it into any browser.

---

## 📊 Results

After running the app on the 500-transaction dataset, the following key findings were observed:

| Metric | Result |
|--------|--------|
| Total Sales (excl. tax) | $156,917.36 |
| Total Revenue (incl. tax) | $164,763.23 |
| Total Transactions | 500 |
| Total Quantity Sold | 2,734 items |
| Avg Transaction Value | $329.53 |
| Avg Customer Rating | 6.94 / 10 |
| Best-Selling Product Line | Fashion accessories |
| Top Branch by Sales | Branch C — Naypyitaw |
| Most Used Payment Method | Cash (35% of transactions) |
| Most Frequent Customer Type | Member (50.4%) |

> All values are computed dynamically. Applying sidebar filters updates every result in real time.

---

## 🚀 Future Scope

1. **Time-series forecasting** — predict future sales using Prophet or ARIMA
2. **Export to PDF/Excel** — add a download button for filtered results
3. **Real-time data** — connect to a live database (MySQL / PostgreSQL)
4. **More datasets** — extend to multi-year or multi-store data
5. **Customer segmentation** — use clustering (K-Means) to group customers
6. **Discount/promotion analysis** — if promotion data is available
7. **Mobile-friendly layout** — optimise for smaller screens
8. **Authentication** — add login so only authorised users can view the dashboard

---

## ✅ Conclusion

This project demonstrates a complete, end-to-end data science workflow applied to a real-world supermarket sales dataset. Starting from raw CSV data, the application automatically cleans the data, computes meaningful KPIs, generates interactive visualisations, and surfaces business insights — all without hardcoding any values.

The interactive sidebar filters make the dashboard practical: any stakeholder can slice the data by branch, product, customer type, payment method, or date range and instantly see updated results.

This project covers key B.Tech Data Science concepts including:
- Data loading and preprocessing with Pandas
- Exploratory data analysis (EDA)
- Data visualisation with Plotly
- Web application development with Streamlit
- Deriving insights from data

---

## 📁 File Structure

```
IBM project/
├── app.py                        ← Main Streamlit application (all code)
├── requirements.txt              ← Python package dependencies
├── README.md                     ← Project documentation (this file)
└── supermarket_cleaned_500.csv   ← Dataset (500 supermarket transactions)
```

---

*Built with Python · Pandas · Streamlit · Plotly*
