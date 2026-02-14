with open("./sample_data/test.txt","a") as file:
  file.write("Cause i am learnig AI/ML\n")
  file.write("Thats why")
Strings = ['Hello','Hi','Bye Bye']
with open("./sample_data/test2.txt","w") as file:
  file.writelines(Strings)
