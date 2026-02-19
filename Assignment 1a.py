num = input().split()
num = list(map(int,num))
even = list(filter(lambda x:x%2==0,num))
print(even)
