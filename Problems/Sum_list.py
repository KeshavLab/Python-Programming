'''Great! Here's how you can take a list of numbers from user input in Python 
and then calculate the sum using your sum_list function.'''


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 🔹 Take user input
# user_input = input("Enter numbers separated by spaces: ")

# # 🔹 Convert the input string into a list of integers
# numbers = list(map(int, user_input.split()))

# 🔹 Call the function and print the result
print("Sum of the list:", sum_list([1,3,4,6]))
