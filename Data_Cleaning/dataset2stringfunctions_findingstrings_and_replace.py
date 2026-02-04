import pandas as pd

df = pd.read_csv("Data_Cleaning/dataset.csv")

print(df.head())

#columns consistency 
print(df.columns)

#lowercasing the string cases 
Lower= df.columns.str.lower()
print(Lower)

# permanent shifting towards the lowercase 
print('\n')
df.columns = df.columns.str.lower()
print(df.columns)

#renaming columns 
print('\n')
df.rename(columns={'full name' : 'full_name' , 'date of birth' : 'date_of_birth'} , inplace = True)
print(df.columns)

#splitting column into multiple
print('\n')
print(df.full_name)

print('\n')
df.full_name.str.split(" ")

#Get first name of the split 
df.full_name.str.split(" ").str.get(0)


#getting last name in a single linme 
print('\n')
df['lastname'] = df.full_name.str.split(" ").str.get(1)
print(df['lastname'])

#storing it in df1 variable
print('\n')
df1 = df

#-------------------------------------------------> next -------------------------------------------------->
# Method 2 Using Expand 
print('\n')
df1.full_name.str.split(" ",expand=True)
print(df1.full_name)

# using expand and n=1 to group all other into one column
df1.full_name.str.split(" ", n=1 , expand=True)
print('\n')
print(df1.full_name)

#
print(df.head())



#------------------------------------------------------------------------> CONTINUED ---------------------------------------------->
print(df['income.1'])

#printing dattype of the column
print('\n')
dtCol=df['income.1'].dtype
print(dtCol)

#Replace with empty
print('\n')
# Replace with Empty
df['income.1'] = df['income.1'].str.replace('$', 'EURO ', regex=False)
print(df.head())




#
print(df.head())
print('\n')


print(df.salary)


