#링크 : https://www.acmicpc.net/problem/15686

#풀이
"""
- N,M의 개수가 적음 > 딱봐도 완전탐색
- 전체 치킨집들의 좌표를 기록
- 전체 집들의 좌표를 기록
- M에 따른 치킨집들의 경우의 수를 구함
- 이때, 모든 집의 모든 치킨집에 대한 거리를 구해서 최소값을 치킨거리로 삼고 그 치킨거리르 더한게 치킨거리의 합이 되게 함
- 구해진 치킨거리의 최소값을 도시의 치킨거리로 삼음
"""

from itertools import combinations

n,m = map(int,input().split())
field = []
for i in range(n):
    input_list = list(map(int,input().split()))
    field.append(input_list)

chickens_stations = []
homes_stations = []

#chickens_stations, homes_stations 좌표 설정
for x in range(n):
    for y in range(n):
        if field[x][y] == 1:
            homes_stations.append((x,y))
        if field[x][y] == 2:
            chickens_stations.append((x,y))
            
print("chickens_stations : ",chickens_stations)
print("homes_stations : ",homes_stations)

#chicken 조합
chickens_combinations = list(combinations(chickens_stations,m))

print("chickens_combinations : ",chickens_combinations)


#계산시작
min_city_chicken_distance = 100000000
for chickens in chickens_combinations:

    test_city_chicken_distance = 0

    for h_x,h_y in homes_stations:
        
        min_distance = 10000000
        
        for c_x,c_y in chickens:
            distance = abs(h_x-c_x)+abs(h_y-c_y)
            min_distance = min(min_distance,distance)

        test_city_chicken_distance += min_distance
    
    min_city_chicken_distance=min(min_city_chicken_distance,test_city_chicken_distance)
    
print(min_city_chicken_distance)




# # test case1
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
