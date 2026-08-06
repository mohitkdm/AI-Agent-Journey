char=input("Enter Here. ")

if 'A'<=char[0]<='Z':
    if 'a'<char[1:]<='z':
        print("This is capetellize Word")
    elif 'A'<char[1:]<='Z':
        print("This is Upper Case Word")
    else:
        print("Its not Capetellize Word ")
elif 'a'<=char[0]<='z':
    if 'a'<=char[1:]<='z':
         print("this is Lower Case Word")
    else:
         print("Bhai kuch samaj hi nahi aa rha h kiya baatu aapko m")
else:
        print("Sahi baat hai JI koi nahi h apna Yaa pe ")
