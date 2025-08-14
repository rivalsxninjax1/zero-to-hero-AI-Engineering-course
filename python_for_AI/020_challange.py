students = {
    "student1": {"name": "sabin", "age": 23, "marks": [20, 40, 50]},
    "student2": {"name": "subin", "age": 43, "marks": [45, 45, 55]},
    "student3": {"name": "rubin", "age": 22, "marks": [22, 35, 25]},
}

def print_all_averages(students):
    for key, student in students.items():
        average = sum(student["marks"]) / len(student["marks"])
        print(f'{student["name"]} has an average mark of {average:.2f}')

print_all_averages(students)
