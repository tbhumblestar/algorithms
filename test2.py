from bisect import bisect_left,bisect_right

w = '????asdf'
w2 = 'asdf????'
# w.sort()
print(w)
res = bisect_left(w,'?')
print(res)
res = bisect_right(w,'?')
res = bisect_left(w,'?')
print(res)