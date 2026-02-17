import numpy as np 
import matplotlib.pyplot as plt

x = np.array([10,20,30,40,50])

plt.plot(x)

#TITLE POSITIONING
plt.title("This is title" , loc='left')
plt.xlabel("this is x label")
plt.ylabel("this is y label")

plt.show()



