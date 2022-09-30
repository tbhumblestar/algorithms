#링크 : https://www.acmicpc.net/problem/14888

#풀이
"""
-dfs
-global을 통해 전역변수로 변수값을 관리하는 게 좋앗음
"""


n = int(input())

#
num_list = list(map(int,input().split()))

# +,-,*,%
add,sub,mul,div = map(int,input().split())

#1e9 = 1*10^9
max_num = -1e9
min_num = 1e9


#i : count, res : 결과값
def dfs(res:int,i:int) -> None:
    
    global max_num,min_num,add,sub,mul,div
    
    if i == n:
        max_num = max(max_num,res)
        min_num = min(min_num,res)
        return None
    
    else:
        if add > 0 :
            add -= 1
            dfs(res+num_list[i],i+1)
            add += 1
            
        if sub > 0 :
            sub -= 1
            dfs(res-num_list[i],i+1)
            sub += 1
            
        if mul > 0 :
            mul -= 1
            dfs(res*num_list[i],i+1)
            mul += 1
            
        if div > 0 :
            div -= 1
            
            if res >= 0:
                dfs(res // num_list[i],i+1)
            else:
                dfs(-((-res) // num_list[i]),i+1)
            div += 1
            
                    
        
        
dfs(num_list[0],1)
    
    
    
    
print(max_num)
print(min_num)


# #t1
# 2
# 5 6
# 0 0 1 0

# # t2
# 3
# 3 4 5
# 1 0 1 0

#t3
# 6
# 1 2 3 4 5 6
# 2 1 1 1