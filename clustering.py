import pandas as pd
from sklearn.cluster import KMeans

def segment_customers(df):
    features = df[["Qty", "Price", "Revenue"]]

    model = KMeans(n_clusters=4, random_state=42)
    df["Cluster"] = model.fit_predict(features)

    return df[["Customer", "Cluster"]].to_dict(orient="records")
