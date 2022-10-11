#문제종류 : 정렬

#유용한 부분(U)
"""

"""


#풀이법 설명
"""
-네개의 조건 > 키를 바꿔가면서 정렬을 4번함
"""

n = int(input())
lst = []
for i in range(n):
    lst.append(tuple(input().split()))


lst.sort(key=lambda x:x[0])
# print("1. ",lst)
# print()
# print()

#수학감소(내림차순)
lst.sort(key=lambda x:int(x[3]),reverse=True)
# print("2. ",lst)
# print()
# print()

#영어 증가(오름차순)
lst.sort(key=lambda x:int(x[2]))
# print("3. ",lst)
# print()
# print()

#국어감소(내림차순)
lst.sort(key=lambda x:int(x[1]),reverse=True)
# print("4. ",lst)
# 
for i in lst:
    print(i[0])



# testcase
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90
