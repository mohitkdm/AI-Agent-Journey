# Atm Menu

print("Welcome to Apna Bank ")
bal=211004
print("How can I help you")
opr=input("1 for Check Balance \n2 for Deposite \n3 for Withdraw \n4 for Exit \nplease select operation to perform....")

if opr=='1':
    print("Your Current Balance is",bal)
elif opr=='2':
    deposite=int(input("Enter the Deposite amount "))
    deposite_amount=deposite+bal
    print("Your amount of",deposite, "is deposite succesfully")
    print("Current Balance is",deposite_amount)

elif opr=='3':
    withdraw=int(input("Enter the Withdraw amount "))
    withdraw_amount=bal-withdraw
    print("Your amount of",withdraw, "is withdraw succesfully")
    print("Current Balance is",withdraw_amount)

elif opr=='4':
    print(exit())

else:
    print("Please select following operations only.....")
    
