#Using NumPy in our code
import numpy as np 
print(np.__version__)


x = np.array([23,56,2])
print (x)
print(type(x))

#from tuple
y = np.array((13, 24, 35, 45, 50))
print(y)
print(type(y))


#0-d array
c=np.array((100))
print(c)
print(type(c))


#Checking the Number of Dimensions of Array:
import numpy as np

# 0-d array
x = np.array(4)
# 1-d array
y = np.array([1, 2, 3])
# 2-d array
z = np.array([[11, 62, 3], [46,95,96]])
# 3-d array
c = np.array([[[11, 2, 3], [48,85, 6]], [[17,78,78], [44,95, 6]]])

print(x.ndim)
print(y.ndim)
print(z.ndim)
print(c.ndim)

