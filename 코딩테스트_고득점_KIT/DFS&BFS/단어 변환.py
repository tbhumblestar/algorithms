#문제종류 : dfs/bfs
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
#풀이
"""

-각 단어에서 그 다음으로 이동할 수 있는 단어들을 모아둔 딕셔너리를 만듬
    이때 각 단어의 길이는 최대 10, 단어는 최대 50이므로 완전탐색처럼 모든 경우의 수를 따져도 괜찮음(50*50*10*10= 25000)

-그 후, 평범하게 bfs함수를 돌리면 됨

"""
from collections import deque

def solution(begin, target, words):
    
    
    new_words = []
    new_words.append(begin)
    new_words += words
    
    #그 다음 단어로 이동할 수 있는 단어들을에 관한 딕셔너리
    move_dict = {}
    
    for word in new_words:
        
        move_dict[word] = []
        length = len(word)
        
        for com_word in words:
            
            cnt = 0
            
            #글자가 같은 경우는 패스
            if word == com_word:
                pass
            
            else:
                for i,v in enumerate(word):
                    if word[i] == com_word[i]:
                        cnt += 1
            
            if cnt == length -1:
                move_dict[word].append(com_word)
    
    #방문 검증 dict
    visited_dict = {v:0 for v in new_words}
    
    #queue 시작
    queue = deque([[begin,0]])
    while queue:
        w,cnt = queue.popleft()
        
        #단어가 타겟과 일치한다면 종료
        if w == target:
            return cnt
        
        #이미 방문했었다면 종료
        if visited_dict[w] != 0:
            continue
        else:
            
            #방문표시
            visited_dict[w] = 1
            for next_word in move_dict[w]:
                queue.append([next_word,cnt+1])

    #while문 종료 == 실패
    return 0


#t1
begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
res = 4

#t2
begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]
res = 0

print(solution(begin,target,words))