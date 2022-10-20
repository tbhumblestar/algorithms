#문제종류 : 해시?
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845
#풀이
"""

"""

def solution(nums):
    
    
    
    length = len(nums)//2
    
    answer = length if length < len(set(nums)) else len(set(nums))
    return answer