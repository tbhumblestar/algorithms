#문제종류 : 이진 탐색

#풀이
"""
-떡을 자를 곳을 이진탐색으로 구하면 됨
-시작점을 0, 끝점을 떡들 중 가장 긴 떡의 길이로 해두고 이진탐색 ㄱ
"""



n,m = list(map(int,input().split()))
f_lst = list(map(int,input().split()))

def binary_search(arr,target,start,end):
    
    while start <= end:
        mid = (start+end) // 2
        t_sum = 0
        for i in f_lst:
            if i > mid:
                t_sum += (i-mid)
                
        print("mid :",mid)
        print("t_sum :",t_sum)
        
        if target == t_sum:
            #탐색 성공
            return mid
        elif target > t_sum:
            end = mid -1
        
        else:
            start = mid + 1
    
    #탐색결과 없음
    return None

#test_case
# 4 6
# 19 15 10 17
# ans = 15

ans = binary_search(f_lst.sort(),m,0,max(f_lst))
print("ans :",ans)
