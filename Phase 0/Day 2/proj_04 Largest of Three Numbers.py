#  Largest of Three Numbers

Number1=int(input("Enter Number1 :- "))
Number2=int(input("Enter Number2 :- "))
Number3=int(input("Enter Number3 :- "))

if Number1>Number2 and Number1>Number3:
    print("Number1",Number1,"is Largest Number")
elif Number2>Number3:
    print("Number2",Number2,"is largest Number")
else:
    print("Number3",Number3,"is largest Number")
    
