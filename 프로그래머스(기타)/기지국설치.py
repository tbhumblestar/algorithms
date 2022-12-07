"""
-기지국설치(https://school.programmers.co.kr/learn/courses/30/lessons/12979)
-N을 일일이 계산하는 것은 너무 숫자가 많음
-따라서 숫자가 적은 station을 활용해 기지국의 전력이 닿는 곳을 계산
    이 과정에서 stack을 활용해 station이 인근에 있어 겹치는 곳이 있다면 합쳐줌
-그 후 전력이 닿는 곳에 대한 값을 바탕으로 전력이 닿지 않는 곳을 계산
    이때 맨 처음과 마지막 부분에 대해 체크해줘야 함
-닿지 않는 곳들을, 기지국하나당 커버할 수 있는 영역(2w+1)로 나누서 더해줌
"""
from math import ceil

def solution(n, stations, w):
    
    
    def making_save_places(save_places,save_places_stack):
    
        for save_place in save_places[1:]:
            
            #stack이 비어있으면 pass
            if len(save_places_stack) == 0:
                save_places_stack.append(save_place)
                continue
            
            #stack이 차있다면
            prev_min,prev_max = save_places_stack[-1]
            curr_min,curr_max = save_place
            
            #겹친다면
            if prev_max >= curr_min-1 :
                save_places_stack.pop()
                save_places_stack.append((prev_min,curr_max))
            
            #겹치지 않는다면
            else:
                save_places_stack.append((curr_min,curr_max))
    
    
    def making_not_save_places(save_places_stack,not_save_places):
        
        #시작부터 닿지 않는 곳이 있다면 체크
        if first_start > 1:
            not_save_places.append((1,first_start-1))

        for idx,save_place in enumerate(save_places_stack):
            
            if idx == 0:
                continue
            
            prev_end = save_places_stack[idx-1][1]
            curr_start = save_places_stack[idx][0]
            not_save_places.append((prev_end+1,curr_start-1))
        
        #마지막에 닿지 않는 곳들이 있다면 체크
        if last_end < n:
            not_save_places.append((last_end+1,n))

    save_places = [(station-w,station+w) for station in stations]
    save_places_stack = []
    save_places_stack.append(save_places[0])
    
    making_save_places(save_places,save_places_stack)
    
    not_save_places = []
    first_start = save_places_stack[0][0]
    last_end = save_places_stack[-1][1]
    
    making_not_save_places(save_places_stack,not_save_places)
    
    #닿지 않는 집들의 무리마다, 몇 개의 기지국들이 있어야 하는지 계산해서 더해줌
    cnt = 0
    for not_save_place in not_save_places:
        start,end = not_save_place
        cnt += ceil((end-start+1) /(2*w + 1))

    return cnt


# t1
# N = 11
# stations = [4,11]
# w = 1
# ans = 3

#t2
N = 16
stations = [9]
w = 2
ans = 3

print(solution(N,stations,w))