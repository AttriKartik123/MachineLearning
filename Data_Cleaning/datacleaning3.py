import numpy as np
import pandas as pd

# Load CSV file
df = pd.read_csv("Data_Cleaning/raw_dataset.csv")

# Print first five rows
print(df.head())
print("\n")

# Renaming column using index
df.columns.values[7] = 'Email Address'
print(df.columns)

# selecting all columns except once 
print('\n')
df = df.loc[:, df.columns != 'SALARY']
print(df.columns)

#df.loc[:, df.columns != 'SALARY'].columns



#### Select Column Names Except One Using Difference
print('\n')
df.columns.difference(['SALARY'])
print(df.columns)


## Select Column Names that Begins with a Word or Character
print('\n')
print(df.filter(like='STREET').columns)


#### Select Column Names that Begins with a Word or Character
print('\n')
print(df.loc[:,df.columns.str.startswith('STREET')].columns)

### Select Column Names that ENDS with a Word or Character
print(df.loc[:,df.columns.str.endswith('ame')].columns)



### Select Column Names that ENDS with a Word or Character Using Filter and Regex name$
print('\n')
regex=df.filter(regex='ame$',axis=1).columns
print(regex)

### Select A Group of Column Names
print('\n')
print(df.columns.values[1:4])

print('\n')
print(df.columns[0:4])

