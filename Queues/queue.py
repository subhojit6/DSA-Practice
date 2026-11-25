from collections import deque

queue = deque()

queue.append(5)
queue.append(15)
queue.append(25)

print(queue[0])
print(queue[-1])

queue.popleft()
print(queue)
print(queue[0])