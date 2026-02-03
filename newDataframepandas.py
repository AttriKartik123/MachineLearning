import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Sharan","Jasleen","Jagroop","Seema","Meena","Teena","Deena","Taj","Raj","Pawan"],
    "Rollno": [1,2,3,4,5,6,7,8,9,10],
     "Gender":["Female","Female","Male","Female","Female","Female","Female","Female","Male","Male"],
        "English":[90,56,67,87,67,89,89,89,78,90],
     "Maths":[45,56,67,87,67,89,89,89,78,90],
     "Science":[45,53,67,86,67,84,89,89,73,90],
     "Hindi":[56,56,65,87,68,89,86,89,73,95],
     "Punjabi":[66,56,64,87,69,89,87,89,78,93]})

print(df1)

#describe
print('\n')
print(df1.describe())


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)   # It gives all the rows and columns in the dataframe 

#loc  and iloc
print('\n') 
d=df1.loc[1:11]
print(d)


#GETTING COLUMNS DATA
print('\n')
print(d[["Name","Gender"]])

#ADDING A RECORD USING LOC
print('\n')
df1.loc[9]=[ "DhruvJaggi" , 55 , "Custom" , 33,444,66,33,56]
print(df1)