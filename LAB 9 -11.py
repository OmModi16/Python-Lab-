def create_list():
    a = [4, 3, 5, 84, 6, 48, 56]
    b = [4, 3, 5, 84]
    c = list(set(a) & set(b))
    print(c)

create_list()
 