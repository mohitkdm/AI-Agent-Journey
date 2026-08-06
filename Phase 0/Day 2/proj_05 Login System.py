#  Login System

createuser=input("Create username ... ")
createpswd=input("Create password ... ")

username=input("Enter username here... ")

if username==createuser:
    pswd=input("Enter password here... ")
    if pswd==createpswd:
        print("Login Succcesfully .... ")
    else:
        print("Write correct Password..")
else:
    print("Username does not exist..")