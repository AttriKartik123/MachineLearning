import pandas as pd

d1={'empid':[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    'Ename':['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
    'Job':['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen'],
    'salary':[55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],
    'comm':[100,'Nan',200,'Nan',100,'Nan',500,'Nan',300,500],
    'Deptno':[10,20,10,10,30,10,20,10,30,40]}

df=pd.DataFrame(d1)
print(df)



# UNDERSTANDING THE HEAD IN PANDAS -> First five records 
print('\n')
print(df.head())


# UNDERSTANDING THE TAIL IN PANDAS -> last 5 records
print('\n')
print(df.tail())


#UNDERSTADING THE INFO 
print('\n')
print(df.info())



#dtatypes  -> no parenthesis
print('\n')
print(df.dtypes)


#head with customzed 
print('\n')
print(df.head(7))


#setoptions     - customised head columns to see 
pd.set_option('display.max_columns', 4)
print(df.head())

# getting desired columns
print(df["empid"])

#getting two columns
print(df[["Ename", "empid"]])


#UNDERSTANDING SHAPE 
print('\n')
print(df[["Ename" , "empid"]].shape)


# .SET OPTIONS -------------->>>>> display.max_columns and display.max_rows
print('\n')
pd.set_option('display.max_columns', 2)
pd.set_option('display.max_rows', 5)
print(df)

