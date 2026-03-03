import numpy as np
import plotly.express as px

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 15, 25])

fig = px.scatter(x, y)   # positional arguments
fig.show()