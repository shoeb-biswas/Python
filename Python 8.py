r = {28, 4, 3, 0, 8}
r.add(25)
print(r)
r.remove(28)
print(r)
r.pop()
r.pop()
print(r)

d = {12, 45, 54, 22, 90, 84}
b = {4, 45, 3 , 5, 49, 4}

print(d.union(b))
print(d.intersection(b))
print(d.isdisjoint(b))
print(d.issubset(b))

dic = {"name": "Shoeb", "age": "20", "Course": "AI/ML"}
print(dic)
print(dic["name"])
print(dic.get("age"))
dic["age"] = 22
print(dic)
dic["adress"] ="Kushtia"
print(dic)
dic.update({"fingerprint":"yes"})
print(dic)
del dic["age"]
print(dic)
keys = dic.keys()
print(keys)
values = dic.values()
print(values)
items = dic.items()
print(items)
for key, value in dic.items():
    print(key,value)
