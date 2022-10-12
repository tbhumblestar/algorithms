#문제종류 : 정렬
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42748

#풀이
"""
-커맨드마다 for문을 돌림
-커맨드에 따라 array를 슬라이싱한 후, sort에서 answer리스트에 반환
"""
def solution(array, commands):
    answer = []
    
    for i in commands:
        # print(i)
        t_array = array[i[0]-1:i[1]]
        t_array.sort()
        # print(t_array)
        answer.append(t_array[i[2]-1])
    
    return answer

#------------------------------------------

#t1
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
#res = [5, 6, 3]

ans = solution(array,commands)
print(ans)