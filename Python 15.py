# Filter
numbers = [i for i in range(100)]
even = list(filter(lambda x: x%2==0, numbers))
print(even)

dta = [0,1, None, "didi", [7,9], None]
data = list(filter(None,dta))
print(data)

# String with lambda and filter
vowel = list(filter(lambda x:x in "AEIOU",string1))
print(vowel)
