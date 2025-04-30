def ls2():
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    if a>b:
        print(a," is largest")
        print(b," is smallest")
    elif a<b:
            print(b,"is largest")
            print(a," is smallest")
    else:
        print(a,"=",b)
ls2()
