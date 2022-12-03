#문제종류 : 같은 숫자는 싫어
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12906

#풀이
"""
-걍풀면됨 쉬움
"""

def solution(arr):
    lst = []
    lst.append(arr[0])
    for i in arr[1:]:
        if len(lst) == 0:
            lst.append(i)
        else:
            if lst[-1] == i:
                pass
            else:
                lst.append(i)
                
    return lst