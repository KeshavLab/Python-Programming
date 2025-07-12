my_dict={}

student={
    "name":"keshav",
    "age":34,
    "city":"panvel"
}

print(student["age"])
print(student.get("marks","Na"))
student.popitem()
print(student)
student.setdefault("gender","male")
print(student)