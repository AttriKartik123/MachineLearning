import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    "Name": [None,"Jasleen","Jagroop","Seema","Meena","Teena","Deena","Taj","Raj","Pawan"],
    "Rollno": [1,2,3,4,5,6,7,8,9,10],
    "Gender":["Female","Female","Male","Female","Female","Female","Female","Female","Male","Male"],
    "English":[90,56,67,87,67,89,89,89,78,90],
    "Maths":[45,56,67,87,67,89,89,89,78,90],
    "Science":[45,53,67,86,67,84,89,89,73,90],
    "Hindi":[56,56,65,87,68,89,86,89,73,95],
    "Punjabi":[66,56,64,87,69,89,87,89,78,93]
})

print(df1)

# ADDING Percentage column
df1["Percentage"] = df1[["English","Maths","Science","Hindi","Punjabi"]].mean(axis=1)
print('\n')
print(df1)

# isnull
print('\n')
result = df1["Name"].isnull().values.any()
print(result)

# OR condition
result1 = df1[(df1["Percentage"] == 66.0) | (df1["Percentage"] == 88.0)]
print("\nRows with Percentage 66 or 88:")
print(result1)

# AND condition
result2 = df1[(df1["Percentage"] == 66.0) & (df1["Percentage"] == 88.0)]
print("\nRows with Percentage 66 and 88:")
print(result2)

#  NOT IN condition using ~isin()    ----> Gives those lines whose percentages is in 66 or 88
result3 = df1[~df1["Percentage"].isin([66.0, 88.0])]
print("\nRows whose Percentage is NOT 66 or 88:")
print(result3)
