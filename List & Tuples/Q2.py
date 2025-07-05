#  WAP to check list contain palidrome of elements
list=[]

for i in range(3):
    elements=int(input("Enter the elements :"))
    list.append(elements)

rev=list.copy()  # creating the reversed copy of list 
rev.reverse()

if(list == rev):
    print("It is a palidrome list")
    
else:
    print("it is not palidrome list")