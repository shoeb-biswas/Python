arr = [1, 2, 3, 4, 5]

arr2 = list((map(lambda x: x*x, arr)))

print(arr2)

scores = [85, 92, 78, 65, 45]

def grade(x):
  if x >=80 : return f"Score is {x} and A+"
  if x >=70 : return f"Score is {x} and A"
  if x >=60 : return f"Score is {x} and A-"
  else : return f"Score is {x} and F-"

grades = list(map(grade,scores))
print(grades)
