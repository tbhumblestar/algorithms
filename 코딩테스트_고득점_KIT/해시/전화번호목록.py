#문제종류 : 해시?
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577
#풀이
"""
-문자열 정렬을 기억하는 게 중요함 : 문자열 정렬은 비교하는 두 문자열의 자릿수를 하나씩 비교함
"""

from itertools import combinations

def solution(phone_book):
    
    phone_book.sort()
    for i,v in enumerate(phone_book):
        #마지막은 패스
        if i == len(phone_book)-1:
            return True
        
        #앞의 단어의 글자수가 더 길다면 매칭 실패임
        pre_len = len(phone_book[i])
        if pre_len <= len(phone_book[i+1]):
            if phone_book[i+1][:pre_len] == phone_book[i]:
                return False
        print("for_end")
    return True


#t1
phone_book = ["119", "97674223", "1195524421"]
res = False

#t2
phone_book = ["123","456","789"]
res = False

#t3
phone_book = ["12","123","1235","567","88"]
res = False

print(solution(phone_book))