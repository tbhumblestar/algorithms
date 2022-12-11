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
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

prices = [1, 2, 3, 2, 3]

print(solution(prices))