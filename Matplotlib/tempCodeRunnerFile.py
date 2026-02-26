import matplotlib.pyplot as plt
import pandas as pd


d = { 'Pid': pd.Series([1,2,3,4,5,6,7]) ,
     'Pname': pd.Series(['Rin' , 'Lux' ,'Pepsi' ,'Eraser' ,'Pen' , 'Pencil' , 'Register']),
     'Prate': pd.Series([85 , 90 , 35,30,96,20,150])
     }

df = pd.DataFrame(d)

for i in range(d['Prate']):
    print(i)

plt.plot(df["Pname"], df["Prate"] , marker = df["Prate"] )
plt.show()