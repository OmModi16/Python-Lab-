def count():
    x=input("enter a string:")
    c1=0
    c2=0
    for char in x:
        if(char.isalpha()):
            c1 +=1
        elif(char.isdigit()):
            c2 +=1
        else:
            print("error")
    print(c1 ," number of alphabets")
    print(c2 ,"number of digits")
count()  

            
    
