import numpy as np

a=np.arange(0,60,5)
print("The array is", a )

a =a.reshape(3,4)
print("After reshaping the array is :\n",a)

print("The first array is:")
print(a)
print('/n')

print("The second arraya is :")
b = np.array([1,2,3,4])
print(b)
print('/n')

print("the modified array is:")
for x,y in np.nditer([a,b]):
    print("%d:%d" %(x,y))

    