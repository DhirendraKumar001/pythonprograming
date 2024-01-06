sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if avg>=60:
    print("division: 1st")
elif avg>=45:
    print("division:2nd")
elif avg>=30:
    print("division:3rd")
elif avg<30:
    print("fail")
