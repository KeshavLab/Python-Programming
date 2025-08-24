from abc import ABC,abstractmethod

class Vehical(ABC):

    @abstractmethod
    def startEngine(self):
        pass


class Bike(Vehical):
    def startEngine(self):
        print("Bike engine started ")


class Car(Vehical):
    def startEngine(self):
        print("car engine is started ")


b=Bike()
b.startEngine()


c=Car()
c.startEngine()