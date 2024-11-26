# visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from forecasting import forecast_trade_volumes, prepare_trade_trend

def set_plot_style():
    """Set the visualization aesthetics."""
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({'figure.max_open_warning': 0})

def plot_trade_volume_by_year_and_goods(trade_with_ports):
    """Plot total trade volume by year and goods category."""
    plt.figure(figsize=(12, 8))
    trade_summary = trade_with_ports.groupby(["Trade Year", "Good Category"]).agg({
        "Trade Volume (Metric Tons)": "sum"
    }).reset_index()

    sns.barplot(
        data=trade_summary,
        x="Trade Year",
        y="Trade Volume (Metric Tons)",
        hue="Good Category",
        palette="viridis"
    )
    plt.title("Total Trade Volume by Year and Goods Category", fontsize=16, weight="bold")
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Trade Volume (Metric Tons)", fontsize=14)
    plt.legend(title="Goods Category", fontsize=12)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_annual_port_capacities(port_info_df):
    """Plot annual port capacities by country."""
    plt.figure(figsize=(12, 8))
    sorted_ports = port_info_df.sort_values("Annual Capacity (Metric Tons)", ascending=False)
    sns.barplot(
        data=sorted_ports,
        x="Port",
        y="Annual Capacity (Metric Tons)",
        hue="Country",
        dodge=False,
        palette="Set2"
    )
    plt.title("Annual Port Capacities by Country", fontsize=16, weight="bold")
    plt.xlabel("Port", fontsize=14)
    plt.ylabel("Capacity (Metric Tons)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title="Country", fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_cost_efficiency_of_vessel_types(vessel_types_df):
    """Plot cost efficiency of vessel types."""
    plt.figure(figsize=(12, 8))
    sorted_vessels = vessel_types_df.sort_values("Cost per Ton (USD)", ascending=True)
    sns.barplot(
        data=sorted_vessels,
        x="Cost per Ton (USD)",
        y="Vessel Type",
        color="#55A868"
    )
    plt.title("Cost Efficiency of Vessel Types (USD per Ton)", fontsize=16, weight="bold")
    plt.xlabel("Cost per Ton (USD)", fontsize=14)
    plt.ylabel("Vessel Type", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_trade_volume_distribution_by_port(trade_with_ports):
    """Plot trade volume distribution by port."""
    plt.figure(figsize=(12, 8))
    sns.boxplot(
        data=trade_with_ports,
        x="Port",
        y="Trade Volume (Metric Tons)",
        palette="Set2"
    )
    plt.title("Trade Volume Distribution by Port", fontsize=16, weight="bold")
    plt.xlabel("Port", fontsize=14)
    plt.ylabel("Trade Volume (Metric Tons)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_port_attributes_correlation(port_info_df):
    """Plot correlation heatmap for numerical variables in ports."""
    plt.figure(figsize=(10, 8))
    numerical_columns = [
        "Annual Capacity (Metric Tons)",
        "Infrastructure Quality (1-10)",
        "Proximity to Trade Hubs (1-10)",
        "Political Stability (1-10)",
        "Customs Efficiency (1-10)"
    ]
    corr = port_info_df[numerical_columns].corr()
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        square=True,
        linewidths=0.5
    )
    plt.title("Correlation Matrix of Port Attributes", fontsize=16, weight="bold")
    plt.tight_layout()
    plt.show()

def plot_yearly_trade_volume_for_top_ports(trade_with_ports):
    """Plot yearly trade volume for top ports."""
    top_ports = trade_with_ports["Port"].value_counts().index[:3]
    top_port_data = trade_with_ports[trade_with_ports["Port"].isin(top_ports)]
    grouped_data = top_port_data.groupby(["Trade Year", "Port"])["Trade Volume (Metric Tons)"].sum().reset_index()
    plt.figure(figsize=(12, 8))
    sns.lineplot(
        data=grouped_data,
        x="Trade Year",
        y="Trade Volume (Metric Tons)",
        hue="Port",
        marker="o"
    )
    plt.title("Yearly Trade Volume for Top Ports", fontsize=16, weight="bold")
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Trade Volume (Metric Tons)", fontsize=14)
    plt.legend(title="Port", fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_trade_volume_predictions(trade_trend, trade_forecast):
    """Visualize trade volume predictions."""
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=trade_trend, x='ds', y='y', label='Historical', marker='o')
    sns.lineplot(data=trade_forecast, x='ds', y='yhat', label='Forecast', linestyle='--')
    plt.title("Trade Volume Predictions (2025–2030)", fontsize=16, weight="bold")
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Trade Volume (Metric Tons)", fontsize=14)
    plt.legend(title="Legend", fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_profits_at_varying_rates(profit_df):
    """Visualize profits at varying shipping rates."""
    plt.figure(figsize=(12, 8))
    sns.barplot(data=profit_df, x="Rate (USD per Ton)", y="Total Profit (Million USD)", palette="Blues_d")
    plt.title("Total Predicted Profits at Varying Shipping Rates (2025–2030)", fontsize=16, weight="bold")
    plt.xlabel("Shipping Rate (USD per Ton)", fontsize=14)
    plt.ylabel("Total Profit (Million USD)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_all():
    """Run all plotting functions."""
    # Load processed data
    trade_with_ports = pd.read_csv('./data/processed/trade_with_ports.csv')
    port_info_df = pd.read_csv('./data/processed/port_info_processed.csv')
    vessel_types_df = pd.read_csv('./data/processed/vessel_types_processed.csv')
    future_trade_volumes = pd.read_csv('./data/prediction/future_trade_and_profit_predictions.csv')
    profit_df = pd.read_csv('./data/prediction/profit_analysis_at_varying_rates.csv')

    # Prepare trade trend data for forecasting plots
    trade_volume_df = pd.read_csv('./data/raw/trade_volume.csv')
    trade_trend = prepare_trade_trend(trade_volume_df)
    trade_forecast = forecast_trade_volumes(trade_trend)

    # Set plot style
    set_plot_style()

    # Generate plots
    plot_trade_volume_by_year_and_goods(trade_with_ports)
    plot_annual_port_capacities(port_info_df)
    plot_cost_efficiency_of_vessel_types(vessel_types_df)
    plot_trade_volume_distribution_by_port(trade_with_ports)
    plot_port_attributes_correlation(port_info_df)
    plot_yearly_trade_volume_for_top_ports(trade_with_ports)
    plot_trade_volume_predictions(trade_trend, trade_forecast)
    plot_profits_at_varying_rates(profit_df)

if __name__ == "__main__":
    plot_all()
