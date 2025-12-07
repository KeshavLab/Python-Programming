# n=int(input("enter a number :"))
# print("Even" if n%2==0 else "Odd")

# n=int(input("enter your number :"))
# area=n*n
# print(f"the square if number {n} is {area}")


# type casting means manual conversion of data type by progreameer

# a="5"
# b=int(a)
# print(b+6)

# type conversion 
# a=7
# b=3.5
# print(a+b)

# dictionary
# my_dict={}

# student={
#     "name":"shivraj",
#     "age":22,
#     "course":"java",
#     "is_active":True
# }
# print(student)

# print(student["course"])
# print(student.get("age"))

# student["age"]=23
# print(student["age"])


# flowers={
#     "flower1":{
#         "name":"rose",
#         "color":"red",
#         "price":100

#     },
#     "flower2":{
#         "name":"mogra",
#         "color":"white",
#         "price":80
#     }
# }

# print(flowers)
a={1,2,3,4,5}
b={4,5,6,7,8}

# union
print("union")
print(a|b)

print("intersection")
print(a&b)

print("set difference")
print(a-b)
print(b-a)