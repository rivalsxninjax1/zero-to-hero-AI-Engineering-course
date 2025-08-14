class Student:
    def __init__(self, name , age , marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average(self):
        return sum(self.marks)/len(self.marks)
    
students =[]
with open('023_txt.txt','r') as file:
    for line in file:
        name, age, marks_str = line.strip().split(',',2)
        age = int(age)
        marks = list(map(int, marks_str.split()))
        students.append(Student(name, age, marks))

def highest_marks(students):
    highest_mark=0
    top_student = None
    for student in students:
        avg = student.get_average()
        if avg > highest_mark:
            highest_mark = avg
            top_student = student
    if top_student:
        print(f'{top_student.name}has the highest average marks of {highest_mark:.2f} ')


highest_marks(students)