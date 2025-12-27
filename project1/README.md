# ⚾ Baseball Players BMI Analyzer

## 📌 Project Overview
A Data Analysis pipeline that processes raw baseball player data to calculate BMI, categorize health metrics, and visualize correlations between physical attributes. 
This project demonstrates a complete **EDA (Exploratory Data Analysis)** workflow using **NumPy**, **Pandas**, and **Matplotlib**.

## 📂 Dataset Schema
The input data is a raw list of lists following this structure:

| Index | Feature | Unit | Type |
| :--- | :--- | :--- | :--- |
| 0 | `height` | Inches | Float |
| 1 | `weight` | Pounds | Float |
| 2 | `age` | Years | Integer |

**Sample Row:** `[72, 180, 29]`

## 🚀 Key Features
1.  **Vectorized Operations:** Uses NumPy for fast, element-wise unit conversions.
2.  **Data Cleaning:** Converts Imperial units (lbs/in) to Metric (kg/m).
3.  **Statistical Analysis:** Computes Mean, Std Dev, and Correlation Coefficient.
4.  **Visualization:** Generates Histograms and Scatter Plots to detect patterns.
5.  **Reporting:** Exports summary statistics to `results.csv`.

## 🛠️ Installation & Usage
Ensure you have Python installed, then install dependencies:
```bash
pip install numpy pandas matplotlib
```
Run the analysis:

```Bash

python project1.py
```
## 📊 Sample Insights
* Strong Correlation: The analysis reveals a correlation of ~0.91 between height and weight.

* Health Metrics: The majority of the sample dataset falls within the "Normal" BMI range.

## 🔮 Future Improvements
Modularity: Refactor the code into separate modules (data_loader.py, viz.py, calc.py) for better scalability.

CLI Arguments: Allow users to upload their own CSV files via command line.

Created for educational purposes to demonstrate Python Data Science fundamentals.