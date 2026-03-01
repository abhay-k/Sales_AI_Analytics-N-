from fastapi import FastAPI
from charts import sales_chart
from report import generate_report
from insights import generate_sales_insights

app = FastAPI()

@app.post("/sales-report")

def sales_report(data:list):

    insight = generate_sales_insights(data)

    chart = sales_chart(data)

    report = generate_report(chart, insight)

    return {
        "insight": insight,
        "report": report
    }
