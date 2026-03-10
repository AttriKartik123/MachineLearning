import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Data (House size in square feet)
size = np.array([500, 700, 900, 1100, 1300, 1500]).reshape(-1,1)

# House prices in thousands
price = np.array([100, 150, 200, 250, 300, 350])

# Step 2: Train the model
model = LinearRegression()
model.fit(size, price)

# Step 3: Predict prices
predicted_price = model.predict(size)

# Step 4: Plot the data
plt.scatter(size, price, label="Actual Price")
plt.plot(size, predicted_price, linestyle='--', label="Regression Line")

plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (thousand Rs)")
plt.title("House Size vs Price Prediction")
plt.legend()

plt.show()