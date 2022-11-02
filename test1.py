#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
#풀이
"""
-첫풀이 > dfs로 풀었었음 > 그러나 시간초과가 발생함 > bfs로 풀 수 있는 문제를 dfs로 풀면 반드시 시간초과가 남 ㅠㅠ
dfs

종료조건
-최대횟수인 n*m를 넘어가면 함수종료
-칸을 넘어가면 함수종료
-벽이면 함수 종료
-이미 갔던 곳이 아니라면

종료되지 않을 경우 해당 지점을 방문표시하고, 동서남북지역으로 dfs
"""



#동, 서 , 남, 북
dx = [0,0,+1,-1]
dy = [1,-1,0,0]

def solution(maps):
    
    #세로 길이
    n = len(maps)
    #가로 길이
    m = len(maps[0])
    
    #시작점
    x,y = 0,0
    cnt = 1
    
    #방문리스트
    visited = [[n*m]*m for i in maps[:]]
    
    res_cnt = n*m + 1
    
    
    
    
    #결과 카운트
    
    def dfs(x,y,cnt):
        
        #최대횟수인 n*m를 넘어가면 함수종료
        if cnt > n * m :
            return None
        
        #칸을 넘어가면 함수종료
        if x <0 or x >= n or y < 0 or y >= m :
            return None
        
        #벽이면 종료
        if maps[x][y] == 0:
            return None
        
        #이미 갔던 곳이면서, 카운트가 지금 보다 낮으면 종료(더 효율적일 수 없으니까)
        # print(visited)
        if visited[x][y] <= cnt :
            return None
        
        #아무 문제 없다면 로직수행
        
        # print(x,y,cnt,visited)
        
        if x == n-1 and y == m-1:
            nonlocal res_cnt
            res_cnt = min(res_cnt,cnt)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny,cnt+1)
            
            
    dfs(x,y,cnt)
    
    #끝에 도달할 수 없다면

    ans = -1 if res_cnt == m*n + 1 else res_cnt
    # print(visited)
    return ans


#t1
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
ans = 11

#t2
maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
ans = -1

#t3
# maps = [[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]
ans = 9

#t4
# maps = [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1]]
ans = 9



print(solution(maps))