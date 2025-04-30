
n = {"Abhishek", "Om", "Het", "Harsh", "Raj", "Kaushal", "Vapi", "Misha"}
a = set()
b = set()
for name in n:
    if name[0] == 'O':
        a.add(name)
    elif name[0] == 'H':
        b.add(name)
print("Names starting with 'o':", a)
print("Names starting with 'h':", b)
