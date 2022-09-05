#문제종류 : 구현

#유용한 부분(U)
"""
-filter적용
-map을 filter개체에 적용
"""

#풀이법 설명
"""
-sorted > 입력어가 리스트가 됨
-filter를 사용해 알바펫과 숫자로 나눠줌
"""

n = str(input())

sorted_n = sorted(n)

num_list = ['1','2','3','4','5','6','7','8','9','0']

word_list = list(filter(lambda x:x not in num_list,sorted_n))
nums_list = list(map(int,filter(lambda x:x in num_list,sorted_n)))

print(''.join(word_list)+str(sum(nums_list)))