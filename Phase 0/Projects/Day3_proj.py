
Number=int(input("Enter a Number Here ... "))

# Check Even/Odd + Positive/Negative/Zero

if Number==0:
    print(f"The Number {Number} is Even and Zero")

elif Number>0:
    if Number%2==0:
        print(f"The Number {Number} is Positive and Even ")
    else:
        print(f"The Number {Number} is Positive and Odd ")

elif Number<0:
    if Number%2==0:
        print(f"The Number {Number} is Negative and Even ")
    else:
        print(f"The Number {Number} is NEgative and Odd ")
    

# Prime Check
count=0
if Number>=1:
    for i in range(1,Number+1):
        if Number%i==0:
            count=count+1
    if count==2:
        print(f"The Number {Number} is Prime")
    else:
        print(f"The Number {Number} is Not Prime")
else:
    print(f"The Number {Number} is Not Prime")


# Multiplication Table
if Number>0:
    for i in range(1,11):
        print(Number,"X",i,"=",Number*i)
else:
    print("The Table is not print for negative number")


# Factorial

if Number<0:
    print("The Factorial Number is not Defined for negative number")
else:
    fact=1
    for i in range(1,Number+1):
        fact=fact*i

    print(f"The factorial of {Number} is ",fact)