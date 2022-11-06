#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43164
#풀이
"""
-각 공항별로, 그 다음 공항으로 이동할 수 있는 항공사를 사전형태로 만듬
-dfs를 돌림
    이때, 각 dfs마다 [출발항공사,도착항공사]에 관한 값을 지워주고, 다시 append함
    dfs는 행선지항공사를 문자열로 계속해서 붙임
    문자열의 개수가, 전체 항공사개수 *3이 되면 조건에 맞게 모두 항공권을 모두 사용한 것임
    조건에 맞는 문자열을 정답에 추가
-dfs 함수가 끝나면 정답문자열을 정렬.
    문자열 정렬은 각 자릿수를 비교하는 것이므로 요구한 방식에 따라 알파벳 순으로 앞서는 이동방식을 선택할 수 있음
"""

def solution(tickets):
    answer = []
    return answer




#t1
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# res = ["ICN", "JFK", "HND", "IAD"]

#t2
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# res = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]


print(solution(n,computers))