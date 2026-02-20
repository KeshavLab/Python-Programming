# 🔹 2. filter() with Lambda
# 📌 What is filter()?

# It selects elements based on a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() to select even numbers from the list

result=list(filter(lambda x: x%2==0, numbers))

print(result)  # Output: [2, 4, 6, 8, 10]