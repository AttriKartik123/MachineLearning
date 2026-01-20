class Student:
    def __init__(self):
        print("Constructor calling...")

    def normal_method(self) :
        print("Normal method calling...")

    def __del__(self):
        print("Destructor calling...")

obj = Student()
obj.normal_method()

objj=Student()
objj.normal_method()


'''
Prog output:
Constructor calling...
Normal method calling...
Constructor calling...
Normal method calling...
Destructor calling...
Destructor calling...
'''