num=int(input("enter yout number" ))
n=len(str(num))

sum_of_digit=0

for digit in str(num):
    sum_of_digit+=int(digit)**n


if sum_of_digit==num:
    print("it is an armstrong number")

else:
    print("it is not armstrong number ")