def generate_sales_insights(df):
    insights = []

    top_region = df.groupby("Region")["Revenue"].sum().idxmax()
    insights.append(f"Top performing region: {top_region}")

    top_customer = df.groupby("Customer")["Revenue"].sum().idxmax()
    insights.append(f"Top customer: {top_customer}")

    avg_order_value = df["Revenue"].mean()
    insights.append(f"Average order value: {avg_order_value:.2f}")

    return insights
