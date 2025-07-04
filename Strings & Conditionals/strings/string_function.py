'''| Function       | Description                                | Example                                |
| -------------- | ------------------------------------------ | -------------------------------------- |
| `endswith()`   | Checks if string ends with given substring | `text.endswith("hard.")` → `True`      |
| `capitalize()` | Capitalizes the first letter               | `text.capitalize()` → `'Keshav is...'` |
| `replace()`    | Replaces one string with another           | `text.replace("keshav", "raj")`        |
| `find()`       | Finds the first index of a substring       | `text.find("good")` → `13`             |
| `count()`      | Counts number of times a substring appears | `text.count("a")` → `4`                |
'''


text="keshav is good boy. keshav work hard"

print(text)

# 1. ✅ endswith(substring)
# Checks if the string ends with the given substring.
print(text.endswith("hard")) # true
print(text.endswith("keshav")) # false

# 2. ✅ capitalize()
# Capitalizes only the first character of the string and converts the rest to lowercase.
print(text.capitalize())  
# Output: 'Keshav is a good boy. keshav works hard.'

# ⚠️ Does not change the original string (strings are immutable in Python).

# 3. ✅ replace(old, new)
# Replaces all occurrences of a substring with another.
print(text.replace("keshav","prakash"))

# You can also limit how many times to replace:
print(text.replace("keshav","prakash",1)) # Only first 'keshav' is replaced

# 4. ✅ find(substring)
# Returns the index of the first occurrence of the substring. Returns -1 if not found.
print(text.find("good"))      # Output: 13
print(text.find("bad"))       # Output: -1 (not found)

# 5. ✅ count(substring)
# Counts how many times a substring appears in the string.
print(text.count("keshav"))   # Output: 2
print(text.count("a"))        # Output: 4
