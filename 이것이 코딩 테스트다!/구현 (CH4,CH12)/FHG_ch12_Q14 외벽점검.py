#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60062?language=python3

#풀이
"""
- N,w의 개수가 적음 > 딱봐도 완전탐색
- 원의 특성상, 원의 끝쪽과 원의 시작점을 이어줄 수도 있음
    + 계산이 편하도록 원을 총 길이 2배가 되는 직선으로 만들어줘서, 원의 끝쪽과 원의 시작점쪽도 동일한 방식으로 계산할 수 있게 해줌
- 직원들을 배치할 순서를 순열을 돌려줘야 함
    + 처음에는 가장 큰 dist를 가진애들만 배치해주면 되니까 순열돌릴필요 없지 않나? 라고 생각했는데, 순열에 따라 값이 다름..ㅅㅂ..
- 각 직원의 마지막 검사 지점과 그 다음으로 나오는 weak point를 비교해서, weak point가 더 클 경우, 해당 weakpoint에서 직원이 검사를 시작하는 방식
- 직원을 더 추가할 수 없는데, weakpoint가 남아있으면 실패
"""

from itertools import permutations

def solution(n,weak,dist):
    
    #weak 개수
    weak_length = len(weak)
    
    #원을 펼치기
    for i in range(weak_length):
        weak.append(weak[i]+n)
    
    dist_perms = permutations(dist,len(dist))
    
    min_count = len(dist)+1
    
    for dist in dist_perms:
        #검사 시작
        for start_weak_index in range(weak_length):
            count = 1
            
            #이거 -1 안해줘도 됨!!! 4에서 시작해서 2칸을 가면 4,5,6을 체크하는 것임!!
            last_check_place = weak[start_weak_index] + dist[count-1]

            for i in range(start_weak_index,start_weak_index+weak_length):
                
                if weak[i] > last_check_place:
                    count +=1
                    if count > len(dist):
                        break
                    last_check_place = weak[i] + dist[count -1]
                
            min_count = min(min_count,count)
    
    if min_count > len(dist):
        return -1
    
    return min_count

#testcase1
# n = 12
# weak = [1,5,6,10]
# dist = [1,2,3,4]

# #testcase2
# n = 12
# weak = [1,3,4,9,10]
# dist = [3,5,7]

#for test
# print(solution(n,weak,dist))