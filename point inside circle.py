x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
r=int(input("Enter radius:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
d=((y2-y1)**2+(x2-x1)**2)**2
if d<r:
    print("point inside the circle")
else:
    print("point outside the circle")
