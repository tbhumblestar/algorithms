#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""
-rocks 정렬
-distance를 기준으로 이분탐색을 실행
-가장 앞의 rocks부터 순회하면서, 기준으로 잡은 distance보다 작을 경우 돌을 제거하고, distance보다 클 경우 돌을 제거하지 않음
-이런식으로 해서, 제거한 돌의 개수가 n보다 많으면 distance를 증가시킴. 반대로 n보다 적으면 distance를 늘려서 더 많은 돌이 제거되도록 함
-동일한 키에 대해서 distance가 최대가 되어야 한다 > upper_bound
"""

def solution(distance, rocks, n):
    min,max = 0, distance
    
    rocks.sort()
    
    start = 0
    end = distance
    
    while True:
        
        mid = (start + end) // 2
        
        rock_cnt = 0
        length = 0
        min_length = 1,000,000,000
        
        
        
        for idx,rock in enumerate(rocks[1:]):
            length += (rock[idx] - rock[idx-1])
            
            #돌을 만났는데, 의도한 길이보다 좁다 > 돌을 제거
            if length <= mid:
                rock_cnt += 1
                
            #돌을 만났는데, 의도한 길이보다 길다 > 돌을 제거하지 않음
            else:
                min_length = min(length,min_length)
                legnth = 0
                
        if rock_cnt <
            
        
    
    answer = 0
    return answer

#t1
0,2,11,14,17,21,25
2,9,3,3,4,4

#t2
0,5,11,14,16,19,25
5,6,3,2,3,6

#최소값이 가장 커야 한다