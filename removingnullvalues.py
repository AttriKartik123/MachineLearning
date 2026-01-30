import numpy as np

a = np.array([np.nan, 1, 12, np.nan, 3, 41, 54])
print("Before removing" , a)

print("After omitting NaN the output array is :")

print(a[~np.isnan(a)])


