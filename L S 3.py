def ls3():
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    c=int(input("enter another number:"))
    if a>b>c:
        print(a,"is largest")
        print(c,"is smallest")
    elif a>c>b:
        print(a,"is largest")
        print(b,"is smallest")
    elif b>a>c:
        print(b,"is largest")
        print(c,"is smallest")
    elif b>c>a:
        print(b,"is largest")
        print(a,"is smallest")
    elif c>b>a:
        print(c,"is largest")
        print(a,"is smallest")
    elif c>a>b:
        print(c,"is largest")
        print(b,"is smallest")
    else:
        print ("error")
ls3()        
