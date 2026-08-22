# Find string length"
'''
tex=input("Enter Here ")
1st method
count=0
for charactor in tex:
    count+=1
print("String Length is ",count,tex)
2nd method
print("Length of String",len(tex),"=",tex)
'''

# Convert string to uppercase
'''
text=input("Enter Here ... ")
1st method
result=""
for char in text:
    if 'a'<=char<='z':
        result+=chr(ord(char)-32)
    else:
        result+=char
print('UpperCase',result)
2nd method
print("UpperCase",text.upper())
'''

# Convert string to lowercase
'''
text=input("Enter Here.... ")
result=""
for char in text:
    if 'A'<=char<='Z':
        result+=chr(ord(char)+32)
    else:
        result+=char
print("LowerCase : ",result)
print("Lowercase : ",text.lower())
'''

# Count a character
'''
text=input("Enter Your String... ")
frequency={}
for i in text:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print("Charactor Count Total :",frequency)
'''

# Find a word
'''
text=input("Enter Your Text.... ")
word=input("Enter Your Word.... ")

words=text.split()
found=False
for w in words:
    if w==word:
        found=True
        break
if found:
    print("Word Found",word)
else:
    print("Word Not Found",word)
'''

# Replace a word
'''
text=input("Enter Your Text... ")
old_word=input("Enter Your Word to replace... ")
new_word=input("Enter Your New Word... ")

replace_text=text.replace(old_word,new_word)
print(f"Before : {text}, After : {replace_text}")
'''

# Remove spaces
'''
text=input("Enter Your text.... ")
removed_space=""
for char in text:
    if char!=" ":
        removed_space+=char
print("With Space :",text)
print("Without Space :",removed_space)
'''

# Reverse a string
'''
text=input("Enter Your Text... ")
reverse_string=text[::-1]
print("Text :",text)
print("Reverse Text :",reverse_string)
'''

# Check first character
'''
text = input("Enter Your Text... ")

if text:
    print("First Character :", text[0])
else:
    print("String is empty")
'''

# Check last character 
'''
text = input("Enter Your Text... ")

if text:
    print("Last Character :", text[-1])
else:
    print("String is empty")
'''

# Palindrome Checker
'''
text = input("Enter Your String... ")

words = text.split()
count = 0

for word in words:
    if word == word[::-1]:
        print("Palindrome Word :", word)
        count += 1

print("Total Palindrome Words :", count)
'''

# Anagram Checker
'''
text1=input("Enter the Fisrt Word.. ")
text2=input("Enter the Secoond Word.. ")

if sorted(text1.lower())==sorted(text2.lower()):
    print('Anagram')
else:
    print("Not Anagram")
'''

# Vowel Counter
'''
text=input("Enter Here..... ")
count=0
for i in text:
    if i in 'AEIOUaeiou':
        count+=1
print("Total Vowel in Text is :",count)
'''

# Character Frequency
'''
text = input("Enter Your Text... ")
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")

for char in frequency:
    print(char, ":", frequency[char])
'''

# Password Strength Checker
password = input("Enter your password.. ")
length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength :", strength)