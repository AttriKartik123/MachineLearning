#Creating Bars
#With Pyplot, you can use the bar() function to draw bar graphs:
import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A","B","C","D"])
y = np.array([10,20,30,40])

plt.bar(x,y)
plt.show()