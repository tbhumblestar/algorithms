#문제종류 : 같은 숫자는 싫어
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

#풀이
"""
-progress와 speed모두 queue형태로 만들어둠
-progress queue 전체에 매번 speed를 더해주면서, progress의 첫번째 값이 100ㅇ넘으면 작업이 완성되었으므로 while문을 실행
-while문 내부에서, 100이 넘는 값이 연달아있을 경우, progress_queue와 speed_queue에서 제거
"""

from collections import deque

def solution(progresses, speeds):
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    done_lst = []
    
    
    while progresses_queue:
        for i,v in enumerate(progresses_queue):
            progresses_queue[i] += speeds_queue[i]
        
        if progresses_queue[0] >= 100:
            done_lst.append(0)
            
        
            while progresses_queue[0]>=100:
                progresses_queue.popleft()
                speeds_queue.popleft()
                done_lst[-1] += 1
    return done_lst

#t1
progresses = [93,39,55]
speeds = [1,30,5]
res = [2,1]

#t2
progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1,1,1,1,1,1]
res = [1,3,2]

print(solution(progresses,speeds))

