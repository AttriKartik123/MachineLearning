import numpy as np

a = np.arange(0,40,5)

print ("The Original array is:")
print (a)
print ('\n')

# showing elements of array one by one
print ("The Modified array is:")

for x in np.nditer(a) :
    print(x)