import copy 
a = {'x' : [10,20] , 'y' : [30,70]}

b = copy.copy(a)

print( a is b )
print("a:", a)
print("b:", b)

b['x'][1] = 100
print(b)