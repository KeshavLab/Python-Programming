# diamond palidrome pattern



n=5
# top of diamond
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


    # bottom of diamond

for i in range(n-1,0,-1):
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