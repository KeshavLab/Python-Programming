'''Fibonaci Searies'''

def fibanachi_searies(num):
    a=0
    b=1

    for i in range(1,num+1):
        print(a," ")

        next=a+b
        # update values
        a=b
        b=next


n=int(input("enter the number :"))
res=fibanachi_searies(n)
print(res)