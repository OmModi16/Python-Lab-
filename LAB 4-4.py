def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d**len(digits) for d in digits)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n) == str(n**2)[-len(str(n)):]


num = int(input("Enter a number: "))

print(f"Prime: {'Yes' if is_prime(num) else 'No'}")
print(f"Perfect: {'Yes' if is_perfect(num) else 'No'}")
print(f"Armstrong: {'Yes' if is_armstrong(num) else 'No'}")
print(f"Palindrome: {'Yes' if is_palindrome(num) else 'No'}")
print(f"Automorphic: {'Yes' if is_automorphic(num) else 'No'}")
