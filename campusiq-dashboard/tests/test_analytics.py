import pandas as pd
from analytics import summarize_sales, filter_sales, chart_data

def sample():
    return pd.DataFrame({"order_id":["A","B","C"],"order_date":pd.to_datetime(["2025-01-02","2025-01-20","2025-02-02"]),"product":["Notebook","Pen","Notebook"],"category":["Stationery"]*3,"region":["North","South","North"],"quantity":[2,5,1],"unit_price":[10.,2.,10.],"unit_cost":[4.,.5,4.],"revenue":[20.,10.,10.],"cost":[8.,2.5,4.],"profit":[12.,7.5,6.]})

def test_summary():
    x=summarize_sales(sample())
    assert x["revenue"]==40 and x["profit"]==25.5 and x["orders"]==3 and x["units"]==8

def test_region_filter():
    assert len(filter_sales(sample(),region="North"))==2

def test_date_filter():
    assert len(filter_sales(sample(),start="2025-01-01",end="2025-01-31"))==2

def test_monthly_chart():
    assert len(chart_data(sample())["monthly"])==2
