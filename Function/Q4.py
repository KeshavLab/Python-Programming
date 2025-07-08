'''Write a function that takes two numbers and returns the greater one.

Example: maximum(10, 20) → 20'''

def greater_one(a,b):
    if(a>b):
        print(a,"is greater")
    
    else:
        print(b,"is greater")


# call the function
a=int(input("enter first number :"))
b=int(input("enter second nuber :"))
greater_one(a,b)