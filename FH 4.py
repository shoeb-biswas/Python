a_friends = input().split()
b_friends = input().split()

# Mutual
uniqe1 = set(a_friends)
uniqe2 = set(b_friends)

mutual = uniqe1.intersection(uniqe2)

intera = uniqe1.difference(uniqe2)
interb = uniqe2.difference(uniqe1)
total = len(intera) + len(interb)

print(f"Mutual friends: {mutual}")
print(f"Unique to A: {intera}")
print(f"Unique to B: {interb}")
print(f"Total unique friends: {total}")
