#문제종류 : Stack / Queue
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

#풀이
"""
-새로운 괄호를, 가장 마지막으로 들어간 괄호와 비교해야함 > Stack활용
"""
def solution(s):

    stack = []

    for idx, letter in enumerate(s):
        
        if len(stack) == 0:
            stack.append(letter)
        
        elif stack[-1] == '(' and letter == ')':
            stack.pop()
        else:
            stack.append(letter)
        
    return len(stack) == 0

s = "()()"
print(solution(s))