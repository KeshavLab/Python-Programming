'''A dictionary in Python is a collection of key-value pairs. It's unordered 
(until Python 3.6+ where insertion order is preserved), mutable, and indexed by keys.'''

# Empty dictionary
my_dict = {}

# Dictionary with data
student = {
    "name": "Keshav",
    "age": 23,
    "course": "Python",
    "is_active": True
}
print(student)


# 🔑 Accessing Elements by keys

print(student["age"])
print(student.get("name"))

# ✏️ Adding / Updating Elements
student["age"] = 24                # Update value
student["city"] = "Mumbai"         # Add new key-value pair
print(student)