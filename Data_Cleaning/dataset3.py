import pandas as pd
import numpy as np

#Loading and reading the file 

#df = pd.read_csv("Data_Cleaning/unclean_data.csv") ---->>> gives error

#SOLUTION1
df1 = pd.read_csv("Data_Cleaning/unclean_data.csv" , encoding='latin1')

print(df1.head())


#INCONSISTENT COLUMN NAMES ------ CHANGE COLUMN NAME TO UPPER 
print(df1.columns)
df1.columns = df1.columns.str.upper()


#Duration to Time(change column name)
df1.rename(columns = {'DURATION':'TIME'})
print(df1.head())



'''Missing Data
Add a default value for missing data or use mean to fill it
Delete the row/column with missing data
Interpolate the rows
Replace
To check for missing data
False means no missing data
df.isnull().sum() int
df.isnull().any() bool'''

print('\n')
nullVal=df1.isnull()
print(nullVal)



#checking null values in columns 
print('\n')
nullCol = df1.isnull().any()
print(nullCol)


# Columns with NAN using True/False
# False means it doesn't have a NAN
print('\n')
columnNan=df1.isnull().any()
print(columnNan)


#for entire dataframe
# For entire DataFrame
print('\n')
fullDataframe=df1.isnull().any().any()
print(fullDataframe)

# Columns with NAN using Integer
print('\n')
print(df1.isnull().sum())

# Total Number of Missing NA
print('\n')
print(df1.isnull().sum().sum())



#Adding A Default Value or Filling the Missing Data
