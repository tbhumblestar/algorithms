#구현

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
    
print(x,y)