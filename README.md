# ShippingLineAnalysis

This repository provides a comprehensive analysis of the feasibility and profitability of establishing a shipping line between Egyptian and Libyan ports. Using synthetic datasets and advanced forecasting tools, the analysis evaluates trade volume trends, port capacities, vessel efficiencies, and dynamic profit simulations. The project aims to support strategic logistics planning and decision-making.

---

## Repository Structure

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
├── scripts/                        # Python scripts for core functionality
│   ├── data_cleaning.py            # Handles raw data cleaning and preparation
│   ├── exploratory_analysis.py     # Conducts exploratory data analysis
│   ├── forecasting_models.py       # Implements predictive models for trade forecasting
│   ├── profitability_metrics.py    # Simulates profits under varying shipping rates
│   ├── visualization_tools.py      # Creates visual representations of the analysis
│   └── main_pipeline.py            # Orchestrates the analysis workflow
├── notebooks/
│   ├── shipping_line_analysis.ipynb # Full analysis in a Jupyter Notebook
├── reports/                        # Reports and findings
│   ├── arabic_report.md
│   ├── arabic_report.pdf
│   ├── english_report.md
│   ├── english_report.pdf
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
└── LICENSE                         # License file
```

---

## Key Findings

1. **Trade Volume Trends:**
   - Trade volumes have recovered post-pandemic and are stabilizing.
   - Major disruptions, such as the Arab Spring and COVID-19, significantly impacted trade volumes.

2. **Port Analysis:**
   - Egyptian ports (Alexandria, Port Said) and Libyan ports (Benghazi, Tripoli) are key nodes for trade.
   - Port capacity correlates strongly with infrastructure quality and proximity to trade hubs.

3. **Vessel Efficiency:**
   - Bulk Carriers and General Cargo vessels offer the best cost per ton, making them ideal for high-volume goods.

4. **Forecasting:**
   - Trade volumes are projected to stabilize at approximately 140,000 metric tons annually between 2025 and 2030.

5. **Profitability:**
   - At a shipping rate of $60/ton, total projected profits exceed $14 million for 2025–2030.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Moamen-Abdelkawy/ShippingLineAnalysis.git
   cd ShippingLineAnalysis
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Analysis
- The main analysis pipeline can be executed using:
  ```bash
  python scripts/main_pipeline.py
  ```

### Jupyter Notebook
- Explore detailed steps and visualizations in the `notebooks/shipping_line_analysis.ipynb`.

---

## Methodology

1. **Data Gathering:**
   - Generated synthetic datasets for trade volumes, fuel costs, and port/vessel details.
2. **Data Wrangling:**
   - Processed and merged datasets, calculating dynamic risk scores for ports and operational costs.
3. **Exploratory Data Analysis (EDA):**
   - Visualized trade trends, port capacities, vessel cost efficiencies, and trade distributions.
4. **Forecasting:**
   - Used Prophet to predict trade volumes for 2025–2030.
5. **Profitability Simulations:**
   - Simulated profits at varying shipping rates, identifying optimal pricing strategies.

---

## Contribution

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/YourFeatureName`.
3. Commit changes: `git commit -m 'Add feature'`.
4. Push the branch: `git push origin feature/YourFeatureName`.
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For inquiries or feedback, please contact:
**Moamen Abdelkawy**  
[moamen.abdelkawy@outlook.com](mailto:moamen.abdelkawy@outlook.com)
