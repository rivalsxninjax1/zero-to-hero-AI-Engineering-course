from collections import deque
queue = deque()

queue.append("batch1")
queue.append("batch2")
queue.append("batch3")
queue.append("batch4")
queue.append("batch5")

print(queue.popleft())
print(queue.popleft())


queue.append("batch6")
queue.append("batch7")

print(queue)