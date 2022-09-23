from collections import deque

queue = deque([1,1,3])
print("queue : ", queue)

queue2 = deque([])
queue2.append([1,1])
print("queue2 : ",queue2)

queue3 = deque([[1,2]])
x,y = queue3.popleft()
print("x,y :",f"{x},{y}")

# x,y = queue.popleft()

# print(x,y)