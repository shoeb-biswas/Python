num =input()
num1 =[]
for a in num:
  num1.append(int(a))

sum = 0
for x in range(len(num1)):
  y = 1
  for z in range(num1[x]):
    y = y * (z+1)
  sum = sum + y

if sum == int(num):
  print("Strong Number")
else:
  print("Not Strong Number")
