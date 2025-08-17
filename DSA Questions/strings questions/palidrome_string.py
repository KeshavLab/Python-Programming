# text=input("enter your text :")

# text=text.replace(" ","").lower()
# '''🧠 In Simple Words:
# (" ") is the thing you want to remove

# "" is what you want to put instead — in this case, nothing'''

# if text==text[::-1]:
#     print("string is palidrome ")

# else:
#     print("it is not palidrome string")

text=input("enter your text :")

text=text.replace(" ","").lower()

if text==text[::-1]:
    print(f"your text {text} is palidrome string")

else:
    print("it is not palidrome string ")