'''🔪 Slicing in Python
Slicing is used to extract a portion (substring or sublist) from a sequence like a string, list, or tuple.

BASIC SYNTAX:
sequence[start:stop:step]

| Part    | Meaning                   |
| ------- | ------------------------- |
| `start` | Starting index (included) |
| `stop`  | Ending index (excluded)   |
| `step`  | Step size (optional)      |


'''
name="keshav"

print(name[0:4])   # 'kesh' → from index 0 to 3
print(name[2:])    # 'shav' → from index 2 to end
print(name[:3])    # 'kes' → from start to index 2
print(name[:])     # 'keshav' → full string
print(name[::2])   # 'ksa' → every 2nd char (step=2)
print(name[::-1])  # 'vahsek' → reversed string

'''⚠️ Things to Remember
stop is exclusive — it stops before that index.

Negative indices work too:'''
print(name[-4:-1]) # sha