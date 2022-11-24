#문제종류 : 다이나믹프로그래밍
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42898

#풀이
"""
-주의 : 문제가 m,n을 바꿔서 줌(문제오류). 따라서 코드를 제출할 때, solution함수의 m,n을 바꿔서 줘야 정답이 맞음
-오른쪽과 아래로만 이동함
-따라서 특정칸은 바로 윗칸과 바로 왼쪽칸에 오는 방법을 합한 것임
-매칸을 저장하는 다이나믹프로그래밍과 BFS를 합쳐서 풀면됨
-BFS는 visitied가 필요함
"""
from collections import deque

#동,남,서,북
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#m,n바꿔줘야 하고(문제오류)
# x,y 둘 중 하나라도 2,2일때 , 1,2가 웅덩이이면 값이 2로 나와야 하는데 1번으로 나옴(테케1)
#효율성테스트전부아작남. > 방문체크를 위한 필드가 필요함

def solution(m, n, puddles):
    dp = [[0]*m for i in range(n)]
    visited = [[0]*m for i in range(n)]
    dp[0][0] = 1
    
    for x,y in puddles:
        dp[x-1][y-1] = -1

    queue = deque([])
    # print(dp)
    if m >=2:
        if dp[1][0] == 0:
            queue.append((1,0))
    
    if n >=2:
        if dp[0][1] == 0:
            queue.append((0,1))
    
    while queue:
        # print("now_dp : ",dp)
        # print("now_queue:",queue)
        
        
        x,y = queue.popleft()
        
        cnt = 0
        for i in range(2,4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #벽이라면 pass
            if nx < 0 or ny < 0:
                continue
            
            #웅덩이라면 pass
            if dp[nx][ny] == -1:
                continue
            
            cnt += dp[nx][ny]
            
        # print(dp)
        dp[x][y] = cnt
        
        #왼쪽과 위 모두 웅덩이인 경우
        if cnt == -2:
            cnt = 0
            
        dp[x][y] = cnt
        
        
        #동사1
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #벽 밖으로 나간다면 pass
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            
            #웅덩이라면 pass

            if dp[nx][ny] != 0:
                continue
            
            if visited[nx][ny] != 0:
                continue
            
            visited[nx][ny] = 1
            queue.append((nx,ny))
    # print(dp)
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
puddles = [[1,2]]

print(solution(m,n,puddles))
