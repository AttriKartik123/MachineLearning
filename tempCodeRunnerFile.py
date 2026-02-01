import numpy as np

#view 1 
a =np.array([1,2,3,4,5])
b = a.view()

print("Original array", a)
print("  View", b)


b[0] = 100
print("After Original array", a)
print(" After change in original", b)


#UNDERSTANDING WITH MEMORY IN VIEWS AND COPY
import numpy as np

a = np.array([10, 20, 30, 40])
b = a.view()
c = a.copy()

print(id(a), id(b), id(c))   # object ids
print(a.base)               # None (original)    -> here none means independent array 
print(b.base)               # points to a
print(c.base)               # None (independent)




print("SAME MEMORY PROOF:", np.shares_memory(a,b))