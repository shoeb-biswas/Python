Sentence = list(input().split())
minimum=" "
for word in Sentence:
  longest = len(word)
  if longest> len(minimum):
    minimum = word

print(minimum)
