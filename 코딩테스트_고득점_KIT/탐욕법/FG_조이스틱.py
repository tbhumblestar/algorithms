#문제종류 : 그리디
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42860

#풀이
"""
-필요한 건 두가지.
    각 자리에서 알파벳을 찾기위한 cnt
    좌우로 움직이는 것에 대한 cnt
-각 자리에서 알파벳을 찾기위한 cnt는 쉬움. 그냥 정방향과 역방향의 개수를 min해주면 됨

-좌우로 움직이는 방법
    일단 최대값을 len(name)-1로 둠
    A를 군집화시킴. A에는 갈필요가 없으므로, 모든 A의 군집의 왼쪽에서 시작하는 것과 오른쪽에서 시작하는 것을 전부 계산해줌
    


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
