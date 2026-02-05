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
