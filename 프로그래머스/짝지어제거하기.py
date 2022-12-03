"""
-짝지어 제거하기(https://school.programmers.co.kr/learn/courses/30/lessons/12973)
-스택을 활용
-스택에 글자가 없다면 스택에 글자를 추가하고 그다음으로 넘어감
-스택에 글자가 있다면, 직전 글자와의 일치여부를 판별해서, 일치할 경우 스택의 글자를 제거(pop)
-일치하지 않으면 글자를 스택에 넣음
-순회가 끝나고 스택이 비면(모두 사라지면) 1을 반환, 스택이 남아있으면(다 없애지 못하면) 0을 반환
"""
def solution(s):
    
    prev_word = s
    string_stack = []
    string_stack.append(prev_word[0])
    prev_let = prev_word[0]
        
    for let in prev_word[1:]:
        
        #글자가 없다면 그다음으로 넘어감
        if len(string_stack) == 0:
            string_stack.append(let)
            continue
        
        #직전 글자와 일치
        if let == string_stack[-1]:
            string_stack.pop()
        else:
            string_stack.append(let)
    return 1 if len(string_stack) == 0 else 0

s = 'baabaa'
res = 1
solution(s)