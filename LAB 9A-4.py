lst=['madam','python','malayalam','12321']
pali=lambda st:str(st)==str(st)[::-1]
res=filter(pali,lst)
print(list(res))