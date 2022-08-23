#문제명 : 정다면체
#출처 : 인프런 / 파이썬 알고리즘 문제풀이(코딩테스트 대비) by 김태원 / 코드 구현력 기르기(2장)-5번문제

########################################################################################

#문제

# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
# ▣ 입력설명
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
# ▣ 출력설명
# 첫 번째 줄에 답을 출력합니다.
# ▣ 입력예제 1 46
# ▣ 출력예제 1 567

##############################################################

#포인트

#value값에 따라 dict를 정렬(dict.items(), sorted, lambda)

##############################################################
#정답코드

n,m = map(int,input().split())

count_dict = {}

for i in range(n):
    for j in range(m):
        
        num = (i+1) + (j+1)
        
        if count_dict.get(num):
            count_dict[num] += 1
        else:
            count_dict[num] = 1


#value값에 따라 dict를 정렬하는 법
sorted_count_dict = sorted(count_dict.items(),key=lambda x:x[1],reverse = True)

max_count = sorted_count_dict[0][1]

for i in sorted_count_dict:
    if i[1] == max_count:
        print(i[0],end = ' ')