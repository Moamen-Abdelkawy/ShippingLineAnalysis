# data_generation.py

import numpy as np
import pandas as pd

def generate_trade_volume_data():
    """Generate synthetic trade volume data."""
    ports = ['Alexandria', 'Damietta', 'Port Said', 'Tripoli', 'Benghazi', 'Misurata']
    goods_categories = ['Raw Materials', 'Manufactured Goods', 'Perishables', 'Machinery', 'Others']
    years = list(range(2003, 2024))
    data = []

    for year in years:
        for port in ports:
            for good in goods_categories:
                volume = np.random.randint(500, 10000)

                # Adjust for major events
                if 2010 <= year <= 2012:  # Arab Spring
                    volume *= 0.7
                elif 2020 <= year <= 2021:  # COVID-19 Pandemic
                    volume *= 0.5
                elif year == 2022:  # Post-pandemic recovery
                    volume *= 0.8

                data.append([port, good, volume, year])

    trade_volume_df = pd.DataFrame(data, columns=['Port', 'Good Category', 'Trade Volume (Metric Tons)', 'Trade Year'])
    return trade_volume_df

def generate_fuel_cost_data():
    """Generate synthetic fuel cost data."""
    years = list(range(2003, 2024))
    fuel_cost_data = {
        'Year': years,
        'Fuel Cost (USD per Metric Ton)': np.random.uniform(300, 700, len(years))
    }
    fuel_cost_df = pd.DataFrame(fuel_cost_data)
    return fuel_cost_df

def generate_port_info_data():
    """Generate synthetic port information data."""
    ports = ['Alexandria', 'Damietta', 'Port Said', 'Tripoli', 'Benghazi', 'Misurata']
    port_info_data = {
        "Port": ports,
        "Country": ['Egypt', 'Egypt', 'Egypt', 'Libya', 'Libya', 'Libya'],
        "Annual Capacity (Metric Tons)": [200000, 180000, 220000, 150000, 160000, 140000],
        "Infrastructure Quality (1-10)": [8, 7, 9, 6, 5, 5],
        "Proximity to Trade Hubs (1-10)": [9, 8, 9, 6, 7, 6],
        "Political Stability (1-10)": [7, 7, 8, 4, 5, 4],
        "Customs Efficiency (1-10)": [8, 7, 9, 5, 6, 5]
    }
    port_info_df = pd.DataFrame(port_info_data)
    return port_info_df

def generate_vessel_types_data():
    """Generate synthetic vessel types data."""
    vessel_types_data = {
        "Vessel Type": ['Container Ship', 'Bulk Carrier', 'Tanker', 'General Cargo', 'Reefer'],
        "Capacity (Metric Tons)": [20000, 30000, 25000, 15000, 12000],
        "Operational Cost per Trip (USD)": [50000, 60000, 70000, 40000, 45000],
        "Suitable for Goods": [
            'Manufactured Goods, Machinery',
            'Raw Materials, Others',
            'Perishables, Liquid Cargo',
            'General Cargo, Machinery',
            'Perishables'
        ]
    }
    vessel_types_df = pd.DataFrame(vessel_types_data)
    return vessel_types_df

def save_raw_datasets():
    """Save generated datasets to CSV files."""
    trade_volume_df = generate_trade_volume_data()
    fuel_cost_df = generate_fuel_cost_data()
    port_info_df = generate_port_info_data()
    vessel_types_df = generate_vessel_types_data()

    trade_volume_df.to_csv('./data/raw/trade_volume.csv', index=False)
    fuel_cost_df.to_csv('./data/raw/fuel_cost.csv', index=False)
    port_info_df.to_csv('./data/raw/port_info.csv', index=False)
    vessel_types_df.to_csv('./data/raw/vessel_types.csv', index=False)

if __name__ == "__main__":
    save_raw_datasets()
