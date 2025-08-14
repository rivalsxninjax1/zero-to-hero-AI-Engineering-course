marks = [65, 70, 90, 85, 77]
marks.append(88)
marks.remove(min(marks))

for i in marks:
   print(i)

ave = sum(marks)/len(marks)
print(ave)