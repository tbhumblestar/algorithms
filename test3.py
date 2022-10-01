import sys
sys.setrecursionlimit(100000)

from itertools import combinations


n,L,R = map(int,input().split())

field = []

for i in range(n):
    lst = list(map(int,input().split()))
    field.append(lst)

#동,서,남,북
dx = [0,0,+1,-1]
dy = [1,-1,0,0]


def dfs_chekcer(x,y,test_field,check_num,position_dict):
    
    global field
    
    #현재 장소가 이미 체크된 장소라면 stop
    if test_field[x][y] != 0:
        pass
    else:
        test_field[x][y] = check_num
        
        if check_num in position_dict:
            position_dict[check_num].append((x,y))

        else:
            position_dict[check_num] = [(x,y)]            

    
    #동서남북
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #새로 만드는 애가 필드를 넘어가면 스탑
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            continue
        
        #새로 이동하는 장소기 이미 체크가 완료된 장소라면 스탑     
        if test_field[nx][ny] != 0:
            continue
        
        if L <= abs(field[x][y] - field[nx][ny]) and abs(field[x][y] - field[nx][ny]) <= R:
            dfs_chekcer(nx,ny,test_field,check_num,position_dict)
            

def bfs(count,field):
    
    test_field = [[0] * n for _ in range(n)]
    position_dict= {}
    for x in range(n):
        for y in range(n):
            check_num = '0' + str(x) + '0' + str(y)
            dfs_chekcer(x,y,test_field,check_num,position_dict)
            
    go = False

    for i,v in position_dict.items():
        pop_sum = 0
        if len(v) > 1:
            go = True
            length = len(v)
            for x,y in v:
                pop_sum += field[x][y]

            for x,y in v:
                field[x][y] = pop_sum // length
            
    if go:
        bfs(count+1,field)
    else:
        print(count)

bfs(0,field)
#t1
# 2 20 50
# 50 30
# 20 40

#t2
# 2 40 50
# 50 30
# 20 40

# t3
# 2 20 50
# 50 30
# 30 40

# t4
# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# t5.1
# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10

# t5.2
# 4 10 50
# 10 100 50 50
# 50 50 50 50
# 50 50 50 50
# 50 50 100 50

# t5.3
# 4 10 50
# 30 66 66 50
# 30 66 50 50
# 50 50 62 50
# 50 62 62 62

# t5.4(끝!)
# 4 10 50
# 48 48 54 54
# 54 54 54 50
# 54 54 54 54
# 54 54 62 54 