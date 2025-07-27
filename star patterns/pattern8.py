# palidrome pattern
'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

'''

n=5
for i in range(1,n+1):
    # spaces
    spaces=n-i
    for j in range(spaces):
        print(" ",end=" ")

    # print assending number
    for j in range(1,i+1):
        print(j,end=" ")

    # print desending number
    for j in range(i-1,0,-1):
        print(j,end=" ")

    print()