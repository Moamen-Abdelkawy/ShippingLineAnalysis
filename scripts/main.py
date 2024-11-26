# main.py

import os

def create_directories():
    """Create necessary directories."""
    os.makedirs('./data/raw', exist_ok=True)
    os.makedirs('./data/processed', exist_ok=True)
    os.makedirs('./data/prediction', exist_ok=True)

def main():
    """Main function to run all modules."""
    create_directories()

    # Data Generation
    import data_generation
    data_generation.save_raw_datasets()

    # Data Processing
    import data_processing
    data_processing.save_processed_datasets()

    # Forecasting
    import forecasting
    trade_trend, trade_forecast, profit_df = forecasting.save_forecasting_results()

    # Visualization
    import visualization
    visualization.plot_all()

    # Display Results
    pd.options.display.float_format = '{:,.2f}'.format
    future_trade_volumes = pd.read_csv('./data/prediction/future_trade_and_profit_predictions.csv')
    print("\nTrade Volume Predictions for 2025–2030:")
    print(future_trade_volumes)

    print("\nProfit Analysis at Varying Shipping Rates:")
    print(profit_df)

if __name__ == "__main__":
    main()
