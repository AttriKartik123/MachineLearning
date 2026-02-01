import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Array a:\n", a)
print("Array b:\n", b)


#concatenate :
c = np.concatenate((a,b) , axis=0)
print("aafter concatenenation : ", c)

#vertical stack :
d = np.vstack((a,b))
print(d)

#Horizontal stack :
e = np.hstack((a,b))
print(e)