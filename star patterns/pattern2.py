#🔷 Example: Right-Angle Triangle of Stars *
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
n=5

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()