students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]
students = dict(students)
sorted_marks = sorted(students.items(), key=lambda x: x[1], reverse=True)
Top3 = sorted_marks[:3]

print("Top 3 Students:")
for name, mark in Top3:
  print(f"{name} - {mark}")
