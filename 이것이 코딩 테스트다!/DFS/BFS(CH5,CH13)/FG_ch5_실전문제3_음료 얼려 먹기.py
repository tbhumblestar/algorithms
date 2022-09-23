#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60062?language=python3

#풀이
"""
- 주변에 0이 있을 경우, 1로 바꾸는 재귀함수를 만듬
- 값들이 전부 1로 변할때까지 직접적으로 실행해야 하는 재귀함수의 횟수를 카운트
"""



n,m = map(int,input().split())
field = []
for i in range(n):
    field.append(list(map(int,input())))

#시작
def dfs(x,y) -> None:
    
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #이거를 안에 안넣어주면, 1>2>1>2>1>2>1>2 이런식으로 무한히 실행됨
    if field[x][y] == 0:
        
    
        field[x][y] = 1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False


count = 0

for x in range(n):
    for y in range(m):
        if dfs(x,y) == True:
            count += 1

print(count)

#testcase
# 4 5
# 00110
# 00011
# 11111
# 00000

#testcase2
# 3 3
# 001
# 010
# 101

#실패한 풀이
"""
-전반적으로 동일했는데, field[x][y]==0 체크하는 게 dfs함수 밖에 있음
> dfs함수안에서 dfs가 조건없이 무한정 계속됨
> 원래는 좌표값으로 한정시켜주면 될거라 생각했지만 좌표값안에서 무한히 증식함
> 예를 들어 n이 3이면 x값이 1>2>1>2>1>2>1>2>1 이런식으로 무한히 증식될 수 있음
"""

n,m = map(int,input().split())
field = []
for i in range(n):
    field.append(list(map(int,input())))

#시작
def dfs(x,y) -> None:
    
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    
    
    field[x][y] = 1
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x+1,y)
    return False


count = 0

for x in range(n):
    for y in range(m):
        if field[x][y] == 0:
            print(x,y)
            count += 1
            dfs(x,y)

print(count)