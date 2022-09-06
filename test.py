#

#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60059

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