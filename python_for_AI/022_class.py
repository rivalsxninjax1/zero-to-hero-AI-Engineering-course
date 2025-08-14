class Student:
    def __init__ (self, name, age , marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average(self):
        return sum(self.marks)/len(self.marks)
 #creating the list of student objects 

students = [
        Student("sabin",23, [23,4,23]),
        Student("nabin",23, [24,4,23]),
        Student("prabin",23, [43,44,23])
]

def find_top_students(students):
 top_student = None
 highest_marks = 0
 for student in students:
    avg = student.get_average()
    if avg > highest_marks:
     highest_marks = avg
     top_student = student

 if top_student:
   print(f'{top_student.name} has the highest average of {highest_marks:.2f}')


find_top_students(students)