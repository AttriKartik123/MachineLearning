import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
# Ensure the "ML" folder exists in your current directory
try:
    df = pd.read_csv("ML/heart.csv")
except FileNotFoundError:
    print("Error: 'heart.csv' not found in the 'ML' folder. Please check your file path.")
    # Fallback to current directory if ML folder isn't found
    df = pd.read_csv("heart.csv")

# 2. Rename columns for readability
to_rename = {
    'age': 'Age', 'sex': 'Sex', 'cp': 'Chest Pain', 'trestbps': 'BPS', 
    'chol': 'Cholesterol', 'fbs': 'FBS', 'restecg': 'RestECG', 
    'thalach': 'Thalach', 'exang': 'EIA', 'oldpeak': 'Oldpeak',
    'slope': 'Slope', 'ca': 'CA', 'thal': 'Thal', 'target': 'Target'
}
df.rename(columns=to_rename, inplace=True)

# 3. Categorical Visualizations (Count Plots)
# We use plt.figure() to create a new window for each plot
plt.figure(figsize=(10, 5))
sns.countplot(x='Age', data=df)
plt.title("Distribution of Age")

plt.figure(figsize=(10, 5))
sns.countplot(x='Sex', data=df)
plt.title("Count by Sex (1=Male, 0=Female)")

plt.figure(figsize=(10, 5))
sns.countplot(x='Chest Pain', data=df)
plt.title("Chest Pain Types")

# 4. Numerical Visualizations
plt.figure(figsize=(10, 5))
sns.histplot(df["Cholesterol"], color='c', kde=True) 
plt.title("Cholesterol Distribution with KDE")

# 5. Relationship Visualizations
# Jointplot creates its own figure, so no need for plt.figure()
sns.jointplot(x='Thalach', y='Oldpeak', data=df, kind='hex', color='blue')

# 6. Multivariate Analysis (Pairplot)
# We select a subset of columns to compare
df1 = df[['Sex', 'BPS', 'Cholesterol', 'Thalach', 'Oldpeak']]
# 'hue' helps us see the difference between groups (Sex) across all charts
sns.pairplot(df1, hue='Sex', palette='Set1')

# 7. Final command to render all plots
plt.show()