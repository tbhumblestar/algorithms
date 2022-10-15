#문제종류 : 다이나믹 프로그래밍


#유용한 부분(U)
"""
-아이디어
"""


#풀이법 설명
"""
-생성되는 못생긴 수를 리스트에 넣음
-못생긴 수에 2,3,5를 곱하면 그대로 못생긴 수가 나온다는 것을 이용해야 함
-2,3,5가 인덱스를 가지고 잇으면서, 각자가 가진 인덱스에 2,3,5를 곱한 값들 중 가장 작은 값이 그 다음 값이 되어야 함
-또한 중복을 배제하기 위해, 만약 값이 같다면, 같은 값들의 인덱스를 함께 증가시키도록 해야 함(그래서 elif가 아니라 if를 사용함!)
"""


n = int(input())

#값을 담을 칸
ugly_num = [0]*(n+1)

#첫번째 값은 1
ugly_num[1] = 1


index_2 = index_3 = index_5 = 1
val_2 = 2
val_3 = 3
val_5 = 5

for i in range(2,n+1):
    ugly_num[i] = min(ugly_num[index_2]*val_2,ugly_num[index_3]*val_3,ugly_num[index_5]*val_5)
    
    if ugly_num[i] == ugly_num[index_2]*val_2:
        print("2")
        index_2 += 1
    if ugly_num[i] == ugly_num[index_3]*val_3:
        print("3")
        index_3 += 1
    if ugly_num[i] == ugly_num[index_5]*val_5:
        print("5")
        index_5 += 1
    print(ugly_num)
print(ugly_num[n])
