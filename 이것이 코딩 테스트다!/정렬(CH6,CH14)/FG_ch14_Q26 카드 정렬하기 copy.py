#문제종류 : 정렬

#링크 : https://www.acmicpc.net/problem/1715

#유용한 부분(U)
"""
-힙 기반의 우선순위 큐의 사용
"""


#풀이법 설명
"""
-아이디어적으로 놓쳣던 부분은
    정렬 후에 작은 수들 부터 단순히 더해나가면 된다고 생각했음
    근데 그게 아니라, 제일 작은 두 수가 더해지고 나서 더해진 그 값이 새로이 배열에 추가되면 새로운 배열이 되는 것임
    즉 새로운 배열에서, 다시 제일 작은 두 수를 선택해야 함
-테크닉적으로 새로 배운 부분은 힙을 사용한 우선순위 큐
    우선순위 큐를 사용하지 않고 코드를 구현한 게 첫번째 풀이법(풀이법1). 답은 잘 나왔는데 시간초과로 문제가 발생
    우선순위 큐를 사용하니까 무난하게 정답이 나왔음. 정렬이 매번 사용되는 경우에는 무조건 우선순위 큐를 사용하자!

"""

#풀이법 1(우선순위 큐 사용 X / 시간초과)
n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

_sum = 0
lst.sort()

test_list = lst[:]


while len(test_list) != 1:
    
    e1,e2 = test_list[0],test_list[1]
    test_list = test_list[2:]
    new_e = e1 + e2
    _sum += new_e
    test_list.append(new_e)
    test_list.sort()

print(_sum)


# 풀이법 2
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
    


# testcase 1
# 3
# 10
# 20
# 40

#ans : 100

#testcase 2
# 10
# 123
# 456
# 234
# 998
# 12
# 7
# 876
# 887
# 455
# 234

#answer : 12108

# testcase3
# 4
# 10
# 15
# 11
# 12