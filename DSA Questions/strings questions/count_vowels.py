# text="keshav"
# vowels='aeiouAEIOU'
# count=0

# for char in text:
#     if char in vowels:
#         count=count+1
# print(f"the count of vowels {text} is {count}")


text=str(input("enter your tect :"))
vowels="aeiouAEIOU"
count=0

for i in text:
    if i in vowels:
        count=count+1
print(f"the count of vowels is {count}")