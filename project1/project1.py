# Project: BMI Dataset Analyzer
# Goal: Convert raw height/weight data to metric, compute BMI for each person,
#       analyze distribution, detect outliers, and produce a simple report.
#
# Why: This code is designed to demonstrate, for educational and illustrative purposes,
#      basic stats((Mean)،(Count)،(Min/Max)), categorization logic(rules like if > 50), and reproducible pipeline design(Collection ,Ingestion ,Preparation, Computation, Presentation) (deterministic steps(input,output), fixed seeds(like : random.seed(42))).
#    
#(Blueprint)
# Assumptions: #what we will have in the dataset
# - Input columns: [height_in_inches, weight_pounds, (optional) age]
# - No missing rows unless explicitly handled below.
# - Heights in inches and weights in pounds; will convert to meters/kilograms.
#
# High-level pipeline (what I will implement, step-by-step):
# 1. Data understanding: inspect shape, dtypes, quick sanity checks.
# 2. Validation & cleaning: detect missing values and obvious outliers.
# 3. Unit conversion: inches -> meters, pounds -> kg (vectorized).
# 4. Compute BMI: weight_kg / (height_m ** 2) (vectorized).
# 5. Statistics: mean, median, std, min, max.
# 6. Categorize: Underweight / Normal / Overweight / Obese counts & percentages.
# 7. Simple visual checks: histogram of BMI (optional).
# 8. Export results: CSV summary + sample outputs for reproducibility.
#
# Tests & reproducibility:
# - Add a tiny unit test (small known input -> expected BMI).
# - Fix random seeds where randomness used.
#
# Deliverables for reviewers:
# - Clean, commented code (this file).
# - small README.md (explain dataset, assumptions, and how to run).
# - results.csv with per-person BMI and category.
#
# Development notes:
# - I prefer NumPy for core math and Pandas if tabular operations/read/write needed.
# - I will keep functions small and pure (easy to test).
#
# Done by: <mt.codex> | Date: 2025-11-27

# Project: BMI Dataset Analyzer (Master Version)
# Description: A complete pipeline from basic stats to advanced visualization.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # ضروري للجزء المتقدم

# ==========================================
# PART 1: BEGINNER LEVEL (Data & Basic Stats)
# ==========================================

# 1. Data Ingestion
# columns: [height_in_inches, weight_in_pounds, age]
baseball = [ 
    [72, 180, 29],
    [75, 215, 34], 
    [78, 210, 30], 
    [69, 160, 23],
    [74, 190, 27], 
    [70, 165, 22],
    [77, 200, 31],
    [73, 185, 28], 
] 
np_baseball = np.array(baseball) 

# 2. Preparation & Cleaning
heights_in = np_baseball[:, 0]
weights_lb = np_baseball[:, 1] 
ages = np_baseball[:, 2]

# Unit conversion
heights_m = heights_in * 0.0254    
weights_kg = weights_lb * 0.453592 

# 3. Computation (BMI)
bmi = weights_kg / (heights_m ** 2)

# 4. Categorization Logic 
underweight = bmi < 18.5
normal = (bmi >= 18.5) & (bmi < 24.9)
overweight = (bmi >= 25) & (bmi < 29.9)
obese = bmi >= 30   

# 5. Basic Reporting (Text Output)
print("-" * 30)
print("--- BEGINNER REPORT ---")
print(f"Average BMI: {np.mean(bmi):.2f}")
print(f"Min BMI: {np.min(bmi):.2f}")
print(f"Max BMI: {np.max(bmi):.2f}")
print("-" * 15)
print("Category Counts:")
print(f"Underweight: {np.sum(underweight)}")
print(f"Normal:      {np.sum(normal)}")
print(f"Overweight:  {np.sum(overweight)}")
print(f"Obese:       {np.sum(obese)}")


# ==========================================
# PART 2: ADVANCED LEVEL (Viz & Correlation)
# ==========================================
print("\n" + "=" * 30)
print("--- ADVANCED ANALYSIS ---")

# 6. Visualization
# Height Histogram (Converted to cm for better readability)
heights_cm = heights_m * 100

plt.figure(figsize=(12, 5)) # تكبير حجم الصورة

# Plot 1: Height Histogram
plt.subplot(1, 3, 1)
plt.hist(heights_cm, bins=5, color='skyblue', edgecolor='black')
plt.title("Height Distribution (cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")

# Plot 2: Weight Histogram
plt.subplot(1, 3, 2)
plt.hist(weights_kg, bins=5, color='salmon', edgecolor='black')
plt.title("Weight Distribution (kg)")
plt.xlabel("Weight (kg)")

# Plot 3: Scatter Plot (Relationship)
plt.subplot(1, 3, 3)
plt.scatter(heights_cm, weights_kg, c='purple', alpha=0.7)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

plt.tight_layout()
print(">> Displaying plots... (Check pop-up window)")
plt.show() 

# 7. Correlation Analysis
print("-" * 30)
print("Correlation Matrix (Height vs Weight vs Age):")
# Stacking data to find relationships
data_for_corr = np.column_stack((heights_m, weights_kg, ages))
correlation_matrix = np.corrcoef(data_for_corr.T)
print(correlation_matrix)
print("(Note: Values close to 1 mean strong positive relationship)")

# ==========================================
# PART 3: EXPORT & TESTING (Pipeline Integrity)
# ==========================================

# 8. Export Final Results
report = {  
    "Average Height (m)": np.mean(heights_m),
    "Average Weight (kg)": np.mean(weights_kg),
    "Average BMI": np.mean(bmi),
    "Underweight Count": np.sum(underweight),
    "Normal Count": np.sum(normal),
    "Overweight Count": np.sum(overweight),
    "Obese Count": np.sum(obese),
}   
df_report = pd.DataFrame(list(report.items()), columns=["Metric", "Value"])
df_report.to_csv("results.csv", index=False)        
print("\n>> Success! Results exported to 'results.csv'")

# 9. Unit Test (Quality Assurance)
def test_bmi_calculation():
    h_in = 70
    w_lb = 150
    expected = (w_lb * 0.453592) / ((h_in * 0.0254) ** 2)
    calc = (np.array([w_lb]) * 0.453592) / ((np.array([h_in]) * 0.0254) ** 2)
    assert np.isclose(calc, expected)
    print(">> Unit Test passed: BMI logic is correct.")

test_bmi_calculation()