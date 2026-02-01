import numpy as np

# Let us create an array
a = np.array([5, 4, 6, 8, 9])
#Let us create the copy of input array
c = a.copy()

#Now let us check the id of a and c
print("The id of input array a :")
print(id(a))
print("The id of c is:")
print(id(c))

#Now changing the original array
a[0] = 25

# printing both input array and copy
print("The original array:")
print(a)
print("The copy is:")
print(c)