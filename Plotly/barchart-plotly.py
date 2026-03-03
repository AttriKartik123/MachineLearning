import plotly.express as px
import numpy as np 

xavlues = np.array(["a","b","c","d"])
yvalues = np.array([10,20,30,40])

abc = px.bar(x=xavlues , y=yvalues )
abc.show()