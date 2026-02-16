def add(*a):
  print(type(a))
  print(a)

add(1, 2, 3, 4, 5, 6, 7, 8)
def info(**k):
    print(type(k))
    print(f"{k['name']} age is: {k['age']} and {k['country']}")

info(age=20, name="Rakib", country="bd", phone="01821", )
def func()->float:
  return 10

print(func())
