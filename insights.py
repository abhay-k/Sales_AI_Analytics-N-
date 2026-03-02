def generate_sales_insights(df):

    total_revenue = df["Revenue"].sum()
    avg_revenue = df["Revenue"].mean()
    top_region = df.groupby("Region")["Revenue"].sum().idxmax()
    top_customer = df.groupby("Customer")["Revenue"].sum().idxmax()

    return f"""
    Total revenue: ${total_revenue}
    Average order value: ${avg_revenue}
    Top region: {top_region}
    Top customer: {top_customer}
    """
