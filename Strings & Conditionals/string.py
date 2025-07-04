# ✅ String Definitions using Different Quotes
str1 = 'keshav'        # Single quotes
str2 = "prakash"       # Double quotes
str3 = """kolekar"""   # Triple quotes (can also be used for multi-line strings)

# ✅ Printing Individual Strings
print(str1)
print(str2)
print(str3)

# ✅ String Concatenation with Space
# You can manually add a space using " "
print(str1 + " " + str2 + " " + str3)

# ✅ Special Characters: \n (new line), \t (tab)
str4 = "keshav is a good boy.\nWe appreciate it."   # \n moves to next line
str5 = "keshav is a good boy.\tWe appreciate it."   # \t adds a tab space

# ✅ Printing Strings with Escape Characters
print(str4)
print(str5)

# ✅ Length of Strings
print("Length of str1:", len(str1))  # Output: 6
print("Length of str2:", len(str2))  # Output: 7
print("Length of str4:", len(str4))  # Counts every character including \n

# ✅ Summary Table (for your reference):
"""
| Syntax                                           | Use Case                                                                           | Example              |
|--------------------------------------------------|------------------------------------------------------------------------------------|----------------------|
| 'single quotes'                                  | Simple strings, commonly used                                                      | 'hello'              |
| "double quotes"                                  | Useful when the string contains single quotes                                      | "It's fine"          |
| '''triple quotes''' or """"triple quotes""""       | For multi-line strings or docstrings                                               | """"Line1\nLine2""""   |
"""
