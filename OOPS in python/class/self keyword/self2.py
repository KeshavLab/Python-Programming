# 👉 Create a Student class with name, roll_number, and grade, and display info for two students using a method.

class Student:

    # constructor 
    def __init__(self,name,roll_number,grade):
        self.name=name
        self.roll_number=roll_number
        self.grade=grade

    # information ko display karane ke liye ek function banayenge
    def display(self):
        print(f"name :{self.name},roll_number :{self.roll_number},grade :{self.grade}")


# creating the object
s1=Student("keshav",23,"A")
s2=Student("rajesh",24,"B")

#display information
s1.display()
s2.display()