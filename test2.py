import heapq

n = int(input())

heap = []
#힙에 자료 구조가 다 들어감
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)
    
res = 0
#힙에 원소가 1개일 떄가지
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    sum_value = one + two
    res += sum_value
    heapq.heappush(heap,sum_value)
    
print(res)
    