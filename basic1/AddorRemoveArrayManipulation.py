import numpy as np 
a = np.array([[1,2], [3,4]])
print("Original array: \n" , a)

#Append
b=np.append(a ,[[5,6]] , axis=0)
print(" After append: \n" , b)

#Insert
c=np.insert(b, 1, [[9,9]] , axis=0)
print("After insertion: \n",c)

#Resize
d=np.resize(c,(2,4))
print("After resize :",d)


#Delete 
e=np.delete(d,1,axis=0)
print("After deletion :",e)


