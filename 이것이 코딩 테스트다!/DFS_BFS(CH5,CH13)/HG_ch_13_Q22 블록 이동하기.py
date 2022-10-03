#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60063?language=python3

#풀이
"""
- 방향성에 따른 visited
    + 가로, 세로 하나씩
- 기기의 상태는 같은 좌표라 해도 두가지임. 가로/세로
- BFS를 구현
    + count를 들고다님
    + 가로세로 방향별로 8가지 케이스(동서남북이동4, 회전4)를 테스트하면서 BFS로 이동

- 런타임 에러남.. 테스트케이스 세개가 시간초과가 발생.. 하 ...
"""
# print()
# print()
# print()
# print()
from collections import deque

queue = deque([])


#가로 0, 세로 ,1
#동,서,남,북
dx = [0,0,+1,-1]
dy = [1,-1,0,0]

#회전
def rotation_checker(x1,y1,direction,field):
    
    x2 = x1 if direction == 0 else x1+1
    y2 = y1+1 if direction == 0 else y1
    
    lst = [2,3] if direction == 0 else [0,1]
    
    n = len(field)

    res = []

    for i in lst:
        
        #nx,ny 회전을 위해 체크해야 하는 지점
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        
        #필드를 넘어가면 종료
        if nx1 < 0 or nx1 > n-1 or ny1 < 0 or ny1 > n-1 or nx2 < 0 or nx2 > n-1 or ny2 < 0 or ny2 > n-1:
            continue
        
        #벽이라면 종료
        if field[nx1][ny1] == 1 or field[nx2][ny2] == 1:
            continue
        
        #세로방향 > 가로방향 . 오른쪽 체크
        if i == 0:    
            res.append([x1,y1,1 if direction == 0 else 0])
            res.append([x1+1,y1,1 if direction == 0 else 0])
        
        #세로방향 > 가로방향 . 왼쪽 체크
        if i == 1:    
            res.append([x1,y1-1,1 if direction == 0 else 0])
            res.append([x1+1,y1-1,1 if direction == 0 else 0])
        
        #가로방향 > 세로방향 . 아래 체크
        if i == 2:    
            res.append([x1,y1,1 if direction == 0 else 0])
            res.append([x1,y1+1,1 if direction == 0 else 0])
            
        #가로방향 > 세로방향 . 위쪽체크
        if i == 3:
            res.append([x1-1,y1,1 if direction == 0 else 0])
            res.append([x1-1,y1+1,1 if direction == 0 else 0])
        
    return res

def bfs(field):
    
    n = len(field)
    visited = [[[0]*n for i in range(n)],[[0]*n for i in range(n)]]
    #시작점
    queue.append([0,0,0,0])
    
    while queue:
        print("queue :",queue)
        
        #기계머리. 항상 꼬리보다 위쪽 혹은 왼쪽에 위치
        x1,y1,direction,count = queue.popleft()
        
        # print("queue start")
        # print("count :",count)
        # print("x,y :",x1,y1)
        
        
        #방문표시
        visited[direction][x1][y1] = 2
        
        #기계꼬리
        x2 = x1 if direction == 0 else x1+1
        y2 = y1+1 if direction == 0 else y1
        
        #도착
        if x1 == n-1 and y1 == n-1:
            break
        if x2 == n-1 and y2 == n-1:
            break
        
        #단순이동
        for i in range(4):
            
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            
            # print('단순이동 (nx1,ny1),(nx2,ny2) :',(nx1,ny1),(nx2,ny2))
            #필드를 넘어가면 종료
            if nx1 < 0 or nx1 > n-1 or ny1 < 0 or ny1 > n-1 or nx2 < 0 or nx2 > n-1 or ny2 < 0 or ny2 > n-1:
                continue
            
            #벽이라면 종료
            if field[nx1][ny1] == 1 or field[nx2][ny2] == 1:
                continue
            
            #이미 방문한 곳이라면 종료
            if visited[direction][nx1][ny1] != 0:
                continue
            
        
            # print(f"{nx1}, {ny1}, {direction} 큐 추가")
            queue.append([nx1,ny1,direction,count+1])
                
                
        #회전
        rotate_place = rotation_checker(x1,y1,direction,field)
        # print("rotate_place :",rotate_place)
        
        
        for nx1,ny1,direction in rotate_place:
            
            #방문한 곳이면 안가도 됨
            if visited[direction][nx1][ny1] != 0:
                continue
            queue.append([nx1,ny1,direction,count+1])
            
    return count     
            

def solution(field):
    
    answer = bfs(field)
    # print("answer :",answer)
    return answer


# t1
# field = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

# t2
# field = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
# ans : 21

# t3
# field = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]
# ans : 33

# solution(field)