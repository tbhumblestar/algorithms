#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43162
#풀이
"""
-방문 리스트를 만들고, 해당 리스트에 , 어떤 네트워크로 방문이 이루어졌는지 체크
-방문을 안했다면, 카운트를 1회 올리고 DFS 함수를 실행
-DFS는 연결되는 모든 지역의 방문 리스트에, 동일한 카운트로 방문을 표시
-방문 리스트를 set으로 만들고 개수를 세주면 전체 네트워크 개수가 나옴
"""

def dfs(i,cnt,visited,computers):
    
    #현재 위치가 이미 방문되었다면 종료
    if visited[i] != 0:
        return None
    else:
        visited[i] = cnt
        new_lst = [idx for idx,val in enumerate(computers[i]) if val == 1]

        for j in new_lst:
            dfs(j,cnt,visited,computers)



def solution(n, computers):

    visited = [0] * (n)
    cnt = 0
    
    for i in range(n):
        
        #방문했다면 패스
        if visited[i] != 0:
            pass
        
        #방문하지 않았다면 dfs
        else:
            cnt += 1
            dfs(i,cnt,visited,computers)
    return cnt


#t1
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
res = 2

#t2
# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# res = 1


print(solution(n,computers))