import copy 

a = [[10,20],[30,40]]
b  = copy.deepcopy(a)

print(a)
print(b)

b[0][0] = 90
print("a is b :" , a is b )

print(a)
print(b)