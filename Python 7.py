n =input()
p = n.split()
brightness = int(p[0])
thresold = int(p[1])
if brightness >= thresold:
    print("ON")
else:
    print("OFF\n")

n = input()
p = n.split()
x = float(p[0])
min_v= float(p[1])
max_v= float(p[2])
norm = (x - min_v) / (max_v - min_v)
print(norm)

s = {1,2,3,4,5,6,3,4,3,4,1}
if 3 in s:
    print("3 present")
else:
    print("not present")
sum=0
for f in s:
    sum+=f
print(sum)
