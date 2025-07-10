'''✅ 🔷 Polymorphism (बहुरूपता)
📘 Definition (Simple Hinglish):
Polymorphism ka matlab hota hai:
"Ek naam, alag-alag kaam" — yani same function/method name, but different behavior depending on context.

🔍 Real-Life Example:
Socho speak() ek method hai:

Dog ke liye speak() → "Bark"

Cat ke liye speak() → "Meow"

Human ke liye speak() → "Hello"

Sabke paas speak() method hai, but output alag hai.
Yahi hota hai Polymorphism!

✅ Types of Polymorphism in Python:
| Type                  | Description                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| Method Overriding     | Child class apne tareeke se method ko redefine karta hai                     |
| Built-in Polymorphism | `+` operator strings ke liye concat karta hai, numbers ke liye add           |
| Duck Typing           | "If it walks like a duck and quacks like a duck..." (Python ki loose typing) |


'''
class Animal:
    def speak(self):
        print("animal speak")

class Dog(Animal):
    def speak(self):
        print("dog bark")

class Cat(Animal):
    def speak(self):
        print("Cat maww")



a=Animal()
a.speak()

print("-----")

d=Dog()
d.speak()

print("-----")

c=Cat()
c.speak()


# ❌ In Python: Method Overloading is not directly supported