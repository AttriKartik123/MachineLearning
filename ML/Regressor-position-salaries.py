import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
dataset = pd.read_csv('Position_Salaries.csv')

# Features and target
X = dataset.iloc[:, 1:2].values   # keep it 2D
y = dataset.iloc[:, -1].values

# Train model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

#predict
y_pred = regressor.predict([[6.5]])
print("Predicted salary:", y_pred)


X_grid = np.arange(X.min(), X.max(), 0.01)
X_grid = X_grid.reshape(-1, 1)

plt.scatter(X, y)
plt.plot(X_grid, regressor.predict(X_grid))
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()