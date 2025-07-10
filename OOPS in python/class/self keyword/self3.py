
class Book:

    #constructor
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    # details show karane ke liye ek function banayenge

    def show_details(self):
        print(f"title :{self.title},author :{self.author},price :{self.price}")


# objects create karenge

b1=Book("Chava","keshav",300)
b2=Book("nisarg","rajesh",500)

# show details

b1.show_details()
b2.show_details()
