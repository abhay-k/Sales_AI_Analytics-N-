import pandas as pd
from prophet import Prophet

def prophet_forecast(df):

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    return forecast[['ds','yhat']].tail(30).to_dict(orient="records")
