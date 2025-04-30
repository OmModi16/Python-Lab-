import random
a = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for num in a if num < 30)
print("Original set of numbers:", a)
a = {num for num in a if num <= 35}
print("Updated set:", a)
print(f"Count of numbers less than 30: {count_less_than_30}")
