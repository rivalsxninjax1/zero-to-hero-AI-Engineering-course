student = {
    "name":"sabin",
    "class" : 9,
    "age":40
}
student["cast"] = "high cast"
student["age"]= 32
print(student["name"])
print(student["age"])
del student["cast"]

#one way
for key, value in student.items():
    print(key, ":", value)



#another way s
for i in student:

    print(i, "=", student[i]) 