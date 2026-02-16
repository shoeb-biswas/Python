numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared.append(num * num)

print(squared)

numbers = [1, 2, 3, 4, 5]

squared = [n for n in numbers]

print(squared)

numbers = [1, 2, 3, 4, 5]

squared = [n for n in numbers if n%2==1]

print(squared)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = [n*n if(n*n >30) else 0 for n in numbers if n%2==1]

print(squared)

scores = [85, 42, 76, 91, 35]
grades = [f'Pass {s}' if s >= 50 else f'Fail {s}' for s in scores]
print(grades)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = [j for i in matrix for j in i]

print(f)
