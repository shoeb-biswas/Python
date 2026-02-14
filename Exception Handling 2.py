#Any exception can be handled by this way
n= int(input())
try:
  a=10/0
except Exception as e:
  print(e)
