import copy
a = [[1,2], [3,4]]
b= copy.copy(a)

print(a is b )    # False

b[1][0] = 99
print(b)   #99 