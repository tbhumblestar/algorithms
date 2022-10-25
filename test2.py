import functools 

def comparator(a,b):
    #문자열 더하기
    t1 = a+b
    t2 = b+a
    
    #t1 > t2이면 1, t1 = t2이면 0, t2 > t1이면 -1
    return (int(t1)>int(t2)) - (int(t2)>int(t1))


def solution(numbers):
    
    str_numbers = [str(i) for i in numbers]
    str_numbers.sort(key=functools.cmp_to_key(comparator),reverse=True)
    
    #0,0,0,0,0체크
    answer = str(int(''.join(str_numbers)))
    
    return answer
    

#t1
numbers	= [6, 10, 2]
res = "6210"

#t2
numbers	= [3, 30, 34, 5, 9]
res = "9534330"

numbers = [0,0,0,0,0]
print(solution(numbers))


