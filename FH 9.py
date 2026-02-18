try:
  with open("./sample_data/data.txt","r") as file:
    lines = file.readlines()
    print(len(lines))
except FileNotFoundError:
  print("There is no file exits with this name")
finally:
  print("Terminated")
