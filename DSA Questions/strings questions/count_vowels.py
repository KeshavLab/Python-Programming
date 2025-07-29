text="keshav"
vowels='aeiouAEIOU'
count=0

for char in text:
    if char in vowels:
        count=count+1
print(f"the count of vowels {text} is {count}")