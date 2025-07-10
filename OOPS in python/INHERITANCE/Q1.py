# 🔷 Parent Class
class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person information
    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# 🔶 Child Class inheriting from Person
class Employee(Person):
    # Constructor to initialize employee-specific data + person data
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)  # Call parent class constructor
        self.employee_id = employee_id
        self.salary = salary

    # Method to display employee-specific information
    def show_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: ₹{self.salary}")


# ✅ Create object of Employee class
emp1 = Employee("Keshav", 25, "E102", 50000)

# Display person info (inherited from Person)
emp1.show_person_info()

# Display employee info (own method of Employee class)
emp1.show_employee_info()
