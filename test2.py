#결과를 메모이제이션할 리스트
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 35

#피보나치함수를 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

import time
a = time.time()
print(d[n])
b = time.time()

print(b-a)