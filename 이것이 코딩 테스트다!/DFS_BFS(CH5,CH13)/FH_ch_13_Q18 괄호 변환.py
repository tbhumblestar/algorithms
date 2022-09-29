#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60058

#풀이
"""
- BFS
- '('와 ')'의 개수를 카운트
- '(' 와 ')'의 개수가 같아지는 지점이 u와 v를 나누는 곳이 됨
- u의 마지막 글자가 ')'이면 무조건 올바른 문자열


"""

def dfs(letters):
        
    # 입력이 빈 문자열일 경우 바로 빈 문자열을 반환할 수 있도록 & 재귀함수가 어느순간 종료되도록
    answer_letters =''
    if letters == '':
        return answer_letters
    
    
    left_count = 0
    right_count = 0
    
    print(letters)
    
    for i,v in enumerate(letters):
        if v == '(' :
            left_count += 1
        else:
            right_count +=1 
        
        print(left_count)    
        print(right_count)    
        
        if left_count == right_count:
            
            u = letters[0:i+1]
            v = letters[i+1:]

            #올바른 괄호 문자열
            if u[-1] == ')':
                answer_letters += u+ dfs(v)
            else:
                answer_letters ='(' + dfs(v) + ')'
                
                u = u[1:-1]
                new_u = ''
                for i in u:
                    if i == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                        
                answer_letters += new_u
            return answer_letters
                    
        


def solution(p):
    
    answer = dfs(p)
    return answer

#test1
# p ='(()())()'

#test2
p = ')('

#test3
p ='()))((()'
print(solution(p))