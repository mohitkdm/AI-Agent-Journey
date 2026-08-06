# Grade Calculator

per=int(input("Enter your percentage in integer number not in float :- "))

if 0<=per<60:
    print("You are Fail....","Your percentage is",per)
elif 60<=per<70:
    print("Your Grade is C ","Your percentage is",per)
elif 70<=per<80:
    print("Your Grade is B ","Your percentage is",per)
elif 80<=per<90:
    print("Your Grade is A","Your percentage is",per)
elif 90<=per<=100:
    print("Your Grade is A+","Your percentage is",per)

else:
    print("Write Percentage Correctly")