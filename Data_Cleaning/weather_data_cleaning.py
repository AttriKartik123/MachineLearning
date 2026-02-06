import numpy as np 
import pandas as pd

df = pd.read_csv('weather_data.csv')

df.columns = df.columns.str.capitalize()    # CAPITALIZED THE WORDS 
print(df.head(5))

df.replace({'Temperature': -99999, 'Windspeed': -99999, 'Event': 0}, np.nan, inplace=True)

# Fixing dates 
print('\n')
df['Day'] = pd.to_datetime(df['Day'])
print(df.head(5))

# Filling missing texts - like filling nan 
df['Event'] = df['Event'].fillna('No Event')
print('\n')
print(df)

#Drop duplicates   06 
print("------------------------")
df.drop_duplicates(subset=['Day'], inplace=True)
print(df)

#interpolating ---> filling apropriate values in place of nan 
df['Temperature'] = df['Temperature'].interpolate()
df['Windspeed'] = df['Windspeed'].interpolate()


#printing the dataset
print('\n')
print(df)