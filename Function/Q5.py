'''Write a function that prints all numbers from 1 to 10.'''

def print_num(n):
    for i in range(1,n):
        print(i)


#  call the function
n=int(input("enter the number :"))

print_num(n)