'''🔹 Constructor Name in Python:
The constructor method is always named __init__()

It is automatically called when you create a new object of a class.

Syntax:
class ClassName:
    def __init__(self, parameters):
        self.attribute = value


'''
class Student:
    def __init__(self,fullName,age):
        self.name=fullName  # instance variable
        self.age=age

    def display(self):
        print(f"Name :{self.name},Age :{self.age}")


s1=Student("keshav",20)
print(s1.display())

s2=Student("Rajesh",20)
print(s2.display())


        
