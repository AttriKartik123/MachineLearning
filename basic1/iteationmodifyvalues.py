import numpy as np 

a = np.arange(0 , 50, 6)
a=a.reshape(3,3)

print("The original array is:")
print('/n')
print(a)

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2+x

print("the modified array is:")
print(a)