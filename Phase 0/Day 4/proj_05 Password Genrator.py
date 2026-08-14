import random
def generator_password():
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@"

    password=''
    length=int(input("Enter Your Required Length of Password : "))
    for i in range(length):
        password=password+random.choice(characters)

    print("Generated Password :",password)

generator_password()