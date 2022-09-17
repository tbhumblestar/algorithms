#

#링크 : https://www.acmicpc.net/problem/3190

#풀이
"""
- n,k의 개수가 작음 > 완전탐색
- 매번 움직일때마다 오면 안되는 곳에 왔는지 체크
- 전체 필드의 외곽에 벽을 한칸씩 추가해서, 벽에 해당하는 좌표를 모두 오면안되는 곳으로 설정
- 몸이 길어진 만큼, 그전의 행동을 추적해서 오면안되는 곳에 추가. 새로운 곳으로 이동할 경우, 맨 뒤의 값은 제거하고 새로 이동된값을 가면 안되는 곳으로 넣어줌 > 큐
"""

#문제요약
"""
-n의 수가 크지 않음 > 완전탐색
-조건이 없다면, build_frame의 입력값에 따라 result를 그려주는 건 어렵지 않다
-그러면 build_frame이 요구하는 케이스별로, 실행해도 되는지 여부를 체크해주면 됨
-build_Frame이 요구하는 건 결국 2*2임. [설치or제거] * [바닥or보]
"""


n = int(input())
field = [[0]*n for _ in range(n)]

#for local test build_frame input
import json
build_frame = json.loads(input())

result = []

#작업진행여부 체크함수
def build_checker(frame,result):
    
    #기둥 삭제
    if frame[2] == 0 and frame[3] == 0:
        pass
    
    #기둥 설치
    if frame[2] == 0 and frame[3] == 1:
        pass
    
    #보 삭제
    if frame[2] == 1 and frame[3] == 0:
        pass
    
    #보 설치
    if frame[2] == 1 and frame[3] == 1:
        pass


#작업시작
for frame in build_frame:
    
    #작업을 진행해도 되는 경우
    if build_checker(frame,result):
        
        #삭제
        if frame[3] == 0:
            result = [i for i in result if i[0] != frame[0] and i[1] != frame[1]]
        
        #설치
        if frame[3] == 1:
            result.append(frame[0:2])
            
        
        
        
