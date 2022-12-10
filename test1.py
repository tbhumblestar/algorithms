


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

