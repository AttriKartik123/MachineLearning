import numpy as np
from sklearn.linear_model import LinearRegression

# X = [Engine Size (Liters), Mileage (Miles)]
X = np.array([
    [2.0, 50000],
    [3.5, 20000],
    [1.5, 80000],
    [4.0, 5000],
    [2.5, 35000]
])

# y = [Price in Dollars] (Single Column)
y_multiple = np.array([20000, 35000, 12000, 50000, 25000])

# Train the model
model_mult = LinearRegression()
model_mult.fit(X, y_multiple)

# Predict for a car with 3.0L engine and 15,000 miles
test_car = [[3.0, 15000]]
pred = model_mult.predict(test_car)

print("--- Multiple Regression Result ---")
print(f"Predicted Price: ${pred[0]:.2f}")