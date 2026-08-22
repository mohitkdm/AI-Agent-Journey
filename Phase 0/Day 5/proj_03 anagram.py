text1 = input("Enter First String... ").lower()
text2 = input("Enter Second String... ").lower()

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")