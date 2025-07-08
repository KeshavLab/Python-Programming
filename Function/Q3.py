'''Write a function that checks whether a number is even or odd.

Example: is_even(4) → "Even"'''

def even_odd(num):
    if(num%2==0):
        print("even number")

    else:
        print("odd number")


n=int(input("enter a number :"))
even_odd(n)