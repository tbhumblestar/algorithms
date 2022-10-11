#문제종류 : 정렬

#링크 : https://www.acmicpc.net/problem/1715

#유용한 부분(U)
"""
-힙 기반의 우선순위 큐의 사용
"""


#풀이법 설명
"""
-스테이지의 개수가 적음 > 계수정렬
-각 스테이지별 머물고 있는 사용자에 대한 수를 카운트
-스테이지별 실패율을 구함
-실패율을 기준으로 정렬
"""
    
def solution(N, stages):
    cnt = [0 for i in range(N)]
    for i in stages:
        if i == N+1:
            pass
        else:
            cnt[i-1] += 1
    # print(cnt)
    
    fail_rate_lst = []
    player = len(stages)
    for i,v in enumerate(cnt):
        # print(i,v)
        if player == 0:
            fail_rate_lst.append((i+1,0))
        else:
            fail_rate_lst.append((i+1,v/player))
            player -= v
    
    fail_rate_lst.sort(key=lambda x:-x[1])

    
    answer = [i[0] for i in fail_rate_lst]
    # print(answer)
    return answer


#testcase1
N = 5
stages = [2,1,2,6,2,4,3,3]
result = [3,4,2,1,5]

#testcase2
# N = 4
# stages = [4,4,4,4,4]
# result = [4,1,2,3]

#TESTCASE3
N=5
stages = [3,3,3,3]

solution(N,stages)