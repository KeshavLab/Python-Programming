'''square pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

n=6     # (6x5) matrix
m=5
for i in range(n):
    for j in range(5):
        print("*",end="  ")
    print()



'''✅ Explanation:
Outer loop (i) controls the number of rows.

Inner loop (j) prints the stars in each row.

end=" " keeps printing on the same line.

print() moves to the next line after each row.'''