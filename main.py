from fastapi import FastAPI
import pandas as pd

from charts import region_chart, customer_chart
from insights import generate_sales_insights
from clustering import segment_customers
from forecasting import prophet_forecast
from report import generate_report

app = FastAPI()

@app.post("/sales-report")
def sales_report(data: dict):

    df = pd.DataFrame(data["sales"])

    # Ensure correct types
    df["Qty"] = df["Qty"].astype(int)
    df["Price"] = df["Price"].astype(float)

    # Revenue
    df["Revenue"] = df["Qty"] * df["Price"]

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Prophet-required columns
    df["ds"] = df["Date"]
    df["y"] = df["Revenue"]

    # Summaries
    total_orders = len(df)
    total_revenue = df["Revenue"].sum()
    region_sales = df.groupby("Region")["Revenue"].sum().to_dict()
    customer_sales = df.groupby("Customer")["Revenue"].sum().to_dict()

    # Analytics
    insights = generate_sales_insights(df)
    clusters = segment_customers(df)
    forecast = prophet_forecast(df)

    # Charts
    region_chart_file = region_chart(df)
    customer_chart_file = customer_chart(df)

    # Report
    report_file = generate_report(
        total_orders,
        total_revenue,
        region_sales,
        customer_sales,
        insights,
        clusters,
        forecast,
        region_chart_file,
        customer_chart_file
    )

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "region_sales": region_sales,
        "customer_sales": customer_sales,
        "insights": insights,
        "clusters": clusters,
        "forecast": forecast,
        "report_file": report_file
    }
