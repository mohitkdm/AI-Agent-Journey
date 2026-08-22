text = input("Enter Your String... ")

characters = 0
vowels = 0
consonants = 0
digits = 0
spaces = 0
uppercase = 0
lowercase = 0
special = 0

for char in text:

    characters += 1

    if char in "AEIOUaeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    elif char == " ":
        spaces += 1

    else:
        special += 1

    if char.isupper():
        uppercase += 1

    elif char.islower():
        lowercase += 1


print("\n----- String Analysis -----")

print("Total Characters :", characters)
print("Vowels           :", vowels)
print("Consonants       :", consonants)
print("Digits           :", digits)
print("Spaces           :", spaces)
print("Uppercase        :", uppercase)
print("Lowercase        :", lowercase)
print("Special Characters :", special)