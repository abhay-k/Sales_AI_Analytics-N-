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
    df["Revenue"] = df["Qty"] * df["Price"]

    # Summaries
    total_orders = len(df)
    total_revenue = df["Revenue"].sum()
    region_sales = df.groupby("Region")["Revenue"].sum().to_dict()
    customer_sales = df.groupby("Customer")["Revenue"].sum().to_dict()

    # Insights
    insight = generate_sales_insights(df)

    # Charts
    region_chart_file = region_chart(df)
    customer_chart_file = customer_chart(df)

    # Clustering (Customer Segmentation)
    clustering_result = segment_customers(df)

    # Forecasting (requires aggregated daily totals)
    # For now, we simulate daily totals by grouping by SO No
    forecast_input = df.groupby("SO No")["Revenue"].sum().reset_index()
    forecast_input.columns = ["ds", "y"]
    forecast = prophet_forecast(forecast_input)

    # PDF Report
    pdf_file = generate_report(
        insight,
        region_chart_file,
        customer_chart_file
    )

    return {
        "totalOrders": total_orders,
        "totalRevenue": total_revenue,
        "regionSales": region_sales,
        "customerSales": customer_sales,
        "insight": insight,
        "customerSegmentation": clustering_result,
        "forecast": forecast,
        "reportFile": pdf_file
    }

