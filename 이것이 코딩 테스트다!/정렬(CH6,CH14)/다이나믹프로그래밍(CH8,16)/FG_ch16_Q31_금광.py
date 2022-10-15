#문제종류 : 다이나믹 프로그래밍


#유용한 부분(U)
"""
-아이디어
"""


#풀이법 설명
"""
-입력받은 값을 2차원배열리스트로 만듬
-2차원 배열리스트에서, 특정 원소의 값은 이전열 -1행, 이전열 +0행, 이전열 +1행 의 값들 중최대값에 자기자신을 더한 값임
-여기에 맨위의 행이거나 맨 아래의 행일 경우를 고려해주면 됨
"""



t = int(input())

for _ in range(t):

    n,m = list(map(int,input().split()))
    test_list = [[0]*m for __ in range(n)]
    
    field_list = list(map(int,input().split()))
    field_list_2_array = [[0]*m for __ in range(n)]
    
    for i,v in enumerate(field_list):
        field_list_2_array[i // m][i % m] = v
    
    print(field_list_2_array)

        

    for j in range(m):
        for i in range(n):
        
            val =  test_list[i][j-1]
            if i == 0 : 
                val2 = test_list[i+1][j-1]
                val = max(val2, val)
                
            if i == n-1 : 
                val2 = test_list[i-1][j-1]
                val = max(val2, val)
            
            else:
                val = max(val,test_list[i+1][j-1],test_list[i-1][j-1])
            test_list[i][j] = val + field_list_2_array[i][j]
            
    

    
    print(test_list)
    
    # print(sum(test_list))
        

    
# testcase1
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2