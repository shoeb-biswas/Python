name = "Shoeb"
age=22
height = 5.5
print(f"My name is {name}. My age is {age}. My height is {height+10}")

numbers = [100, 20, 30, 70, 80]
print(numbers[2])
numbers[2] = 90
numbers.append(80)
print(numbers[0:3])
print(numbers)
numbers.insert(0,75)
print(numbers)
numbers.pop()
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

even = [x for x in range(1,101) if x%2==0]
print(even)
