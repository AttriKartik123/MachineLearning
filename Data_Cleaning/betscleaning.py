import pandas as pd 
df = pd.read_csv("Data_Cleaning/Bets.csv")
print("\n")
print(len(df))
print(df.shape)

#print(df.head(10))

# removing duplicate rows ---> bet id should be unique
df = df.drop_duplicates()

#splitting the created at columns into two columns named as creation_date and creation_time
# firstly converting them in date time format
df['created_at'] = pd.to_datetime(df['created_at'], dayfirst=True , format = 'mixed')  #day/month/year
#$format='mixed'$ tells Pandas to be flexible and try to figure out the format for each row individually rather than expecting every row to look exactly the same.

# --- CRITICAL CHANGE AREA ---
# We find the position of 'created_at' BEFORE we create the new columns.
# If we create them first (like in your previous draft), they go to the end of the dataframe.
position = df.columns.get_loc('created_at')

# We insert Date first at the position, then Time at position + 1 
# This ensures they appear exactly where 'created_at' used to be.
df.insert(position, 'creation_date', df['created_at'].dt.date)
df.insert(position + 1, 'creation_time', df['created_at'].dt.time)

# now we will drop the created at column 
df = df.drop(columns=["created_at"])
# ----------------------------

print("\n")
print(df.head())

    
# now handling missing values 
#option a :Check for nulls: print(df.isnull().sum())
print("\n")
print(df.isnull().sum())

print("\n")
print(df.head())

# 5. HANDLING MISSING VALUES (Nulls)
# Since your check showed 0 nulls, this is "safety" code.
# For money columns, we fill empty cells with 0.0
print("\n")
df["turnover"] = df["turnover"].fillna(0.0)
print(df.head())


print("\n")
print(len(df))
print(df.shape)


#  FINAL POLISH :
# After dropping duplicates, the row index will have gaps (e.g., 1, 2, 4, 5).
# This resets it to be continuous (0, 1, 2, 3).
df = df.reset_index(drop=True)


print("--- CLEANING COMPLETE ---")
print(df.head())



#final
df.to_csv("Data_Cleaning/Bets_Cleaned.csv" , index = False)
print('File is saved and cleaned successfully ')