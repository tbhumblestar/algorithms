#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86491

#풀이
"""
-사이즈들 전체를 순회하면서, 가장 큰 변의 길이를 비교를 통해 얻고 + 지갑마다 작은 변을 리스트에 기록
-가장 큰 변의 길이가 상자의 가로가 되고, 작은 변을 기록한 리스트들 중 가장 큰 값이 세로 변이 됨
-이때 가장 큰 변의 길이를 가진 지갑의 나머지 변이, 기록된 작은 변들 중 가장 큰 값인지도 체크해야 함
"""

def solution(sizes):
    
    max_size = 1
    min_length_lst = []
    index = 0
    check_index = []
    
    
    for i in range(len(sizes)):
        i_min = min(sizes[i])
        i_max = max(sizes[i])
        min_length_lst.append(i_min)
        
        if max_size == i_max:
            check_index.append(i)
            
        if i_max > max_size:
            check_index = [i]
            max_size = i_max
        
    #작은 변들 중 최댓값
    min_length_max = max(min_length_lst)
    answer = max_size*min_length_max
    return answer

#t1
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
#ans = 4000

#t2
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
#ans = 120

#t3
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
#ans = 133

ans = solution(sizes)
print(ans)