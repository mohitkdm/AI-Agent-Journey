char=input("Enter Here. ")
if 'A'<= char[0]<='Z':
    print("The is Capetellize Case",char[0])
elif 'a'<=char[0]<='z':
    print("The is lower Case",char[0])
elif 'a'<=char<='z':
    print("The is Upper Case",char[0])
else:
    print("Sahi baat h bhai First Letter Upper case nahi hai",char[0])