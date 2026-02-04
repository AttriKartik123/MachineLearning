import pandas as pd

df = pd.read_csv("Data_Cleaning/dataset.csv")

print(df.head())

# -------------------- Columns consistency --------------------
print(df.columns)

# lowercasing the string cases 
Lower = df.columns.str.lower()
print(Lower)

# permanent shifting towards the lowercase 
print('\n')
df.columns = df.columns.str.lower()
print(df.columns)

# renaming columns 
print('\n')
df.rename(columns={'full name': 'full_name', 'date of birth': 'date_of_birth'}, inplace=True)
print(df.columns)

# -------------------- Splitting full name --------------------
print('\n')
print(df.full_name)

print('\n')
print(df.full_name.str.split(" "))

# Get first name
df['firstname'] = df.full_name.str.split(" ").str.get(0)

# getting last name in a single line 
print('\n')
df['lastname'] = df.full_name.str.split(" ").str.get(1)
print(df['lastname'])

# storing it in df1 variable
print('\n')
df1 = df

# -------------------- Method 2 Using Expand --------------------
print('\n')
print(df1.full_name.str.split(" ", expand=True))

# using expand and n=1
print('\n')
print(df1.full_name.str.split(" ", n=1, expand=True))

# using expand and n=2
print('\n')
print(df1.full_name.str.split(" ", n=2, expand=True))

print('\n')
print(df.head())

# -------------------- Income column cleaning --------------------
print('\n')
print(df['income.1'])

# printing datatype of the column
print('\n')
dtCol = df['income.1'].dtype
print(dtCol)

# Replace $ with EURO
print('\n')
df['income.1'] = df['income.1'].astype(str).str.replace('$', 'EURO ', regex=False)
print(df.head())

# -------------------- Salary column operations --------------------
print('\n')
print(df.salary)

# as boolean
print('\n')
print(df.salary.astype(str).str.contains('19', na=False))

# Get the values of entire rows
print('\n')
print(df[df.salary.astype(str).str.contains('19', na=False)])

# Check For Multiple Expression
print('\n')
print(df.salary.astype(str).str.contains('19|17', na=False))

# regex = true (same as above, but explicit)
print('\n')
print(df.salary.astype(str).str.contains('19|17', regex=True, na=False))

# using match (checks only from start of string)
print('\n')
print(df.salary.astype(str).str.match('19', na=False))

# -------------------- Quote column --------------------
print('\n')
print(df.quote)

# Find rows where quote starts with "Operative"
print('\n')
print(df[df.quote.astype(str).str.match('Operative', na=False)])

# -------------------- Joining columns --------------------
print('\n')
joined = df.firstname + df.email
print(joined)

# method two
print('\n')
joinedName = df.firstname + "_" + df.lastname
print("joinedName:", joinedName)

# -------------------- Text statistics --------------------
# Using str.count() to count number of spaces (+1 = words)
print('\n')
print(df.quote.astype(str).str.count(' ') + 1)

# Using str.split().map(len) to get number of words per row
print('\n')
print(df.quote.astype(str).str.split().map(len))

# Using str.split().apply(len) to get number of words per row
print('\n')
print(df.quote.astype(str).str.split().apply(len))

# Get frequency of word counts
print('\n')
print(df.quote.astype(str).str.split().apply(len).value_counts())


print('\n')
print(df.quote)