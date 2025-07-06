'''🧺 What is a Set?
A set is a collection of unique, unordered items in Python.

No duplicates

Unordered (no indexing)

Mutable (you can add/remove items)

Uses curly braces {} or set() constructor

'''

# With curly braces
my_set = {1, 2, 3, 4}

# With set() function
my_set2 = set([1, 2, 3])

# Duplicates are automatically removed
my_set3 = {1, 2, 2, 3, 3}
print(my_set3)  # Output: {1, 2, 3}


# ➕ Add & ➖ Remove Elements

my_set = {1, 2, 3}

my_set.add(4)         # Adds 4
my_set.remove(2)      # Removes 2
my_set.discard(5)     # Safe remove (won't give error if 5 not in set)

print(my_set)         # Output: {1, 3, 4}

for item in my_set:
    print(item)