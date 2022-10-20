#문제종류 : 그리디
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42860

#유용한 부분 : 프로그래머스 1등 풀이.. 
#프로그래머스

#풀이
"""
-필요한 건 두가지.
    각 자리에서 알파벳을 찾기위한 cnt
    좌우로 움직이는 것에 대한 cnt
-각 자리에서 알파벳을 찾기위한 cnt는 쉬움. 그냥 정방향과 역방향의 개수를 min해주면 됨

-좌우로 움직이는 방법
    일단 최대값을 len(name)-1로 둠
    A를 군집화시킴. A에는 갈필요가 없으므로, 모든 A의 군집의 왼쪽에서 시작하는 것과 오른쪽에서 시작하는 것을 전부 계산해줌
    
#프로그래머스 풀이에 프로그래머스 풀이에 대한 설명있음

"""

#len : 26

    
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#글자변환 계산
def letter_index_cal(let):
    
    for i,v in enumerate(letters):
        if let == v:
            return min(25-i+1,i)

#클러스터별 이동거리 계산
def move_cal(cluster,name):
    
    length = len(name)
    
    min_place = min(cluster)
    max_place = max(cluster)
    
    #오른쪽갔다가 다시 왼쪽으로 쭈욱
    right_to_left = (min_place-1)*2 + (length-max_place-1)
    
    #왼쪽으로 갔다가 다시 오른쪽으로 쭈욱
    left_to_right = (length-max_place-1)*2 + (min_place-1)
    
    print(cluster,right_to_left,left_to_right)
    
    return min(right_to_left,left_to_right)
    

def solution(name):
    print(name)
    #A가 있는지 체크
    A_cnt = name.count("A")

    A_cluster = []    
    cluster_idx = -1
    
    #A를 군집화
    for i,v in enumerate(name):
        if i==0:
            continue
        
        if v=='A':
            if name[i-1] != 'A' or i == 1:
                A_cluster.append([i])
                cluster_idx += 1
            else:
                A_cluster[cluster_idx].append(i)
    # print(A_cluster)
    
    #일직선으로 움직이는 경우
    min_mv_cnt = len(name)-1
    
    for i in A_cluster:
        
        min_mv_cnt = min(min_mv_cnt,move_cal(i,name))

    #글자변환체크
    cnt = 0
    for i,v in enumerate(name):
        cnt += letter_index_cal(v)

    # print(cnt)
    # print(min_mv_cnt)
    return cnt + min_mv_cnt

#t1
name = 'JEROEN'
#res = 56

#t2
name = 'JAN'
#res = 23

#t3
# name = 'TABBBB'
# name = 'TAACCABBAAA'

#t4
name = 'AABAAAAAABA'
res = 8

#t5
name = 'AABBBABAAAABBAABAAAAAAZBBAA'

print("len:",len(name))
print(solution(name))



### 프로그래머스 풀이

def solution(name):
    answer = 0
    n = len(name)

    #자리에서 다른 글자로 바꾸기 위한 카운트 계산 함수
    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    #글자 카운트
    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    
    #이 부분이 핵심
    #모든 인덱스마다 완전탐색처럼 이동해야 하는 횟수를 구함
    #단 이때의 인덱스는 시작점이라기 보다는 A의 cluster가 있는지 확인하는 느낌임
    for idx in range(n):
        
        
        next_idx = idx + 1
        
        #A의 클러스터가 있는지, 있다면 어디까지인지를 선택
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        
        #정방향과 역방향중 가까운 방향을 선택
        distance = min(idx, n - next_idx)
        
        #min의 두번재 인자는 클러스터를 기준으로 왼쪽한번 오른쪽한번, 그리고 가까운쪽한번을 더한 것임 ㄸ
        move = min(move, idx + (n - next_idx) + distance)

    answer += move
    return answer