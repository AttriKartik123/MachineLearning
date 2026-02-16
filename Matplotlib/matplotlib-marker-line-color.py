import matplotlib.pyplot as plt
import numpy as np

yvalues=np.array([10,20,30,40,50,60])

plt.plot(yvalues,'o:g',mec='red',mfc='red') #takes x axis as 0 1 2 3 4 by default
#marker-edge-color and marker-face-color

plt.show()