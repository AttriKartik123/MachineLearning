import pandas as pd 
from sklearn.linear_model import LinearRegression

df = pd.read_csv("cars.csv")
print(df.head())

# 2. Define Features (X) and Target (y)
# We use 'Volume' (Engine Size) and 'Weight' to predict 'CO2'

X = df[['Volume' , 'Weight']]
Y = df['CO2']

#3 Create and train the model 
model = LinearRegression()

model.fit(X , Y)

# 4. Predict the CO2 emission of a car 
# where engine volume is 1300cm3 and weight is 2300kg:

predictedCO2= model.predict([[1300 , 2300]])


print("--- RESULTS ---")
print(f"I predict this car will emit {predictedCO2[0]:.1f} grams of CO2.")
print(f"Every 1cc of engine size adds {model.coef_[0]:.4f}g to the total.")
print(f"Every 1kg of car weight adds {model.coef_[1]:.4f}g to the total.")