import matplotlib.pyplot as plt
import pandas as pd

def sales_chart(data):

    df = pd.DataFrame(data)

    plt.figure()

    plt.plot(df["date"], df["sales"])

    plt.title("Sales Trend")

    plt.xlabel("Date")

    plt.ylabel("Sales")

    file = "sales_chart.png"

    plt.savefig(file)

    return file
