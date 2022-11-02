#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844

#유용한 부분 : 첫 풀이를 dfs로 풀었으나 시간초과가 발생함 > bfs로 풀 수 있는 문제를 dfs로 풀면 더 많은 연산이 사용되므로 bfs로 풀 수 있으면 bfs로 풀자


#풀이
"""
#첫풀이 : dfs로 풀었었음 > 그러나 시간초과가 발생함 > bfs로 풀 수 있는 문제를 dfs로 풀면 반드시 시간초과가 남 ㅠㅠ

#두번쨰 풀이
bfs를 사용
-최대횟수인 n*m를 넘어가면 함수종료
-칸을 넘어가면 함수종료
-벽이면 함수 종료
-이미 갔던 곳이면 종료
종료되지 않으면(유효하면)
해당 위치에 방문을 표시
동서남북으로 이동한 위치 & 카운트를 1증가 큐에 넣음
"""

from collections import deque

#동, 서 , 남, 북
dx = [0,0,+1,-1]
dy = [1,-1,0,0]

def solution(maps):
    
    #세로 길이
    n = len(maps)
    #가로 길이
    m = len(maps[0])
    
    #방문리스트
    visited = [[0]*m for i in maps[:]]
    
    #시작점
    queue = deque([[0,0,1]])

    while queue:
        x,y,cnt = queue.popleft()
        
        #최대횟수인 n*m를 넘어가면 종료
        if cnt > n*m :
            continue
        
        #칸을 넘어가면 함수종료
        if x <0 or x >= n or y < 0 or y >= m :
            continue
        
        #벽이면 종료
        if maps[x][y] == 0:
            continue
        
        #방문했으면 종료
        if visited[x][y] != 0:
            continue
        
        visited[x][y] = cnt
        # print(x,y,cnt,visited)
        # print(queue)
        
        if x == n-1 and y == m-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            queue.append([nx,ny,cnt+1])
            # print(queue)
            

    #도착하지 못했음
    return -1

#t1
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
ans = 11

#t2
# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
ans = -1

#t3
# maps = [[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]
ans = 9

#t4
# maps = [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1]]
ans = 9

print(solution(maps))