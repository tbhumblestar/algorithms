#문제종류 : 해시?
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42579
#풀이
"""

"""

def solution(genres, plays):
    cnt_dict = {}
    song_dict = {}
    
    n = len(genres)
    for i in range(n):
        
        #카운트 계산
        cnt_dict.setdefault(genres[i],0)
        cnt_dict[genres[i]]+=plays[i]
        
        #곡마다 계산
        song_dict.setdefault(genres[i],{})
        song_dict[genres[i]][i] = plays[i]
        
        print(cnt_dict)
        print(song_dict)
        

        
    
    answer = []
    return answer