
#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86971

#풀이
"""
-n의 개수가 적음 > 완전탐색

- 와이어의 연결을 딕셔너리로 만듬
    > [3,4]가 있다면 딕셔너리 키 3의 벨류 리스트에 4가 추가되고, 딕셔너리 키 4에 벨류리스트에 3이 추가되는 식
- 방문유무를 체크하는 리스트를 만듬
- 와이어를 하나씩 제거해보면서, count를 측정
- dfs함수를 통해, 자신과 연결된 모든 자리를 방문하고, 방문을 표시함
- 방문이 되었을 경우 다시 방문X
- 그러면 결국, 문제에서 출제한 대로, 전력망은 두개밖에 생성되지 않음
- 그 두개의 전력망에 속한 place를 카운트해서 빼주면 됨
"""

def dfs(t_wires_dict,i,count,t_visited_list):
    
    #방문완료
    t_visited_list[i] = count
    #해당 지역에서 갈 수 있는 곳이 있다면
    if t_wires_dict.get(i):
        #갈수있는 곳들마다 체크
        for end in t_wires_dict[i]:
            #이미방문했다면 다시 갈 필요 없음
            if t_visited_list[end] != 0:
                continue
            
            #아직 방문하지 않았다면
            else:
                dfs(t_wires_dict,end,count,t_visited_list)
    

        

def solution(n, wires):
    wires_dict = {}
    for start,end  in wires:
        wires_dict.setdefault(start,[])
        wires_dict.setdefault(end,[])
        wires_dict[start].append(end)
        wires_dict[end].append(start)
    #0번 제외 n개
    visited_list = [0]*(n+1)
    
    min_val = 1000
    
    #전력망 하나씩 잘라보기 시작
    for start,end  in wires:
        
        #기본 세팅
        t_visited_list = [0]*(n+1)
        t_wires_dict = {i:v[:] for i,v in wires_dict.items()}
        count = 1
        
        #이번 회차의 전력망 자르기
        t_wires_dict[start].remove(end)
        t_wires_dict[end].remove(start)
        
        #이번 회차의 순회시작
        for i in range(1,n+1):
            
            #이미 방문했다면 지나갈 것
            if t_visited_list[i] != 0:
                continue
            
            #방문안했다면 dfs시작
            dfs(t_wires_dict,i,count,t_visited_list)
            
            #이번회차가 끝나면 2번 전략망 시작
            count += 1
        
        cnt_1 = t_visited_list.count(1)    
        cnt_2 = t_visited_list.count(2)    
        
        min_val = min(min_val,abs(cnt_1-cnt_2))
        

    return min_val


#t1
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
res = 3

# #t2
# n = 4
# wires = [[1,2],[2,3],[3,4]]
# res = 0

# #t3
# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
# res = 1

print(solution(n,wires))