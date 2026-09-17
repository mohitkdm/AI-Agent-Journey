# Dictionary Opeartion 

dictionary={
    "name":"Mohit",
    "age":21,
    "course":"python"
}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.get("age"))
dictionary.pop("name")
print(dictionary)
dictionary["age"]=22
print(dictionary)
# dictionary.clear()
# print(dictionary)


# get vs []

print(dictionary.get("name")) # they are not give error if key not present in dictionary
print(dictionary["name"]) # they are give error if key not present in dictionary