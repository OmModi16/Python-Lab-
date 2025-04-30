import random
random_integers = [random.randint(1, 100) for _ in range(20)]
print("Generated list of 20 random integers:")
print(random_integers)
a = int(input("\nEnter a number to find its positions in the list: "))
positions = [index for index, value in enumerate(random_integers) if value == a]
if positions:
    print(f"The number {a} is found at positions: {positions}")
else:
    print(f"The number {a} was not found in the list.")
