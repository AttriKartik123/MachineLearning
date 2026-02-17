#Explode
'''Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

The explode parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed: '''

#Pull the "Apples" wedge 0.2 from the center of the pie:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

myexplode = [0.2 , 0 , 0 ,0]
plt.pie(y , labels= mylabels , explode=myexplode)

