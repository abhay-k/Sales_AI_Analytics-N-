def generate_sales_insights(data):

    sales = [d["sales"] for d in data]

    avg = sum(sales)/len(sales)

    trend = "increasing" if sales[-1] > sales[0] else "decreasing"

    insight = f"""
    Average sales are {avg}.
    Overall trend is {trend}.
    Consider increasing marketing in high growth segments.
    """

    return insight
