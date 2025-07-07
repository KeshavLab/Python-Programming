'''
i = 0
while i < 5:
    if i == 3:
        continue
    print("i =", i)
    i += 1

🧠 Why?
When i == 3, continue runs.

i += 1 never happens, so i stays 3 forever.

Loop repeats endlessly → infinite loop

'''


i=0
while i<=5:
    i+=1   # the correct way to increment first 
    if(i==3):
        continue  # skip the current iteration
    print(i)
    