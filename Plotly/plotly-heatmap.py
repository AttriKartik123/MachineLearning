import plotly.express as px
import numpy as np

# Create 2D data (matrix)
data = np.array([
    [10, 20, 30],
    [25, 15, 35],
    [40, 22, 18]
])

fig = px.imshow(data, 
                title="Simple Heatmap",
                labels=dict(x="Columns", y="Rows", color="Value"))

fig.show()


#------------------------

values = np.array([10, 20, 30, 40, 50])

# Convert to 2D (1 row, 5 columns)
heatmap_data = values.reshape(1, -1)

fig = px.imshow(heatmap_data,
                title="Single Row Heatmap",
                labels=dict(color="Value"))

fig.show()