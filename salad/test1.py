"""
-전체 수에 대해서, 스트링으로 바꿔서 팰린드롬인지를 단순히 체크하고, 펠린드롬일 경우 +1한 값을 반환
"""
def solution(n,m):
    answer = 0
    num_list = [i for i in range(n,m+1)]
    
    palindrome_cnt = 0
    
    for num in num_list:
        
        str_num = str(num)
        half_length = len(str_num) // 2
        cnt = 0
        
        for i in range(half_length+1):
            if str_num[i] == str_num[-(i+1)]:
                cnt += 1
                
        if half_length+1 == cnt:
            palindrome_cnt += 1
    return palindrome_cnt


#t1
n = 1
m = 100
print(solution(n,m))