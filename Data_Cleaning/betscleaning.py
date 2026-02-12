import pandas as pd 
df = pd.read_csv("Data_Cleaning/Bets.csv")

print(df.head(10))

# removing duplicate rows ---> bet id should be unique
df = df.drop_duplicates()
print("\n")
print(df.head())

#splitting the created at columns into two columns named as creation_date and creation_time
# firstly converting them in date time format
df['created_at'] = pd.to_datetime(df['created_at'], dayfirst=True , format = 'mixed')  #day/month/year
#$format='mixed'$ tells Pandas to be flexible and try to figure out the format for each row individually rather than expecting every row to look exactly the same.

