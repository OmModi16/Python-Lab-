
list = [("John", "Boy"), ("Emma", "Boy"), "Sophia", "Olivia", ("James", "Boy"), "Mia"]
boys_count = 0
girls_count = 0
for ele in list:
    if isinstance(ele, tuple):
        boys_count += 1  
    else:
        girls_count += 1  
print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")

