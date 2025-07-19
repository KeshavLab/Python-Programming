class Animal:
    def speak(self):
        print("animal speak")


class Dog(Animal):
    def speak(self):
        print("dog speak")

class Cat(Animal):
    def speak(self):
        print("cat speak")

Animals=[Dog(),Cat(),Animal()]

for animal in Animals:
    animal.speak()
