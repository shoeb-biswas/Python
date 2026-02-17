scores = [85, 92, 78, 65, 45]

select = list(filter(lambda x: x>80 , scores))
print(select)

# Valid Email Filter
emails = ["user@mail.com", "invalid", "test@gmail.com", "no@", "admin@site.org"]

def check(s):
  if '@' in s and '.' in s:
    return s;


# selected = list( filter(lambda e: '@' in e and '.' in e  , emails) )
selected = list( filter(check , emails) )
print(selected)
