number=int(input("Enter Your range Number "))
square=[i*i for i in range(1,number+1)]
print(square)

square=[i*i for i in range(1,number+1) if i%2==0]
print(square)

square=[i*i if i%2==0 else i**3 for i in range(1,number+1)]
print(square)

