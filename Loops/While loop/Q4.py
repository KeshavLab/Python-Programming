# search number x in tuple using loop

tup=(1,2,3,4,5,45,7,8)

search_element=int(input("enter your search element :"))
found = False   # flag to track presence

for i in range(len(tup)):
    if tup[i]==search_element:
        print("Search element is found at index ",i)
        found=True
        break
    if not found:
        print("search element is not present in tuple")
    
    