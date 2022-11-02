from collections import deque

queue = deque([[0,0,1]])

print(queue)
x,y,z = queue.pop()
print(x)