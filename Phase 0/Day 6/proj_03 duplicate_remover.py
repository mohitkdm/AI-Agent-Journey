
# Dulpicate Remover

a = list(map(int, input("Enter Your Numbers without comma(,):- ").split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("Unique Data",b)