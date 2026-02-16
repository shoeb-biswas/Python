arr = [10, 20, 30, 40]

itr = iter(arr) # 0
print(next(itr)) #
print(next(itr))
print(next(itr))
print(next(itr))

student = {'name': 'Alice', 'age': 20, 'city': 'Dhaka'}


itr = iter(student.keys())
print(next(itr))
print(next(itr))

for a in student.keys():
  print(a)
