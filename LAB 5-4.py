import random
n = [random.randint(-50, 50) for _ in range(30)]
print("Generated list of 30 random numbers:")
print(n)
a = [num for num in n if num > 0]
b= [num for num in n if num < 0]
print("\nPositive numbers:")
print(a)
print("\nNegative numbers:")
print(b)
