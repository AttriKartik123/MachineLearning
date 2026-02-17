#Histogram
#A histogram is a graph showing frequency distributions.
#t is a graph showing the number of observations within each given interval.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)  #“Create 250 random numbers that are centered around 170, and usually vary by about 10.”

plt.hist(x)
plt.show() 