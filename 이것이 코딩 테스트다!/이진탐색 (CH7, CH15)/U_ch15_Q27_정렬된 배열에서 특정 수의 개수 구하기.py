#문제종류 : 이진탐색

#풀이
"""
- 걍 bisect 라이브러리를 사용하면 됨
"""


from bisect import bisect_left,bisect_right

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))

l = bisect_left(arr,m)
r = bisect_right(arr,m)

if l == n and r == n:
    print(-1)
else:
    print(r-l)


#testcase1
# 7 2
# 1 1 2 2 2 2 3


#testcase2
# 7 4
# 1 1 2 2 2 2 3