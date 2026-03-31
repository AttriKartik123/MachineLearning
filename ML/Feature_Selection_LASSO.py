import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

from sklearn.linear_model import Lasso

# Apply Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

# Visualize selected features
plt.bar(X.columns, lasso.coef_)
plt.title('Lasso Regression Feature Importance')
plt.xlabel('Features')
plt.ylabel('Coefficients')
plt.show()