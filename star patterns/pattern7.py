# pyramid pattern
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

'''

n=5
for i in range(1,n+1):

    # spaces
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")
    
    # stars
    stars=2*i-1
    for j in range(stars):
        print("*",end=" ")

    print()