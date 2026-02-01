import numpy as np

#view 1 
a =np.array([1,2,3,4,5])
b = a.view()

print("Original array", a)
print("  View", b)


b[0] = 100
print("After Original array", a)
print(" After change in original", b)