#링크 : https://www.acmicpc.net/problem/14502

#풀이
"""
- M,N의 개수가 작음 > 완전탐색
- 막을 수 있는 벽의 경우의 수를 Combination으로 구한다음
- 각 케이스별로 DFS를 구함
"""

from itertools import combinations

#n=가로, m=세로
n,m = map(int,input().split())

field = []

#0은 빈칸, 1은 벽, 2는 바이러스
for i in range(n):
    field.append(list(map(int,input().split())))

max_place = 0

can_build_wall_place = []

for x in range(n):
    for y in range(m):
        if field[x][y] == 0:
            can_build_wall_place.append((x,y))

virus_place =[]
for x in range(n):
    for y in range(m):
        if field[x][y] == 2:
            virus_place.append((x,y))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,test_field):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <0 or nx > n-1 or ny <0 or ny > m-1:
            continue
        
        print(test_field)
        if test_field[nx][ny] == 0:
            test_field[nx][ny] = 2
            print(test_field)
            dfs(nx,ny,test_field)
            
#시작
print(field)

for new_walls in combinations(can_build_wall_place,3):
    test_field = [item[:] for item in field]
    
    for x,y in new_walls:
        test_field[x][y] = 1
        
    for x,y in virus_place:
        dfs(x,y,test_field)
    
    count = 0
    
    for x in range(n):
        for y in range(m):
            if test_field[x][y] == 0:
                count += 1
    
    # print("test_field :",test_field)
    # print("count :",count)
                
    max_place = max(max_place,count)
print(virus_place)
print(max_place)
        
# print(max_place)
    
#testcase1
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2