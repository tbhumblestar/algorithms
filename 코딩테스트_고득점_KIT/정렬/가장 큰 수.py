#문제종류 : 정렬
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42746

#풀이
"""
아이디어가 매우 중요
1. 숫자를 비교할 때, str형태로 비교하면 실제로 숫자가 얼마나 큰지가 아니라, 첫번째 글자부터 한 글자씩 비교를 진행. 만약 동일한 글자일 경우 그 다음으로 넘아감
예를 들어 13과 121중 큰수는 121을 str형태로 비교하면 13의 두번째 글자인 3이 121의 두번째 글자인 2보다 크기때문에 13이 더 큰것으로 나옴

2. 숫자가 1~1000까지이므로,숫자를 str로 바꾼 후, *3을 해서 비교

그러면 아래와 같이 됨
3 > 333
31 > 313131
41 > 414141
444 > 444444444

이걸 str로 비교하면, 의도한대로 정렬됨. 
특히 두자리수와 세자리수를 비교하는 게 진짜 멋지다고 생각한다..

41과 413를 비교하면 41이 앞에 나와야함
실제로 414141 과 413413413을 비교하면 414141이 앞에 나오게 됨

또 41과 414를 비교하면 414가 앞에 나와야 함
414414414 414141
세번째 글자를 넘어서 네번째 글자에서 비교가 되기 때문에 진짜 fancy한 방법이라고 생각된다..
------------------------------
풀이
-문자열로 바꾸고, *3을 함
-정렬

## 두번째 풀이
-key에 functools.cmp_to_key를 사용하여 정렬기준을 제시함
-첫번째 풀이는 아이디어가 너무좋아서 다른 데 응용하기가 힘든 첫번째 풀이에 비해, 두번쨰 풀이가 일반성이 높아 다른 문제에 적용할만 해보임
"""
import functools


def solution(numbers):
    
    str_numbers = [[str(i)*3,str(i)] for i in numbers]
    str_numbers.sort(reverse= True,key = lambda x:x[0])
    
    sorted_numbers = [i[1] for i in str_numbers]
    
    #0,0,0,0,0 이런 케이스 > 0 이나와야 되는데 00000이 나옴
    answer = str(int(''.join(sorted_numbers)))
    return answer

functools.cmp_to_key()
    

#t1
numbers	= [6, 10, 2]
res = "6210"

#t2
numbers	= [3, 30, 34, 5, 9]
res = "9534330"

numbers = [0,0,0,0,0]
print(solution(numbers))


#풀이 2

##### import functools 

# def comparator(a,b):
#     #문자열 더하기
#     t1 = a+b
#     t2 = b+a
    
#     #t1 > t2이면 1, t1 = t2이면 0, t2 > t1이면 -1
#     return (int(t1)>int(t2)) - (int(t2)>int(t1))


# def solution(numbers):
    
#     str_numbers = [str(i) for i in numbers]
#     str_numbers.sort(key=functools.cmp_to_key(comparator),reverse=True)
    
#     #0,0,0,0,0체크
#     answer = str(int(''.join(str_numbers)))
    
#     return answer
    

# #t1
# numbers	= [6, 10, 2]
# res = "6210"

# #t2
# numbers	= [3, 30, 34, 5, 9]
# res = "9534330"

# numbers = [0,0,0,0,0]
# print(solution(numbers))


