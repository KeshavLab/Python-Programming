'''
🔢 Indexing in Python (Strings, Lists, Tuples, etc.)
Indexing means accessing elements by their position in a sequence. Python uses zero-based indexing, which means the first element has index 0.
'''
name = "keshav"

print(name[0])   # Output: k
print(name[3])   # Output: h
print(name[-1])  # Output: v (last character)
print(name[-3])  # Output: h (third last character)

# ⚠️ Index Out of Range
# print(name[10])
print("indexing by loop")

# INDEXING USING LOOPS
for i in range(len(name)):
    print(name[i])