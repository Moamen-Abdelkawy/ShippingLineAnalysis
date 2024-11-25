# Shipping Line Analysis

## Overview
This repository contains a detailed analysis and forecasting study for establishing a shipping line between Egyptian and Libyan ports. The analysis is based on synthetic data designed to replicate real-world scenarios, focusing on trade volumes, port capacities, vessel cost efficiency, and profitability under varying conditions. Advanced forecasting methods are used to predict trade volumes and profits for 2025–2030.

**Note**: This analysis is based on synthetic data, and additional real-world variables (e.g., labor, maintenance costs) can be easily integrated.

---

## Features
### **1. Data Analysis**
- Historical trade volume trends (2003–2023).
- Exploration of port capacities and risk scores.
- Evaluation of vessel types for cost efficiency.

### **2. Predictive Modeling**
- **Trade Volume Forecasting**:
  - Leveraged `Prophet` for accurate trade volume predictions (2025–2030).
- **Profit Simulations**:
  - Simulated profits under varying shipping rates ($40–$60 per ton).

### **3. Profitability Assessment**
- Evaluated total profits for multiple pricing strategies, identifying optimal rates for profitability.

---

## Key Results
### **Forecasted Trade Volumes (2025–2030)**

| Year | Predicted Trade Volume (Metric Tons) |
|------|--------------------------------------|
| 2025 | 138,524                              |
| 2026 | 137,322                              |
| 2027 | 137,558                              |
| 2028 | 138,444                              |
| 2029 | 138,951                              |
| 2030 | 139,216                              |

### **Profit Analysis**

| Shipping Rate (USD per Ton) | Total Profit (Million USD) |
|-----------------------------|----------------------------|
| 40                          | 6.06                       |
| 45                          | 9.09                       |
| 50                          | 12.12                      |
| 55                          | 13.89                      |
| 60                          | 15.66                      |

---

## Visualizations
### Trade Volume Trends by Year and Goods Category
![Trade Volume Trends](link-to-image)

### Annual Port Capacities
![Port Capacities](link-to-image)

### Cost Efficiency of Vessel Types
![Vessel Cost Efficiency](link-to-image)

### Trade Volume Distribution by Port
![Trade Volume Distribution](link-to-image)

### Correlation Matrix of Port Attributes
![Correlation Matrix](link-to-image)

### Trade Volume Predictions (2025–2030)
![Trade Volume Forecast](link-to-image)

### Profit Analysis at Varying Rates
![Profit Analysis](link-to-image)

---

## Requirements
### **Python Libraries**
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `prophet`
- `plotly` (for interactive visuals)

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ShippingLineAnalysis.git
   cd ShippingLineAnalysis
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis script:
   ```bash
   python analysis.py
   ```

---

## Folder Structure
```
ShippingLineAnalysis/
├── data/
│   ├── raw/                        # Raw synthetic datasets
│   │   ├── trade_volume.csv
│   │   ├── fuel_cost.csv
│   │   ├── port_info.csv
│   │   └── vessel_types.csv
│   ├── processed/                  # Processed datasets
│   │   ├── trade_with_ports.csv
│   │   ├── port_info_processed.csv
│   │   └── vessel_types_processed.csv
│   └── prediction/                 # Prediction results
│       ├── future_trade_and_profit_predictions.csv
│       └── profit_analysis_at_varying_rates.csv
├── visuals/                        # Visualizations
│   ├── trade_volume_trends.png
│   ├── port_capacities.png
│   ├── vessel_cost_efficiency.png
│   ├── trade_volume_distribution.png
│   ├── correlation_matrix.png
│   ├── trade_forecast.png
│   └── profit_analysis.png
├── scripts/                        # Python scripts
│   ├── data_synthesis.py
│   ├── analysis.py
│   ├── forecasting.py
│   └── visualization.py
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
└── LICENSE                         # License file
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Notes
This analysis is designed to:
- Provide insights into trade volume forecasting and profitability for shipping operations.
- Demonstrate adaptability for real-world applications in trade and logistics.
