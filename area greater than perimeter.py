l=float(input("Enter length of the rectangle:"))
b=float(input("Enter breath pf the rectangl:"))
area=l*b
peri=2*(l+b)
if area>peri:
    print("Area is greater than perimeter")
else:
    print("Area is smaller than perimeter")
