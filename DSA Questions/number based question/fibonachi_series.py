n=int(input("Enter a number :"))

a,b=0,1

print("fibonachi series :")
for _ in range(n):
    print(a,end=" ")

    temp=a+b
    a=b
    b=temp