#문제종류 : 구현

#유용한 부분(U)
"""

"""


#풀이법 설명
"""
-입력된 숫자를 문자열로 바꿈
-문자열의 절반까지 더한합과 절반 후의 합을 비교
"""


n = str(input())

length = len(n)

left_sum = 0
right_sum = 0

for i in range(0,length//2):
    left_sum += int(n[i])

for i in range(length//2,length):
    right_sum += int(n[i])
    
if left_sum == right_sum:
    print("lucky")
else:
    print("READY")