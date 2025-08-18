# using mathematiical way

num=int(input("enter your number :"))
rev=0

while num > 0:
    digit= num%10
    rev=rev*10 +digit
    num =num//10

print(rev)

# / → normal division → always gives a float
# // → floor division → gives an integer (whole number)
