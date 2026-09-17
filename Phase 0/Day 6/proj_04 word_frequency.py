# word Frequency

line=input("Enter Your text :- ").split()
frequency={}

for text in line:
    if text in frequency:
        frequency[text]+=1
    else:
        frequency[text]=1

for word,count in frequency.items():
    print(word,"=",count)