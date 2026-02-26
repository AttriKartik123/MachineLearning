'''import matplotlib.pyplot as plt
import pandas as pd


d = { 'Pid': pd.Series([1,2,3,4,5,6,7]) ,
     'Pname': pd.Series(['Rin' , 'Lux' ,'Pepsi' ,'Eraser' ,'Pen' , 'Pencil' , 'Register']),
     'Prate': pd.Series([85 , 90 , 35,30,96,20,150])
     }

df = pd.DataFrame(d)

for rate in df["Prate"]:
    print(rate)



plt.plot(df["Pname"], df["Prate"]  )
plt.show()
'''

import matplotlib.pyplot as plt
import pandas as pd

# 1. Data
d = {
    'Pname': ['Rin' , 'Lux' ,'Pepsi' ,'Eraser' ,'Pen' , 'Pencil' , 'Register'],
    'Prate': [85 , 90 , 35, 30, 96, 20, 150]
}
df = pd.DataFrame(d)

# 2. Plot
plt.plot(df["Pname"], df["Prate"], marker='o')

# 3. Add numbers above markers
for x, y in zip(df["Pname"], df["Prate"]):
    plt.text(x, y + 5, y, ha='center')

plt.show()