'''🔹 Tuples in Python
A tuple is a built-in data structure in Python that is:

✅ Ordered
✅ Immutable (cannot be changed)
✅ Allows duplicate values

'''
# 🔍 Explanation:
# 🔸 tup = (1,) ✅
# This is a tuple with one element.
# The comma , is required to create a single-element tuple.
# Without the comma, Python treats it as a normal value inside parentheses.
tup = (1,)
print(tup)         # Output: (1,)
print(type(tup))   # Output: <class 'tuple'>


'''🔸 tup = (1) ❌
This is not a tuple.

It is just the integer 1 wrapped in parentheses.

Parentheses are just for grouping in math or expressions, unless there's a comma.'''
tup = (1)
print(tup)         # Output: 1
print(type(tup))   # Output: <class 'int'>


print("Here is a tuple with multiple elements:")