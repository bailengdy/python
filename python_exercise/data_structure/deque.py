from collections import deque

queue = deque()

# enqueue: append at right, O(1)
queue.append("A")
queue.append("B")
queue.append("C")

# dequeue: popleft from left, O(1)
first = queue.popleft()  # "A"
print(first)
print(queue)             # deque(['B', 'C'])