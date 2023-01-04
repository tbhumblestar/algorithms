# 문제종류 : 다이나믹프로그래밍
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43105

#풀이법 설명
"""
-입력받은 값을 2차원배열리스트로 만듬
-2차원 배열리스트에서, 특정 원소의 값은 이전행 -1열, 이전행 0중 최대값임
-여기에 현재 행이 최외곽쪽에 있는지를 체크해주면 됨
"""
def solution(triangle):
    
    calculated_triange = [[0]*(i+1) for i in range(len(triangle))]
    calculated_triange[0] = triangle[0][:]

    for row in range(1, len(calculated_triange)):
        for column in range(row + 1):
            if column == 0:
                calculated_triange[row][column] = calculated_triange[row - 1][column] + triangle[row][column]

            elif column == row:
                calculated_triange[row][column] = calculated_triange[row - 1][column-1] + triangle[row][column]

            else:
                calculated_triange[row][column] = max(
                    calculated_triange[row - 1][column - 1], calculated_triange[row - 1][column]
                ) + triangle[row][column]

    return max(calculated_triange[len(calculated_triange)-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))