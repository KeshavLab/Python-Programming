class Student:

    def __init__(self,fullName,age):
        self.name=fullName
        self.age=age

    def show(self):
        print(f"the name of student is {self.name} and age is {self.age}")



s1=Student("keshav",34)
print(s1.show())

s2=Student("Rajesh",33)
print(s2.show())