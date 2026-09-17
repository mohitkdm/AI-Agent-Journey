# Lists
# Find list length
'''
number=[1,2,3,45,6,798,1454,54,5,54,"MOHIT","Nikhil","Yashwant"]
print(len(number))
'''

# Find largest number
'''
number=[1,465,16,46,264764,15851,13247861,0]
print(max(number))
'''

# Find smallest number
'''
number=[1,465,16,46,264764,15851,13247861,0]
print(min(number))
'''

# Calculate sum
'''
number=[1,2,3,4,5,6]
print(sum(number))
'''

# Reverse a list
'''
number=[1,2,3,4,5,6]
number.reverse()
print(number)
'''

# Remove duplicates
'''
number=[1,2,3,4,5,61,2,3,4]
print(number)
number=set(number)
number=list(number)
print(number)
'''

# Count an element
'''
number=[1,2,3,4,56,1,23,4,56]
print(number.count(3))
'''

# Tuples
# Create a tuple
'''
t=(1,2,3,4,5,6,"Mohit")
print(t)
'''

# Access tuple elements
'''
t=(1,2,3,4,5,6,"Mohit")
print(t[5])
'''

# Tuple unpacking
'''
student=("Mohit","Nikhil","Yash")
a,b,c=student
print(a)
print(b)
print(c)
'''

# Sets
# Union
'''
a={1,2,3,4}
b={4,5,6,7}
print("Union :",a|b)
'''

# Intersection
'''
a={1,2,3,4}
b={4,5,6,7}
print("Intersection :",a&b)
'''

# Difference
'''
a={1,2,3,4}
b={4,5,6,7}
print("Difference :",a-b)
print("Difference :",b-a)
'''

# Remove duplicates using set
'''
a={1,12,1,2,1,1,1,2,1,2,12,12,11,5,156,164,144,68768,4,4,4}
print(a)
'''

# Dictionaries
# Create student dictionary
'''
student={
    "name":"yash",
    "age":16,
    "course":10
}
print("Dict : ",student)
'''

# Add a key
'''
student={
    "name":"yash",
    "age":16,
    "course":10
}
student["city"]="Hodal"
print("Dict : ",student)
'''

# Update a value
'''
student={
    "name":"yash",
    "age":16,
    "course":10
}
student["age"]=15
print("Dict : ",student)
'''

# Delete a key
'''
student={
    "name":"yash",
    "age":16,
    "course":10
}
student.pop("name")
print("Dict : ",student)
'''

# Loop through dictionary
'''
student={
    "name":"yash",
    "age":16,
    "course":10
}
for i,j in student.items():
    print(i,":",j)
'''

# Word frequency counter
'''
text=input("Enter a String Here... ")
words=text.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)
'''