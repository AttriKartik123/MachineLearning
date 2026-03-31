import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Apply RFE
rfe_selector = RFE(estimator=RandomForestClassifier(), n_features_to_select=2)
X_rfe = rfe_selector.fit_transform(X, y)

# Visualize selected features
selected_features_rfe = X.columns[rfe_selector.get_support()]
plt.bar(selected_features_rfe, rfe_selector.ranking_[rfe_selector.get_support()])
plt.title('RFE Selected Features')
plt.xlabel('Features')
plt.ylabel('Ranking')
plt.show()