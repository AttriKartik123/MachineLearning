import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Training Data (House Size in sq ft)
house_size = np.array([500, 700, 900, 1100, 1300, 1500]).reshape(-1,1)

# House prices in thousand Rs
house_price = np.array([100, 150, 200, 250, 300, 350])

# Step 2: Train the Model
model = LinearRegression()
model.fit(house_size, house_price)

# Step 3: Save the Model using Pickle
pickle.dump(model, open("house_price_model.pkl", "wb"))

print("Model saved successfully!")

# Step 4: Load the Saved Model
loaded_model = pickle.load(open("house_price_model.pkl", "rb"))

# Step 5: Predict Price for New House
new_house = np.array([[1200]])   # size = 1200 sq ft
predicted_price = loaded_model.predict(new_house)

print("Predicted price for 1200 sq ft house:", predicted_price)