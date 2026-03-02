import pandas as pd
from prophet import Prophet

def prophet_forecast(df):
    # Prophet requires only ds (date) and y (value)
    ts = df[["ds", "y"]]

    model = Prophet()
    model.fit(ts)

    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)

    return forecast[["ds", "yhat"]].tail(30).to_dict(orient="records")
