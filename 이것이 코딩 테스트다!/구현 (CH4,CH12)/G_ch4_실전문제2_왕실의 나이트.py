#문제종류 : 구현

#유용한 부분(I)
"""

"""

#좋았던 부분(G)
"""
-발생하는 경우의 수가 적으면 그냥 완전탐색으로 왠만하면 가자!
"""


#풀이법 설명
"""
-입력받는 위치에 대하여, 발생할 수 잇는 모든 경우의수를 숫자로표현
-표현된 숫자들 중 조건에 부합하는 모든 경우를 카운트
"""
column_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
}



place = input()

c = column_dict[place[0]]
r = int(place[1])

dc = [2,2,-2,-2,1,1,-1,-1]
dr = [1,-1,1,-1,2,-2,2,-2]

count = 0
for i in range(0,8):
    nc = c + dc[i]
    nr = r + dr[i]
    
    if nc >= 1 and nc <= 8  and nr >= 1 and nr <= 8 :
        count += 1
        
print(count)


