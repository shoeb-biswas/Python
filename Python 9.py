squre = {x:x**2 for x in range(1,11) if x%2==0}
print(squre)

co = [(10.7, 9),(10, 70 ,8),(8.7)]
ordi = ["ak","Dilli","Dhaka"]
dicyionaty ={co:ordi for co,ordi in zip(co,ordi)}
print(dicyionaty)

lst = [10, 928, 82, 74, 38, 10, 928, 748, 38, 10]
lst1 = set(lst)
print(lst1)
lst2 = list(lst1)
print(lst2)
