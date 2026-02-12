import numpy as np
import pandas as pd 

df = pd.read_csv("Data_Cleaning/weather2.csv")
print(df.head())

print("\n")
print(df.columns) 

# changing the columns name day with date 
df.rename(columns={"DAY" : "DATE"} , inplace = True)
print(df.head())

#replace -99999 with 0
df = df.replace("-99999", "0")
print(df.head())

#interpolating
#df["TEMPERATURE"] = df["TEMPERATURE"].interpolate() - becoz we cant interpolate the string values 

