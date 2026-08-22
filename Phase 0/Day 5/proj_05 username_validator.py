username = input("Enter Your Username... ")

if len(username) >= 5 and len(username) <= 15:
    if username.isalnum():
        print("Valid Username")
    else:
        print("Username can contain only letters and numbers")
else:
    print("Username must be 5 to 15 characters long")