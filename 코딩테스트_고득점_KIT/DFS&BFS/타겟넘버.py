from itertools import permutations

def solution(numbers, target):
    
    #0은 -, 1은 +
    lst = [0,1]
    
    perm_lst = list(permutations(lst,len(lst)-1))
    
    
    
    
    
    answer = 0
    
    
    return answer

#t1
numbers = [1, 1, 1, 1, 1]	
target = 3
res = 5

#t2
numbers = [4,1,2,1]	
target = 4
res = 2


print(solution(numbers,target))