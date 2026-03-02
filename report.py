def generate_report(total_orders, total_revenue, region_sales, customer_sales,
                    insights, clusters, forecast, region_chart_file, customer_chart_file):

    report = {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "region_sales": region_sales,
        "customer_sales": customer_sales,
        "insights": insights,
        "clusters": clusters,
        "forecast": forecast,
        "region_chart": region_chart_file,
        "customer_chart": customer_chart_file
    }

    return report
