'''
🔹 Slicing in Python (with Lists)
Slicing is a technique used to extract a portion (sublist) of a list using the syntax:

list[start:stop:step]

'''
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers)

# sclicing

print(numbers[:])   # to print whole list
print(numbers[1:5])  # 1 index se 4 index tak
print(numbers[::2])  # every 2nd element in list
print(numbers[-5:-1])  # last 5 se last 2nd tak 
print(numbers[:3])  # 0 se 2nd tak