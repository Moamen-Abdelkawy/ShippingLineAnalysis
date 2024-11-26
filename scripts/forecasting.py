# forecasting.py

import pandas as pd
from prophet import Prophet
import numpy as np

def prepare_trade_trend(trade_volume_df):
    """Prepare the data for forecasting."""
    trade_trend = trade_volume_df.groupby('Trade Year')['Trade Volume (Metric Tons)'].sum().reset_index()
    trade_trend.rename(columns={'Trade Year': 'ds', 'Trade Volume (Metric Tons)': 'y'}, inplace=True)
    trade_trend['ds'] = pd.to_datetime(trade_trend['ds'], format='%Y')
    return trade_trend

def forecast_trade_volumes(trade_trend):
    """Forecast trade volumes using Prophet."""
    trade_model = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
    trade_model.fit(trade_trend)
    future_years = trade_model.make_future_dataframe(periods=6, freq='Y')
    trade_forecast = trade_model.predict(future_years)
    return trade_forecast

def evaluate_profits(future_trade_volumes):
    """Evaluate profits at varying shipping rates."""
    rates = np.arange(40, 61, 5)
    profit_results = []

    for rate in rates:
        future_trade_volumes[f'Revenue at ${rate}/ton'] = (
            future_trade_volumes['Predicted Trade Volume (Metric Tons)'] * rate
        )
        future_trade_volumes[f'Profit at ${rate}/ton'] = (
            future_trade_volumes[f'Revenue at ${rate}/ton'] -
            future_trade_volumes['Predicted Trade Volume (Metric Tons)'] * 35  # Operational cost at $35/ton
        )
        total_profit = future_trade_volumes[f'Profit at ${rate}/ton'].sum()
        profit_results.append({'Rate (USD per Ton)': rate, 'Total Profit (Million USD)': total_profit / 1e6})

    profit_df = pd.DataFrame(profit_results)
    return profit_df, future_trade_volumes

def save_forecasting_results():
    """Save forecasting results to CSV files."""
    trade_volume_df = pd.read_csv('./data/raw/trade_volume.csv')
    trade_trend = prepare_trade_trend(trade_volume_df)
    trade_forecast = forecast_trade_volumes(trade_trend)

    future_trade_volumes = trade_forecast[['ds', 'yhat']].copy()
    future_trade_volumes.rename(columns={'ds': 'Year', 'yhat': 'Predicted Trade Volume (Metric Tons)'}, inplace=True)
    future_trade_volumes['Year'] = future_trade_volumes['Year'].dt.year
    future_trade_volumes = future_trade_volumes[future_trade_volumes['Year'].between(2025, 2030)]

    profit_df, future_trade_volumes = evaluate_profits(future_trade_volumes)

    for col in future_trade_volumes.columns:
        if 'Revenue' in col or 'Profit' in col:
            future_trade_volumes[col] /= 1e6  # Convert to millions

    future_trade_volumes.to_csv('./data/prediction/future_trade_and_profit_predictions.csv', index=False)
    profit_df.to_csv('./data/prediction/profit_analysis_at_varying_rates.csv', index=False)

    return trade_trend, trade_forecast, profit_df

if __name__ == "__main__":
    save_forecasting_results()
