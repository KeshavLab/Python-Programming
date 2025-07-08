'''✅ What is a Function?
A function is a block of organized, reusable code that performs a specific task.

You define it once and use it multiple times, which makes your code:

Modular

Clean

Easier to debug'''

# 📌 Types of Functions:
# Built-in functions – Predefined (e.g., print(), len(), type())

# User-defined functions – Created by the user using def



# 🔍 Example 1: Function without Parameters and Return
def greet():
    print("hello welcome to python")

greet()
     

# 🔍 Example 2: Function with Parameters

def greet_user(name):
    print("hello",name)

greet_user("keshav")



# 🔍 Example 3: Function with Return Value

def add(a,b):
    return a+b

sum=add(2,3)
print(sum)


# 🛠️ Example 4: Default Parameter
def greet_default(name="keshav"):
    print("hellow",name)

greet_default(name="rajesh")