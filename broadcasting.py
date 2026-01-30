import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,7,8,9])
c = a+b
print(c)



'''Adding two 1-d Arrays of different shape In the example given below we will add two one-dimensional arrays with different shapes and will check what we get in the output:


import numpy as np

a = np.array([4,5,6,7])
b = np.array([1,3,5,7,9,11,14])
c = a+b
print(c)



errro:ValueError                                Traceback (most recent call last)
<ipython-input-3-a634d462e7c0> in <cell line: 5>()
      3 a = np.array([4,5,6,7])
      4 b = np.array([1,3,5,7,9,11,14])
----> 5 c = a+b
      6 print(c)

ValueError: operands could not be broadcast together with shapes (4,) (7,) 

'''

#solution:
import numpy as np
b = np.array([4,8,10,12])
a = np.array([[1,2,3,4],[11,10,8,6],[10,20,39,3]])


print("\n The array b is :")
print(b)
print("\n The array a is :")
print(a)

print("\n After addition of array a and b resultant array is:")
c = a + b;
print(c)