#그리디 알고리즘
#정당성 검토
# 나눌 수 있으면 더 많이 나누는 게, 다른 선택지(1을 빼는 것)보다 무조건 수를 크게 줄인다.
# 또한 항상 N=1에 도달한다.

N,k = map(int,input().split())
cnt = 0

while N > 1:
    
    if N % k == 0:
        N = N//k
    else:
        N-= 1
    
    cnt += 1
print(cnt)