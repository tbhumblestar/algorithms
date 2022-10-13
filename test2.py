#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86491

#풀이
"""
-N의 최대범위가 백만
-M의 최대 범위가 십만
-N을 처음에 정렬하는데 O(NlogN)가 필요
-M마다 N에 대한 이진탐색을 돌려야 하므로 O(MlogN)이 필요
-따라서 시간복잡도는 O((M+N)logN)이고
-최대일 때 1,100,000 * log1000000 = 1,100,000 * 20 = 22,000,000 정도 된다
-파이썬이 1초에 2천만 언저리로 계산할 수 있으므로 나쁘지 않음(비벼볼만 함)
"""


n = int(input())
arr = list(map(int,input().split()))
m = int(input())
find_arr = list(map(int,input().split()))

arr.sort()
def binary_search(arr,target,start,end):
    
    """
    정렬된 배열에 대해서 이진탐색을 실행하고 찾지 못했을 경우 None을, 찾았을 경우 값이 존재하는 인덱스를 반환
    """
    
    while start <= end :
        #중간점이 target일 경우
        
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        #중간점이 target보다 클 경우 > 오른쪽 확인
        elif arr[mid] > target:
            start = mid + 1
        #중간점이 target보다 작을 경우 > 왼쪽 확인
        else:
            end = mid -1
            
    #while문 밖으로 나온다 > 일치하는 값이 없음
    return None

for i in find_arr:
    if binary_search(arr,i,0,len(arr)-1):
        print("yes",end =' ')
    else:
        print("no",end = ' ')
            

#testcase
# 5
# 8 3 7 9 2
# 3 
# 5 7 9