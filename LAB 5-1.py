import random
odds = [random.randrange(1, 100, 2) for _ in range(5)]
print("Odd numbers:", odds)
evens = [random.randrange(2, 100, 2) for _ in range(4)]
print("Even numbers:", evens)
odds[2] = evens
print("After replacing 3rd element with even list:", odds)
flat = []
for item in odds:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)
print("Flattened list:", flat)
flat.sort()
print("Sorted list:", flat)
