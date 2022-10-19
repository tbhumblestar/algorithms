#문제종류 : 모의고사
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

#풀이
"""
-걍풀면됨 쉬움
"""

def solution(answers):
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5,3,3]
    
    c1 = 0
    c2 = 0
    c3 = 0
    
    n = len(answers)
    for i in range(0,n):
        if answers[i] == p1[i%5]:
            c1+=1
        if answers[i] == p2[i % 8]:
            c2 += 1
        if answers[i] == p3[i % 10]:
            c3 += 1
    
    max_c = max(c1,c2,c3)
    
    answer = []
    
    for i,v in enumerate([c1,c2,c3]):
        if v == max_c:
            answer.append(i+1)
            
    return answer
        
print(solution([1,2,3,4,5]))