# reverse string using Sclicing

text="keshav kolekar"
reversed_text=text[::-1]
print(reversed_text)


# 2 using .join() method
'''
📌 What does ''.join(...) mean?
'' = means nothing between letters.

.join(...) = means stick the letters together.
'''
text1="gopika kolekar"
reversed_text1=''.join(reversed(text1))
print(reversed_text1)

# simple example for join 
letters = ['a', 'b', 'c']
print(''.join(letters))  # 👉 abc
print('-'.join(letters)) # 👉 a-b-c
print(' '.join(letters)) # 👉 a b c


# using   loop 

text2="prakash kolekar"
reversed_text2=''

for char in text2:
    reversed_text2=char+reversed_text2
print(reversed_text2)