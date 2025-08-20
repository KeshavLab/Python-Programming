num=int(input("enter your number :"))

str_num=str(num)

reversed_num=int(str_num[::-1])

if(num==reversed_num):
    print("it is palidrome number ")

else:
    print("it is not palidrome number ")

