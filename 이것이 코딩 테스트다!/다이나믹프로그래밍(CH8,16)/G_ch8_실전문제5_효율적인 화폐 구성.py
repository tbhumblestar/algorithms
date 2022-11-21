#문제종류 : 다이나믹 프로그래밍


#유용한 부분(U)
"""
-아이디어
"""


#풀이법 설명
"""
-각 금액별 필요한 동전 개수를 구함
-매 금액은 , 해당 금액에서 동전별 금액을 뺀 값 + 1개임
"""

d = [0]* 10001

n,m = list(map(int,input().split()))
money_list = []
for i in range(n):
    money = int(input())
    money_list.append(money)
    d[money] = 1
    
for i in range(1,m+1):
    for money in money_list:
        if d[i-money] != 0:
            if d[i] != 0:
                d[i] = min(d[i],d[i-money]) + 1
            else:
                d[i] = d[i-money] + 1


if d[m] == 0:
    print(-1)
else:
    print(d[m])

#testcase1
# 2 15
# 2
# 3

#testcase2
# 3 4
# 3
# 5
# 7