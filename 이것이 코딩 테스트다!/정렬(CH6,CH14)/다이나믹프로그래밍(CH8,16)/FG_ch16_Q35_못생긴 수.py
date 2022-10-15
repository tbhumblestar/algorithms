#문제종류 : 다이나믹 프로그래밍


#유용한 부분(U)
"""
-아이디어
"""


#풀이법 설명
"""
-입력받은 값을 2차원배열리스트로 만듬
-2차원 배열리스트에서, 특정 원소의 값은 이전행 -1열, 이전행 0중 최대값임
-여기에 현재 행이 최외곽쪽에 있는지를 체크해주면 됨
"""



n = int(input())
field = []
test_field = []

for i in range(n):
    
    lst = list(map(int,input().split()))
    field.append(lst)
    test_field.append([0]*(len(lst)))


test_field[0][0] = field[0][0]

for i in range(1,n):
    for j in range(len(field[i])):
        if j == 0:
            test_field[i][j] = test_field[i-1][j]
        if j == i:
            test_field[i][j] = test_field[i-1][j-1]
        else:
            test_field[i][j] = max(test_field[i-1][j],test_field[i-1][j-1])
            
        if i != n-1:
            test_field[i][j] += field[i][j]        
        
print(max(test_field[n-1]))
    
# testcase1
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5