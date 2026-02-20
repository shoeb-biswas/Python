string = "Welcome to Phitron ML course"
processed_string = string.lower()
print(processed_string)
print(len(string))
print("phitron" in processed_string)

string = "Welcome to phitron ML course, phitron"
print(len(string))
print("phitron" in string)
index = string.find("phitron")
index1 = string.rfind("phitron")
print(index)
print(index1)

string = "Welcome to phitron ML course, phitron"
print(len(string))
print("phitron" in string)
index = string.find("phitron")
index1 = string.rfind("phitron")
count = string.count("phitron")
print(count)
print(index)
print(index1)
