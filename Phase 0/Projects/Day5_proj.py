text = input("Enter Your Text... ")

# Counters
characters = 0
words = 0
spaces = 0
vowels = 0
consonants = 0
digits = 0
uppercase = 0
lowercase = 0

# Character Analysis
for char in text:
    characters += 1
    if char == " ":
        spaces += 1
    elif char in "AEIOUaeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

# Word Count
words = len(text.split())

# Reverse Text
reverse_text = text[::-1]

# Palindrome Check
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
    palindrome = "Yes"
else:
    palindrome = "No"

# Result
print("\n========== TEXT ANALYZER ==========")

print("Original Text       :", text)
print("Reverse Text        :", reverse_text)
print("Palindrome          :", palindrome)
print("Characters          :", characters)
print("Words               :", words)
print("Spaces              :", spaces)
print("Vowels              :", vowels)
print("Consonants          :", consonants)
print("Digits              :", digits)
print("Uppercase Characters:", uppercase)
print("Lowercase Characters:", lowercase)