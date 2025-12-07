"""
  1️⃣ Constructor

A special function inside a class.

Its name is always __init__().

Runs automatically when an object is created.

Used to initialize variables of the object.


"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_student_info(self):
        print(f"Name : {self.name}, Age :{self.age}")


s1=Student("keshav",21)
s1.show_student_info()


"""
2️⃣ Function (Method)

A normal block of code inside or outside a class.

Runs only when you call it.

Used to perform actions / tasks.
"""
def add(a, b):
    return a + b

sum=add(10,20)
print("Sum is :",sum)