
from bisect import bisect_left,bisect_right

arr = [0,1,3,3,3,4]

l = bisect_left(arr,3)
print(l)

r = bisect_right(arr,3)
print(r)

