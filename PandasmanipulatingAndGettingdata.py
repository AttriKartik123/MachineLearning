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

#whose name starts with s of string
print('\n')
print(df1[df1['Name'].str.startswith('S')])


#whose name ends with a
print('\n')
print(df1[df1["Name"].str.endswith('a')])

#whose lenght is 6
print('\n')
print(df1[df1["Name"].str.len()==6])

#whose name's 2nd alphabet is e
print('\n')
print(df1[df1["Name"].str[1]== 'e'])

#count
print('\n')
print(df1.count())

#counts 
print(df1.value_counts(df1["Name"]))


#value_counts : specific value counts 
print('\n')
result= df1.value_counts(df1["Gender"])
print(result)

#
print(df1.value_counts(df1["Gender"]=='Female'))


