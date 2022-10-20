#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

#풀이
"""
-던전이 8개 > 완전탐색
-모든 경우의 수에 대해서 순서를 바꿔가며 완전탐색 실시
"""
from itertools import permutations


def solution(k, dungeons):
    
    max_cnt = 0
    
    for i in list(permutations(dungeons,len(dungeons))):
        
        life = k
        cnt = 0
        for need,use in i:
            if life >= need:
                cnt += 1
                life -= use
        
        max_cnt = max(max_cnt,cnt)
    
    return max_cnt
    

#t1
k = 80
dungeons = [[80,20],[50,40],[30,10]]
res = 3


print(solution(k,dungeons))