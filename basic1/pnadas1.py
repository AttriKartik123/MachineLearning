import pandas as pd 

d= {
    'Name' :pd.Series(['karan', 'Harleen', 'Iman', 'Kaniesha', 'Jatin'] , index = [1,2,3,4,5]) ,
    'Age' :pd.Series([21,21,21,22,21] ),
    'Salary' :pd.Series([20000 , 21000 , 20500 , 500 , 80000] , index = [1,2,3,4,5] ) ,


}

df=pd.DataFrame(d)
print(df)



# why float ???
'''Age series has no index, so pandas assigns default index:

0, 1, 2, 3, 4


But the other columns use:

1, 2, 3, 4, 5


So pandas tries to align rows by index. Because index 5 is missing in Age, pandas inserts:

NaN (Not a Number)


And since NaN is a float, pandas converts the whole column to float.'''

import pandas as pd 

d= {
    'Name' :pd.Series(['karan', 'Harleen', 'Iman'] , index = [1,2,3]) ,
    'Age' :pd.Series([21,21,21]  , index = [1,2,3]) ,
    'Salary' :pd.Series([20000 , 21000 , 20500] , index = [1,2,3] ) ,


}

df=pd.DataFrame(d)
print(df)
