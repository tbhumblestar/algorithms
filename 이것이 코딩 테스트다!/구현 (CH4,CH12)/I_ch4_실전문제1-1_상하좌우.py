#문제종류 : 구현

#유용한 부분
"""
-각 움직임(LRUD)를 리스트를 사용해서 (+1,-1)과 같은 수식으로 정리
"""


#풀이법 설명
"""
-각 움직임(LRUD)를 리스트를 사용해서 (+1,-1)과 같은 수식으로 정리
-문제에서 제시한 조건(지도 밖으로 튀어나갈 수 없다)아래에서 움직임에 따른 수식을 더해주면 됨
"""


n= int(input())
move_list = list(input().split())
#시작점
x,y = 1,1

#동,서,남,북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

move_dict = {
    'R':0,
    'L':1,
    'D':2,
    'U':3,
}

for move in move_list:
    if x + dx[move_dict[move]] <1 or x + dx[move_dict[move]] > n or y + dy[move_dict[move]]<1 or y + dy[move_dict[move]] > n:
        pass
    else:
        x += dx[move_dict[move]]
        y += dy[move_dict[move]]
    
print(x,y)