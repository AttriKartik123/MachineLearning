import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Data: [Size, Rooms]
X = np.array([
    [500, 1], [700, 2], [900, 2], 
    [1100, 3], [1300, 3], [1500, 4]
])
y = np.array([100, 150, 200, 250, 300, 350])

# 2. Train Model
model = LinearRegression()
model.fit(X, y)

# 3. Setup the 3D Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 4. Create the "Best Fit" Plane
# We create a grid of Size (x) and Rooms (y) to predict the Price (z)
x_grid, y_grid = np.meshgrid(np.linspace(500, 1500, 10), np.linspace(1, 4, 10))
# Combine grid into [Size, Rooms] pairs for the model to predict
grid_combined = np.c_[x_grid.ravel(), y_grid.ravel()]
z_predict = model.predict(grid_combined).reshape(x_grid.shape)

# 5. Drawing
ax.scatter(X[:, 0], X[:, 1], y, color='blue', s=100, label="Actual Houses") # Actual Dots
ax.plot_surface(x_grid, y_grid, z_predict, color='red', alpha=0.3)          # Prediction Plane

ax.set_xlabel('Size (sq ft)')
ax.set_ylabel('Rooms')
ax.set_zlabel('Price (k Rs)')
plt.title("Simple 3D Multiple Regression")
plt.show()