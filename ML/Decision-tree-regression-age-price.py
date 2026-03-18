import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# 1. Prepare Data (Age of car vs. Price)
# X = Age, y = Price
X = np.array([[1], [2], [3], [5], [7], [8], [9], [10]])
y = np.array([45000, 42000, 37000, 28000, 20000, 15000, 12000, 9000])

# 2. Create and Train the Model
# 'max_depth' limits how many questions the tree can ask
model = DecisionTreeRegressor(max_depth=3)
model.fit(X, y)

# 3. Predict for a 6-year-old car
prediction = model.predict([[6]])
print(f"Predicted price for a 6-year-old car: ${prediction[0]:,.2f}")

# 4. Visualize the "Staircase" effect
X_grid = np.arange(np.min(X), np.max(X), 0.01).reshape(-1, 1)
y_values = model.predict(X_grid)

plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X_grid, y_values, color='blue', label='Tree Prediction')
plt.title('Decision Tree Regression (Car Price)')
plt.xlabel('Age (Years)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()