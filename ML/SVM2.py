import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# 1. Load dataset (using the relative path from your project root)
try:
    data = 'ML/pulsar_stars.csv'
    df = pd.read_csv(data)
except FileNotFoundError:
    data = 'pulsar_stars.csv'  # Fallback if run from inside the folder
    df = pd.read_csv(data)

# 2. Data Cleaning: Strip spaces and rename columns
df.columns = df.columns.str.strip()
df.columns = ['IP Mean', 'IP Sd', 'IP Kurtosis', 'IP Skewness', 
              'DM-SNR Mean', 'DM-SNR Sd', 'DM-SNR Kurtosis', 'DM-SNR Skewness', 'target_class']

# 3. Data Inspection
print(f"Dataset Shape: {df.shape}\n")
print("--- First 5 Rows ---")
print(df.head(), "\n")

print("--- Target Class Distribution ---")
# Fixed np.float error by using standard len()
print(df['target_class'].value_counts() / len(df), "\n")

print("--- Missing Values ---")
print(df.isnull().sum(), "\n")

print("--- Summary Statistics ---")
print(round(df.describe(), 2))

# 4. Visualization: Outlier detection using Boxplots
plt.figure(figsize=(24, 20))

columns_to_plot = df.columns[:-1] # All columns except target_class

for i, col in enumerate(columns_to_plot, 1):
    plt.subplot(4, 2, i)
    df.boxplot(column=col)
    plt.title(f'Boxplot of {col}')
    plt.ylabel('Value')

plt.tight_layout()
plt.show()