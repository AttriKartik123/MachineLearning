import numpy as np

print("\n",np.random.rand(3))


print("\n",np.random.rand(3,5))

print("\n",np.random.randn(2,3))

#from low to high 
print("\n",np.random.randint(2,100))

#RANDOM IN THE FORM OF MULTIDIMENSION 
print("\n",np.random.randint(-4,8, size=(3,3)))





#important 
rana = np.random.randint(1,10,8)
print("\n Rana is :",rana)



#max, min, argmax, argmin
print(rana.max())
print(rana.min())
print(rana.argmax())  #-> returns the index of the largest in the array 
print(rana.argmin())

highest = rana.max()
print("Highest:", highest)

