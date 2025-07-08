'''Write a function that takes a number and prints its multiplication table.'''
def mul_table(num):
    
    for i in range(1,11):
        
        print(num,"x",i,"=",num*i)


# call the function 
num=int(input("enter the number :"))
mul_table(num)
