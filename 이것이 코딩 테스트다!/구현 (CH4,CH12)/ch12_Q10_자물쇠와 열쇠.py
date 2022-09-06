#문제종류 : 구현
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60059

#유용한 부분(U)
"""
"""


#풀이
"""
- 완전탐색 : 리스트의 수가 그렇게 많지 않음 > 완전탐색
- 자물쇠를 열쇠가 둘러싸는 형태토, M(열쇠의 한 변)+N(자물쇠의 한 변)+M을  한변으로 하는 넓은 Lock을 만듬
- 열쇠를 0/90/180/270도 회전시킨 4개의 열쇠를 만듬
- 4개의 열쇠를, 새로만들어진 넓은 Lock을 처음부터 끝까지 순회시킴
- 순회시키면서, Lock과 Key를 더해줌. 이때 실제 Lock 범위에 해당하는 element들이 모두 1이 될 경우 1을 반환
- 네가지 열쇠를 첫칸부터 한칸씩 이동시켜가며, 열쇠의 1들을 한번에 포함시킬 수 있는지 확인
"""

import json

# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(matrix):
    n = len(matrix) # 행 길이 계산
    m = len(matrix[0]) # 열 길이 계산

		#이런식으로 하면, 각 element가 동일한 주소를 참조하게 되어 값이 같이 변함
		#rotated = [[0] * n] * m     

    rotated = [[0] * n for _ in range(m)] # 결과 리스트
    
		
    for i in range(n):
        for j in range(m):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated


def lock_checker(lock,lock_length,key_length):
    
    for i in range(lock_length):
        for j in range(lock_length):
            #1이상이면 안됨. 2는 에러가 나야함. 무조건 1인지만 체크
            if lock[key_length+i][key_length+j] != 1:
                return False
    return True


    
def solution(key, lock):
    
    #길이 설정
    key_length  = len(key)
    lock_length = len(lock)
    total_length = key_length + lock_length + key_length
    
    #-2추가 할지? > -2추가 하면 안됨. 처음부터 1만 가득한(그냥 지혼자 열려버리는) Lock이 있을 때, -2를 빼면 반드시 모든 경우에 lock에 관여하게 됨
    
    new_lock = [[0]*total_length for _ in range(total_length)]
    print(new_lock)
    for i in range(lock_length):
        for j in range(lock_length):
            if lock[i][j] == 1:
                print(i,j)
                print(key_length)
                new_lock[i+key_length][j+key_length] =1
    
    
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        
        for i in range(key_length+lock_length):
            for j in range(key_length+lock_length):
                
                for n in range(key_length):
                    for m in range(key_length):
                        new_lock[n+i][m+j] += key[n][m]
                if lock_checker(new_lock,lock_length,key_length) == True:
                    return True
                for n in range(key_length):
                    for m in range(key_length):
                        new_lock[n+i][m+j] -= key[n][m]
                            
    return False
                

#테스트 / 리스트변환
key = json.loads(input())
lock = json.loads(input())


#Key  : [[0,0,0],[1,0,0],[0,1,1]]
#Lock : [[1,1,1],[1,1,0],[1,0,1]]

print(lock)
a = solution(key,lock)
print(a)



#아래는 기존 버전. 프로그래머스 홈페이지에서 실패는 기록되지 않았으나, 시간초과 케이스 3가지가 나왔음


#풀이
"""
- 완전탐색 : 리스트의 수가 그렇게 많지 않음 > 완전탐색
- 자물쇠를 열쇠가 둘러싸는 형태토, M(열쇠의 한 변)+N(자물쇠의 한 변)+M을  한변으로 하는 정사각형을 만듬
- 열쇠의 1들과 자물쇠의 1들의 좌표를 구함
- 열쇠를 0/90/180/270도 회전시켰을 때의 좌표를 구함 > 90도씩 돌릴때, 각 좌표가 어떻게 변하는지 확인
- 네가지 열쇠를 첫칸부터 한칸씩 이동시켜가며, 열쇠의 1들을 한번에 포함시킬 수 있는지 확인
"""



import json, copy

def coordinates_maker(list,length):
    
    d = []
    
    for i in range(length):
        for j in range(length):
            if list[i][j] == 1:
                d.append([i,j])
    
    return d

def list_rotater(list,length):
    
    d_0 = list
    
    #이런식으로 하면 리스트 특성상 메모리 주소가 복사되어 값들이 한번에 바뀜(주소참조)
    #d_90 = [[0]*(length)]*length
    
    #90
    d_90 = [[0] * (length) for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if list[i][j] == 1:
                d_90[j][length-1-i] = 1
    
    #180
    d_180 = [[0] * (length) for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if d_90[i][j] == 1:
                d_180[j][length-1-i] = 1
    
    #270
    d_270 = [[0] * (length) for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if d_180[i][j] == 1:
                d_270[j][length-1-i] = 1
    
    return [d_0,d_90, d_180, d_270]
    
    

def solution(key, lock):
    
    #길이 설정
    key_length  = len(key)
    lock_length = len(lock)
    length = key_length + lock_length
    
    #0,90,180,270도 회전된 key 획득 후, 각 key의 값에 좌표를 줌
    lists = list_rotater(key,key_length)
    coordinated_lists = [coordinates_maker(i,key_length) for i in lists]
    
    #lock을 뒤집음
    switched_lock = [[0]*lock_length for _ in range(lock_length)]
    for i in range(lock_length):
        for j in range(lock_length):

            switched_lock[i][j] = 0 if lock[i][j] == 1 else 1
    
    #lock에 좌표를 부여
    switched_coordinated_lock  = coordinates_maker(switched_lock,lock_length)
    # print("switched_coordinated_lock :",switched_coordinated_lock)
    for i in switched_coordinated_lock:
        i[0] += key_length
        i[1] += key_length

    point_count = len(switched_coordinated_lock)

    simple_coordinated_lock = coordinates_maker(lock,lock_length)
    for i in simple_coordinated_lock:
        i[0] += key_length
        i[1] += key_length

    # print("point_count : ",point_count)
    # print("coordinated_lists :",coordinated_lists)
    # print("switched_coordinated_lock :",switched_coordinated_lock)
    # print("simple_coordinated_lock :",simple_coordinated_lock)
    
    #Key들을 이동
    for key in coordinated_lists:
        for i in range(length+1):
            for j in range(length+1):
                use_key = copy.deepcopy(key)
                for point in use_key:
                    point[0] += i
                    point[1] += j
                    
                    if point in simple_coordinated_lock:
                        break
                    
                    else:
                    
                        count = 0
                        
                        #이동된 키가, lock에 들어맞는지 확인
                        for lock_point in switched_coordinated_lock:
                            if lock_point in use_key:
                                count += 1
                        
                    if count == point_count:
                        return True


    # print("coordinated_lists :",coordinated_lists)
    # print("switched_coordinated_lock :",switched_coordinated_lock)
    
    
    return False


#테스트 / 리스트변환
key = json.loads(input())
lock = json.loads(input())


#Key  : [[0,0,0],[1,0,0],[0,1,1]]
#Lock : [[1,1,1],[1,1,0],[1,0,1]]

print(lock)
a = solution(key,lock)
print(a)