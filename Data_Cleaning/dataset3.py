import pandas as pd
import numpy as np

# Loading and reading the file 
# df = pd.read_csv("Data_Cleaning/unclean_data.csv") ---->>> gives error

# SOLUTION1
df1 = pd.read_csv("Data_Cleaning/unclean_data.csv", encoding='latin1')
print(df1.head())

# INCONSISTENT COLUMN NAMES ------ CHANGE COLUMN NAME TO UPPER 
print(df1.columns)
df1.columns = df1.columns.str.upper()

# Duration to Time (change column name)
df1.rename(columns={'DURATION': 'TIME'}, inplace=True)
print(df1.head())

'''
Missing Data
Add a default value for missing data or use mean to fill it
Delete the row/column with missing data
Interpolate the rows
Replace
To check for missing data
False means no missing data
df.isnull().sum() int
df.isnull().any() bool
'''

print('\n')
nullVal = df1.isnull()
print(nullVal)

# checking null values in columns 
print('\n')
nullCol = df1.isnull().any()
print(nullCol)

# Columns with NAN using True/False
# False means it doesn't have a NAN
print('\n')
columnNan = df1.isnull().any()
print(columnNan)

# for entire dataframe
print('\n')
fullDataframe = df1.isnull().any().any()
print(fullDataframe)

# Columns with NAN using Integer
print('\n')
print(df1.isnull().sum())

# Total Number of Missing NA
print('\n')
print(df1.isnull().sum().sum())

# Adding A Default Value or Filling the Missing Data
print('\n')
print(df1.head())

df_with_0 = df1.fillna(0)
print(df_with_0.head(10))

print('\n')
print(df1['TIME'].mean())

# FILLING WITH MEAN 
df_with_mean = df1['TIME'].fillna(df1['TIME'].mean())
print(df_with_mean)

# Dropping NA
print('\n')
print(df1.head(10))

print('\n')
print(df1.isnull().sum().sum())

# shape
print('\n')
print(df1.shape)

df_drop = df1.dropna()
print(df_drop)

# drop rows having less than 4 non-null values
df_drop_with_condition = df1.dropna(thresh=4)
print('\n')
print("-------------------------------------------------------------------------")
print(df1)
print("-------------------------------------------------------------------------")
print('\n')
print(df_drop_with_condition)


#changing the axis 
df_drop_column = df1.dropna(axis=1)
print(df_drop_column)
