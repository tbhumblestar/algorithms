#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60058

#풀이
"""
- BFS
- '('와 ')'의 개수를 카운트
- '(' 와 ')'의 개수가 같아지는 지점이 u와 v를 나누는 곳이 됨
- u의 마지막 글자가 ')'이면 무조건 올바른 문자열
"""

def change_letters(letters):
    length = len(letters)
    
    ret = '(' + letters[1:length-1] + ')'

def dfs(letters,answer_letters):
    
    left_count = 0
    right_count = 0
    
    for i,v in enumerate(p):
        if v == '(' :
            left_count += 1
        else:
            right_count +=1 
            
        if left_count == right_count:
            
            if i == len(letters)-1:
                u = letters[:]
                v = ''
            else:
                u = letters[0:i+1]
                v = letters[i+1:]
        
        if u[-1] == ')':
            answer_letters += u
            dfs(v,answer_letters)
        
        


def solution(p):
    
    
    
    
    
    
    answer = ''
    return answer


from collections import deque

#n=실험관, k=바이러스종류
n,k = map(int,input().split())

#virus를 넣을 칸
data = []

field = []
for i in range(n):
    field.append(list(map(int,input().split())))
    for j in range(n):
        if field[i][j] != 0:
            data.append((field[i][j],0,i,j))

s,p_x,p_y = map(int,input().split())

#data의 첫번째 원소를 기준으로 정렬(낮은 번호의 바이러스부터 증식하니까)
data.sort()

queue = deque(data)
            
dx = [0,0,+1,-1]
dy = [-1,1,0,0]

#시작
while queue:

    virus,time,x,y = queue.popleft()

    #시목표시간초에 도달하면 바로 정지
    if time == s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx > n-1 or ny < 0  or ny > n-1:
            continue
        
        if field[nx][ny] == 0:
            field[nx][ny] = virus
            queue.append((virus,time+1,nx,ny))


print(field[p_x-1][p_y-1])
        
#testcase1
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

#testcase2
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2