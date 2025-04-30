def count_lower_upper(str):
    count = {"uppercase": 0, "lowercase": 0}
    
    for ele in str:
        if ele.isupper():
           count["uppercase"]+=1
        elif ele.islower():
            count["lowercase"]+=1
    return count
str = input("Enter any string: ")
result = count_lower_upper(str)
print("Uppercase and Lowercase counts:", result)   
            
                
