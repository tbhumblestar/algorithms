#링크 : https://www.acmicpc.net/problem/14888

#풀이
"""
-벽이 세우질 수 있는 모든 경우의 수를 구함
-구해진 모든 겨웅의 수에 대해 dfs를 돌려서 T를 전이
    -dfs에 카운트를 넣어서, 카운트가 n을 넘어가면 종료
    -필드를 넘어가도 종료
    -벽을 만나도 종료
    -dfs가 동서남북으로 전이되는 게 아니라, 가로 세로 중 하나로만 전이되어야 함
-T를 전이했는데, 학생을 발견하면 그 케이스는 실패
-전체 케이스에서 학생이 발견되지 않는 케이스가 있으면 Yes
"""


from itertools import combinations
from re import S


n = int(input())

field = []
student_places = []
teacher_places = []
empty_places = []
for i in range(n):
    lst = list(input().split())
    field.append(lst)
    for j in range(n):
        empty_places.append((i,j))

        if lst[j] == 'S':
            student_places.append((i,j))
        if lst[j] == 'T':
            teacher_places.append((i,j))

empty_places = [i for i in empty_places if i not in student_places + teacher_places]

#동,서,남,북
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y,count,test_field,direction):
    
    global surv
    #카운트가 넘으면 전이 종료
    if count == n-1:
        return None
    
    #맵을 벗어나면 전이 종료
    if x < 0 or x > n-1 or y <0 or y > n-1:
        return None
    
    #벽을 만나면 전이종료
    if test_field[x][y] == 'W':
        
        return None
    
    
    #현재 위치에 S가 있다면 > 실패
    if test_field[x][y] == 'S':
        surv = False
        # print("faield station :",x,y)
        # print("failed")
        # print(test_field)
        return None
        
    #아무문제가없다면 전이됨
    test_field[x][y] = 'T'
        
    #전이 : 모든 방향으로 전방위 전이가 아니라, 한줄로만 전이가됨.
    for i in direction:
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        dfs(nx,ny,count+1,test_field,direction)
        

for w1,w2,w3 in combinations(empty_places,3):
    test_wall_places = [w1,w2,w3]
    test_field = [item[:] for item in field]
    test_field[w1[0]][w1[1]] = 'W'
    test_field[w2[0]][w2[1]] = 'W'
    test_field[w3[0]][w3[1]] = 'W'
    surv = True
    
    for x,y in teacher_places:
        dfs(x,y,0,test_field,[0,1])
        dfs(x,y,0,test_field,[2,3])
        # print(test_field)
    
    if surv:
        # print("true!")
        # print(test_field)
        break

if surv:
    print("YES")
else:
    print("NO")




#testcase1
# 5
# X S X X T
# T X S X X
# X X X X X 
# X T X X X 
# X X T X X 

#TESTCASE2
# 4
# S S S T
# X X X X
# X X X X 
# T T T X

#TESTCASE3
# 6
# S X T X X S
# X X X T X X 
# X X X X X S
# X X X X X X 
# X X X X X X 
# X X X X X T