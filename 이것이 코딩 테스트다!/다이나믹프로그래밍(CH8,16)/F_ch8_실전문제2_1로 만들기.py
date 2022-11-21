#문제종류 : 다이나믹 프로그래밍


#유용한 부분(U)
"""
-아이디어
"""


#풀이법 설명
"""
-점화식이 중요
d[i] = min(d[i-1],d[i//2],d[i//3],d[i//5])

"""

n = int(input())
d = [0] * 30001

d[1] = 1
for i in range(2+n):
    
    d[i] = d[i-1] + 1
    
    #순차적으로 해주면 모든 경우의 수를 다 돔
    if i % 2 ==0:
        d[i] = min(d[i //2 ], d[i])
    
    if i % 3 ==0:
        d[i] = min(d[i //3 ], d[i])
    
    if i % 5 ==0:
        d[i] = min(d[i //5 ], d[i])
    
print(d[n])
