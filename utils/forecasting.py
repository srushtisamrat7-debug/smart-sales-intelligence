from prophet import Prophet


def forecast_sales(df, periods=30):
    forecast_df = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    forecast_df.columns = ["ds", "y"]

    model = Prophet()
    model.fit(forecast_df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast