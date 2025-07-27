# diamond star pattern
'''
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

n=5

# top of diamond star 
for i in range(1,n+1):
    # spaces
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    # print the numbers in assending number
    for j in range(1,i+1):
        print("*",end=" ")

    # print the number in desending order
    for j in range(i-1,0,-1):
        print("*",end=" ")

    print()

# bottom of diamond star 
for i in range(n-1,0,-1):
    # spaces
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    # print the numbers in assending number
    for j in range(1,i+1):
        print("*",end=" ")

    # print the number in desending order
    for j in range(i-1,0,-1):
        print("*",end=" ")

    print()