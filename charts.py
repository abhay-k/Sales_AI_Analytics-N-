import matplotlib.pyplot as plt

def region_chart(df):
    region_data = df.groupby("Region")["Revenue"].sum()
    plt.figure()
    region_data.plot(kind="bar")
    plt.title("Revenue by Region")
    file = "region_chart.png"
    plt.savefig(file)
    return file

def customer_chart(df):
    customer_data = df.groupby("Customer")["Revenue"].sum()
    plt.figure()
    customer_data.plot(kind="bar")
    plt.title("Revenue by Customer")
    file = "customer_chart.png"
    plt.savefig(file)
    return file
