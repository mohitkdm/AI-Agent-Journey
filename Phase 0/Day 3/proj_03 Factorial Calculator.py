num=int(input("Enter the Factorial Number .. "))

fac=1

for i in range(1,num+1):
    fac=fac*i

print(f"The Factorial of {num} is",fac)