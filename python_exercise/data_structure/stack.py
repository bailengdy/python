stack = []

# push: O(1) 摊销
stack.append(1)
stack.append(2)
stack.append(3)

# pop: (LIFO)/O(1)
top = stack.pop()
print(top)           # 3
print(stack)         # [1, 2]

#Using list as a stack with append / pop() at the end is amortised O(1).