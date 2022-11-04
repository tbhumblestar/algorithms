#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
#풀이
"""
#첫풀이 : dfs로 풀었었음 > 그러나 시간초과가 발생함 > bfs로 풀 수 있는 문제를 dfs로 풀면 반드시 시간초과가 남 ㅠㅠ

#두번쨰 풀이
bfs를 사용
-최대횟수인 n*m를 넘어가면 함수종료
-칸을 넘어가면 함수종료
-벽이면 함수 종료
-이미 갔던 곳이면 종료
종료되지 않으면(유효하면)
해당 위치에 방문을 표시
동서남북으로 이동한 위치 & 카운트를 1증가 큐에 넣음
"""



from collections import deque

a = deque([1,2])
print(a)
b = a.popleft()
print(a)