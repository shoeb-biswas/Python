with open("./sample_data/test2.txt","r") as file:

  print(file.tell())

  #read can only go forward
  print(file.read(5))
  print(file.tell())

  # seek can go backward
  file.seek(0)
  print(file.read(5))
