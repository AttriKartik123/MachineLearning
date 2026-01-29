import numpy as np 


#INT
a=np.array([1,2,3,4,5] , dtype=np.int32)
print(a)
print(type(a))
print(a.dtype)

b=np.array([10,20,30,40,50] , dtype=np.int64)
print(b)
print(b.dtype)



#FLoat
a=np.array([1.4,2.5,3.6,4.8,5.0] , dtype=np.float32)
print(a)
print(type(a))
print(a.dtype)

b=np.array([10.00,20.77,30.8,40.6,50.22] , dtype=np.float64)
print(b)
print(b.dtype)


#Complex datatype
import numpy as np
a = np.array([1+2j, 2+3j, 3+4j], dtype=np.complex64)
b = np.array([10+20j, 20+30j, 30+40j], dtype=np.complex128)

print(a.dtype)  
print(b.dtype)  


#Time delta
import numpy as np
a = np.array(["2022-01-01", "2022-02-01", "2022-03-01"], dtype=np.datetime64)
b = np.array(["2022-01-02", "2022-02-03", "2022-03-04"], dtype=np.datetime64)

delta = b - a

print(delta.dtype)  # Output: timedelta64[D]