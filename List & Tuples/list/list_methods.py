


# ✅ 1. append()
# Adds an element to the end of the list.
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']


# ✅ 2. insert(index, element)
# Inserts an element at a specific index.
fruits.insert(1,"orange")
print(fruits)

# ✅ 3. extend()
# Adds elements from another list (or iterable) to the end.
fruits.extend(["grape","melon"])
print(fruits)# ['apple', 'orange', 'banana', 'cherry', 'grape', 'melon']

# ✅ 4. remove(element)
# Removes the first occurrence of the element.
fruits.remove("banana")
print(fruits)

# ✅ 5. pop([index])
# Removes and returns an element at the given index (last item by default).

fruits.pop()
print(fruits)

# ✅ 6. clear()
# Removes all elements from the list.
'''fruits.clear()
print(fruits)  # []
'''

# ✅ 9. sort()
# Sorts the list in ascending order (by default).

fruits.sort()
print(fruits)

# ✅ 10. reverse()
# Reverses the order of elements in the list.
fruits.reverse()
print(fruits)