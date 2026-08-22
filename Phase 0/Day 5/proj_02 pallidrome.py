text = input("Enter Your String... ")

reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome",text)
else:
    print("Not Palindrome",text)