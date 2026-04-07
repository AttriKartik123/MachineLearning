import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Load dataset
data = 'pulsar_stars.csv'
df = pd.read_csv(data)

# FIX: Remove leading/trailing spaces from column names (common in this CSV)
df.columns = df.columns.str.strip()

# View dimensions
print(f"Dataset Shape: {df.shape}")

# Preview the first 5 rows
print(df.head())