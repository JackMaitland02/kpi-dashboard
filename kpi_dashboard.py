import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. LOAD DATA
# ==============================
df = pd.read_csv("monthly_financials.csv")

# ==============================
# 2. CLEAN DATA
# ==============================
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

DATE_COL = "date"
REVENUE_COL = "revenue"
EXPENSE_COL = "expense"   # set to None if not applicable

df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce")
df[REVENUE_COL] = pd.to_numeric(df[REVENUE_COL], errors="coerce")

if EXPENSE_COL and EXPENSE_COL in df.columns:
    df[EXPENSE_COL] = pd.to_numeric(df[EXPENSE_COL], errors="coerce")
    df["profit"] = df[REVENUE_COL] - df[EXPENSE_COL]
    df["margin_pct"] = (df["profit"] / df[REVENUE_COL]) * 100

# ==============================
# 3. KPI SUMMARY
# ==============================
monthly = df.dropna(subset=[DATE_COL]).groupby(
    pd.Grouper(key=DATE_COL, freq="MS")
).agg(
    revenue=(REVENUE_COL, "sum"),
).reset_index()

monthly["mom_growth_pct"] = monthly["revenue"].pct_change() * 100

print("\n=== KPI SUMMARY ===")
print(f"Total Revenue: {monthly['revenue'].sum():,.2f}")
print(f"Latest Month Revenue: {monthly['revenue'].iloc[-1]:,.2f}")
print(f"Average MoM Growth (%): {monthly['mom_growth_pct'].dropna().mean():,.2f}")

if "profit" in df.columns:
    print(f"Total Profit: {df['profit'].sum():,.2f}")
    print(f"Overall Margin (%): {(df['profit'].sum() / df[REVENUE_COL].sum()) * 100:,.2f}")

# ==============================
# 4. VISUALIZATION
# ==============================
plt.figure()
plt.plot(monthly["date"], monthly["revenue"])
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
