#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
#풀이
"""
-n의 개수가 최대 20개 > 2^20은 백만이므로 완전탐색
-각 숫자를 +,-하는 모든 경우의 수를 완전탐색으로 구함
"""

from itertools import product

def solution(numbers, target):
    
    cnt = 0
    
    #0은 -, 1은 +
    lst = [0,1]
    
    product_lst = list(product(lst,repeat = len(numbers)))
    # print(product_lst)
    
    for pro in product_lst:
        val = 0
        for i,v in enumerate(pro):
            
            if v == 0:
                val -= numbers[i]
            else:
                val += numbers[i]
                
        # print(pro,val)
        if val == target:
            cnt += 1
    
    
    return cnt

#t1
numbers = [1, 1, 1, 1, 1]	
target = 3
res = 5

#t2
# numbers = [4,1,2,1]	
# target = 4
# res = 2


print(solution(numbers,target))