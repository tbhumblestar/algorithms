n,k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

sum = 0

for i in range(n):
    if i < k:
        sum += max(A[i],B[i])
    else:
        sum += A[i]
        
print(sum)