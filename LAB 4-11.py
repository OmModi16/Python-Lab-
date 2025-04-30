
x = float(input("Enter the value of x (in radians): "))
terms = int(input("Enter number of terms in the series: "))
sin_x = 0
sign = 1  
power = 1
for i in range(terms):
    
    num = 1
    for j in range(power):
        num *= x

   
    fact = 1
    for j in range(1, power + 1):
        fact *= j

    
    sin_x += sign * (num / fact)

    
    sign *= -1
    power += 2


print(f"Approximate value of sin({x}) using Taylor series: {sin_x}")
