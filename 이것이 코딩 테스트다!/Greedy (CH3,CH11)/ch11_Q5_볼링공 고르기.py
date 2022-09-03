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
-문제를 이상하게 이해해서 그렇지 문제자체는 엄청 쉬운편
-for문으로 리스트를 돌리면서, 중복되지 않도록 자신의 인덱스 너머이면서 & 자신과 무게가 일치하지 않는 공들의 개수를 모두 더해주면 됨
"""



n,m = map(int,(input().split()))
num_list = list(map(int,input().split()))

count = 0

for i in range(0,len(num_list)):
    for j in range(i+1,len(num_list)):
        if num_list[i] != num_list[j]:

            count += 1           
print(count)