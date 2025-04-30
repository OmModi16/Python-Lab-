def time():
    for i in range (24):
        if i == 12:
            print("noon")
        elif i == 0:
            print("midnight")
        elif i < 12:
            print (i,"AM")
        else:
            print (i-12, "PM")
time()            
            
    
