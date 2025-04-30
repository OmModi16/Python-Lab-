import random
lst=[]
while len(lst)<10:
    num=random.randint(-15,15)
    if num not in lst:
        lst.append(num)


print(lst)
sq=lambda x:x**2
a=map(sq,lst)
print(list(a))        