def is_dict_empty():
        n=int(input("how many names you need"))
        d1={}
        for i in range (n):
                key=int(input("enter roll number:"))
                val=input("enter name:")
                d1[key]=val
        if not d1:
                print("d1 is empty")
        else:
                print (d1)
is_dict_empty()                                



