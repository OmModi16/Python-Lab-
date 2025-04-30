from collections import Counter
user_input = input("Enter a string: ")

char_frequencies = Counter(user_input)

print("Character Frequencies:")
for char, freq in char_frequencies.items():
    print(f"'{char}': {freq}")
