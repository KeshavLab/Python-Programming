'''🔷 self kya hota hai Python mein?
self ka matlab hota hai: "yeh object khud"
Jaise hum kehte hain "main khud", waise hi Python mein object apne aap ko self kehta hai.

Jab bhi hum kisi method ko call karte hain object ke through, to Python self ka use karke 
batata hai ki kaun sa object ye method chala raha hai.


| Word                | Matlab                                           |
| ------------------- | ------------------------------------------------ |
| `self`              | Current object (ye object khud)                  |
| Kyu use karte hain? | Apne object ka data/methods access karne ke liye |
| Kab use hota hai?   | Har method ke pehle (`__init__`, `show`, etc.)   |
'''

# Example

class Student:
    #constructor
    def __init__(self,name):
        self.name=name

    #  information show karane ke liye ek function likjhenge
    def introduce(self):
        print("Hello My name is ",self.name)



# object create karenge
s1=Student("keshav")

s2=Student("priya")

#print the information
s1.introduce()
s2.introduce()

