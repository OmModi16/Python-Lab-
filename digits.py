def digits():
    a = int(input("Enter any number between 1-999: "))
    if 1 <= a < 10:
        print("One digit")
    elif 10 <= a < 100:
        print("Two digits")
    elif 100 <= a < 1000:
        print("Three digits")
    else:
        print("Error: Number is out of range")

digits()
   
    
