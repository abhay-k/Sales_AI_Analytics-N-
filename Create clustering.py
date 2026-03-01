from sklearn.cluster import KMeans
import pandas as pd

def segment_customers(data):

    df = pd.DataFrame(data)

    model = KMeans(n_clusters=4)

    clusters = model.fit_predict(df)

    df["cluster"] = clusters

    return df.to_dict()
