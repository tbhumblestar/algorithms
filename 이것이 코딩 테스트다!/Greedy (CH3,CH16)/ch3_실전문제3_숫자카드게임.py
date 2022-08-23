n,m = map(int,input().split())
cnt = 0

d = []
min_list = []

for i in range(n):
    d.append([])
    nums_list = list(map(int,input().split()))
    min_list.append(min(nums_list))
    d[i].append(nums_list)

print(d)
print(min_list)
print(max(min_list))
