#문제종류 : 이진 탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60060


#풀이
"""
#내가 생각한 풀이법 : 정확성은 통과했는데, 효율성 두개를 통과하지 못함 ㅠㅠ
- 단어 전체를 글자수별로 딕셔너리에 담음
- 입력받은 쿼리별로, '?'의 위치를 셈. 이때 bisect라이브러리를 사용
- 쿼리의 글자수와 매칭되는 단어들에 대하여, '?'를 제외하고 남은 글자들이 존재하는 단어의 개수를 세서 리턴

#동빈햄 풀이
-아예 단어를 체크해버리는 방식
-단어들 간에도, abaaa < abaab < abaac와 같은 관계가 성립한다는 것을 이용
-query에 대해서 ?를 a<?<z로 해석함
-예를 들어 abaa?를 abaaa < 단어 < abaaz와 같은 식으로 해석하여, 해당 범위에 포함되는 단어의 개수를 세는 함수를 만들고,
-각 쿼리별로 해당 함수를 적용하여 범위안에 포함되는 단어가 있는지의 개수를 체크
"""

from bisect import bisect_left,bisect_right


def count_by_range(a,left_value,right_value):
    #right_index 이하의 값들은 right_value보다 작거나 같음
    right_index = bisect_right(a,right_value)
    
    #left_index 이상의 값들은 left_value보다 크거나 같음
    left_index = bisect_right(a,left_value)

    return right_index-left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    
    res =[]
    
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    
    for q in queries:
        
        
        #시작에만 '?'가 이음
        if q[0] != '?':
            cnt = count_by_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))
            
        
        #끝에만 '?'가 있음
        else:
            cnt = count_by_range(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        
        res.append(cnt)


    # print(res)
    return res
    

# #testcase1
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?","?????","???st","??ame"]
# queries = ["??ame"]
ans = [3, 2, 4, 1, 0]

res = solution(words,queries)
print(res)





# ### 내가 생각한 풀이법(실패 : 정확성은 통과했는데, 효율성 두개를 통과하지 못함 ㅠㅠ)
# from bisect import bisect_left,bisect_right


# def solution(words, queries):
    
#     words_dict = {}
#     for w in words:
#         words_dict.setdefault(len(w),[])
#         words_dict[len(w)].append(w)

#     res = []
    
#     for q in queries:
        
        
#         #처음부터 끝까지 전부다 '?'로 구성된 쿼리
#         if q[0] == '?' and q[-1] == '?':
#             if words_dict.get(len(q)):
#                 res.append(len(words_dict[len(q)]))
#             else:
#                 res.append(0)    
            
        
#         #시작에만 '?'가 이음
#         elif q[0] == '?':
            
#             #idx아래로는 전부다 ?표임
#             idx = bisect_right(q,'?')
#             match_letters = q[idx:]
#             cnt = 0
            
#             if words_dict.get(len(q)):
#                 for i in words_dict.get(len(q)):
#                     if i[idx:] == match_letters:
#                         cnt += 1
                        
#             res.append(cnt)
            
        
#         #끝에만 '?'가 있음
#         else:
            
#             reverse_q = q[::-1]
#             reverse_idx = bisect_right(reverse_q,'?')
#             match_letters = q[:-reverse_idx]
            
#             cnt = 0
            
#             if words_dict.get(len(q)):
#                 for i in words_dict.get(len(q)):
#                     if i[:-reverse_idx] == match_letters:
#                         cnt += 1
                        
#             res.append(cnt)

#     # print(res)
#     return res
    

# # #testcase1
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?","?????","???st","??ame"]
# # queries = ["??ame"]
# res = [3, 2, 4, 1, 0]

# res = solution(words,queries)
# print(res)
