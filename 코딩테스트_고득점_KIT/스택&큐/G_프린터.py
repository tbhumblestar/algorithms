#문제종류 : 같은 숫자는 싫어
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42587
#풀이
"""
-location > 0 으로 고침
-각 우선순위가 등장한 수를 카운트하여 딕셔너리로 만듬
-등장한 우선순위의 리스트를 만듬(priorities > set > list)
-등장한 우선순위를 큐로 만들고, while문을 실행
    첫번째 항을 popleft로 가져오고, 그 항이 나의 작업물인지 아닌지 / 출력할 수 있는지 없는지(최대 우선순위값과 동일한지 아닌지를 따져서 체크)
"""
from collections import defaultdict, deque

def solution(priorities, location):
    
    priorities_count_dict = defaultdict(int)
    max_priority = 1
    priorities_unique = list(set(priorities))
    priorities_unique.sort()
    
    for work in priorities:
        priorities_count_dict[work] += 1
        max_priority = max(max_priority,work)
        
    my_priority = priorities[location]
    priorities[location] = 0
    
    priorities_queue = deque(priorities)
    
    cnt = 0
    while priorities_queue:
        q = priorities_queue.popleft()
        
        #내 작업물
        if q == 0:
            if my_priority == max_priority:
                return cnt + 1
            else:
                priorities_queue.append(q)
        
        #
        elif q == max_priority:
            # print("hi!")
            priorities_count_dict[q] -= 1
            cnt += 1
            
            if priorities_count_dict[q] == 0:
                priorities_unique.pop()
                max_priority = priorities_unique[-1]
        
        
        #인쇄되지 못하는 경우
        else:
            priorities_queue.append(q)
            
        # print(priorities_queue)
            
            
            

#t1
priorities = [2, 1, 3, 2]
location = 2
res = 1

#t2
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# res = 5

print(solution(priorities,location))

#두번쨰 풀이
"""
-any를 사용하는 것이 인상적이여서 가져옴
-다만 any역시 결국 순회를 돌기 때문에 시간복잡도가 위의 풀이보다 좋은 것은 아님. max_priority를 업데이트 해주는 방식이 훨씬 효율적이다
-any: 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환
"""

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        #any: 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer