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


# n = int(input())
# field = [[0]*n for _ in range(n)]

#for local test build_frame input
import json
build_frame = json.loads(input())

result = []

def result_checker(result):

    #각 구조물별로 괜찮은지 체크
    for frame in result:
        
        x = frame[0]
        y = frame[1]
        a = frame[2]
        
        broken = 0
        
        #기둥
        if a == 0:
            
            if y == 0:
                broken += 1
            
            #보 + 기둥
            #보(앞에 2개) + 기둥(뒤에 1개)
                for obj in result:
                    if obj in [[x-1,y,1],[x,y,1],[x,y-1,0]]:
                        broken += 1
        
        #보
        if a == 1 :
        
            #보가 있는지 확인
            if [x-1,y,1] in result and [x+1,y,1] in result:
                broken += 1
            
        #기둥이 있는지 확인
            for obj in result:
                if obj in [[x,y-1,0],[x+1,y-1,0]]:
                    broken += 1
            
        
        #부서진다면
        if broken == 0:
            return False
    
    return True
        

#작업진행여부 체크함수
def build_checker(frame,result):
    
    print("for_frame :",frame)
    
    
    x = frame[0]
    y = frame[1]
    a = frame[2]
    b = frame[3]
    
    #기둥 : a = 0
    """
    -바닥위에 설치되거나
    -보의 한쪽 끝부분 위에 있거나
    -다른 기둥 위에 있거나
    """
    
    #보 : a = 1
    """
    -한쪽 끝부분이 기둥 위에 있거나
    -양쪽끝부분이 다른 보와 연결되어 있거나
    """
    
    #삭제
    if b == 0 :
        
        #삭제한 test_result 생성
        test_result = [i for i in result if i[0] != frame[0] or i[1] != frame[1] or i[2] != frame[2]]
        
        if result_checker(test_result):
            return True
        
        print("삭제실패_result : ",result)
    
    #기둥 설치
    if a == 0 and b == 1:
        if y == 0:
            return True

        #보(앞에 2개) + 기둥(뒤에 1개)
        for obj in result:
            if obj in [[x-1,y,1],[x,y,1],[x,y-1,0]]:
                return True
    
    #보 설치
    if a == 1 and b == 1:
        #보가 있는지 확인
        if [x-1,y,1] in result and [x+1,y,1] in result:
            return True
            
        #기둥이 있는지 확인
        for obj in result:
            if obj in [[x,y-1,0],[x+1,y-1,0]]:
                return True
    
    print("build_checker :","False")
    print("build_checker_result :",result)
    return False


print(build_frame)

#작업시작
for frame in build_frame:
    
    
    print(result)
    #작업을 진행해도 되는 경우
    if build_checker(frame,result):
        print(result)
        print("build_checker :","True")
        
        #삭제
        if frame[3] == 0:
            result = [i for i in result if i[0] != frame[0] or i[1] != frame[1] or i[2] != frame[2]]
        
        #설치
        if frame[3] == 1:
            result.append(frame[0:3])
            
        
        print("for_result :",result)
            
        
print(sorted(result))
        
#1 [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#2 [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]