#문제종류 : 구현
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60059

#유용한 부분(U)
"""
"""


#

#링크 : https://www.acmicpc.net/problem/3190

#풀이
"""
- n,k의 개수가 작음 > 완전탐색
- 매번 움직일때마다 오면 안되는 곳에 왔는지 체크
- 전체 필드의 외곽에 벽을 한칸씩 추가해서, 벽에 해당하는 좌표를 모두 오면안되는 곳으로 설정
- 몸이 길어진 만큼, 그전의 행동을 추적해서 오면안되는 곳에 추가. 새로운 곳으로 이동할 경우, 맨 뒤의 값은 제거하고 새로 이동된값을 가면 안되는 곳으로 넣어줌 > 큐
"""

n = int(input())
k = int(input())

A_place_list = []

for i in range(k):
    x,y = map(int,input().split())
    A_place_list.append((x,y))

move_list = []
move_count = int(input())
time = 0
for i in range(move_count):
    
    x, c = input().split()

    x = int(x) - time
    time += x
    
    move_list.append((int(x),c))

#마지막값 추가(이게 있어야 마지막 회전 후에도 꾸준히 움직임)
move_list.append((10000,'R'))

#이차원 리스트 생성 + 외곽벽=1로 지정
field_list = [[0]*(n+2) for _ in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        if i == 0 or i == n+1:
            field_list[i][j] = 1
        
        if j == 0 or j == n+1:
            field_list[i][j] = 1



for place in A_place_list:
    field_list[place[0]][place[1]] = "A"


#뱀 위치. x가 행임!!!!
x,y = 1,1
#directioin
direction = 'e'
#direction_dict

L_dict = {
    'e':'n',
    'n':'w',
    'w':'s',
    's':'w'
}
#direction_dict
R_dict = {
    'e':'s',
    's':'w',
    'w':'n',
    'n':'e'
}
#
dx = {
    'e':0,
    'w':0,
    's':+1,
    'n':-1,
}

dy = {
    'e':1,
    'w':-1,
    's':0,
    'n':0,
}

#뱀 몸 길이, 이전 위치
prev_place = [(1,1)]

#움직인 시간
play_count = 0

fin = False


for move in move_list:
    if fin:
        #마지막 츄라이를 더해줘야 함
        break
    
    for i in range(0,move[0]):
        
        #방향에 따른 좌표변환
        x += dx[direction]
        y += dy[direction]
        
        
        
        if field_list[x][y] == 1 or (x,y) in prev_place:
            fin = True
            break
        
        #사과일경우 몸 길이 증가 > 가면안되는 장소 추가
        if field_list[x][y] == 'A':
            prev_place.append((x,y))
            #사과제거
            field_list[x][y] = 0
            
        else:
            del prev_place[0]
            prev_place.append((x,y))
        
        #방향 전환
        if i == move[0]-1:
            if move[1] == 'L':
                direction = L_dict[direction]
            
            else:
                direction = R_dict[direction]
                
        print(x,y)
        print(prev_place)
        play_count += 1

print(x,y)
#마지막 값을 더해줘야 함
play_count += 1
print(play_count)