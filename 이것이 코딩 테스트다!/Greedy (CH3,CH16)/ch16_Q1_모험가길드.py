#그리디 알고리즘


#정당성 검토
"""
공포도가 낮은 사람은 언제나 공포도가 높은 사람의 역할을 할 수 있다. 따라서 공포도가 높은 사람들끼리 먼저 짠다고 공포도가 낮은 사람들이 만들 수 없는 팀을 구성할 수 없다. 즉 공포도가 높은 사람들끼리 만들어낼 수 있는 특별한 경우의 수가 존재하지 않음.
"""

#풀이법 요약
"""
입력된 수들을 오름차순으로 정렬
숫자:출현횟수 형식의 dict구현
dict의 각 원소에서 v//i 가 곧 하나의 팀이 되므로 cnt에 더해줌
각 원소에서 v/%를 한 값이 해당 수에서 떠나지 못한 팀이 되므로, 그다음 숫자에 더해주면 됨(그리디))
"""


n = int(input())
nums_list = list(map(int,input().split()))

nums_list.sort()

nums_dict = {}
for i in nums_list:
    
    if nums_dict.get(i):
        nums_dict[i]+=1
    else:
        nums_dict[i] = 1

max_num = max(nums_list)

cnt = 0    

for i,v in nums_dict.items():
    cnt += (v//i)
    if i == max_num:
        pass
    else:
        nums_dict[i+1] += (v%i)
        
print(cnt)