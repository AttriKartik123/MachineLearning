import numpy as np
from sklearn.linear_model import LinearRegression

# X remains the same: [Engine Size, Mileage]
X = np.array([
    [2.0, 50000],
    [3.5, 20000],
    [1.5, 80000],
    [4.0, 5000],
    [2.5, 35000]
])

# y = [[Price, Days_to_Sell]] (Two Columns)
y_multivariate = np.array([
    [20000, 30],
    [35000, 15],
    [12000, 45],
    [50000, 10],
    [25000, 20]
])

# Train the model
model_mv = LinearRegression()
model_mv.fit(X, y_multivariate)

# Predict for the same car (3.0L engine, 15,000 miles)
test_car = [[3.0, 15000]]
preds = model_mv.predict(test_car)

print("--- Multivariate Regression Results ---")
print(f"Predicted Price: ${preds[0][0]:.2f}")
print(f"Predicted Days to Sell: {preds[0][1]:.1f} days")