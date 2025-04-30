import random
a = [random.randint(1, 30) for _ in range(50)]
print("Generated list of 50 random numbers:")
print(a)
b = list(set(a))
print("\nList after removing duplicates:")
print(b)
