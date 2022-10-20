#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

#풀이
"""
-완전탐색
-만들 수 있는 모든 수를 만들고 > 이때 11 / 011 같은 것들은 체크
-만들어진 숫자가 소수인지를 체크해야 함
"""
def prime_number_check(n):
    if n == 1 or n == 0:
        return False
    
    if n == 2 or n == 3:
        return True
    
    for i in range(2,n+1//2):
        if n % i == 0 :
            return False
        
    return True
        
from itertools import permutations

def solution(numbers):

    nums_lst = []

    #글자수에따라
    for i in range(1,len(numbers)+1):
        
        #만들어지는 모든 경우의 수를 만듬
        t_lst = list(permutations(numbers,i))
        
        #만들어진 수들을 nums_lst에 추가
        for i in t_lst:
            nums_lst.append(int(''.join(i)))
            
    #중복제거
    nums_lst = list(set(nums_lst))
    
    cnt = 0
    print(nums_lst)
    for i in nums_lst:
        
        #소수라면
        if prime_number_check(i):
            print(i)
            cnt += 1
    
    return cnt


#t1
numbers = '17'
res = 3

#t2
numbers = '011'
#res = '2'

numbers = '3179'

print(solution(numbers))