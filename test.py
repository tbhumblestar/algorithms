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
#n+1이 되어야 함. 마지막 날에 시작한 일이 마지막 날에 끝날 수 있기 때문
d = [0]*(n+1)

for i in range(0,n):
    field.append(list(map(int,input().split())))

max_val = 0

for i in range(n-1,-1,-1):
    print(i)
    day, pay = field[i]
    
    
    #오늘날짜에 상담을 하면, 날짜가 초과되어서 일을 하지 못할 경우 > 기존의 값들 중 최고값을 얻는 수밖에 없음
    if (i) + day > n:
        d[i] = max_val
        
    
    else:
        #오늘 일을 할 수 있다면
        if i  + day <=n:
            d[i] = max(max_val,pay+d[i+day])
            max_val = d[i]
    print(d)


#testcase1
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

#testcase2
# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10


#testcase3
# 10
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
