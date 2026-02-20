l = ["a","b","c","d"]
print(l[1:4][::-2])

stack = []
for i in range(1,4):
    stack.append(i)
stack.pop()
print(stack[-1])

question = [10,20,30,40]
question.pop(1)
question.append(50)
question.pop(0)
print(question[0])
