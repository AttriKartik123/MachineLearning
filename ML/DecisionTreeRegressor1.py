import pandas as pd 
pd.set_option("display.max_columns", 30)
df = pd.read_csv("housing_data.csv")
df.isna().sum()

X = df.drop(columns = ['price', 'id', 'date'])
y = df['price']

from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeRegressor 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state = 1)
rg = DecisionTreeRegressor() 
rg.fit(X_train, y_train)

y_predict = rg.predict(X_test)
mean_absolute_error(y_test, y_predict)

y_predict_train = rg.predict(X_train)
mean_absolute_error(y_train, y_predict_train)


parameters = {'max_depth': [6, 7, 8, 9, 10, 12], 'max_leaf_nodes': [36, 40, 44, 48, 50, 52],
             'max_features': [10, 12, 14, 16, 18]}
rg1 = DecisionTreeRegressor()
rg1 = GridSearchCV(rg1, parameters)
rg1.fit(X_train, y_train)
y_predict = rg1.predict(X_test)
mean_absolute_error(y_test, y_predict)

y_predict_train = rg1.predict(X_train)
mean_absolute_error(y_train, y_predict_train)