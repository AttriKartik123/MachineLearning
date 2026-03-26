import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Data
X = np.array([1, 2, 3, 5, 8, 10]).reshape(-1, 1)
y = np.array([30000, 28000, 25000, 20000, 15000, 10000])

# Model
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Prediction
predicted_price = regressor.predict([[4]])
print(f"Predicted Price of 4-year-old car: ${predicted_price[0]:,.2f}")

# Visualization (FIXED)
X_grid = np.arange(X.min(), X.max(), 0.1).reshape(-1, 1)
y_pred_grid = regressor.predict(X_grid)

plt.scatter(X, y, label='Actual Prices')
plt.plot(X_grid, y_pred_grid, label='Decision Tree Prediction')

plt.xlabel("Car Age (Years)")
plt.ylabel("Car Price ($)")
plt.title("Decision Tree Regression: Car Age vs Price")
plt.legend()
plt.show()