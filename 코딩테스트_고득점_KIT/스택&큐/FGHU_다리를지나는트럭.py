# 문제종류 : 다리를 지나는 트럭
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 풀이
"""
-다리 그자체를 큐로 표시하는 것이 핵심
    다리는 길이만큼의 원소를 가짐
    차가 없는 지역은 0으로 표현합니다
    그리고 트럭은 무게를 자연수로 가지고 있으므로, 도로위에서 트럭은 해당 트럭의 무게로 표현
-큐는 1초마다 한칸씩 앞으로 가면서, 맨 앞의 큐는 사라지고, 맨 뒤에 새로운 큐가 추가된다
    맨 앞의 큐가 사리질때마다, 사라지는 큐의 무게가 전체 다리무게에서빠짐
    맨 뒤의 큐에는, '현재 다리 위의 무게 + 새로 올라올 트럭의 무게' 보다 다리가 버틸 수 있는 무게가 더 크다면 새 트럭이 추가되고, 그렇지 않으면 그냥 0이 추가됨
-마지막 트럭이 올라선 시점에서 while문 종료되므로, 마지막 트럭이 다리위를 지나는 시간을 더해줘야 함
"""

from collections import deque


def weight_checker(new_truck, current_weight, cover_weight):
    """Check weight is over"""
    if new_truck + current_weight > cover_weight:
        return False

    return True


def solution(bridge_length, weight, truck_weights):

    waiting_que = deque(truck_weights)
    bridge_que = deque([0] * bridge_length)
    print(bridge_que)
    cnt = 0
    current_weight = 0

    # 대기차량과 다리위의 차량이 없을 때까지
    while waiting_que:

        cnt += 1
        current_weight -= bridge_que.popleft()

        if weight_checker(waiting_que[0], current_weight, weight):  # 초과하지 않으면
            truck = waiting_que.popleft()
            bridge_que.append(truck)
            current_weight += truck

        else:  # 초과
            bridge_que.append(0)

        print("check!")

    ans = cnt + bridge_length # 마지막 트럭이 올라선 시점에서 while문 종료되므로, 마지막 트럭이 다리위를 지나는 시간을 더해줘야 함
    return ans


# t1
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
res = 8

# t2
bridge_length = 100
weight = 100
truck_weights = [10]
res = 101

# t3
bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
res = 110

print(solution(bridge_length, weight, truck_weights))
