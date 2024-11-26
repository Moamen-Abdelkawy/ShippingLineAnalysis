# data_processing.py

import pandas as pd

def calculate_vessel_costs(vessel_types_df):
    """Calculate cost per ton for each vessel type."""
    vessel_types_df["Cost per Ton (USD)"] = vessel_types_df["Operational Cost per Trip (USD)"] / vessel_types_df["Capacity (Metric Tons)"]
    return vessel_types_df

def calculate_port_risk_scores(port_info_df):
    """Calculate dynamic risk scores for ports."""
    weights = {
        'Infrastructure Quality (1-10)': 0.3,
        'Proximity to Trade Hubs (1-10)': 0.2,
        'Political Stability (1-10)': 0.3,
        'Customs Efficiency (1-10)': 0.2
    }

    for column, weight in weights.items():
        port_info_df[column + ' Norm'] = port_info_df[column] / 10

    port_info_df['Risk Score'] = 1 - (
        port_info_df['Infrastructure Quality (1-10) Norm'] * weights['Infrastructure Quality (1-10)'] +
        port_info_df['Proximity to Trade Hubs (1-10) Norm'] * weights['Proximity to Trade Hubs (1-10)'] +
        port_info_df['Political Stability (1-10) Norm'] * weights['Political Stability (1-10)'] +
        port_info_df['Customs Efficiency (1-10) Norm'] * weights['Customs Efficiency (1-10)']
    )
    return port_info_df

def merge_datasets(trade_volume_df, port_info_df, fuel_cost_df):
    """Merge trade data with port info and fuel costs."""
    trade_with_ports = trade_volume_df.merge(port_info_df, on="Port", how="left")
    trade_with_ports = trade_with_ports.merge(fuel_cost_df, left_on='Trade Year', right_on='Year', how='left')
    trade_with_ports['Operational Cost'] = trade_with_ports['Trade Volume (Metric Tons)'] * trade_with_ports['Fuel Cost (USD per Metric Ton)'] / 1000
    return trade_with_ports

def save_processed_datasets():
    """Save processed datasets to CSV files."""
    trade_volume_df = pd.read_csv('./data/raw/trade_volume.csv')
    port_info_df = pd.read_csv('./data/raw/port_info.csv')
    fuel_cost_df = pd.read_csv('./data/raw/fuel_cost.csv')
    vessel_types_df = pd.read_csv('./data/raw/vessel_types.csv')

    vessel_types_df = calculate_vessel_costs(vessel_types_df)
    port_info_df = calculate_port_risk_scores(port_info_df)
    trade_with_ports = merge_datasets(trade_volume_df, port_info_df, fuel_cost_df)

    trade_with_ports.to_csv('./data/processed/trade_with_ports.csv', index=False)
    port_info_df.to_csv('./data/processed/port_info_processed.csv', index=False)
    vessel_types_df.to_csv('./data/processed/vessel_types_processed.csv', index=False)

if __name__ == "__main__":
    save_processed_datasets()
