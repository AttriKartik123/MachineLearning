import pandas as pd 
df = pd.read_csv("Data_Cleaning/Bets.csv")

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