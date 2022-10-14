#문제종류 : 다이나믹 프로그래밍


#유용한 부분(U)
"""
-아이디어
"""


#풀이법 설명
"""
-어떤 지점에서 얻을 수 있는 식량의 최대값에 대한 점화식 : table[i] = max(table[i-2],table[i-3]) + lst[i]
-table[0],table[1],table[2]은 무조건 주어지니까 넣어주고나서 점화식을 돌려주면 됨

#책 풀이는 조금 다름. 
-i번째 식량창고를 털지말지 결정하는 로직을 사용함
-필요할 경우 p.221참고
"""

n = int(input())
lst = list(map(int,input().split()))

length = len(lst)

table = [0] * (length+1)


table[0],table[1],table[2], = lst[0],lst[1],lst[2]

for i in range(3,length):
    table[i] = max(table[i-2],table[i-3]) + lst[i]

print(max(table))


#testcase
# 4
# 1 3 1 5 2 3