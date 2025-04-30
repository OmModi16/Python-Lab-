n = int(input("Enter how many Fibonacci numbers to generate: "))

a = 0
b = 1
count = 0
print("Fibonacci series:")
while count < n:
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term
    count += 1
