import numpy as np

a = np.array([[11,2,3,4],[29,4,15,6],[11,21,39,31]])
print("The array is :")
print(a)


at = a.T
print(" Transpose of matrix is:" , a.T)


print(at)

print("Iterating over the array: ")
for x in np.nditer(at) :
    print(x , end=' ')