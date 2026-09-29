import streamlit as st
import pandas as pd
import plotly.express as px

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🛒",
    layout="wide",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Page header ── */
.page-header {
    padding: 1.2rem 1.6rem 1rem;
    background: linear-gradient(90deg, #1e3a5f 0%, #2563a8 100%);
    border-radius: 12px;
    margin-bottom: 1.4rem;
    color: #fff;
}
.page-header h1 {
    font-size: 1.75rem;
    font-weight: 800;
    margin: 0 0 0.25rem;
    color: #fff;
}
.page-header p  { font-size: 0.9rem; margin: 0; opacity: 0.85; }
.badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 0.78rem;
    margin-top: 0.5rem;
    font-weight: 600;
}

/* ── Section heading ── */
.section-header {
    border-left: 5px solid #2563a8;
    padding: 6px 0 6px 14px;
    margin-bottom: 1rem;
}
.section-header h2 { font-size: 1.25rem; font-weight: 700; margin: 0; color: #1f2328; }
.section-header p  { font-size: 0.83rem; color: #57606a; margin: 2px 0 0; }

/* ── KPI card ── */
div[data-testid="metric-container"] {
    background: #f7f8fa;
    border: 1px solid #e5e7eb;
    border-radius: 10px;
    padding: 14px 18px !important;
}
div[data-testid="metric-container"] label {
    font-size: 0.78rem !important;
    color: #57606a !important;
    font-weight: 600 !important;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
    font-size: 1.45rem !important;
    font-weight: 800 !important;
    color: #1f2328 !important;
}

/* ── Dataframe table ── */
div[data-testid="stDataFrame"] { border-radius: 8px; overflow: hidden; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] { background: #f0f4f8; }
section[data-testid="stSidebar"] .stRadio label {
    font-size: 0.87rem !important;
}
.sidebar-brand {
    font-size: 1.1rem;
    font-weight: 800;
    color: #1e3a5f;
    padding: 0.3rem 0 0.6rem;
    letter-spacing: 0.3px;
}
.sidebar-section-label {
    font-size: 0.70rem;
    font-weight: 700;
    color: #9ca3af;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 8px 0 2px;
}
</style>
""", unsafe_allow_html=True)

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1>🛒 Supermarket Sales Analysis Dashboard</h1>
  <p>Interactive exploration of sales, products, branches, customers and ratings.</p>
  <span class="badge">📂 supermarket_cleaned_500.csv</span>
  <span class="badge" style="margin-left:6px;">🐍 Streamlit · Pandas · Plotly</span>
</div>
""", unsafe_allow_html=True)

# ── Load dataset ─────────────────────────────────────────────────────────────
CSV_FILE = "supermarket_cleaned_500.csv"

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df

try:
    df = load_data(CSV_FILE)
except FileNotFoundError:
    st.error(f"Dataset file **{CSV_FILE}** not found. Please place it in the same folder as app.py.")
    st.stop()

# ── Data Cleaning ─────────────────────────────────────────────────────────────
@st.cache_data
def clean_data(raw: pd.DataFrame):
    """
    Performs all cleaning steps and returns (cleaned_df, report_dict).
    The report tracks every change made so the UI can display a full audit log.
    """
    df = raw.copy()
    report = []
    rows_before = len(df)

    # 1. Correct data types ────────────────────────────────────────────────────
    # date → datetime (already done in load_data, but guard here too)
    if not pd.api.types.is_datetime64_any_dtype(df["date"]):
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        report.append("🗓️ **date**: converted to datetime.")

    # time → string (kept as HH:MM text — no conversion needed)

    # Ensure numeric columns are actually numeric
    numeric_cols = ["unit_price", "quantity", "tax_5pct", "total",
                    "cogs", "gross_margin_percentage", "gross_income", "rating"]
    for col in numeric_cols:
        if col in df.columns:
            before = df[col].dtype
            df[col] = pd.to_numeric(df[col], errors="coerce")
            if str(before) != str(df[col].dtype):
                report.append(f"🔢 **{col}**: coerced to numeric (was `{before}`).")

    # Ensure categorical columns are strings
    cat_cols = ["invoice_id", "branch", "city", "customer_type",
                "gender", "product_line", "payment", "time"]
    for col in cat_cols:
        if col in df.columns and df[col].dtype != object:
            df[col] = df[col].astype(str)
            report.append(f"🔤 **{col}**: cast to string.")

    # 2. Missing value handling ────────────────────────────────────────────────
    missing_before = df.isnull().sum()

    # Critical columns — drop rows where these are null
    critical = ["invoice_id", "branch", "city", "date",
                "unit_price", "quantity", "product_line", "payment"]
    for col in critical:
        if col in df.columns:
            n_null = df[col].isnull().sum()
            if n_null > 0:
                df = df.dropna(subset=[col])
                report.append(f"🗑️ **{col}**: dropped {n_null} row(s) with missing values (critical column).")

    # Non-critical numeric columns — fill with median
    fill_median = ["unit_price", "quantity", "tax_5pct",
                   "total", "cogs", "gross_income", "rating"]
    for col in fill_median:
        if col in df.columns:
            n_null = df[col].isnull().sum()
            if n_null > 0:
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                report.append(f"🔧 **{col}**: filled {n_null} missing value(s) with median ({median_val:.4f}).")

    # Non-critical categorical columns — fill with mode
    fill_mode_cols = ["customer_type", "gender"]
    for col in fill_mode_cols:
        if col in df.columns:
            n_null = df[col].isnull().sum()
            if n_null > 0:
                mode_val = df[col].mode()[0]
                df[col] = df[col].fillna(mode_val)
                report.append(f"🔧 **{col}**: filled {n_null} missing value(s) with mode ('{mode_val}').")

    total_filled = missing_before.sum() - df.isnull().sum().sum()
    if total_filled == 0 and df.isnull().sum().sum() == 0:
        report.append("✅ **Missing values**: none found — no imputation needed.")

    # 3. Duplicate removal ─────────────────────────────────────────────────────
    n_dupes = df.duplicated().sum()
    if n_dupes > 0:
        df = df.drop_duplicates()
        report.append(f"🗑️ **Duplicates**: removed {n_dupes} fully duplicate row(s).")
    else:
        report.append("✅ **Duplicates**: no duplicate rows found.")

    # Also deduplicate on invoice_id (keep first occurrence)
    n_inv_dupes = df.duplicated(subset=["invoice_id"]).sum()
    if n_inv_dupes > 0:
        df = df.drop_duplicates(subset=["invoice_id"], keep="first")
        report.append(f"🗑️ **invoice_id**: removed {n_inv_dupes} duplicate transaction(s).")
    else:
        report.append("✅ **invoice_id**: all transaction IDs are unique.")

    # 4. Numeric validation ────────────────────────────────────────────────────
    # unit_price must be > 0
    if "unit_price" in df.columns:
        invalid = (df["unit_price"] <= 0).sum()
        if invalid > 0:
            df = df[df["unit_price"] > 0]
            report.append(f"🗑️ **unit_price**: removed {invalid} row(s) with price ≤ 0.")
        else:
            report.append("✅ **unit_price**: all values are positive.")

    # quantity must be >= 1 (integer-like)
    if "quantity" in df.columns:
        invalid = (df["quantity"] < 1).sum()
        if invalid > 0:
            df = df[df["quantity"] >= 1]
            report.append(f"🗑️ **quantity**: removed {invalid} row(s) with quantity < 1.")
        else:
            report.append("✅ **quantity**: all values are ≥ 1.")

    # rating must be in [1, 10]
    if "rating" in df.columns:
        invalid = (~df["rating"].between(1, 10)).sum()
        if invalid > 0:
            df = df[df["rating"].between(1, 10)]
            report.append(f"🗑️ **rating**: removed {invalid} row(s) with rating outside [1, 10].")
        else:
            report.append("✅ **rating**: all values are within [1, 10].")

    # total must be > 0
    if "total" in df.columns:
        invalid = (df["total"] <= 0).sum()
        if invalid > 0:
            df = df[df["total"] > 0]
            report.append(f"🗑️ **total**: removed {invalid} row(s) with total ≤ 0.")
        else:
            report.append("✅ **total**: all values are positive.")

    # 5. Calculate Sales column if missing ────────────────────────────────────
    if "sales" not in df.columns:
        if "unit_price" in df.columns and "quantity" in df.columns:
            df["sales"] = df["unit_price"] * df["quantity"]
            report.append("➕ **sales**: calculated as `unit_price × quantity` (column did not exist).")
    else:
        report.append("✅ **sales**: column already present.")

    rows_after = len(df)
    return df, report, rows_before, rows_after

df_clean, clean_report, rows_before, rows_after = clean_data(df)

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.markdown(
    '<div class="sidebar-brand">🛒 Sales Dashboard</div>', unsafe_allow_html=True
)
st.sidebar.markdown(
    '<div class="sidebar-section-label">📌 Navigation</div>', unsafe_allow_html=True
)
section = st.sidebar.radio(
    "",
    [
        "📊 Dashboard",
        "📋 Dataset Preview",
        "ℹ️ Dataset Information",
        "🔍 Missing Values",
        "🔄 Duplicate Rows",
        "🧹 Data Cleaning",
        "── Analysis ──",
        "🔎 Live Analysis",
        "💡 Business Insights",
        "🛍️ Product Sales Analysis",
        "🏪 Branch / Store Analysis",
        "🗂️ Category Sales Analysis",
        "💳 Payment Method Analysis",
        "👤 Customer Type Analysis",
        "⚥ Gender Analysis",
        "⭐ Customer Rating Analysis",
    ],
    label_visibility="collapsed",
)
# Strip emoji prefix to get the plain section key used in elif blocks
_section_map = {
    "📊 Dashboard":               "Dashboard",
    "📋 Dataset Preview":         "Dataset Preview",
    "ℹ️ Dataset Information":     "Dataset Information",
    "🔍 Missing Values":          "Missing Values",
    "🔄 Duplicate Rows":          "Duplicate Rows",
    "🧹 Data Cleaning":           "Data Cleaning",
    "── Analysis ──":             "── Analysis ──",
    "🔎 Live Analysis":           "Live Analysis",
    "💡 Business Insights":       "Business Insights",
    "🛍️ Product Sales Analysis":  "Product Sales Analysis",
    "🏪 Branch / Store Analysis": "Branch / Store Analysis",
    "🗂️ Category Sales Analysis": "Category Sales Analysis",
    "💳 Payment Method Analysis": "Payment Method Analysis",
    "👤 Customer Type Analysis":  "Customer Type Analysis",
    "⚥ Gender Analysis":          "Gender Analysis",
    "⭐ Customer Rating Analysis": "Customer Rating Analysis",
}
section = _section_map.get(section, section)

st.sidebar.markdown("---")
st.sidebar.markdown(
    '<div class="sidebar-section-label">🔽 Filters</div>', unsafe_allow_html=True
)

# ── Sidebar Filters ───────────────────────────────────────────────────────────
all_branches = sorted(df_clean["branch"].unique().tolist())
sel_branch = st.sidebar.multiselect("Branch", all_branches, default=all_branches, key="f_branch")

all_cities = sorted(df_clean["city"].unique().tolist())
sel_city = st.sidebar.multiselect("City", all_cities, default=all_cities, key="f_city")

all_products = sorted(df_clean["product_line"].unique().tolist())
sel_product = st.sidebar.multiselect("Product / Category", all_products, default=all_products, key="f_product")

all_ctypes = sorted(df_clean["customer_type"].unique().tolist())
sel_ctype = st.sidebar.multiselect("Customer Type", all_ctypes, default=all_ctypes, key="f_ctype")

all_genders = sorted(df_clean["gender"].unique().tolist())
sel_gender = st.sidebar.multiselect("Gender", all_genders, default=all_genders, key="f_gender")

all_payments = sorted(df_clean["payment"].unique().tolist())
sel_payment = st.sidebar.multiselect("Payment Method", all_payments, default=all_payments, key="f_payment")

date_min = df_clean["date"].min().date()
date_max = df_clean["date"].max().date()
sel_dates = st.sidebar.date_input(
    "Date Range",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max,
    key="f_dates",
)
if st.sidebar.button("↺ Reset All Filters", key="reset_filters", use_container_width=True):
    for k in ["f_branch", "f_city", "f_product", "f_ctype", "f_gender", "f_payment", "f_dates"]:
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()

# Guard: if a multiselect is cleared entirely, fall back to all values
if not sel_branch:   sel_branch   = all_branches
if not sel_city:     sel_city     = all_cities
if not sel_product:  sel_product  = all_products
if not sel_ctype:    sel_ctype    = all_ctypes
if not sel_gender:   sel_gender   = all_genders
if not sel_payment:  sel_payment  = all_payments

# Resolve date range (handles single-date edge case)
if isinstance(sel_dates, (list, tuple)) and len(sel_dates) == 2:
    d_start, d_end = pd.Timestamp(sel_dates[0]), pd.Timestamp(sel_dates[1])
else:
    d_start = d_end = pd.Timestamp(sel_dates[0] if isinstance(sel_dates, (list, tuple)) else sel_dates)

# ── Apply filters to produce df_filtered ─────────────────────────────────────
df_filtered = df_clean[
    df_clean["branch"].isin(sel_branch) &
    df_clean["city"].isin(sel_city) &
    df_clean["product_line"].isin(sel_product) &
    df_clean["customer_type"].isin(sel_ctype) &
    df_clean["gender"].isin(sel_gender) &
    df_clean["payment"].isin(sel_payment) &
    (df_clean["date"] >= d_start) &
    (df_clean["date"] <= d_end)
].copy()

# ── Filter status ─────────────────────────────────────────────────────────────
_filters_active = len(df_filtered) != len(df_clean)
st.sidebar.markdown("---")
if _filters_active:
    st.sidebar.success(f"✅ {len(df_filtered):,} / {len(df_clean):,} rows match filters")
else:
    st.sidebar.info(f"📦 Showing all {len(df_clean):,} rows")

if df_filtered.empty:
    st.warning("⚠️ No data matches the current filters. Adjust the sidebar filters.")
    st.stop()

# ── Reusable section header helper ───────────────────────────────────────────
def section_header(icon, title, subtitle=""):
    st.markdown(
        f'<div class="section-header"><h2>{icon} {title}</h2>'
        f'{"<p>" + subtitle + "</p>" if subtitle else ""}</div>',
        unsafe_allow_html=True,
    )

# ── Filter status banner (shown on every section) ────────────────────────────
def filter_banner():
    if _filters_active:
        st.info(
            f"🔽 Filters active — **{len(df_filtered):,}** of {len(df_clean):,} "
            f"transactions · {df_filtered['date'].min().date()} to "
            f"{df_filtered['date'].max().date()}"
        )
    else:
        st.caption(
            f"Showing all {len(df_filtered):,} transactions · "
            f"{df_filtered['date'].min().date()} to {df_filtered['date'].max().date()}"
        )

# ══════════════════════════════════════════════════════════════════════════════
# 1. DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
if section == "Dashboard":
    section_header("📊", "Dashboard", "Key Performance Indicators — updated by sidebar filters")
    filter_banner()
    st.markdown("---")

    # ── Compute KPIs from the cleaned dataset ────────────────────────────────
    total_sales          = df_filtered["sales"].sum()
    total_transactions   = len(df_filtered)
    total_quantity       = df_filtered["quantity"].sum()
    avg_transaction_val  = df_filtered["total"].mean()       # total includes tax
    avg_rating           = df_filtered["rating"].mean()

    # ── KPI cards ─────────────────────────────────────────────────────────────
    k1, k2, k3, k4, k5 = st.columns(5)

    k1.metric(
        label="💰 Total Sales",
        value=f"${total_sales:,.2f}",
        help="Sum of unit_price × quantity across all transactions (excl. tax)"
    )
    k2.metric(
        label="🧾 Total Transactions",
        value=f"{total_transactions:,}",
        help="Number of unique invoice records in the cleaned dataset"
    )
    k3.metric(
        label="📦 Total Quantity Sold",
        value=f"{int(total_quantity):,}",
        help="Total number of individual items sold"
    )
    k4.metric(
        label="💳 Avg Transaction Value",
        value=f"${avg_transaction_val:,.2f}",
        help="Average of the 'total' column (cogs + 5% tax) per transaction"
    )
    k5.metric(
        label="⭐ Avg Customer Rating",
        value=f"{avg_rating:.2f} / 10",
        help="Average customer satisfaction rating (scale 1–10)"
    )

    st.markdown("---")

    # ── Secondary KPIs ────────────────────────────────────────────────────────
    st.markdown("### Additional Metrics")
    s1, s2, s3, s4 = st.columns(4)

    total_tax          = df_filtered["tax_5pct"].sum()
    total_gross_income = df_filtered["gross_income"].sum()
    avg_unit_price     = df_filtered["unit_price"].mean()
    avg_qty_per_txn    = df_filtered["quantity"].mean()

    s1.metric(
        label="🏷️ Total Tax Collected (5%)",
        value=f"${total_tax:,.2f}",
        help="Sum of the tax_5pct column"
    )
    s2.metric(
        label="📈 Total Gross Income",
        value=f"${total_gross_income:,.2f}",
        help="Sum of gross_income (equals total tax at 4.76% margin)"
    )
    s3.metric(
        label="🔖 Avg Unit Price",
        value=f"${avg_unit_price:,.2f}",
        help="Average price per individual product unit"
    )
    s4.metric(
        label="🛒 Avg Items per Transaction",
        value=f"{avg_qty_per_txn:.2f}",
        help="Average number of items bought per visit"
    )

    st.markdown("---")

    # ── Breakdown by Branch ───────────────────────────────────────────────────
    st.markdown("### KPIs by Branch")
    branch_kpi = (
        df_filtered.groupby("branch")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Total_Revenue=("total", "sum"),
            Avg_Rating=("rating", "mean"),
            Total_Qty=("quantity", "sum"),
        )
        .round(2)
        .reset_index()
    )
    branch_kpi.columns = ["Branch", "Transactions", "Total Sales ($)",
                          "Total Revenue incl. Tax ($)", "Avg Rating", "Total Qty Sold"]
    st.dataframe(branch_kpi, use_container_width=True)

    # ── Breakdown by Product Line ─────────────────────────────────────────────
    st.markdown("### KPIs by Product Line")
    product_kpi = (
        df_filtered.groupby("product_line")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Avg_Rating=("rating", "mean"),
            Total_Qty=("quantity", "sum"),
        )
        .round(2)
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )
    product_kpi.columns = ["Product Line", "Transactions", "Total Sales ($)",
                           "Avg Rating", "Total Qty Sold"]
    st.dataframe(product_kpi, use_container_width=True)

    # ── Breakdown by Payment Method ───────────────────────────────────────────
    st.markdown("### KPIs by Payment Method")
    payment_kpi = (
        df_filtered.groupby("payment")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Avg_Transaction=("total", "mean"),
        )
        .round(2)
        .reset_index()
        .sort_values("Transactions", ascending=False)
    )
    payment_kpi.columns = ["Payment Method", "Transactions",
                           "Total Sales ($)", "Avg Transaction Value ($)"]
    st.dataframe(payment_kpi, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 2. DATASET PREVIEW
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Dataset Preview":
    section_header("📋", "Dataset Preview", "Browse the raw cleaned dataset")
    filter_banner()

    total_rows, total_cols = df.shape
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", total_rows)
    col2.metric("Total Columns", total_cols)
    col3.metric("Date Range", f"{df['date'].min().date()} → {df['date'].max().date()}")

    st.markdown("### First N Rows")
    n = st.slider("Number of rows to display", min_value=5, max_value=50, value=10, step=5)
    st.dataframe(df.head(n), use_container_width=True)

    st.markdown("### Last N Rows")
    st.dataframe(df.tail(n), use_container_width=True)

    st.markdown("### Column Names")
    st.write(list(df.columns))

# ══════════════════════════════════════════════════════════════════════════════
# 3. DATASET INFORMATION
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Dataset Information":
    section_header("ℹ️", "Dataset Information", "Column types, statistics and unique values")
    filter_banner()

    # Data types
    st.markdown("### Column Data Types")
    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.values.astype(str),
        "Non-Null Count": df.notnull().sum().values,
        "Null Count": df.isnull().sum().values,
        "Unique Values": [df[c].nunique() for c in df.columns],
    })
    st.dataframe(dtype_df, use_container_width=True)

    # Numerical statistics
    st.markdown("### Basic Statistics — Numerical Columns")
    num_cols = df.select_dtypes(include="number").columns.tolist()
    st.dataframe(df[num_cols].describe().T.round(4), use_container_width=True)

    # Categorical overview
    st.markdown("### Categorical Columns — Unique Values")
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    for col in cat_cols:
        unique_vals = df[col].unique().tolist()
        st.write(f"**{col}** ({len(unique_vals)} unique): {unique_vals}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. MISSING VALUES
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Missing Values":
    section_header("🔍", "Missing Value Analysis", "Per-column null counts and percentages")
    filter_banner()

    missing_counts = df.isnull().sum()
    missing_pct = (missing_counts / len(df) * 100).round(2)

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": missing_counts.values,
        "Missing %": missing_pct.values,
    })

    total_missing = missing_counts.sum()

    if total_missing == 0:
        st.success("✅ No missing values found in the dataset. All columns are complete.")
    else:
        st.warning(f"⚠️ {total_missing} missing value(s) detected across the dataset.")

    st.markdown("### Missing Values per Column")
    st.dataframe(missing_df, use_container_width=True)

    # Highlight columns with missing data
    cols_with_missing = missing_df[missing_df["Missing Count"] > 0]
    if not cols_with_missing.empty:
        st.markdown("### Columns with Missing Data")
        st.dataframe(cols_with_missing, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 5. DUPLICATE ROWS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Duplicate Rows":
    section_header("🔄", "Duplicate Row Analysis", "Full-row and invoice-ID duplicate checks")
    filter_banner()

    duplicate_rows = df[df.duplicated()]
    duplicate_count = len(duplicate_rows)

    col1, col2 = st.columns(2)
    col1.metric("Total Rows", len(df))
    col2.metric("Duplicate Rows", duplicate_count)

    if duplicate_count == 0:
        st.success("✅ No duplicate rows found. Every row in the dataset is unique.")
    else:
        st.warning(f"⚠️ {duplicate_count} duplicate row(s) found.")
        st.markdown("### Duplicate Rows")
        st.dataframe(duplicate_rows, use_container_width=True)

    # Also check invoice_id uniqueness specifically
    st.markdown("### Invoice ID Uniqueness")
    invoice_dupes = df["invoice_id"].duplicated().sum()
    if invoice_dupes == 0:
        st.success("✅ All `invoice_id` values are unique — no duplicate transactions.")
    else:
        st.error(f"❌ {invoice_dupes} duplicate `invoice_id` values detected.")
        dup_invoices = df[df["invoice_id"].duplicated(keep=False)].sort_values("invoice_id")
        st.dataframe(dup_invoices, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 6. DATA CLEANING
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Data Cleaning":
    section_header("🧹", "Data Cleaning", "Steps taken to prepare the dataset")

    # ── Row count summary ──────────────────────────────────────────────────────
    st.markdown("### Rows Before vs After Cleaning")
    rows_removed = rows_before - rows_after
    c1, c2, c3 = st.columns(3)
    c1.metric("Rows Before Cleaning", rows_before)
    c2.metric("Rows After Cleaning", rows_after)
    c3.metric(
        "Rows Removed",
        rows_removed,
        delta=f"-{rows_removed}" if rows_removed > 0 else "0",
        delta_color="inverse",
    )

    if rows_removed == 0:
        st.success("✅ All rows retained — no records were removed during cleaning.")
    else:
        st.warning(f"⚠️ {rows_removed} row(s) were removed during cleaning.")

    st.markdown("---")

    # ── Cleaning audit log ─────────────────────────────────────────────────────
    st.markdown("### Cleaning Audit Log")
    st.caption("Each step performed during data cleaning is listed below.")
    for step in clean_report:
        st.markdown(f"- {step}")

    st.markdown("---")

    # ── Data type comparison ───────────────────────────────────────────────────
    st.markdown("### Data Types: Before vs After")
    dtype_before = df.dtypes.rename("Before")
    dtype_after  = df_clean.dtypes.rename("After")
    dtype_compare = pd.concat([dtype_before, dtype_after], axis=1).astype(str)
    dtype_compare["Changed"] = dtype_compare["Before"] != dtype_compare["After"]
    st.dataframe(dtype_compare, use_container_width=True)

    st.markdown("---")

    # ── Missing values: before vs after ────────────────────────────────────────
    st.markdown("### Missing Values: Before vs After")
    miss_before = df.isnull().sum().rename("Before")
    miss_after  = df_clean.isnull().sum().rename("After")
    miss_compare = pd.concat([miss_before, miss_after], axis=1)
    miss_compare["Resolved"] = miss_before - miss_after
    st.dataframe(miss_compare, use_container_width=True)

    total_remaining = df_clean.isnull().sum().sum()
    if total_remaining == 0:
        st.success("✅ Zero missing values remain after cleaning.")
    else:
        st.warning(f"⚠️ {total_remaining} missing value(s) still remain.")

    st.markdown("---")

    # ── Sales column confirmation ──────────────────────────────────────────────
    st.markdown("### Sales Column")
    if "sales" in df_clean.columns:
        st.success("✅ `sales` column is present in the cleaned dataset.")
        st.markdown(
            "**Formula used:** `sales = unit_price × quantity`  \n"
            "This equals the `cogs` (cost of goods sold) column."
        )
        st.dataframe(
            df_clean[["invoice_id", "unit_price", "quantity", "sales", "cogs"]]
            .head(10),
            use_container_width=True,
        )
    else:
        st.error("❌ `sales` column could not be created.")

    st.markdown("---")

    # ── Cleaned dataset preview ────────────────────────────────────────────────
    st.markdown("### Cleaned Dataset Preview")
    st.dataframe(df_clean.head(20), use_container_width=True)

    st.markdown("### Cleaned Dataset — Shape")
    st.write(f"**{df_clean.shape[0]} rows × {df_clean.shape[1]} columns**")

# ══════════════════════════════════════════════════════════════════════════════
# 7. LIVE ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Live Analysis":
    section_header("🔎", "Live Analysis", "Six key questions answered from the filtered data")
    filter_banner()
    if _filters_active:
        st.info(
            f"🔽 Filters active — showing **{len(df_filtered):,}** of "
            f"{len(df_clean):,} transactions."
        )
    else:
        st.caption(f"Showing all {len(df_filtered):,} transactions.")
    st.markdown("---")

    # ── Pre-compute all answers ───────────────────────────────────────────────
    # Q1 — Highest-sales product line
    q1 = df_filtered.groupby("product_line")["sales"].sum()
    q1_name  = q1.idxmax()
    q1_value = q1.max()
    q1_share = q1_value / q1.sum() * 100

    # Q2 — Highest-sales branch
    q2 = df_filtered.groupby("branch")["sales"].sum()
    q2_branch = q2.idxmax()
    q2_city   = df_filtered.loc[df_filtered["branch"] == q2_branch, "city"].iloc[0]
    q2_value  = q2.max()
    q2_share  = q2_value / q2.sum() * 100

    # Q3 — Highest-sales category (same as product_line in this dataset)
    q3 = df_filtered.groupby("product_line")["sales"].sum().reset_index()
    q3 = q3.sort_values("sales", ascending=False)
    q3_name  = q3.iloc[0]["product_line"]
    q3_value = q3.iloc[0]["sales"]
    q3_qty   = df_filtered.loc[df_filtered["product_line"] == q3_name, "quantity"].sum()

    # Q4 — Most-used payment method
    q4 = df_filtered["payment"].value_counts()
    q4_method = q4.idxmax()
    q4_count  = q4.max()
    q4_share  = q4_count / q4.sum() * 100

    # Q5 — Customer type with higher avg transaction value
    q5 = df_filtered.groupby("customer_type")["total"].mean()
    q5_type   = q5.idxmax()
    q5_val    = q5.max()
    q5_other  = q5.drop(q5_type)
    q5_diff   = q5_val - q5_other.values[0] if len(q5_other) > 0 else 0

    # Q6 — Average customer rating
    q6_avg    = df_filtered["rating"].mean()
    q6_med    = df_filtered["rating"].median()
    q6_min    = df_filtered["rating"].min()
    q6_max    = df_filtered["rating"].max()
    q6_best_branch = (
        df_filtered.groupby("branch")["rating"].mean()
        .round(2).idxmax()
    )
    q6_best_branch_val = df_filtered.groupby("branch")["rating"].mean().max()

    # ── Display answer cards ─────────────────────────────────────────────────
    CARD = """
    <div style="background:#f7f8fa;border:1px solid #e5e7eb;border-radius:10px;
                padding:18px 22px;margin-bottom:16px;">
      <div style="font-size:13px;color:#57606a;margin-bottom:4px;">{label}</div>
      <div style="font-size:22px;font-weight:700;color:#1f2328;">{answer}</div>
      <div style="font-size:13px;color:#57606a;margin-top:6px;">{detail}</div>
    </div>
    """

    q_labels = [
        ("Q1", "Which product line has the highest sales?",
         f"<b>{q1_name}</b>",
         f"Total sales: <b>${q1_value:,.2f}</b> &nbsp;·&nbsp; "
         f"{q1_share:.1f}% of filtered sales"),

        ("Q2", "Which branch has the highest sales?",
         f"<b>Branch {q2_branch}</b> &nbsp;({q2_city})",
         f"Total sales: <b>${q2_value:,.2f}</b> &nbsp;·&nbsp; "
         f"{q2_share:.1f}% of filtered sales"),

        ("Q3", "Which category has the highest sales?",
         f"<b>{q3_name}</b>",
         f"Total sales: <b>${q3_value:,.2f}</b> &nbsp;·&nbsp; "
         f"{int(q3_qty):,} units sold"),

        ("Q4", "Which payment method is used most?",
         f"<b>{q4_method}</b>",
         f"Used in <b>{q4_count:,}</b> transactions "
         f"({q4_share:.1f}% of filtered transactions)"),

        ("Q5", "Which customer type has the higher avg transaction value?",
         f"<b>{q5_type}</b>",
         f"Avg transaction: <b>${q5_val:,.2f}</b> &nbsp;·&nbsp; "
         f"${abs(q5_diff):,.2f} more than the other type"),

        ("Q6", "What is the average customer rating?",
         f"<b>{q6_avg:.2f} / 10</b>",
         f"Median: {q6_med:.2f} &nbsp;·&nbsp; Range: {q6_min:.1f}–{q6_max:.1f} &nbsp;·&nbsp; "
         f"Best branch: <b>{q6_best_branch}</b> ({q6_best_branch_val:.2f})"),
    ]

    for q_num, label, answer, detail in q_labels:
        left, right = st.columns([1, 11])
        with left:
            st.markdown(
                f"<div style='background:#3b82d4;color:#fff;border-radius:8px;"
                f"text-align:center;padding:10px 0;font-weight:700;font-size:15px;"
                f"margin-top:4px'>{q_num}</div>",
                unsafe_allow_html=True,
            )
        with right:
            st.markdown(
                CARD.format(label=label, answer=answer, detail=detail),
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # ── Summary table ────────────────────────────────────────────────────────
    st.markdown("### Summary Table")
    summary = pd.DataFrame([
        {"Question": "Highest-sales product line",       "Answer": q1_name,   "Value": f"${q1_value:,.2f}"},
        {"Question": "Highest-sales branch",             "Answer": f"Branch {q2_branch} ({q2_city})",  "Value": f"${q2_value:,.2f}"},
        {"Question": "Highest-sales category",           "Answer": q3_name,   "Value": f"${q3_value:,.2f}"},
        {"Question": "Most-used payment method",         "Answer": q4_method, "Value": f"{q4_count:,} transactions"},
        {"Question": "Highest avg txn customer type",    "Answer": q5_type,   "Value": f"${q5_val:,.2f} avg"},
        {"Question": "Average customer rating",          "Answer": f"{q6_avg:.2f} / 10", "Value": f"Median {q6_med:.2f}"},
    ])
    st.dataframe(summary, use_container_width=True, hide_index=True)

    st.markdown("---")

    # ── Supporting mini-charts ────────────────────────────────────────────────
    st.markdown("### Supporting Charts")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Sales by Product Line**")
        fig_q1 = px.bar(
            q1.sort_values(ascending=False).reset_index().rename(
                columns={"product_line": "Product Line", "sales": "Total Sales ($)"}
            ),
            x="Total Sales ($)", y="Product Line", orientation="h",
            color="Product Line",
            color_discrete_sequence=px.colors.qualitative.Set2,
            text="Total Sales ($)",
        )
        fig_q1.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
        fig_q1.update_layout(showlegend=False,
                             yaxis=dict(categoryorder="total ascending"),
                             margin=dict(l=0, r=40, t=10, b=0))
        st.plotly_chart(fig_q1, use_container_width=True)

    with col2:
        st.markdown("**Sales by Branch**")
        q2_df = df_filtered.groupby(["branch", "city"])["sales"].sum().reset_index().rename(
            columns={"branch": "Branch", "city": "City", "sales": "Total Sales ($)"}
        )
        fig_q2 = px.bar(
            q2_df.sort_values("Total Sales ($)", ascending=False),
            x="Branch", y="Total Sales ($)", color="City",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            text="Total Sales ($)",
        )
        fig_q2.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
        fig_q2.update_layout(showlegend=True,
                             margin=dict(l=0, r=10, t=10, b=0))
        st.plotly_chart(fig_q2, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("**Payment Method Usage**")
        q4_df = q4.reset_index().rename(columns={"payment": "Payment Method", "count": "Transactions"})
        fig_q4 = px.pie(
            q4_df, names="Payment Method", values="Transactions",
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Safe,
        )
        fig_q4.update_traces(textinfo="label+percent+value")
        fig_q4.update_layout(margin=dict(l=0, r=0, t=10, b=0))
        st.plotly_chart(fig_q4, use_container_width=True)

    with col4:
        st.markdown("**Avg Transaction Value by Customer Type**")
        q5_df = df_filtered.groupby("customer_type")["total"].mean().round(2).reset_index().rename(
            columns={"customer_type": "Customer Type", "total": "Avg Transaction ($)"}
        )
        fig_q5 = px.bar(
            q5_df, x="Customer Type", y="Avg Transaction ($)",
            color="Customer Type", text="Avg Transaction ($)",
            color_discrete_sequence=["#636EFA", "#EF553B"],
        )
        fig_q5.update_traces(texttemplate="$%{text:,.2f}", textposition="outside")
        fig_q5.update_layout(showlegend=False,
                             margin=dict(l=0, r=10, t=10, b=0))
        st.plotly_chart(fig_q5, use_container_width=True)

    st.markdown("**Customer Rating Distribution**")
    fig_q6 = px.histogram(
        df_filtered, x="rating", nbins=18,
        color_discrete_sequence=["#19D3F3"],
        labels={"rating": "Customer Rating"},
    )
    fig_q6.add_vline(x=q6_avg, line_dash="dash", line_color="red",
                     annotation_text=f"Mean: {q6_avg:.2f}",
                     annotation_position="top right")
    fig_q6.update_layout(bargap=0.05,
                         xaxis_title="Rating", yaxis_title="Transactions",
                         margin=dict(l=0, r=10, t=10, b=0))
    st.plotly_chart(fig_q6, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 8. BUSINESS INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Business Insights":
    section_header("💡", "Business Insights", "Findings derived from the actual data — no hardcoded values")
    filter_banner()
    if _filters_active:
        st.info(
            f"🔽 Filters active — insights based on **{len(df_filtered):,}** of "
            f"{len(df_clean):,} transactions."
        )
    else:
        st.caption(f"Insights based on all {len(df_filtered):,} transactions.")
    st.markdown("---")

    # ── Pre-compute all values needed for insights ────────────────────────────

    # Product / Category
    prod_sales   = df_filtered.groupby("product_line")["sales"].sum().sort_values(ascending=False)
    top_prod     = prod_sales.index[0]
    bot_prod     = prod_sales.index[-1]
    top_prod_val = prod_sales.iloc[0]
    bot_prod_val = prod_sales.iloc[-1]
    top_prod_share = top_prod_val / prod_sales.sum() * 100

    prod_qty     = df_filtered.groupby("product_line")["quantity"].sum().sort_values(ascending=False)
    top_prod_qty = prod_qty.index[0]

    prod_rating  = df_filtered.groupby("product_line")["rating"].mean().round(2)
    top_rated_prod = prod_rating.idxmax()
    top_rated_prod_val = prod_rating.max()

    # Branch
    branch_sales = df_filtered.groupby("branch")["sales"].sum().sort_values(ascending=False)
    top_branch   = branch_sales.index[0]
    bot_branch   = branch_sales.index[-1]
    top_branch_city = df_filtered.loc[df_filtered["branch"] == top_branch, "city"].iloc[0]
    top_branch_val  = branch_sales.iloc[0]
    branch_gap   = branch_sales.iloc[0] - branch_sales.iloc[-1]

    branch_txn   = df_filtered.groupby("branch")["invoice_id"].count().sort_values(ascending=False)
    top_branch_txn = branch_txn.index[0]

    branch_rating = df_filtered.groupby("branch")["rating"].mean().round(2)
    top_rated_branch     = branch_rating.idxmax()
    top_rated_branch_val = branch_rating.max()
    bot_rated_branch     = branch_rating.idxmin()
    bot_rated_branch_val = branch_rating.min()

    # Payment
    pay_counts  = df_filtered["payment"].value_counts()
    pay_sales   = df_filtered.groupby("payment")["sales"].sum().sort_values(ascending=False)
    top_pay     = pay_counts.idxmax()
    top_pay_cnt = pay_counts.max()
    top_pay_share = top_pay_cnt / pay_counts.sum() * 100
    top_pay_sales = pay_sales.idxmax()
    pay_avg_txn = df_filtered.groupby("payment")["total"].mean().round(2)
    top_pay_avg_txn = pay_avg_txn.idxmax()
    top_pay_avg_val = pay_avg_txn.max()

    # Customer behaviour
    ctype_txn   = df_filtered["customer_type"].value_counts()
    ctype_sales = df_filtered.groupby("customer_type")["sales"].sum()
    ctype_avg   = df_filtered.groupby("customer_type")["total"].mean().round(2)
    ctype_qty   = df_filtered.groupby("customer_type")["quantity"].mean().round(2)
    top_ctype_freq  = ctype_txn.idxmax()
    top_ctype_freq_share = ctype_txn.max() / ctype_txn.sum() * 100
    top_ctype_sales = ctype_sales.idxmax()
    top_ctype_avg   = ctype_avg.idxmax()
    top_ctype_avg_val = ctype_avg.max()
    top_ctype_qty   = ctype_qty.idxmax()

    # Gender
    has_gender  = "gender" in df_filtered.columns
    if has_gender:
        gen_txn   = df_filtered["gender"].value_counts()
        gen_sales = df_filtered.groupby("gender")["sales"].sum()
        top_gen_freq  = gen_txn.idxmax()
        top_gen_freq_share = gen_txn.max() / gen_txn.sum() * 100
        top_gen_sales = gen_sales.idxmax()

    # Rating
    avg_rating   = df_filtered["rating"].mean()
    med_rating   = df_filtered["rating"].median()
    pct_above_7  = (df_filtered["rating"] >= 7).sum() / len(df_filtered) * 100
    pct_below_5  = (df_filtered["rating"] < 5).sum() / len(df_filtered) * 100

    # ── Helper to render an insight card ─────────────────────────────────────
    def insight_card(icon, title, text, tag="positive"):
        colours = {
            "positive": ("#d1fae5", "#065f46", "#059669"),
            "warning":  ("#fef3c7", "#92400e", "#d97706"),
            "neutral":  ("#eff6ff", "#1e40af", "#3b82f6"),
        }
        bg, txt, border = colours.get(tag, colours["neutral"])
        st.markdown(
            f"""<div style="background:{bg};border-left:4px solid {border};
                border-radius:8px;padding:14px 18px;margin-bottom:12px;">
              <span style="font-size:20px;">{icon}</span>
              <span style="font-weight:700;color:{txt};font-size:15px;
                    margin-left:8px;">{title}</span>
              <div style="color:#374151;font-size:14px;margin-top:6px;
                    line-height:1.6;">{text}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    # ── 1. Top Product Insights ───────────────────────────────────────────────
    st.markdown("### 🛍️ Product Insights")

    insight_card("🏆", "Best-selling product line",
        f"<b>{top_prod}</b> leads with <b>${top_prod_val:,.2f}</b> in sales, "
        f"contributing <b>{top_prod_share:.1f}%</b> of total filtered revenue. "
        f"It is followed by {prod_sales.index[1]} and {prod_sales.index[2]}.",
        "positive")

    insight_card("📦", "Highest unit volume",
        f"<b>{top_prod_qty}</b> records the most items sold by quantity, "
        f"making it the most frequently purchased product line.",
        "neutral")

    insight_card("⚠️", "Lowest-revenue product line",
        f"<b>{bot_prod}</b> generates the least revenue at "
        f"<b>${bot_prod_val:,.2f}</b>. "
        f"There may be opportunity to boost promotions or pricing for this line.",
        "warning")

    insight_card("⭐", "Highest-rated product line",
        f"Customers rate <b>{top_rated_prod}</b> highest at an average of "
        f"<b>{top_rated_prod_val:.2f} / 10</b>, indicating strong satisfaction "
        f"in this category.",
        "positive")

    st.markdown("---")

    # ── 2. Branch / Store Insights ────────────────────────────────────────────
    st.markdown("### 🏪 Branch / Store Insights")

    insight_card("🏆", "Top-performing branch",
        f"Branch <b>{top_branch}</b> in <b>{top_branch_city}</b> leads with "
        f"<b>${top_branch_val:,.2f}</b> in sales. "
        f"The gap between the top and bottom branch is "
        f"<b>${branch_gap:,.2f}</b>.",
        "positive")

    insight_card("🧾", "Most transactions",
        f"Branch <b>{top_branch_txn}</b> handles the highest number of "
        f"transactions, indicating the busiest store footfall.",
        "neutral")

    insight_card("⭐", "Highest customer satisfaction branch",
        f"Branch <b>{top_rated_branch}</b> achieves the best average rating of "
        f"<b>{top_rated_branch_val:.2f} / 10</b>. "
        f"Branch <b>{bot_rated_branch}</b> has the lowest at "
        f"<b>{bot_rated_branch_val:.2f} / 10</b> and may benefit from "
        f"service improvement initiatives.",
        "positive" if top_rated_branch_val >= 7 else "warning")

    st.markdown("---")

    # ── 3. Payment Insights ───────────────────────────────────────────────────
    st.markdown("### 💳 Payment Insights")

    insight_card("💳", "Most preferred payment method",
        f"<b>{top_pay}</b> is used in <b>{top_pay_cnt:,}</b> transactions "
        f"({top_pay_share:.1f}% of all filtered transactions), making it the "
        f"dominant payment channel.",
        "positive")

    insight_card("💰", "Payment method with highest total sales",
        f"<b>{top_pay_sales}</b> accounts for the most revenue among all "
        f"payment methods, suggesting high-value purchases are concentrated "
        f"through this channel.",
        "neutral")

    insight_card("🔝", "Highest average transaction by payment",
        f"Customers using <b>{top_pay_avg_txn}</b> spend an average of "
        f"<b>${top_pay_avg_val:,.2f}</b> per transaction — the highest across "
        f"all payment methods.",
        "neutral")

    st.markdown("---")

    # ── 4. Customer Behaviour Insights ───────────────────────────────────────
    st.markdown("### 👤 Customer Behaviour Insights")

    insight_card("👥", "Most frequent customer type",
        f"<b>{top_ctype_freq}</b> customers account for "
        f"<b>{top_ctype_freq_share:.1f}%</b> of all filtered transactions. "
        f"<b>{top_ctype_sales}</b> customers contribute the most to total sales.",
        "positive")

    insight_card("💵", "Higher spending customer type",
        f"<b>{top_ctype_avg}</b> customers have the higher average transaction "
        f"value at <b>${top_ctype_avg_val:,.2f}</b> per visit, making them the "
        f"more valuable segment per transaction.",
        "positive")

    insight_card("🛒", "Items per transaction",
        f"<b>{top_ctype_qty}</b> customers buy more items per transaction on "
        f"average (<b>{ctype_qty.max():.2f}</b> units), suggesting a stronger "
        f"basket-building behaviour.",
        "neutral")

    if has_gender:
        insight_card("⚥", "Gender shopping frequency",
            f"<b>{top_gen_freq}</b> customers make up <b>{top_gen_freq_share:.1f}%</b> "
            f"of transactions. <b>{top_gen_sales}</b> customers generate the "
            f"higher total sales, indicating stronger overall revenue contribution.",
            "neutral")

    st.markdown("---")

    # ── 5. Customer Rating Insights ───────────────────────────────────────────
    st.markdown("### ⭐ Customer Rating Insights")

    rating_tag = "positive" if avg_rating >= 7 else ("warning" if avg_rating >= 5 else "warning")
    insight_card("📊", "Overall customer satisfaction",
        f"The average customer rating is <b>{avg_rating:.2f} / 10</b> "
        f"(median: <b>{med_rating:.2f}</b>). "
        f"<b>{pct_above_7:.1f}%</b> of customers rate their experience "
        f"7 or above, while <b>{pct_below_5:.1f}%</b> rate below 5.",
        rating_tag)

    insight_card("🏆", "Best-rated branch for satisfaction",
        f"Branch <b>{top_rated_branch}</b> earns the highest satisfaction score "
        f"of <b>{top_rated_branch_val:.2f} / 10</b>.",
        "positive")

    insight_card("🛍️", "Best-rated product line for satisfaction",
        f"<b>{top_rated_prod}</b> is the highest-rated product line at "
        f"<b>{top_rated_prod_val:.2f} / 10</b>, suggesting customers are "
        f"most satisfied with purchases in this category.",
        "positive")

    if pct_below_5 > 10:
        insight_card("⚠️", "Low-rating alert",
            f"<b>{pct_below_5:.1f}%</b> of transactions received a rating "
            f"below 5. Investigating common factors in these transactions "
            f"(branch, product line, payment method) could uncover "
            f"improvement areas.",
            "warning")

    st.markdown("---")

    # ── Insight summary table ─────────────────────────────────────────────────
    st.markdown("### 📋 Insight Summary")
    rows = [
        ("Best-selling product line",       top_prod,             f"${top_prod_val:,.2f} sales"),
        ("Lowest-revenue product line",     bot_prod,             f"${bot_prod_val:,.2f} sales"),
        ("Highest-rated product line",      top_rated_prod,       f"{top_rated_prod_val:.2f} / 10"),
        ("Top branch",                      f"Branch {top_branch} ({top_branch_city})", f"${top_branch_val:,.2f} sales"),
        ("Highest-rated branch",            f"Branch {top_rated_branch}", f"{top_rated_branch_val:.2f} / 10"),
        ("Most-used payment method",        top_pay,              f"{top_pay_cnt:,} transactions"),
        ("Highest avg spend payment",       top_pay_avg_txn,      f"${top_pay_avg_val:,.2f} avg"),
        ("Most frequent customer type",     top_ctype_freq,       f"{top_ctype_freq_share:.1f}% of txns"),
        ("Higher avg spend customer type",  top_ctype_avg,        f"${top_ctype_avg_val:,.2f} avg"),
        ("Average customer rating",         f"{avg_rating:.2f} / 10", f"{pct_above_7:.1f}% rated ≥ 7"),
    ]
    if has_gender:
        rows.insert(8, ("Most frequent gender", top_gen_freq, f"{top_gen_freq_share:.1f}% of txns"))
    ins_df = pd.DataFrame(rows, columns=["Insight", "Finding", "Supporting Value"])
    st.dataframe(ins_df, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# SEPARATOR — not a real section, just a visual divider in the sidebar
# ══════════════════════════════════════════════════════════════════════════════
elif section == "── Analysis ──":
    st.info("👈 Select an analysis from the sidebar.")

# ══════════════════════════════════════════════════════════════════════════════
# 7. PRODUCT SALES ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Product Sales Analysis":
    section_header("🛍️", "Product Sales Analysis", "Sales performance by product line")
    filter_banner()
    st.markdown("---")

    prod = (
        df_filtered.groupby("product_line")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Total_Revenue=("total", "sum"),
            Total_Qty=("quantity", "sum"),
            Avg_Unit_Price=("unit_price", "mean"),
            Avg_Transaction=("total", "mean"),
        )
        .round(2)
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
        .rename(columns={
            "product_line": "Product Line",
            "Transactions": "Transactions",
            "Total_Sales": "Total Sales ($)",
            "Total_Revenue": "Total Revenue ($)",
            "Total_Qty": "Qty Sold",
            "Avg_Unit_Price": "Avg Unit Price ($)",
            "Avg_Transaction": "Avg Transaction ($)",
        })
    )

    top_product = prod.iloc[0]["Product Line"]
    top_sales   = prod.iloc[0]["Total Sales ($)"]

    c1, c2 = st.columns(2)
    c1.metric("Best-Selling Product Line", top_product)
    c2.metric("Its Total Sales", f"${top_sales:,.2f}")

    st.markdown("### Product Line Summary Table")
    st.dataframe(prod, use_container_width=True)

    st.markdown("### Total Sales by Product Line")
    fig1 = px.bar(
        prod,
        x="Product Line", y="Total Sales ($)",
        color="Product Line",
        text="Total Sales ($)",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig1.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
    fig1.update_layout(showlegend=False, xaxis_title="", yaxis_title="Total Sales ($)")
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### Quantity Sold by Product Line")
    fig2 = px.pie(
        prod, names="Product Line", values="Qty Sold",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4,
    )
    fig2.update_traces(textinfo="label+percent")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Transactions vs Avg Transaction Value")
    fig3 = px.scatter(
        prod,
        x="Transactions", y="Avg Transaction ($)",
        size="Total Sales ($)", color="Product Line",
        text="Product Line",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig3.update_traces(textposition="top center")
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 8. BRANCH / STORE ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Branch / Store Analysis":
    section_header("🏪", "Branch / Store Analysis", "Performance comparison across branches")
    filter_banner()
    st.markdown("---")

    branch = (
        df_filtered.groupby(["branch", "city"])
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Total_Revenue=("total", "sum"),
            Total_Qty=("quantity", "sum"),
            Avg_Rating=("rating", "mean"),
            Avg_Transaction=("total", "mean"),
        )
        .round(2)
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
        .rename(columns={
            "branch": "Branch", "city": "City",
            "Transactions": "Transactions",
            "Total_Sales": "Total Sales ($)",
            "Total_Revenue": "Total Revenue ($)",
            "Total_Qty": "Qty Sold",
            "Avg_Rating": "Avg Rating",
            "Avg_Transaction": "Avg Transaction ($)",
        })
    )

    top_branch = branch.iloc[0]["Branch"]
    top_city   = branch.iloc[0]["City"]
    top_bs     = branch.iloc[0]["Total Sales ($)"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Top Branch", f"Branch {top_branch} — {top_city}")
    c2.metric("Its Total Sales", f"${top_bs:,.2f}")
    c3.metric("Its Avg Rating", f"{branch.iloc[0]['Avg Rating']:.2f} / 10")

    st.markdown("### Branch Summary Table")
    st.dataframe(branch, use_container_width=True)

    st.markdown("### Total Sales by Branch")
    fig1 = px.bar(
        branch,
        x="Branch", y="Total Sales ($)",
        color="City", text="Total Sales ($)",
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig1.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
    fig1.update_layout(xaxis_title="Branch", yaxis_title="Total Sales ($)")
    st.plotly_chart(fig1, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Transactions by Branch")
        fig2 = px.pie(
            branch, names="Branch", values="Transactions",
            color_discrete_sequence=px.colors.qualitative.Pastel, hole=0.4,
        )
        fig2.update_traces(textinfo="label+percent+value")
        st.plotly_chart(fig2, use_container_width=True)

    with col_b:
        st.markdown("### Avg Rating by Branch")
        fig3 = px.bar(
            branch, x="Branch", y="Avg Rating",
            color="City", text="Avg Rating",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        fig3.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig3.update_layout(yaxis=dict(range=[0, 10]), xaxis_title="", showlegend=False)
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("### Monthly Sales Trend by Branch")
    monthly_branch = (
        df_filtered.assign(Month=df_filtered["date"].dt.to_period("M").astype(str))
        .groupby(["Month", "branch"])["sales"].sum()
        .reset_index()
        .rename(columns={"branch": "Branch", "sales": "Total Sales ($)"})
    )
    fig4 = px.line(
        monthly_branch, x="Month", y="Total Sales ($)", color="Branch",
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    st.plotly_chart(fig4, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 9. CATEGORY SALES ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Category Sales Analysis":
    section_header("🗂️", "Category Sales Analysis", "Sales and quantity by product category")
    filter_banner()
    st.markdown("---")

    cat = (
        df_filtered.groupby("product_line")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Total_Qty=("quantity", "sum"),
            Avg_Unit_Price=("unit_price", "mean"),
            Avg_Rating=("rating", "mean"),
        )
        .round(2)
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
        .rename(columns={
            "product_line": "Category",
            "Transactions": "Transactions",
            "Total_Sales": "Total Sales ($)",
            "Total_Qty": "Qty Sold",
            "Avg_Unit_Price": "Avg Unit Price ($)",
            "Avg_Rating": "Avg Rating",
        })
    )

    top_cat     = cat.iloc[0]["Category"]
    top_cat_qty = int(cat.sort_values("Qty Sold", ascending=False).iloc[0]["Qty Sold"])
    top_cat_qty_name = cat.sort_values("Qty Sold", ascending=False).iloc[0]["Category"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Highest Revenue Category", top_cat)
    c2.metric("Highest Volume Category", top_cat_qty_name)
    c3.metric("Its Units Sold", f"{top_cat_qty:,}")

    st.markdown("### Category Summary Table")
    st.dataframe(cat, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Total Sales by Category")
        fig1 = px.bar(
            cat, x="Total Sales ($)", y="Category",
            orientation="h", color="Category", text="Total Sales ($)",
            color_discrete_sequence=px.colors.qualitative.Bold,
        )
        fig1.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
        fig1.update_layout(showlegend=False, yaxis=dict(categoryorder="total ascending"))
        st.plotly_chart(fig1, use_container_width=True)

    with col_b:
        st.markdown("### Quantity Sold by Category")
        fig2 = px.bar(
            cat.sort_values("Qty Sold", ascending=False),
            x="Qty Sold", y="Category",
            orientation="h", color="Category", text="Qty Sold",
            color_discrete_sequence=px.colors.qualitative.Bold,
        )
        fig2.update_traces(texttemplate="%{text:,}", textposition="outside")
        fig2.update_layout(showlegend=False, yaxis=dict(categoryorder="total ascending"))
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Avg Rating by Category")
    fig3 = px.bar(
        cat.sort_values("Avg Rating", ascending=False),
        x="Category", y="Avg Rating", color="Category", text="Avg Rating",
        color_discrete_sequence=px.colors.qualitative.Bold,
    )
    fig3.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig3.update_layout(showlegend=False, yaxis=dict(range=[0, 10]))
    st.plotly_chart(fig3, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 10. PAYMENT METHOD ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Payment Method Analysis":
    section_header("💳", "Payment Method Analysis", "Transaction frequency and revenue by payment type")
    filter_banner()
    st.caption("How customers pay — usage frequency, sales contribution and avg spend.")
    st.markdown("---")

    pay = (
        df_filtered.groupby("payment")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Total_Revenue=("total", "sum"),
            Avg_Transaction=("total", "mean"),
            Total_Qty=("quantity", "sum"),
        )
        .round(2)
        .reset_index()
        .sort_values("Transactions", ascending=False)
        .rename(columns={
            "payment": "Payment Method",
            "Transactions": "Transactions",
            "Total_Sales": "Total Sales ($)",
            "Total_Revenue": "Total Revenue ($)",
            "Avg_Transaction": "Avg Transaction ($)",
            "Total_Qty": "Qty Sold",
        })
    )

    top_pay       = pay.iloc[0]["Payment Method"]
    top_pay_count = pay.iloc[0]["Transactions"]
    top_pay_sales = pay.sort_values("Total Sales ($)", ascending=False).iloc[0]["Payment Method"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Most Used Payment Method", top_pay)
    c2.metric("Its Transaction Count", f"{int(top_pay_count):,}")
    c3.metric("Highest Sales by Method", top_pay_sales)

    st.markdown("### Payment Method Summary Table")
    st.dataframe(pay, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Transactions by Payment Method")
        fig1 = px.pie(
            pay, names="Payment Method", values="Transactions",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Safe,
        )
        fig1.update_traces(textinfo="label+percent+value")
        st.plotly_chart(fig1, use_container_width=True)

    with col_b:
        st.markdown("### Total Sales by Payment Method")
        fig2 = px.pie(
            pay, names="Payment Method", values="Total Sales ($)",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Safe,
        )
        fig2.update_traces(textinfo="label+percent")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Avg Transaction Value by Payment Method")
    fig3 = px.bar(
        pay, x="Payment Method", y="Avg Transaction ($)",
        color="Payment Method", text="Avg Transaction ($)",
        color_discrete_sequence=px.colors.qualitative.Safe,
    )
    fig3.update_traces(texttemplate="%{text:,.2f}", textposition="outside")
    fig3.update_layout(showlegend=False, xaxis_title="", yaxis_title="Avg Transaction ($)")
    st.plotly_chart(fig3, use_container_width=True)

    if "branch" in df_filtered.columns:
        st.markdown("### Payment Method Preference by Branch")
        pay_branch = (
            df_filtered.groupby(["branch", "payment"])["invoice_id"]
            .count()
            .reset_index()
            .rename(columns={"branch": "Branch", "payment": "Payment Method", "invoice_id": "Transactions"})
        )
        fig4 = px.bar(
            pay_branch, x="Branch", y="Transactions",
            color="Payment Method", barmode="group",
            color_discrete_sequence=px.colors.qualitative.Safe,
        )
        st.plotly_chart(fig4, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 11. CUSTOMER TYPE ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Customer Type Analysis":
    section_header("👤", "Customer Type Analysis", "Member vs Normal customer comparison")
    filter_banner()
    st.caption("Comparison between Member and Normal (guest) customers.")
    st.markdown("---")

    cust = (
        df_filtered.groupby("customer_type")
        .agg(
            Transactions=("invoice_id", "count"),
            Total_Sales=("sales", "sum"),
            Total_Revenue=("total", "sum"),
            Avg_Transaction=("total", "mean"),
            Total_Qty=("quantity", "sum"),
            Avg_Rating=("rating", "mean"),
        )
        .round(2)
        .reset_index()
        .sort_values("Transactions", ascending=False)
        .rename(columns={
            "customer_type": "Customer Type",
            "Transactions": "Transactions",
            "Total_Sales": "Total Sales ($)",
            "Total_Revenue": "Total Revenue ($)",
            "Avg_Transaction": "Avg Transaction ($)",
            "Total_Qty": "Qty Sold",
            "Avg_Rating": "Avg Rating",
        })
    )

    top_type        = cust.iloc[0]["Customer Type"]
    top_type_count  = cust.iloc[0]["Transactions"]
    top_type_sales  = cust.sort_values("Total Sales ($)", ascending=False).iloc[0]["Customer Type"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Most Frequent Customer Type", top_type)
    c2.metric("Its Transaction Count", f"{int(top_type_count):,}")
    c3.metric("Highest Spending Type", top_type_sales)

    st.markdown("### Customer Type Summary Table")
    st.dataframe(cust, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Transactions Share")
        fig1 = px.pie(
            cust, names="Customer Type", values="Transactions",
            hole=0.4,
            color_discrete_sequence=["#636EFA", "#EF553B"],
        )
        fig1.update_traces(textinfo="label+percent+value")
        st.plotly_chart(fig1, use_container_width=True)

    with col_b:
        st.markdown("### Total Sales Share")
        fig2 = px.pie(
            cust, names="Customer Type", values="Total Sales ($)",
            hole=0.4,
            color_discrete_sequence=["#636EFA", "#EF553B"],
        )
        fig2.update_traces(textinfo="label+percent")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Avg Transaction Value & Avg Rating by Customer Type")
    fig3 = px.bar(
        cust, x="Customer Type",
        y=["Avg Transaction ($)", "Avg Rating"],
        barmode="group",
        color_discrete_sequence=["#636EFA", "#EF553B"],
    )
    fig3.update_layout(yaxis_title="Value", xaxis_title="")
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("### Customer Type Spending by Product Line")
    cust_prod = (
        df_filtered.groupby(["customer_type", "product_line"])["sales"]
        .sum().round(2).reset_index()
        .rename(columns={"customer_type": "Customer Type",
                         "product_line": "Product Line", "sales": "Total Sales ($)"})
    )
    fig4 = px.bar(
        cust_prod, x="Product Line", y="Total Sales ($)",
        color="Customer Type", barmode="group",
        color_discrete_sequence=["#636EFA", "#EF553B"],
    )
    fig4.update_layout(xaxis_title="", yaxis_title="Total Sales ($)")
    st.plotly_chart(fig4, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 12. GENDER ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Gender Analysis":
    if "gender" not in df_filtered.columns:
        st.warning("⚠️ `gender` column not found in the dataset.")
    else:
        section_header("⚥", "Gender Analysis", "Shopping behaviour by customer gender")
        filter_banner()
        st.markdown("---")

        gen = (
            df_filtered.groupby("gender")
            .agg(
                Transactions=("invoice_id", "count"),
                Total_Sales=("sales", "sum"),
                Total_Revenue=("total", "sum"),
                Avg_Transaction=("total", "mean"),
                Total_Qty=("quantity", "sum"),
                Avg_Rating=("rating", "mean"),
            )
            .round(2)
            .reset_index()
            .sort_values("Transactions", ascending=False)
            .rename(columns={
                "gender": "Gender",
                "Transactions": "Transactions",
                "Total_Sales": "Total Sales ($)",
                "Total_Revenue": "Total Revenue ($)",
                "Avg_Transaction": "Avg Transaction ($)",
                "Total_Qty": "Qty Sold",
                "Avg_Rating": "Avg Rating",
            })
        )

        top_gender       = gen.iloc[0]["Gender"]
        top_gender_sales = gen.sort_values("Total Sales ($)", ascending=False).iloc[0]["Gender"]

        c1, c2 = st.columns(2)
        c1.metric("Most Frequent Gender", top_gender)
        c2.metric("Highest Spending Gender", top_gender_sales)

        st.markdown("### Gender Summary Table")
        st.dataframe(gen, use_container_width=True)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### Transactions by Gender")
            fig1 = px.pie(
                gen, names="Gender", values="Transactions",
                hole=0.4,
                color_discrete_sequence=["#AB63FA", "#FFA15A"],
            )
            fig1.update_traces(textinfo="label+percent+value")
            st.plotly_chart(fig1, use_container_width=True)

        with col_b:
            st.markdown("### Total Sales by Gender")
            fig2 = px.pie(
                gen, names="Gender", values="Total Sales ($)",
                hole=0.4,
                color_discrete_sequence=["#AB63FA", "#FFA15A"],
            )
            fig2.update_traces(textinfo="label+percent")
            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### Avg Transaction Value & Avg Rating by Gender")
        fig3 = px.bar(
            gen, x="Gender",
            y=["Avg Transaction ($)", "Avg Rating"],
            barmode="group",
            color_discrete_sequence=["#AB63FA", "#FFA15A"],
        )
        fig3.update_layout(yaxis_title="Value", xaxis_title="")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### Gender Spending by Product Line")
        gen_prod = (
            df_filtered.groupby(["gender", "product_line"])["sales"]
            .sum().round(2).reset_index()
            .rename(columns={"gender": "Gender",
                             "product_line": "Product Line", "sales": "Total Sales ($)"})
        )
        fig4 = px.bar(
            gen_prod, x="Product Line", y="Total Sales ($)",
            color="Gender", barmode="group",
            color_discrete_sequence=["#AB63FA", "#FFA15A"],
        )
        fig4.update_layout(xaxis_title="", yaxis_title="Total Sales ($)")
        st.plotly_chart(fig4, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 13. CUSTOMER RATING ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif section == "Customer Rating Analysis":
    if "rating" not in df_filtered.columns:
        st.warning("⚠️ `rating` column not found in the dataset.")
    else:
        section_header("⭐", "Customer Rating Analysis", "Satisfaction score distribution and segmentation")
        filter_banner()
        st.markdown("---")

        avg_rating = df_filtered["rating"].mean()
        min_rating = df_filtered["rating"].min()
        max_rating = df_filtered["rating"].max()
        med_rating = df_filtered["rating"].median()

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Avg Rating", f"{avg_rating:.2f}")
        c2.metric("Median Rating", f"{med_rating:.2f}")
        c3.metric("Min Rating", f"{min_rating:.1f}")
        c4.metric("Max Rating", f"{max_rating:.1f}")

        st.markdown("---")

        st.markdown("### Rating Distribution")
        fig1 = px.histogram(
            df_filtered, x="rating", nbins=20,
            color_discrete_sequence=["#19D3F3"],
            labels={"rating": "Customer Rating"},
        )
        fig1.add_vline(x=avg_rating, line_dash="dash", line_color="red",
                       annotation_text=f"Mean: {avg_rating:.2f}", annotation_position="top right")
        fig1.update_layout(bargap=0.05, xaxis_title="Rating", yaxis_title="Number of Transactions")
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("### Avg Rating by Branch")
        rat_branch = (
            df_filtered.groupby("branch")["rating"].mean().round(2)
            .reset_index().rename(columns={"branch": "Branch", "rating": "Avg Rating"})
        )
        top_rated_branch = rat_branch.sort_values("Avg Rating", ascending=False).iloc[0]
        st.info(f"🏆 Highest-rated branch: **Branch {top_rated_branch['Branch']}** — {top_rated_branch['Avg Rating']:.2f} / 10")
        fig2 = px.bar(
            rat_branch, x="Branch", y="Avg Rating",
            color="Branch", text="Avg Rating",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        fig2.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig2.update_layout(showlegend=False, yaxis=dict(range=[0, 10]))
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### Avg Rating by Product Line")
        rat_prod = (
            df_filtered.groupby("product_line")["rating"].mean().round(2)
            .reset_index()
            .rename(columns={"product_line": "Product Line", "rating": "Avg Rating"})
            .sort_values("Avg Rating", ascending=False)
        )
        top_rated_prod = rat_prod.iloc[0]
        st.info(f"🏆 Highest-rated product line: **{top_rated_prod['Product Line']}** — {top_rated_prod['Avg Rating']:.2f} / 10")
        fig3 = px.bar(
            rat_prod, x="Avg Rating", y="Product Line",
            orientation="h", color="Product Line", text="Avg Rating",
            color_discrete_sequence=px.colors.qualitative.Bold,
        )
        fig3.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig3.update_layout(showlegend=False, yaxis=dict(categoryorder="total ascending"))
        st.plotly_chart(fig3, use_container_width=True)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### Avg Rating by Payment Method")
            rat_pay = (
                df_filtered.groupby("payment")["rating"].mean().round(2)
                .reset_index().rename(columns={"payment": "Payment Method", "rating": "Avg Rating"})
                .sort_values("Avg Rating", ascending=False)
            )
            top_rated_pay = rat_pay.iloc[0]
            st.caption(f"🏆 Best: **{top_rated_pay['Payment Method']}** — {top_rated_pay['Avg Rating']:.2f}")
            fig4 = px.bar(
                rat_pay, x="Payment Method", y="Avg Rating",
                color="Payment Method", text="Avg Rating",
                color_discrete_sequence=px.colors.qualitative.Safe,
            )
            fig4.update_traces(texttemplate="%{text:.2f}", textposition="outside")
            fig4.update_layout(showlegend=False, yaxis=dict(range=[0, 10]))
            st.plotly_chart(fig4, use_container_width=True)

        with col_b:
            st.markdown("### Avg Rating by Customer Type")
            rat_cust = (
                df_filtered.groupby("customer_type")["rating"].mean().round(2)
                .reset_index().rename(columns={"customer_type": "Customer Type", "rating": "Avg Rating"})
                .sort_values("Avg Rating", ascending=False)
            )
            top_rated_cust = rat_cust.iloc[0]
            st.caption(f"🏆 Best: **{top_rated_cust['Customer Type']}** — {top_rated_cust['Avg Rating']:.2f}")
            fig5 = px.bar(
                rat_cust, x="Customer Type", y="Avg Rating",
                color="Customer Type", text="Avg Rating",
                color_discrete_sequence=["#636EFA", "#EF553B"],
            )
            fig5.update_traces(texttemplate="%{text:.2f}", textposition="outside")
            fig5.update_layout(showlegend=False, yaxis=dict(range=[0, 10]))
            st.plotly_chart(fig5, use_container_width=True)

        if "gender" in df_filtered.columns:
            st.markdown("### Avg Rating by Gender")
            rat_gen = (
                df_filtered.groupby("gender")["rating"].mean().round(2)
                .reset_index().rename(columns={"gender": "Gender", "rating": "Avg Rating"})
            )
            fig6 = px.bar(
                rat_gen, x="Gender", y="Avg Rating",
                color="Gender", text="Avg Rating",
                color_discrete_sequence=["#AB63FA", "#FFA15A"],
            )
            fig6.update_traces(texttemplate="%{text:.2f}", textposition="outside")
            fig6.update_layout(showlegend=False, yaxis=dict(range=[0, 10]))
            st.plotly_chart(fig6, use_container_width=True)
