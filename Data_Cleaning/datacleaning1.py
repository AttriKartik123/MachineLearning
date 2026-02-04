import numpy as np
import pandas as pd

#df= pd.read_csv("raw_dataset.csv")
df = pd.read_csv("Data_Cleaning/raw_dataset.csv")

#printing first five entries from the csv
print(df.head())
print('\n')

#printing the columns
print(df.columns) 
print('\n')

#FEATURES of COLUMNS
prop=dir(df.columns)
#print(prop)
print('\n')

#Getting columns as an array
print('\n')
ColArray= df.columns.array
print(ColArray)

#getting columns as list
print('\n')
LisArray= df.columns.tolist()
print(LisArray)

#Viewing columns names 
print('\n')
colName = df.columns.view
print(colName)

#VIEWING SUMMARY OF COL NAMES
print('\n')
# sumCol = df.columns.summary()    ------> Its depriciated 

