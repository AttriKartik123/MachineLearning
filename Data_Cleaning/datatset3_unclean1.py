import pandas as pd
import numpy as np

df1 = pd.read_csv("Data_Cleaning/unclean_data1.csv", encoding='latin1')

print(df1.head(10))

# duplicated 
print('\n')
print(df1.duplicated())

# duplicated movie title
print('\n')
print(df1.duplicated('movie_title'))

# dropping the duplicated rows 
print('\n')
print(df1.shape)

df_drop_dup = df1.drop_duplicates('movie_title')
print(df_drop_dup.shape)




#DATAT TYPE INCONSISTENCY
