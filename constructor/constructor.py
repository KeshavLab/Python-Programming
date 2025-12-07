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