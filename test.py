#풀이
"""
- 완전탐색 : 문자열의 길이가 1000이하 > 완전탐색 가능
- 문자열을 자르는 단위를 기반으로, 잘린 문자열을 매번 그 전 문자열과 비교. 같을 경우 count를 올려주고, 다를 경우 문자열 자체를 추가
- 1부터 글자수//2 까지를 단위로 삼아 문자열을 자르고, 각 단위별 생성되는 최종문자열의 문자수를 비교하여 문자수가 제일 적은애를 선택
"""

def solution(s):

    answer = len(s)
    
    for step in range(1,len(s)//2 + 1):
        
        compressed = ""
        prev_letters = s[0:step]
        
        count =1 
        
        for i in range(step,len(s),step):
            new_word = s[i:i+step]
            
            if prev_letters == new_word:
                count +=1
            else:
                compressed += str(count) + prev_letters if count >=2 else prev_letters
                prev_letters = new_word
                count = 1
        
        compressed += str(count) + prev_letters if count >=2 else prev_letters
        
        answer = min(answer,len(compressed))
        
    return answer
                
                

#테스트
s = input()
a = solution(s)
print(a)