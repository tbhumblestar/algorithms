#문제종류 : 다이나믹프로그래밍
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43238

#풀이
"""
-타임즈(상담시간) 오름차순 정렬
-정해진 시간동안, 정렬된 순으로 각 상담시간을 나눈 몫을 더해주면, 상담시간이 오름차순으로 정렬되어 있기 때문에 문제의 조건에 맞게 상담시간이 빠른 애부터 상담을 할 수 있음
-이러한 방식으로, 상담시간이 정해졌을 때 몇명이나 상담이 가능한지 체크할 수 있다
-이를 통해, 상담시간을 이분탐색으로 탐색해나가면 됨
-이때, 가장 짧은 시간을 사용해야 하므로, lower_bound방식을 사용함
-lower_bound방식은 노션블로그에 따로 정리해뒀으니, 복습하다가 모르면 그 부분을 참고할 것
"""
def solution(n,times):
    times.sort()
    #최소
    start = 1
    #최대
    end = n * times[-1]    
    
    #lower_bound를 수행하기 위해
    while start < end:
        
        mid = (start + end) // 2

        people = 0
        for time in times:
            people += mid // time
            
        #people(key값) = n(target값)일때도 end를 옮겨, 이분탐색으로 이동할 수 있는 최대한의 범위까지 end를 옮김
        if people >= n:
            end = mid
        
        #end를 더이상 옮길 수 없다
        elif people < n:
            start = mid + 1

    return start
#t1
times = [7,10]
n=6

res = 2
print(solution(n,times)) 