#문제종류 : 완전 탐색

#풀이
"""
- 인덱스가 값보다 크다 > 기준 인덱스보다 인덱스가 큰쪽을 탐색
- 인덱스가 값보다 작다 > 기준 인덱스보다 인덱스가 작은쪽을 탐색
"""

n = int(input())
arr = list(map(int,input().split()))

start = 0
end = len(arr)-1

fail = True

while start <= end:
    mid = (start + end) // 2
    
    if arr[mid] == mid:
        print(mid)
        fail = False
        break
    
    elif arr[mid] > mid:
        end = mid-1
    
    elif arr[mid] < mid:
        start = mid +1

if fail:
    print(-1)
        
    


# #testcase1
# 5
# -15 -6 1 3 7

# #testcase2
# 7
# -15 -4 2 8 9 13 15

# #testcase3
# 7
# -15 -4 3 8 9 13 15