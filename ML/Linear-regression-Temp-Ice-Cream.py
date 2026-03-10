import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Prepare the Data
temperature = np.array([20, 25, 30, 35, 40, 45]).reshape(-1, 1)  # Temperature in °C
sales = np.array([200, 250, 400, 450, 600, 650])  # Ice Cream Sales in Rs

# Step 2: Train the Linear Regression Model
model = LinearRegression()
model.fit(temperature, sales)

# Step 3: Make Predictions
predicted_sales = model.predict(temperature)

# Step 4: Visualize the Regression Line
plt.scatter(temperature.flatten(), sales, color='blue', label="Actual Sales")  
plt.plot(temperature.flatten(), predicted_sales, color='red', linestyle='--', label="Regression Line")

# Labels and Title
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales (Rs)")
plt.title("Temperature vs Ice Cream Sales Prediction")
plt.legend()

# Show Plot
plt.show()