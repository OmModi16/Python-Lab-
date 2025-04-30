def factorial():
    x=int(input("enter any number:  "))
    factorial = 1
    for i in range (1, x+1):
        factorial *= i
    print("the fatorial of",x,"is",factorial)
factorial()    
