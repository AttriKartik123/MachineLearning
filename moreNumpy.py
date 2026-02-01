import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Array:\n", a)

# 1️ Array-wise sum
print("\nSum of all elements:", a.sum())

# 2️ Minimum value
print("Minimum value:", a.min())

# 3️ Maximum value along axis=0 (column-wise)
print("Maximum value along axis=1:", a.max(axis=1))
print("Maximum value along axis=0:", a.max(axis=0))

# 4️ Cumulative sum along axis=0 (column-wise running total)
print("Cumulative sum along axis=0:\n", a.cumsum(axis=0))
