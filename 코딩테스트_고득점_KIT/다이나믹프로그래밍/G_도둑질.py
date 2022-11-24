#문제종류 : 다이나믹프로그래밍
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42897

#풀이
"""
-손쉬운 dp문제인 줄 알았으나.. 원모양임
-따라서 맨 마지막 집을 털면, 맨 첫번째 집도 방문할 수 없음
    'dp[-1]과 dp[-2]중에 dp[-1]이 더 크면서 & d[0]이 d[1]보다 더 큰 경우'
    라고 생각했는데 틀림
    dp[0] <= dp[1]라고 해도 dp[0]은 dp[2]에 무조건 사용됨.
-따라서 dp[-1]이 배제된 경우와 dp[0]이 배제된 경우 모두 구해서, 그냥 최댓값을 구하면 됨..
"""
def solution(money):
    
    length = len(money)
    
    #3개일 때는 그냥 최댓값 하나만 사용될 수 있음
    if length == 3:
        return max(money[0],money[1],money[2])
    
    dp0 = [0]*length
    dp1 = [0]*length
    
    dp0[0] = money[0]
    dp0[1] = money[1]
    dp0[2] = dp0[0] + money[2]
    dp0[3] = money[3] + max(dp0[1],dp0[0])
    
    dp1[1] = money[1]
    dp1[2] = money[2]
    dp1[3] = money[3] + dp1[1]

    
    for i in range(4,length):
        dp0[i] = money[i] + max(dp0[i-2],dp0[i-3])
        dp1[i] = money[i] + max(dp1[i-2],dp1[i-3])
        
    return max(dp0[-2],dp0[-3],dp1[-1],dp1[-2])
    #dp[-1]이나 dp[0] 둘 중 하나를 안써야 하는 상황

#t1
money = [1, 2, 3, 1]
res = 4

#t2
money = [90,0,0,95,1,1]
res = 185

#t3
money = [1000,1,0,1,2,1000,0]
res = 2001

#t4
# money = [0,0,0,0,100,0,0,100,0,0,1,1]
res = 201

#t5
# money = [1000,0,0,1000,0,0,1000,0,0,1000]
res = 3000

#t6
money = [11,0,2,5,100,100,85,1]
res = 198

#t7
money = [1,2,3]
res = 3

#t8
money = [91,90,5,7,5,7]
res = 104

#t9
money = [10,0,0,1000,10,2]
res = 1010

#t10
money = [40,5,3,40]
res = 45

#t11
money = [1,1,4,1,4]
res = 8

print(solution(money)) 