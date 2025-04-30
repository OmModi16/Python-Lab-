a=int(input("Enter marks in mathematics:"))
b=int(input("Enter marks in science:"))
c=int(input("Enter marks in history:"))

total=(a+b+c)
avg=total/3
print("Total marks:",total)
print("Average marks:",avg)

if a<39 or b<39 or c<39:
    print("Student has failed")
else:
    print("Student has passed")

print("In mathematics student got: ",end="")
if 80<=a<=100:
    print("Grade O")
elif 70<=a<80:
    print("Grade A+")
elif 60<=a<70:
    print("Grade A")
elif 55<=a<60:
    print("Grade B")
elif 50<=a<55:
    print("Grade C")
elif 45<=a<50:
    print("Grade D")
elif 40<=a<45:
    print("Grade P")
else:
    print("Grade F")

print("In science student got: ",end="")
if 80<=b<=100:
    print("Grade O")
elif 70<=b<80:
    print("Grade A+")
elif 60<=b<70:
    print("Grade A")
elif 55<=b<60:
    print("Grade B")
elif 50<=b<55:
    print("Grade C")
elif 45<=b<50:
    print("Grade D")
elif 40<=b<45:
    print("Grade P")
else:
    print("Grade F")

print("In history student got: ",end="")
if 80<=c<=100:
    print("Grade O")
elif 70<=c<80:
    print("Grade A+")
elif 60<=c<70:
    print("Grade A")
elif 55<=c<60:
    print("Grade B")
elif 50<=c<55:
    print("Grade C")
elif 45<=c<50:
    print("Grade D")
elif 40<=c<45:
    print("Grade P")
else:
    print("Grade F")
