#추가풀이2
"""
재귀함수(dfs) + dp를 함께 사용한 방식
너무 멋잇어서 같이정리해둠
"""

def solution(m, n, puddles):
    answer = 0
    #시작점
    info = dict([((2, 1), 1), ((1, 2), 1)])
    #웅덩이표시
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        #저장된 값이 있다면 연산없이 저장된 값을 사용(dp)
        if (m, n) in info:
            return info[(m, n)]
        #재귀함수
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007