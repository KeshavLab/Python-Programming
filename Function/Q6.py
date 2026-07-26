'''Write a function that calculates the factorial of a number.

Example: factorial(5) → 120'''

def fatorial_of_num(num):
    fact=1
    for i in range(1,num+1):
        fact=fact *i
    print("factorial of numbr is ",fact)


num=int(input("enter the number :"))
fatorial_of_num(num)


# using recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

n=int(input("enter the number :"))
print(factorial(n))