def dfs(letters):
    
    answer = ''
    if letters == '':
        return letters
    
    left_count = 0
    right_count = 0
    
    for i,v in enumerate(letters):
        if v == '(':
            left_count += 1
        else:
            right_count += 1
            
        if left_count == right_count:
            
            u = letters[:i+1]
            v = letters[i+1:]
            
            if u[-1] == ')':
                answer = u + dfs(v)
            else:
                new_u = ''
                for i in u[1:-1]:
                    if i == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                
                answer += '(' + dfs(v) + ')' + new_u
        
            return answer
        

def solution(p):
    
    answer = dfs(p)
    return answer

#test1
p ='(()())()'

#test2
p = ')('

#test3
p ='()))((()'
print(solution(p))