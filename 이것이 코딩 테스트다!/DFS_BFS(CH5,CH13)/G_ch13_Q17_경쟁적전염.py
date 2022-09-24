#링크 : https://www.acmicpc.net/problem/18405

#풀이
"""
- BFS
- 처음에 2차원리스트틀 만들면서, 바이러스가 리 있을 경우, 바이러스리스트에 해당 바이러스의 종류, 시간(0), x좌표, y좌표를 넣어줌
- 바이러스 리스트를 정렬(숫자가 낮은것부터 증식)
- 바이러스 리스트를 큐로 만들고
- 큐가 비거나, 시간초에 도달할 때까지 진행
"""

from collections import deque

#n=실험관, k=바이러스종류
n,k = map(int,input().split())

#virus를 넣을 칸
data = []

field = []
for i in range(n):
    field.append(list(map(int,input().split())))
    for j in range(n):
        if field[i][j] != 0:
            data.append((field[i][j],0,i,j))

s,p_x,p_y = map(int,input().split())

#data의 첫번째 원소를 기준으로 정렬(낮은 번호의 바이러스부터 증식하니까)
data.sort()

queue = deque(data)
            
dx = [0,0,+1,-1]
dy = [-1,1,0,0]

#시작
while queue:

    virus,time,x,y = queue.popleft()

    #시목표시간초에 도달하면 바로 정지
    if time == s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx > n-1 or ny < 0  or ny > n-1:
            continue
        
        if field[nx][ny] == 0:
            field[nx][ny] = virus
            queue.append((virus,time+1,nx,ny))


print(field[p_x-1][p_y-1])
        
#testcase1
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

#testcase2
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2