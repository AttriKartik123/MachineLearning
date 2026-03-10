import numpy as np
import pickle

# Step 1: Load the saved model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Step 2: New data (house size)
new_house = np.array([[1200]])

# Step 3: Predict price
predicted_price = model.predict(new_house)

print("Predicted house price:", predicted_price)