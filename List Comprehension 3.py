# CSV data cleaning
raw_data = [' 25 ', '30 ', ' 42', 'abc', '50']

clean = [int(r.strip()) for r in raw_data if r.strip().isdigit()]

print(clean)
# [25, 30, 42, 50]

d = [ [[1, 3], [4, 5]], [[6, 7], [8,9]]]

a = [k  for i in d for j in i for k in j]
print(a)

# for i in d:
#   for j in i:
#     for k in j:
#       print(k)
