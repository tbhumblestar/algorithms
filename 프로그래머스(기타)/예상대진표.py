"""
-예상대진표(https://school.programmers.co.kr/learn/courses/30/lessons/12985)
-받은 수를 정렬해줘서, 큰 수를 구별
-경기가 진행되면서 선수는 각각 2로 나눈 값을 올림한 값을 배정받음
-두 사람이 만나려면, 큰 수가 2의 배수이면서 & 두 사람의 값의 차이가 1이 되어야 함
-조건에 맞게 while문을 실행해주면 끝
"""

from math import ceil

def solution(n,a,b):
    
    x,y = list(sorted([a,b]))
    cnt = 1
    
    while y-x != 1 or y % 2 != 0:
        cnt += 1
        x = ceil(x/2)
        y = ceil(y/2)

        
    return cnt

#t1
n,a,b = 8,4,7
res = 3
print(solution(n,a,b))
