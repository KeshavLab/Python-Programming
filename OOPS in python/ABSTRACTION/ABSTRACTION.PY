'''✅ 🔷 Abstraction (संक्षेप में केवल ज़रूरी जानकारी दिखाना)
📘 Definition (Simple Hinglish):
Abstraction ka matlab hai user ko sirf zaroori details dikhana, aur complex logic ko chhupana.

🔒 Just like how you use a mobile phone:

Tum call karte ho, message bhejte ho

Lekin andar circuit, hardware, OS kaise kaam karta hai — woh tum nahi dekhte

Wahi abstraction hai!

🔍 In Python:
Python mein abstraction achieve hota hai:

Using abstract classes

Using abstract methods

🧠 Use:
Abstract class banane ke liye use karo: from abc import ABC, abstractmethod



@abstractmethod
def sound(self):
    pass
    

✅ What is pass?
pass ek placeholder statement hota hai Python mein.

Jab aap function/method likh rahe ho, lekin abhi kuch bhi body nahi dena chahte, tab pass likh dete ho.

Ye syntax error se bachata hai.





Yahaan sound() ek abstract method hai — iska matlab hai:

Iska implementation child class mein hoga.

Parent class sirf design batata hai, kaam nahi karta.

So, since:
Python requires method body (even if it's empty)

But abstract method should not have actual logic

→ We use pass as a do-nothing placeholder ✅

'''
from abc import ABC, abstractmethod

# 🔷 Abstract class
'''ABC: Stands for Abstract Base Class.

abstractmethod: Marks a method that must be implemented by any subclass.'''
class Animal(ABC):

    # 🔒 Abstract method (must be defined by child)
    @abstractmethod      #tells Python: “This method is compulsory for all subclasses.” (Every animal must have a sound().
                                         #But each animal makes a different sound.)
    def sound(self):     #means the method has no body here.
        pass

# 🔶 Concrete class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")




#uses the class 
d = Dog()
d.sound()   # Output: Dog barks

c = Cat()
c.sound()   # Output: Cat meows

'''| Name  | Type   | Meaning               | Used For                                        |
| ----- | ------ | --------------------- | ----------------------------------------------- |
| `abc` | Module | Abstract Base Classes | Importing tools like `ABC` and `abstractmethod` |
| `ABC` | Class  | Abstract Base Class   | Creating abstract classes in your code          |
'''