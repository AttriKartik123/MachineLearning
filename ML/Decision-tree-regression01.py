import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Step 1: Define the Dataset (Car Age vs Price)
X = np.array([1, 2, 3, 5, 8, 10]).reshape(-1, 1)  # Car Age
y = np.array([30000, 28000, 25000, 20000, 15000, 10000])  # Car Price

# Step 2: Train the Decision Tree Model
# Added max_depth=3 to prevent potential overfitting on larger datasets
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Step 3: Make Predictions
age_to_predict = 4
predicted_price = regressor.predict([[age_to_predict]])
print(f"Predicted Price of {age_to_predict}-year-old car: ${predicted_price[0]:,.2f}")

# Step 4: Visualize Decision Tree Regression
# We use a higher resolution grid to see the "staircase" effect of the model
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1) 
y_pred_grid = regressor.predict(X_grid)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='red', label='Actual Data (Training)')
plt.plot(X_grid, y_pred_grid, color='blue', label='Decision Tree Prediction')

# Highlight the prediction for the 4-year-old car
plt.scatter([[4]], predicted_price, color='green', s=100, label='Prediction for Age 4', zorder=5)

plt.xlabel("Car Age (Years)")
plt.ylabel("Car Price ($)")
plt.title("Decision Tree Regression: Car Age vs Price")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()