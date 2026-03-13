import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Multiple Inputs (Size, Rooms, Age)
features = np.array([ 
    [500, 1, 20],
    [700, 2, 15],
    [900, 3, 10]
])

price = np.array([100, 150, 200])

model = LinearRegression()
model.fit(features, price)

# Predict based on the 3D features
predicted_price = model.predict(features)

# Extract ONLY the first column (Size) for the 2D graph
size = features[:, 0]

# USE 'size' instead of 'features' here
plt.scatter(size, price, label="Actual Price", color='blue')  # instead of size , features shouldn't be passed becoz it works on only 1d  , thats why shape and size 
plt.plot(size, predicted_price, linestyle='--', label="Regression Line", color='red')

plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (thousand Rs)")
plt.title("House Size vs Price Prediction")
plt.legend()

plt.show()