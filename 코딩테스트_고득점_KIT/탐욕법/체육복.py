#문제종류 : 정렬
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

#풀이
"""
-겹치는 값을 우선 제거(여벌 옷이 있는데 도난당하면 못빌려주니까)
-reserve를 순회를 돌면서 시작. 어차피 n<=30이므로 완전탐색도 편안하게 쌉가능
-Greedy
    체육복이 있는 학생은, 
    우선 자기자신이 도난당했으면 옷을 빌려줄 수 없음.
    여벌옷이 있다면, 맨 앞에 있는 애한테 주면 됨. 이게 이 문제의 Greedy임
    맨 앞에 있는 애 말고 다른 애 한테 주는 게, 맨 앞에 있는 애한테 주는 것보다 더 나은 결과를 만들 수 없음
"""


def solution(n, lost, reserve):
    
    #reserve 정렬 안되어 있음;;
    reserve.sort()

    #겹치는 값 제거    
    new_duplicated_reserve = list(set(reserve)-set(lost))
    new_duplicated_lost = list(set(lost)-set(reserve))

    #순회시작
    for i in new_duplicated_reserve[:]:

        if i-1 in new_duplicated_lost:
            new_duplicated_lost.remove(i-1)
        elif i +1 in new_duplicated_lost:
            new_duplicated_lost.remove(i+1)
            
    answer = n-len(new_duplicated_lost)
    return answer

lost=[2,4]
reserve = [1,3,5]

print(solution(5,lost,reserve))