# ✅ Method 1: Using Python’s Multiple Assignment (Recommended)
a=4
b=5

a,b=b,a

print(a)
print(b)

print("Using Arithmetic Operations (No third variable)")

# ✅ Method 2: Using Arithmetic Operations (No third variable)
a1=6
a2=7

a1=a1+a2
a2=a1-a2
a1=a1-a2
print(a1)
print(a2)

print("using third variable")
b1=6
b2=3

temp=b1
b1=b2
b2=temp
print(b1)
print(b2)