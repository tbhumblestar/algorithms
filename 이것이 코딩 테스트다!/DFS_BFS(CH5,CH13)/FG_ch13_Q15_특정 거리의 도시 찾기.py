#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60062?language=python3

#풀이
"""
- BFS문제
"""

#n:도시개수, m:도로개수, k: 거리정보, x : 출발도시 번호
from collections import deque
n,m,k,x = map(int,input().split())

city_connection = [[] for i in range(n)]
city_connection.append([])

visited = [0]*(n+1)

for i in range(m):
    input_list = list(map(int,input().split()))
    city_connection[input_list[0]].append(input_list[1])

queue = deque([x])
visited[0] = 'not_city'

print("city_connection : ",city_connection)

while queue:

    val = queue.popleft()
    print("val :",val)
    
    for ccn in city_connection[val]:
        print("ccn :",ccn)
        print("visited :",visited)
        if visited[ccn] == 0:
        #     continue
            visited[ccn] = visited[val] + 1
            queue.append(ccn)
            print("queue :",queue)

print(visited)

if k not in visited:
    print(-1)
    
for i,v in enumerate(visited):
    if v == k:
        print(i)

#test case1
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

#test case2
# 4 3 2 1
# 1 2
# 1 3
# 1 4

#test case3
# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4