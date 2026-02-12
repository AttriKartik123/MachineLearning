import numpy as np
import pandas as pd

# Load CSV file
df = pd.read_csv("Data_Cleaning/raw_dataset.csv")

# Print first five rows
print(df.head())
print("\n")

# Converting column names to Series
colToSeries = df.columns.to_series() 
print(colToSeries)
print("\n")

# Converting column names to DataFrame
colToData = df.columns.to_frame()
print(colToData)

# Check to see if column names contains a phrase
print("\n")
print(df.columns.__contains__('First Name'))

## Check to see if column names are duplicated
print("\n")
print(df.columns.duplicated())


