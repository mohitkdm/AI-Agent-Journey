number=int(input("Enter a Number : "))

count=0

for i in range(1,number+1):
    if number%i==0:
        count=count+1
    
if count==2:
    print(f"The number of {number} is a Prime Number")
else:
    print(f"The number of {number} is Not a Prime Number")