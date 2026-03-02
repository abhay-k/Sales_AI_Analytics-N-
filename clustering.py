from sklearn.cluster import KMeans
import pandas as pd

def segment_customers(df):

    # Aggregate revenue per customer
    agg = df.groupby("Customer")["Revenue"].sum().reset_index()
    agg.columns = ["Customer", "Revenue"]

    model = KMeans(n_clusters=4, n_init=10)
    agg["Cluster"] = model.fit_predict(agg[["Revenue"]])

    return agg.to_dict(orient="records")
