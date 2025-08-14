person = {
    "name" :"sabin",
    "age" : 24,
    "hobbies" : ["guitar","singing"] 
}

person["is_student"] = True

print(person["hobbies"])

for i, j in person.items():
    print(i,":",j)

del person["age"]

for i,j in person.items():
    print(i,":",j)

