import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


temperature = np.array([20, 25, 30, 35, 40, 45]).reshape(-1, 1)  # Temperature in °C
sales = np.array([200, 250, 400, 450, 600, 650])  # Ice Cream Sales in Rs

# Step 2: Train the Linear Regression Model
model = LinearRegression()
model.fit(temperature, sales)

# Step 3: Make Predictions
predicted_sales = model.predict(temperature)

# Step 4: Visualize the Regression Line
plt.scatter(temperature, sales, color='blue', label="Actual Sales")  # Data points
plt.plot(temperature, predicted_sales, color='red', linestyle='--', label="Regression Line")  # Best fit line

# Labels and Title
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales (Rs)")
plt.title("Temperature vs Ice Cream Sales Prediction")
plt.legend()

# Show Plot
plt.show()