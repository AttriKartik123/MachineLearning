import pandas as pd
import numpy as np

'''Task 1: Reading and Inspection'''

data = pd.read_csv('Data_Cleaning/Melbourne.csv')
OrgData = data
print(data)

print('\n')
print(data.shape)

print('\n')
print(data.info())


'''Task 2: Cleaning the Data
### Subtask 2.1: Inspect Null values
Find out the number of Null values in all the columns and rows. Also, find the percentage of Null values in each column. Round off the percentages upto two decimal places.'''


#Write your code for column-wise null count here
print('\n')
print(data.isnull().sum(axis=0).sort_values(ascending=False))

#Write your code for row-wise null count here
print('\n')
print(data.isnull().sum(axis=1).sort_values(ascending=False))

#Find Columns having at least one missing value
print(data.isnull().sum() >0)

#Find Columns having at least one missing value using any() function
d = data.isnull().any()
print('\n')
print(d)


#By default any() operates on columns
e = data.isnull().any(axis=0)
print('\n')
print(e)

#Find the missing value row wise if any found return True/False
data.isnull().any(axis=1)

print(data[data.isnull().any(axis=1)])   #RETURNS ACTUAL LINESSSSSSS


#columns having all missing values 
data.isnull().any(axis=0)   #axis = 0 columns
#Rows having all missing values
data.isnull().all(axis=1)

print(data.isnull().all(axis=1).sum())


#Summing up the missing values (column-wise) : Cal in %
print("Length of data :",len(data))    # down the rows

colWise = data.isnull().sum(axis=0).sort_values(ascending=False)/len(data)*100  #This line calculates the percentage of missing values in each column.
print(colWise)


#Removing the three columns where the max null value percentage
col = data.isnull().sum(axis=0).sort_values(ascending=False).head(3).index.values
print(col)

