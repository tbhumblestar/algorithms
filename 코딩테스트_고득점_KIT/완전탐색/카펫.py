#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

#풀이
"""
-완전탐색
-가로 길이의 최대값과 최소값을 구함
-가로길이의 최소갑부터 최대값까지 바꾸면서
-그에 따른 높이 결정
-가로와 세로의 길이가 조건(yellow)에 부합하는지 확인
"""
def solution(brown, yellow):
    
    #가로의 최대값과 최소값을 구함
    max_center_width = (brown -4)//2-1
    min_center_width = ((brown -4)//2+1)//2
    print(max_center_width,min_center_width)
    
    #가로길이의 최소갑부터 최대값까지 바꾸면서
    for i in range(min_center_width,max_center_width+1):
        
        #그에 따른 높이 결정
        h = max_center_width+1-i
        
        #가로와 세로의 길이가 조건(yellow)에 부합하는지 확인
        if i*h == yellow:
            return [i+2,h+2]
        
    
    

#t1
brown = 10
yellow = 2
res = [4,3]

#t2
brown = 8
yellow = 1
res = [3,3]

#t3
brown = 24
yellow = 24
res = [8,6]

print(solution(brown,yellow))