stack = []

stack.append("a")
stack.append("b")
stack.append("c")
print(stack)

print(" top item", stack[-1])

item = stack.pop()
print("popped item", item)
print(stack)
print(len(stack)==0)