num=int(input("enter your number :"))

n=len(str(num))

sum_of_power=0
for digit in str(num):
    sum_of_power+=int(digit)**n

if num==sum_of_power:
    print("it is an Armstrong number :")

else:
    print("it is not armstrong number |||")