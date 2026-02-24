import pandas as pd
d={'empid':pd.Series([1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],index=[1,2,3,4,5,6,7,8,9,10]),
   'Ename':pd.Series(['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],index=[1,2,3,4,5,6,7,8,9,10]),
   'Job':pd.Series(['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen',],index=[1,2,3,4,5,6,7,8,9,10]),
   'salary':pd.Series([55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],index=[1,2,3,4,5,6,7,8,9,10]),
   'comm':pd.Series([100,200,100,500,300,500],index=[1,3,5,7,9,10]),
   'Deptno':pd.Series([10,20,10,10,30,10,20,10,30,40],index=[1,2,3,4,5,6,7,8,9,10])}
df=pd.DataFrame(d)
print(df)


#Default index starts by 0 
import pandas as pd

d1={'empid':[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    'Ename':['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
    'Job':['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen'],
    'salary':[55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],
    'comm':[100,'Nan',200,'Nan',100,'Nan',500,'Nan',300,500],
    'Deptno':[10,20,10,10,30,10,20,10,30,40]}

df=pd.DataFrame(d1)
print(df)