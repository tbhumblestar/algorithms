#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60062?language=python3

#풀이
"""
- 주변에 0이 있을 경우, 1로 바꾸는 재귀함수를 만듬
- 값들이 전부 1로 변할때까지 직접적으로 실행해야 하는 재귀함수의 횟수를 카운트
"""

#n:세로, m:가로
n,m = map(int,input().split())
field = []
for i in range(n):
    

    field.append(list(map(int,input())))


from collections import deque

queue = deque([[0,0]])


#동,서,남,북
#x : 세로 , y : 가로
dx = [0,0,+1,-1]
dy = [1,-1,0,0]

while queue:
    x,y = queue.popleft()
    
    for i in range(4):
        n_x = x + dx[i]
        n_y = y +dy[i]
    
        if n_x < 0 or n_x >n-1 or n_y < 0 or n_y > m-1:
            continue
        
        if field[n_x][n_y] == 1:
            queue.append([n_x,n_y])
            field[n_x][n_y] += field[x][y]


print(field)
print(field[n-1][m-1])

#testcase
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111