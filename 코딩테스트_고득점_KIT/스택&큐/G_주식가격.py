#문제종류 : 주식가격
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42584
#풀이
"""
-가격이 떨어지지 않은 값들을 계속 기억해두면서, 새로 입력받은 값이 가격이 떨어지지 않는 값들과 비교해서 큰지 작은지를 체크해야 함
-prices를 순회를 돌면서, 모든 값들을 기본적으로 가격이 떨어지지 않는 값을 기억하는 set에 저장
    이때 set을 사용하는 이유는, 원소를 삭제(remove)할 때의 시간복잡도가 리스트의 pop(n)보다 낮기 때문
-각 price마다 가격이 떨어지지 않는 값을 기걱하는 set의 원소들과 비교하면서, 가격이 낮은 price를 제거하고, result 리스트의 적합한 인덱스에 얼마나 오래 살아있었는지를 기록
-마지막까지 살아있는 값들에 대해 처리

"""
def solution(prices):
    
    live_prices_set = set()
    res = [0]* (len(prices))
    
    for i,v in enumerate(prices):
        
        #delete_lst를 따로두는 이유는 아래에서 set을 순회를 돌면서 바로바로 원소를 제거할 수 없기 때문. 따라서 기록해뒀다가 한번에 제거함
        delete_prices_lst = []
        
        live_prices_set.add((i,v))
        
        #현재값을, 살아있는 값들과 비교
        for l_i,l_v in live_prices_set:
            
            #현재값이 살아있는 값들보다 작은 경우, 즉 가격이 떨어진 경우에
            if v < l_v:
                delete_prices_lst.append((l_i,l_v))
                res[l_i] = i-l_i
            
        for del_element in delete_prices_lst:
            live_prices_set.remove(del_element)

    #마지막까지 살아있는 값들을 처리
    for l_i,l_v in live_prices_set:
        res[l_i] = len(prices)-l_i-1
        
    return res
prices = [1, 2, 3, 2, 3]

print(solution(prices))