def squre_addition(a,b):
    a=a**2
    b=b**2
    print(a+b)
squre_addition(10,20) 

# positional argument

def squre_addition(a,b):
    a=a**2
    b=b**2
    return a+b
squre_addition(10,20) + 10

#keyword argument
squre_addition(b=10,a=20) + 10
