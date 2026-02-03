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


#ADDING A COLUMN USINF COLUMN ASSIGNMENT
#df1["Percentage"] =  (df1["English"] + df1["Maths"] + df1["Science"] + df1["Hindi"] + df1["Punjabi"]) / 5


#Another way of adding percentage
df1["Percentage"] = df1[["English","Maths","Science","Hindi","Punjabi"]].mean(axis=1)

print("After insertion new column the df is :")
print('\n')
print(df1)

#printing namens having the max percentages 
maxx = df1["Percentage"].max()
print('\n')
print(maxx)

# also printing the name of the stuidengt along with percentage marks 

print('\n')
top_student = df1[df1["Percentage"] == maxx][["Name", "Percentage"]]
print(top_student)







#now printing one having minimum percentage
print('\n')
avg_student = df1["Percentage"].min()
print(avg_student)

print('\n')
below_avg = df1[df1["Percentage"] == avg_student] [["Name" , "Percentage"]]
print(below_avg)


# printing those students whose marks are not equals to 88.0
result= df1[df1["Percentage"] != 88.0]
print('\n')
print(result)



