import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array:", a)

# 1️ Mean
print("\nMean:", np.mean(a))

# 2️ Median
print("Median:", np.median(a))

# 3️ Correlation Coefficient (with another array)
b = np.array([12, 18, 33, 39, 52])
print("Correlation Coefficient:\n", np.corrcoef(a, b))

# 4️ Standard Deviation
print("Standard Deviation:", np.std(a))
