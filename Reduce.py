from functools import reduce
arr = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, arr)
print(sum)

from functools import reduce
arr = [1,2,3,4,5]

sum = reduce(lambda x,y: x*y, arr, 10)
print(sum)

from functools import reduce

sentences = ["I love Python", "Machine Learning is fun", "AI is the future"]

def count_vowel(text):
  sum=0
  for ch in text.lower():
    if ch in 'aeiou':
      sum+=1

  return sum

total = reduce(lambda x, y: x + count_vowel(y), sentences, 0)
print(total)
