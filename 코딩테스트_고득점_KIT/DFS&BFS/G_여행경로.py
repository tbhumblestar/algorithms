#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43164
#풀이
"""
-각 공항별로, 그 다음 공항으로 이동할 수 있는 항공사를 사전형태로 만듬
-dfs를 돌림
    visited로 방문한지역을 체크하면서 dfs를 수행
    dfs는 방문하는 항공사를 문자열로 계속해서 붙임
    문자열의 개수가, 전체 항공사개수 *3이 되면 조건에 맞게 모두 항공권을 모두 사용한 것임
    모든 항공사를 다 돌 경우, 문자열을 비교
    문자열은 각 자릿수를 비교하는 것이므로 요구한 방식에 따라 알파벳 순으로 앞서는 이동방식을 선택할 수 있음
"""
from collections import defaultdict

def solution(tickets):
    
    start_end_dict = defaultdict(list)
    visited = defaultdict(list)
    length = (len(tickets)+1)*3
    
    for ticket in tickets:
        start_end_dict[ticket[0]].append(ticket[1])
        visited[ticket[0]].append(0)
    
    answer_str = 'Z'*length

    #완성됐는지 체크하고 글자바꿔주는 애
    def arrive_checker(let):
        # print("let in arrive_checker:",let)
        if len(let) == length:
            nonlocal answer_str
            answer_str = min(answer_str,let)
            return True
        
        return False
    
    
    def dfs(let,start_place):
        
        #마지막에 도착
        if arrive_checker(let):
            return None
        
        #갈 수 있는 곳이 있다면 패스
        if start_end_dict.get(start_place):
            for idx,end in enumerate(start_end_dict[start_place]):
                
                    #이미 방문
                    if visited[start_place][idx] == 1:
                        continue
                    
                    #아직방문하지않았음
                    let += end
                    visited[start_place][idx] = 1
                    dfs(let,end)
                    let = let[:-3]
                    visited[start_place][idx] = 0
            
        return None
    

    dfs("ICN","ICN")
        
    answer = []
    for i in range(length//3):
        answer.append(answer_str[i*3:(i+1)*3])
    
    return answer




#t1
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# res = ["ICN", "JFK", "HND", "IAD"]

#t2
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# res = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]


print(solution(tickets))