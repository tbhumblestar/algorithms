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