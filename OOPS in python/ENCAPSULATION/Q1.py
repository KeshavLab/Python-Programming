class Student:
    def __init__(self, name):
        self.name = name              # public attribute
        self.__marks = 0              # private attribute (encapsulated)

    # ✅ Setter method to set marks safely
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Enter between 0 and 100.")

    # ✅ Getter method to access private marks
    def get_marks(self):
        return self.__marks

    # ✅ Grade method to check pass/fail
    def grade(self):
        if self.__marks >= 40:
            print("Grade: Pass")
        else:
            print("Grade: Fail")


# ✅ Create object of Student class
s1 = Student("Keshav")

# ✅ Set and show marks
s1.set_marks(85)
print("Marks:", s1.get_marks())   # Access private marks via method
s1.grade()                        # Check pass/fail
