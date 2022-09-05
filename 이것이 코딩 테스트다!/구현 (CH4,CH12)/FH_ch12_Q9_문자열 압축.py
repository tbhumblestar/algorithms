#문제종류 : 구현

#유용한 부분(U)
"""
"""

#풀이법 설명
"""
- 완전탐색 : 문자열의 길이가 1000이하 > 완전탐색 가능
- 문자열을 자르는 단위를 기반으로, 잘린 문자열을 매번 그 전 문자열과 비교. 같을 경우 count를 올려주고, 다를 경우 문자열 자체를 추가
- 1부터 글자수//2 까지를 단위로 삼아 문자열을 자르고, 각 단위별 생성되는 최종문자열의 문자수를 비교하여 문자수가 제일 적은애를 선택
"""

def solution(s):

    answer = len(s)
    
    #전체 길이에서 1/2만해도 됨(그 이상은 어차피 전체 문자열과 값이 같음)
    for step in range(1,len(s)//2 + 1):
        
        #압축된 문자열. 여기에 문자열을 조건에 맞게 더해간다
        compressed = ""
        
        #첫번째 문자열은 미리 만들어줌
        prev_letters = s[0:step]
        count =1 
        
        for i in range(step,len(s),step):
            
            #스텝마다 새 문자열 설정
            new_word = s[i:i+step]
            
            #기존문자열과 새 문자열이 같을 경우 카운트만 추가
            if prev_letters == new_word:
                count +=1
            #기존 문자열과 새 문자열이 다를 경우, 기존 문자열과 카운트를 압축된 문자열에 더해주고, 새 문자열을 기존 문자열(prev_letters)로 설정하고 카운트를 초기화
            else:
                compressed += str(count) + prev_letters if count >=2 else prev_letters
                prev_letters = new_word
                count = 1

        # 문자열의 마지막부분은 더해지지 않으므로, 끝자락에 더해준다.
        compressed += str(count) + prev_letters if count >=2 else prev_letters
        
        answer = min(answer,len(compressed))
        
    return answer
                
                

#테스트
s = input()
a = solution(s)
print(a)
        
