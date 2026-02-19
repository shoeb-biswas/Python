def safe_divide (a, b):
  try:
    result = a/b
    print(result)
  except ZeroDivisionError:
    print("Division by zero")

safe_divide (3,0)
