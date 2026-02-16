def fun():
  for i in range(5):
    print("Kaj shuru holo ", i)
    yield i


ltr = fun()
print(next(ltr))
# #sdfsdf
# #sdfsdf
print("hello ")
print(next(ltr))
