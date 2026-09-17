#  Dictionary loop
student={
    "name":"Mohit",
    "Age":21,
    "course":"python"
    }

for key,value in student.items():
    print(f"{key}:{value}")

#  Dictionary nested

students={
    "student1":{
        "name":"Mohit",
        "age":21,
        "course":"btech"
    },
    "student2":{
        "name":"Nikhil",
        "age":18,
        "course":12
    }

}

print(students["student1"]["name"])
print(students["student2"]["name"])