#문제종류 : 이진 탐색
#링크 : www.acmipc.net/problem/2110

#풀이
"""
- 집들의 위치인덱스 최대값-최소값 = 공유기 거리의 최대값
- 공유기 거리의 최대값속에서, 이진탐색을 실행
- 이진탐색을 통해 매번 체크하는 것은, 설정된 공유기 거리값이 조건으로 받는 m(공유기 개수)를 만족할 수 있는지 체크
- 이때 체크하는 방법은, 그냥 앞에서 부터 집을 만날떄마다, 이전에 공유기가 설치된 집으로부터 설정된 공유기 거리값보다 멀리있는지를 체크하고 설치하여, 설치된 총 공유기를 세는 것임
- 가능한 것들 공유기 거리들 중 최대값을 출력

"""

n,m = list(map(int,(input().split())))
places_lst = []
for i in range(n):
    places_lst.append(int(input()))

#오름차순 정렬
places_lst.sort()

start = 1
end = places_lst[-1] - places_lst[0]

#이전 설치 장소

possible_m = 0


while start <= end :
    
    #이번회차의 공유기 사이의 거리
    mid = (end+start) // 2
    # print("start :",start)
    # print("end :",end)
    # print("mid :",mid)

    #첫번째 집은 무조건 설치
    cnt = 1
    #이전 설치 장소
    prev = 0
    #설치시작
    for i in range(1,len(places_lst)):
        
        
        if places_lst[i] >= places_lst[prev] + mid:
            prev = i
            # print("i :",i)
            cnt += 1
            
    # print("cnt :",cnt)
    if cnt < m:
        end = mid -1
    
    elif cnt >= m:
        possible_m = mid
        start = mid + 1
        
print(possible_m)
        
    


# #testcase1
# 5 3
# 1
# 2
# 8
# 4
# 9
