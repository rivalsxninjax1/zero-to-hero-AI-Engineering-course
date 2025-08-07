students = {
    "student1": {"name": "sabin", "age": 23, "marks": [20, 40, 50]},
    "student2": {"name": "subin", "age": 43, "marks": [45, 45, 55]},
    "student3": {"name": "rubin", "age": 22, "marks": [22, 35, 25]},
}


def print_all_averages(students):
     heighest_avg = 0
     top_student = None
     for key, student in students.items():
        average = sum(student["marks"]) / len(student["marks"])
        if average > heighest_avg:
         heighest_avg = average
         top_student = student
     if top_student:
      print(f'{top_student["name"]} has the heightest average mark of  {heighest_avg:.2f}')
print_all_averages(students)
