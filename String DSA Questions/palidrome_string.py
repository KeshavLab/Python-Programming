text=input("enter your text :")

text=text.replace(" ","").lower()

if text==text[::-1]:
    print("string is palidrome ")

else:
    print("it is not palidrome string")