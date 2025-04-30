def ispalindrome(s):
   cleaned = ''.join(char.lower() for char in s if char.isalnum())
   return cleaned == cleaned[::-1]


test_strings = ["Racecar"]

for s in test_strings:
    if ispalindrome(s):
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')
