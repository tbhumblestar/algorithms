#그리디 알고리즘
"""
탐욕적인 선택들이 만들어낼 수 없는 결과를 탐욕적이지 않는 선택들도 만들어낼 수 없다는 것을 증명하면 됨. 그러면 굳이 탐욕적이지 않은 선택을 할 필요가 없으니까
"""

#정당성 검토

"""
?
"""

#풀이법 요약

"""

-이코테 답지를 보고 아이디어는 이해한 상태임

"""


from collections import Counter

food_times = list(map(int,input().split()))
k = int(input())
min_num = min(food_times)
max_num = max(food_times)

index_dict = {}
count_dict = {}


for i in range(max_num,min_num-1,-1):    
    #리스트에서 중복되는 값 index찾기
    index_dict[i] = list(filter(lambda x:food_times[x]==i,range(len(food_times))))
    
    if i == max_num:
        count_dict[i] = len(index_dict[i])
    else:
        count_dict[i] = len(index_dict[i]) + count_dict[i+1]
        
    

print(index_dict)
print(count_dict)


print(index_dict)

count = 0
for i in range(min_num,max_num+1):
    count += count_dict[i]
    print(count)
    if k < count:
        print(index_dict[i][count-k-1]+1)

        
    
# food_t

# def solution(food_times, k):
#     if k > sum(food_times):
#         return -1
#     min_num = min(food_times)
#     max_num = max(food/_times)
    
#     count = 0
#     count_dict = {}
#     Counter=()
#     for i in range(min_num,max_num+1):
        
    
#     answer = 0
    
    
#     return answer