from collections import deque

queue = deque([])
queue.append([0,1])
print(queue)


x1,y1,direction = [1,1,1]
        

n = 4
visited_LR = [[0]*n for i in range(n)]
print(visited_LR)

direction = 0
a = [1 if direction == 0 else 0]
print(a)