#그리디 알고리즘
#정당성 검토
# '가장 큰 수 * k + 두번째로 큰수'의 배열이 반복됨. ex([6,6,6,5],[6,6,6,5]...)

n,m,k = map(int,input().split())
nums_list = list(map(int,input().split()))

max_num = max(nums_list)
nums_list.remove(max_num)
max_num2 = max(nums_list)

quotient = m // (k+1)
remainder = m % (k+1)

res = quotient*(max_num*k + max_num2) + remainder * max_num

print(res)