import numpy as np
import pandas as pd

# Load CSV file
df = pd.read_csv("Data_Cleaning/raw_dataset.csv")

# Print first five rows
print(df.head())
print("\n")

### Attributes and Methods of Str
print('\n')
strMethods = dir(df.columns.str)
#print(strMethods)

### Making Column Name Lower Case
print('\n')
print(df.columns.str.lower())


### Making Column Name upper Case
print('\n')
print(df.columns.str.upper())

#### Making Column Name Title Case
print('\n')
TitleCase = df.columns.str.title()
print("Title case :",TitleCase)

#Replacing empty spaces with underscores
df.columns.str.replace(' ','_')
print(df.head())

import numpy as np
import pandas as pd

# Load CSV file
df = pd.read_csv("Data_Cleaning/raw_dataset.csv")

# Print first five rows
print(df.head())
print("\n")

### Attributes and Methods of Str
strMethods = dir(df.columns.str)

### Making Column Name Lower Case
print(df.columns.str.lower())
print("\n")

### Making Column Name Upper Case
print(df.columns.str.upper())
print("\n")

### Making Column Name Title Case
TitleCase = df.columns.str.title()
print("Title case:", TitleCase)
print("\n")

#  Replacing spaces with underscores (corrected)
df.columns = df.columns.str.replace(' ', '_')
print(df.head())

## Renaming Column Name
df.rename(columns={'Age':'Date of Birth'})
print(df)

### Renaming Column Name /Inplace
df.rename(columns={'Age':'Date of Birth'},inplace=True)
print(df.columns)

print('\n')
print(len(df.columns.values))

