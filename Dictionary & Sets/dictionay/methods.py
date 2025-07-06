'''| Method                       | Description                                                                 |
| ---------------------------- | --------------------------------------------------------------------------- |
| `clear()`                    | Removes all items from the dictionary                                       |
| `copy()`                     | Returns a **shallow copy** of the dictionary                                |
| `fromkeys(seq, value)`       | Creates a new dictionary from a sequence of keys and a single value         |
| `get(key[, default])`        | Returns the value for a key, or `default` if key not found                  |
| `items()`                    | Returns a view of (key, value) pairs                                        |
| `keys()`                     | Returns a view of all keys                                                  |
| `values()`                   | Returns a view of all values                                                |
| `pop(key[, default])`        | Removes and returns value for given key                                     |
| `popitem()`                  | Removes and returns the last inserted (key, value) pair                     |
| `setdefault(key[, default])` | Returns value if key exists, otherwise inserts key with default value       |
| `update([other])`            | Updates dictionary with key-value pairs from another dictionary or iterable |
'''
# dictionary
person = {"name": "Keshav", "age": 23, "city": "Pune"}
person1 = {"name": "Keshav", "age": 23, "city": "Pune"}


# 1. clear()  Removes all items from the dictionary    
person.clear()
print(person)  # {}

# 2. copy()  Returns a **shallow copy** of the dictionary
copy_dict=person1.copy()
print(copy_dict)


#3. get(key[, default])

print(person1.get("name"))
print(person1.get("marks","NA"))

# 4.items()  Returns a view of (key, value) pairs
print(person1.items())

# 5.keys()   Returns a view of all keys
print(person1.keys())

# 6.values()   Returns a view of all values

print(person1.values())

# 7. pop()
print(person1.pop("age"))

# 8. popitem()
print(person1.popitem())  # remove last item 

# 9. setdefault()
person1.setdefault("gender","male")
print(person1)

# 10. update()
person1.update({"name":"kolekar"})
print(person1)