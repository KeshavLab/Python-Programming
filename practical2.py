from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("DOg is barking")

class Cat(Animal):
    def sound(self):
        print("cat is maww")


# uses class
d=Dog()
d.sound()

c=Cat()
c.sound()