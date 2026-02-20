# Map Function

lst = [847, 73,3, 43, 3,24,50]
def square(x):
    return x**2
lst = list(map(square, lst))
print(lst)

string = "Hello beasty, this is shoeb"
string1 = list(map(str.upper, string))
print(string1)

string1 = " ".join(string1)
print(string1)

# Map with Lambda
lst = [847, 73,3, 43, 3,24,50]
lst = list(map(lambda x: x**2 if x%2==0 else x, lst))
print(lst)
