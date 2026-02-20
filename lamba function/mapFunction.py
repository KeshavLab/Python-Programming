#📌 What is map()?

# It applies a function to every element in a list.


numbers = [1, 2, 3, 4, 5]


# Using map() to square each number in the list
square= list(map(lambda x: x*x, numbers))
print(square) 


cube  =list(map(lambda y: y**3, numbers))
print(cube)