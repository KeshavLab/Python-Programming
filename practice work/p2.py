from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print("dog sound")

class Dog(Animal):
    def sound(self):
        print("Dog is sounding")


d=Dog()
d.sound()

c=Cat()
c.sound()