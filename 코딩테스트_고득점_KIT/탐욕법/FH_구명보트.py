
#문제종류 : 그리디
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42885
#풀이
"""
#풀이
-(기존풀이)사람을 무거운 순서대로 정렬하고, 제일 무거운 사람과 같이 갈 수 있는 사람들 중에 제일 무거운 사람을 짝지어서 보내야 한다고 생각했었음
-그러나 그럴필요 없음. 제일 무거운 사람보다 더 무거운 사람은 없기에, 제일 무거운 사람한테 제일 가벼운 사람을 매칭시키는 방식이 맞음
-즉 제일 가벼운 사람을 아껴도, 제일 무거운 사람을 제외하면 더 적합한 곳에 쓸 수가 없음

-그리디
    사람을 무거운 순서대로 정렬
    같이탈 사람을 정할 때, 그다음으로 무거운 사람을 태워본다
    안되면 그다음사람... 이런식으로 진행
    효율성을 위해, 맨뒤의 사람을 태웟을 경우 무게를 초과하는지 체크하면 좋을 듯
"""

from collections import deque

def solution(people, limit):
    
    #내림차순 정렬
    people.sort(reverse = True)
    
    que = deque(people)
    storage = deque([])

    t_limit = limit
    
    cnt = 0
    p =0

    #큐가 빈다 = 모든 사람 다태워보냈음
    while que:
        
        #사람이 아무도 안탔으면
        if p == 0:
            
            # 다음 사람
            q = que.popleft()
            
            #마지막 사람이였다면 바로 배에 태우보냄
            if len(que)== 0:
                cnt += 1
                
            else:
                #그 다음에 태울 수 있는 사람
                t_limit = limit -q 
            
                #인원수 체크
                p += 1
                # print("if fin")


        #사람이 한명 타있는 상태
        else:
            
            #효율성을 위해 마지막 사람이랑 비교
            l = que.pop()
            
            #마지막 사람이 t_limit보다 크다면 아무도 못태우는 거임
            if l > t_limit:
                que.append(l)
                t_limit = limit
                cnt += 1
                p = 0
            
            #탈 수 있다면 보내고 기본 값들을 초기화 및 cnt정리
            else:
                t_limit = limit
                cnt += 1
                p = 0
                
    return cnt


#t1
people = [70, 50, 80, 50]
limit = 100
res = 3

#t2
people = [70, 80, 50]
limit = 100
res = 3

print(solution(people, limit))