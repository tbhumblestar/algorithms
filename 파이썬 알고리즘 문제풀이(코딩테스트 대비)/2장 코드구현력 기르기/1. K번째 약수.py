n, k = map(int,input().split())


div_list = []
for i in range(1,n+1):
    if n % i == 0:
        div_list.append(i)

if len(div_list) < k:
    print(-1)
else:
    print(div_list[k-1])