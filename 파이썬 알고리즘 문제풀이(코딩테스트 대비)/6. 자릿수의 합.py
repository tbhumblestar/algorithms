#문제명 : 자릿수의 합
#출처 : 인프런 / 파이썬 알고리즘 문제풀이(코딩테스트 대비) by 김태원 / 코드 구현력 기르기(2장)-6번문제

########################################################################################

# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.
# ▣ 출력설명
# 자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.
# ▣ 입력예제 1 3
# 125 15232 97
# ▣ 출력예제 1 97

##############################################################

#포인트

#함수를 만들어서 사용
#자연수의 각 자릿수를 더하는 두가지방법
# 1)일자리를 더하고, 10으로 나눈 몫을 반환한 후 다시 일자리를 더하고 10으로 나눔. 이를 반복 
# 2)숫자를 문자열로 바꾼 후, for문을 돌려 각 글자를 int시켜 더함

##############################################################
#정답코드

n = int(input())
        
def digit_sum(num):
    # #방법1
    sum = 0
    while num > 0 :
        sum += (num%10)
        num = (num//10)
        
    #방법2
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum

max_sum = 0
digit_list = []
res = 0
nums = list(map(int,input().split()))
for i in nums:
    _digit_sum = digit_sum(i)
    if _digit_sum > max_sum:
        max_sum = _digit_sum
        res = i

print(res)