#Variable sized argument
def squre_addition(*args):
    sumation = 0
    for i in args:
        i**2
        sumation+=i
    return sumation
    
squre_addition(10,45,3,4,4,89)

#Keyword Variable sized argument
def square_addition(**kwargs):
    print(kwargs)
    for key, val in kwargs.items():
        print(f"{key} : {val}")
square_addition(Name = "Shoeb",Age= "20",Status="Single") 

def give_domes():
    return 10,29
give_domes() 

#unpacking

x,y = give_domes()
print(x,y)
