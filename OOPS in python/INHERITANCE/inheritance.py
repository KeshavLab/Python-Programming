'''✅ 🔶 INHERITANCE (विरासत / विरासती गुण)
📘 Definition:
Inheritance ka matlab hota hai:

Ek child class (बच्चा क्लास) kisi parent class (मूल क्लास) 
ke features (properties & methods) ko use aur extend kar sakta hai.'''


# ✅ Parent class (Base class)
class Vehical:
    # Method to start engine
    def startEngine(self):
        print("engine is started")


# ✅ Child class Car, jo Vehical se inherit kar rahi hai
class Car(Vehical):
    # Car-specific method
    def drive(self):
        print("car is driving ")


# ✅ Child class Bike, jo Vehical se inherit kar rahi hai
class Bike(Vehical):
    # Bike-specific method
    def ride(self):
        print("Bike is riding")


# ✅ Car class ka object banaya
c1 = Car()

# Parent class ka method (startEngine) call kiya
c1.startEngine()  # Output: engine is started

# Car class ka apna method call kiya
c1.drive()        # Output: car is driving


# ✅ Bike class ka object banaya
b1 = Bike()

# Parent class ka method (startEngine) call kiya
b1.startEngine()  # Output: engine is started

# Bike class ka apna method call kiya
b1.ride()         # Output: Bike is riding
