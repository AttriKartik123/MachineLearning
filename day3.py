'''class student :
    pass 

import sys 
obj = student()
print(id(obj))
print(type(obj))
print(sys.getsizeof(obj)) 

its output :
1754601451408
<class '__main__.student'>
48
'''

'''class student(object) :
    pass

import sys 
obj = student()
print(id(obj))
print(type(obj))
print(sys.getsizeof(obj)) 


its output:
2499660181392
<class '__main__.student'>
48

'''

'''class student :
    def __init__(self)-> None :

        pass 


import sys 
obj = student()
print(id(obj))
print(type(obj))
print(sys.getsizeof(obj)) 
 

 its output:
2196948545424
<class '__main__.student'>
48
'''
