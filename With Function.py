with open("./sample_data/meri_marji.txt","r") as file:
  content = file.readlines()
  print(content)
print(file.closed)
