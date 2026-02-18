with open("./sample_data/data.txt","w") as file:
  file.write("Learning Python is fun!")

with open("./sample_data/data.txt","r") as file:
  data = file.read()
  print(data)
