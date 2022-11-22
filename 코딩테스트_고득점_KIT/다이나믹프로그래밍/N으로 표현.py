#문제종류 : 다이나믹프로그래밍
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42895

#풀이
"""
-완전탐색이되, dp를 사용해 경우의 수를 줄인 것임
-수들의 조합은 다음과 같음 : 55, 5+5 , 5*5, 5/5, 5-5
-또한 수의 개수 조합을 전부 계산해줘야 함
    예를 들어, 수가 4개이다 > 수가 1개 & 3개, 2개 & 2개, 3개 & 1개의 케이스를 모두 계산해줘야 함
-사칙연산이 아니라 그냥 숫자를 이어붙이는 경우(55,555,5555...)등에 대해서는 따로 처리해줘야 함
"""


def lst_appender(a,b,next_lst):
    next_lst.append(a+b)
    next_lst.append(a*b)
    next_lst.append(a-b)
    next_lst.append(b-a)
    
    if b != 0:
        next_lst.append(a//b)
    if a != 0:
        next_lst.append(b//a)
    

def solution(N, number):
    
    if N == number:
        return 1
    
    d = []
    d.append([N])
    
    def next_lst_maker(d,N,curr_idx):
        for i in range(curr_idx):
            other_i = curr_idx - (i+1)
            
            for j in d[i]:
                for q in d[other_i]:
                    lst_appender(j,q,d[curr_idx])
    
    #idx : 1~7
    for idx in range(1,8):
        d.append([])
        next_lst_maker(d,N,idx)

        special_num = 0
        for i in range(0,idx+1):
            special_num += N*(10**(i))
        
        # print(idx,special_num)

        d[idx].append(special_num)
        d[idx] = list(set(d[idx]))

        if number in d[idx]:
            return idx+1

    # for i in d:
    #     print()
    #     print(i)
    #     print()
    return -1

# t1
N = 5
number = 12
# res = 4

# # t2
# N = 2
# number = 150
# # res = 3

#t3
N = 8
number = 5800

print("시작!")
print(solution(N,number))