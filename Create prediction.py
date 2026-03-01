from sklearn.linear_model import LogisticRegression
import pandas as pd

def predict_conversion(data):

    df = pd.DataFrame(data)

    X = df[['visits','time_spent','pages']]
    y = df['converted']

    model = LogisticRegression()
    model.fit(X,y)

    prediction = model.predict(X)

    return prediction.tolist()
