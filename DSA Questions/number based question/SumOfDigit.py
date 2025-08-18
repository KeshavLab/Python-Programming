num=22244
count=0
while(num>0):
    digit=num %10
    count=count +digit
    num=num//10

print(count)