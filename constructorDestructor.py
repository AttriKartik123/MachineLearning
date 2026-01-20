class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno 
    def normalmethod(self):
        print("Student name:", self.name)
        print("Student rollno:", self.rollno)

    def __del__(self):
        print("Destructor calling...")

obj = Student("HArry" , 1)
obj.normalmethod()

objj = Student("Karry", 2)
objj.normalmethod()