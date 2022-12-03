"""
-소수만들기(https://school.programmers.co.kr/learn/courses/30/lessons/12977)
-3개의 수를 고르는 경우의 수 계산
-고른 수를 합친수가 소수인지 체크하여, 소수일 경우 +1
"""


from itertools import combinations

def solution(nums):

    nums_sum_lst = ([x+y+z for x,y,z in combinations(nums,3)])

    def prime_number_check(num):
        for i in range(2,(num//2)+1):
            if num % i == 0:
                return False
        return True
    
    cnt = 0
    for num in nums_sum_lst:
        if prime_number_check(num):
            cnt += 1

    return cnt


#t1
nums = [1,2,3,4]
res = 1

#t2
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
res
print(solution(nums))