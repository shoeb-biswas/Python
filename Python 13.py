s = {3,4,12,45,3,2,34}
s_iter = iter(s)
print(s_iter)

# Iterator
s = {3,4,12,45,3,2,34}
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))

for i in s:
    print(i)

# Lambda Function
sqr_addition = lambda x,y: x**2 + y**2
print(sqr_addition(2,3))

even = lambda x: x%2==0
print(even(10))
