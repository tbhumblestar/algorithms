#문제종류 : 다이나믹프로그래밍
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42898

#풀이
"""
-주의 : 문제가 m,n을 바꿔서 줌(문제오류). 따라서 코드를 제출할 때, solution함수의 m,n을 바꿔서 줘야 정답이 맞음
-오른쪽과 아래로만 이동함
-따라서 특정칸은 바로 윗칸과 바로 왼쪽칸에 오는 방법을 합한 것임
-매칸을 저장하는 다이나믹프로그래밍과 BFS를 합쳐서 풀면됨
-BFS는 visitied를 사용해서 방문표시를 해줘야 함. 그렇지 않으면 큐가 너무많이 생김(중복되는 큐가 발생함) > 시간초과
"""

from collections import deque

#동,남,서,북
#x:좌우(가로),y:남북(세로)
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def solution(m, n, puddles):
    #m:가로, n:세로
    dp = [[0] * m for i in range(n)]
    visited = [[0]*m for i in range(n)]
    dp[0][0] = 1
    
    #웅덩이 표시
    for x,y in puddles:
        dp[x-1][y-1] = -1
    
    queue = deque([])
    
    #첫부분 추가
    if m >= 2:
        if dp[0][1] == 0:
            queue.append((0,1))
            
    if n >= 2:
        if dp[1][0] == 0 :
            queue.append((1,0))
    
    def dp_writer(x,y):
        cnt = 0
        for i in range(2,4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #벽이라면 pass
            if nx < 0 or ny <0 :
                continue
            
            if dp[nx][ny] == -1:
                continue

            cnt += dp[nx][ny]
            
        dp[x][y] = cnt
    
    def queue_appender(x,y):
        for i in range(0,2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #벽 밖으로 나간다면 pass
            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            
            #웅덩이라면 pass
            if dp[nx][ny] != 0:
                continue
            
            #이미 방문했었다면 pass
            if visited[nx][ny] != 0:
                continue
            
            #방문표시
            visited[nx][ny] = 1
            queue.append((nx,ny))
    
    while queue:
        # print(queue)
        # print(dp)
        x,y = queue.popleft()
        dp_writer(x,y)
        queue_appender(x,y)

    
    return (dp[n-1][m-1] % 1000000007)


#t1
m = 4
n = 3
# puddles	= [[2, 2]]

#t2
m = 4
n = 3
puddles = []

#t3
# m = 4
# n = 4
# puddles = [[1,2]]

print(solution(m,n,puddles))