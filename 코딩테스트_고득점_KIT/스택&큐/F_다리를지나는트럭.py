#문제종류 : 다리를 지나는 트럭
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42583
#풀이
"""
-대기트럭을 큐로관리
-다리를 건너는 트럭은 큐로 관리
    큐 안에 있는 차들의 진행양상을 매초카운트 하면 시간초과가 발생할 것 같음 > 앞차가 빠져나간 시점에서, 현재차가 도로를 벗어나는데 걸리는 시간을 측정

-도로가 비어있다면
    대기트럭중 하나를 넣어줌. 이때, 앞차가 없으므로, 해당차가 도로를 벗어나는데 필요한 시간은 다리길이만큼임. weight는 들어간 차량만큼 추가됨

-



"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_wait_que = deque(truck_weights)
    truck_on_bridge_que = deque([])
    
    time_cnt = 0
    weight_on_bridge = 0
    
    #대기차량과 다리위의 차들이 전부 없으면
    while truck_wait_que or truck_on_bridge_que:
        
        
        
        #도로가 비어있다면
        if not truck_on_bridge_que:
            truck_on_bridge_que.append([bridge_length,truck_wait_que.popleft()])
            weight_on_bridge += truck_on_bridge_que[-1][1]
            time_cnt += 1
    
    
        #도로가 비어있지 않음
        else:
            #무게초과로 차를 추가할 수 없음 > 다리위의 차를 한대빼줌
            if weight < truck_wait_que[0] + weight_on_bridge:
                curr_time,curr_weight = truck_on_bridge_que.popleft()
                time_cnt += curr_time
                weight_on_bridge -= curr_weight
                
                #다리에서 나가는 트럭의 남은 시간을, 함께 다리위에 있는 모든 트럭들에서 빼줌
                for truck in truck_on_bridge_que:
                    truck[0] -= curr_time
                
            #무게가 초과되지 않아 차를 추가할 수 있음 > 다리위에 차를 추가
            else:
                #기다리는 트럭이 있으면
                if truck_wait_que:
                    truck_on_bridge_que.append([1+bridge_length,truck_wait_que.popleft()])
                    weight_on_bridge += truck_on_bridge_que[-1][1]
                #없으면 걍 패스
                
        print("truck_wait_que :",truck_wait_que)
        print("truck_on_bridge_que :",truck_on_bridge_que)

    

    
    return time_cnt+1


#t1
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
res = 8

print(solution(bridge_length, weight, truck_weights))

#t2
bridge_length = 100
weight = 100
truck_weights = [10]
res = 101

#t3
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
res = 110