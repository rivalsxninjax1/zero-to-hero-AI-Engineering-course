from collections import deque
queue = deque()
queue.append("data1")
queue.append("data2")
queue.append("data3")
queue.append("data4")
queue.append("data5")

print(queue.popleft())


print(queue)