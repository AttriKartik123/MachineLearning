import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

from sklearn.decomposition import FastICA

# Apply ICA
ica = FastICA(n_components=2)
X_ica = ica.fit_transform(X)

# Visualize ICA components
plt.scatter(X_ica[:, 0], X_ica[:, 1], c=y, cmap='plasma')
plt.title('ICA Components')
plt.xlabel('Independent Component 1')
plt.ylabel('Independent Component 2')
plt.show()