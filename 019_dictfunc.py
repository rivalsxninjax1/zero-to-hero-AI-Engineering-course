student = {
    "name" : "sabin",
    "age" : 23,
     "marks" : [23,45,53,43,43]
}

def calculate_avg (student):
    average = sum(student["marks"])/ len(student["marks"])
    print(student["name"], "has an average marks of ", average)

calculate_avg(student)