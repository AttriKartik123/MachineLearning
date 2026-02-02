import pandas as pd 

d= {
    'Name' :pd.Series(['karan', 'Harleen', 'Iman'] , index = [1,2,3]) ,
    'Age' :pd.Series([21,21,21] ) ,
    'Salary' :pd.Series([20000 , 21000 , 20500] , index = [1,2,3] ) ,


}

df=pd.DataFrame(d)
print(df)
