names=["taksh","dhruv","MLA savaliya","J.dodhiya","keshwala"]
chk_len=lambda st:len(st)>=8
res= filter (chk_len,names)
print(list(res))