#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844

#풀이
"""
어려웠던 부분
    1. 각 점에서는 동서남북중 직사각형의 변이 있는 곳으로 움직일 수 있다. 이때 가면 안되는 곳을 체크하는 방법을 떠올리지 못했음. 
        가면 안되는 곳 = 등장하는 직사각형의 내부에 있는 점임
        직사각형이 최대 네개까지 등장하므로, 체크하는 게 그렇게 어렵지 않음(시간 복잡도가 그렇게 높지않음)
    
    2. 스케일 두배
        이동할 수 있는 점들을 구하고, 각 점에서 동서남북의 지점이 이동할 수 있는지의 유무를, 단순히 이동할 수 있는 점에 들어가있는지로 체크하면, 볼록하게 한칸 들어간 부분을 그냥 건너뛰게 된다. 따라서 이런 일 자체가 발생하지 않도록, 사각형들의 크기를 두배해서 계산한 후에 다시 구해진 값을 다시 2로 나눠줌
    
풀이
-각 점에서, 동서남북 중 이동할 수 있는 곳을 찾아 DFS로 풀면됨
-먼저 사각형의 스케일을 두배로 키움. 또한 첫 시작점과 아이템의 위치역시 *2를 해줌
    볼록하게 한칸 들어간 부분에서 발생하는 건너뜀을 미연에 방지하기 위함
-우선 이동할 수 있는 모든 점을 구함
    각 직사각형의 네변 위에 있는 모든 점을 구하고, 이를 집합으로 관리
    집합으로 관리하는 이유는, 집합이 해시테이블로 되어 있어 탐색속도가 빠르기 때문
-각 점의 동서남북을 구함
    새 점이 전체 범위를 넘어가지 않는지 체크
    새점이 이전에 구한 이동할 수 있는 모든 점 안에 포함되는지 체크. 이때 이동할 수 있는 점의 집합은 Set이기 때문에 탐색속도가 매우 빠르다 ㅇㅇ
    이동할 수 있는 점이라면, 그 점이 직사각형 안에 있는지를 확인(없어야 함)
    이까지 통과한 점들에 대해 cnt +1을 해주고 dfs를 재귀적으로 계속 실행
-캐릭터는 두 방향으로 이동할 수 있는데, 두 방향 모두를 계산해서 더 작은 움직임을 가진 방향을 택한 후, 2로 나눠서 반환
"""

from collections import deque

#동, 서 , 남, 북
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def make_rectangle_double(rectangle_lst:list)->list:
    
    for rec in rectangle_lst:
        for idx, station in enumerate(rec):
            rec[idx] = station *2
            
def is_in_rectangle_check(rectangle_lst:list,point:tuple) -> bool:
    """포인트가 직사각형 안에 있으면 False를 반환"""
        
    x,y = point
    for rec in rectangle_lst:
        rec_min_x, rec_min_y , rec_max_x, rec_max_y = rec
        
        if rec_min_x <x < rec_max_x and rec_min_y < y < rec_max_y:
            return False
            
    return True

def add_can_move_point(rectangle:list,can_move_set:set) -> set:
    """이동할 수 있는 지점을 더함"""
    rec_min_x, rec_min_y, rec_max_x, rec_max_y = rectangle
    
    for x in range(rec_min_x,rec_max_x+1):
        can_move_set.add((x,rec_min_y))
        can_move_set.add((x,rec_max_y))
        
    for y in range(rec_min_y,rec_max_y+1):
        can_move_set.add((rec_min_x,y))
        can_move_set.add((rec_max_x,y))
        
    return can_move_set
    


def solution(rectangle_lst, characterX, characterY, itemX, itemY):
    
    make_rectangle_double(rectangle_lst) #사각형 스케일 두배로 증가
    
    can_move_set = set()
    for rec in rectangle_lst: #이동할 수 있는 지점 구하기
        add_can_move_point(rec,can_move_set)
        
    visited_dict = {point:0 for point in can_move_set} #방문표시를 위한 dict

    #기본 셋팅
    queue = deque([])
    queue.append((characterX,characterY,0))
    ans_cnt = float('inf')
    
    
    def dfs(x,y,cnt):
        
        if x == itemX*2 and y == itemY*2:
            nonlocal ans_cnt
            ans_cnt = min(ans_cnt,cnt) #최솟값이 사용되도록 함
            return None # 함수의 종료(그래야 반대편으로 오는 방식도 계산할 수 있음)
        
        visited_dict[(x,y)] = 1 #방문표시
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 1 or ny <1 or nx >100 or ny > 100 : #벽을 넘어감
                continue
            
            if (nx,ny) not in can_move_set: #갈 수 있는 지점이 아님
                continue
            
            if visited_dict[(nx,ny)] != 0: #방문했으면 패스
                continue
            
            if is_in_rectangle_check(rectangle_lst,(nx,ny)):
                dfs(nx,ny,cnt+1)
    
    
    dfs(characterX*2,characterY*2,0)
    
    return ans_cnt // 2

#t1
rectangle, characterX, characterY, itemX, itemY = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7 ,8
result = 17

#t2
# rectangle, characterX, characterY, itemX, itemY = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9,7,6,1
# result = 11

#t3
# rectangle, characterX, characterY, itemX, itemY = [[1,1,5,7]], 1,1,4,7
# result = 9

#t4
# rectangle, characterX, characterY, itemX, itemY = [[2,1,7,5],[6,4,10,10]], 3,1,7,10
# result = 15

#t5
# rectangle, characterX, characterY, itemX, itemY = [[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1,4,6,3
# result = 10

print(solution(rectangle, characterX, characterY, itemX, itemY))