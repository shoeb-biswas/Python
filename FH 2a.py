# Creating file with names
with open("./sample_data/names.txt","w") as file:
  file.write(" sHOeb\n")
  file.write("ontor \n")
  file.write(" shoeB\n")
  file.write(" saDmAn\n")


  with open("./sample_data/names.txt","r") as file:
    names = file.readlines()

  # Removing duplicate names
  clean_names = set()

  # Removing extra spaces & capitalized
  for name in names:
    clean_name = name.strip().capitalize()
    clean_names.add(clean_name)

  clean_names = sorted(clean_names)
  print(clean_names)
# saving

with open("./sample_data/clean_names.txt","w") as file:
  file.write('\n'.join(clean_names))
