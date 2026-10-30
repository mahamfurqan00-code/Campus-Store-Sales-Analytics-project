import pandas as pd
import numpy as np

REQUIRED = {"order_id","order_date","product","category","region","quantity","unit_price","unit_cost"}

def load_sales(path="data/sales.csv"):
    df = pd.read_csv(path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    for col in ["quantity","unit_price","unit_cost"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["order_date","quantity","unit_price","unit_cost"])
    df = df[(df.quantity > 0) & (df.unit_price >= 0) & (df.unit_cost >= 0)].copy()
    df["revenue"] = np.round(df.quantity * df.unit_price, 2)
    df["cost"] = np.round(df.quantity * df.unit_cost, 2)
    df["profit"] = np.round(df.revenue - df.cost, 2)
    return df

def filter_sales(df, start=None, end=None, category=None, region=None):
    out = df.copy()
    if start: out = out[out.order_date >= pd.to_datetime(start)]
    if end: out = out[out.order_date < pd.to_datetime(end) + pd.Timedelta(days=1)]
    if category: out = out[out.category == category]
    if region: out = out[out.region == region]
    return out

def summarize_sales(df):
    revenue = float(df.revenue.sum()) if len(df) else 0
    profit = float(df.profit.sum()) if len(df) else 0
    orders = int(df.order_id.nunique()) if len(df) else 0
    units = int(df.quantity.sum()) if len(df) else 0
    return {"revenue": round(revenue,2), "profit": round(profit,2), "orders": orders,
            "units": units, "margin": round(profit/revenue*100,1) if revenue else 0,
            "avg_order_value": round(revenue/orders,2) if orders else 0}

def chart_data(df):
    if df.empty: return {"monthly":[],"categories":[],"regions":[],"products":[]}
    x = df.copy()
    x["month"] = x.order_date.dt.to_period("M").astype(str)
    m = x.groupby("month",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"))
    c = x.groupby("category",as_index=False).revenue.sum().sort_values("revenue",ascending=False)
    r = x.groupby("region",as_index=False).revenue.sum().sort_values("revenue",ascending=False)
    p = x.groupby("product",as_index=False).agg(units=("quantity","sum"),revenue=("revenue","sum")).sort_values("revenue",ascending=False).head(7)
    return {"monthly":[{"month":a.month,"revenue":round(a.revenue,2),"profit":round(a.profit,2)} for a in m.itertuples()],
            "categories":[{"category":a.category,"revenue":round(a.revenue,2)} for a in c.itertuples()],
            "regions":[{"region":a.region,"revenue":round(a.revenue,2)} for a in r.itertuples()],
            "products":[{"product":a.product,"units":int(a.units),"revenue":round(a.revenue,2)} for a in p.itertuples()]}
