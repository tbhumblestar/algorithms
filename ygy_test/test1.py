def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10
    
    answer = []
    while True:
            
        if stack1:
            s1 = [1,stack1[-1]]
        else:
            s1 = [1,-1]
            
        if stack2:
            s2 = [2,stack2[-1]]
        else:
            s2 = [2,-1]
            
        if stack3:
            s3 = [3,stack3[-1]]
        else:
            s3 = [3,-1]
            
        compare_storage = [s1,s2,s3]
        _max = max(compare_storage,key = lambda x:x[1])
        
        if len(stack1) == 0 and len(stack2) == 0 and len(stack3)== 0:
            break
        
        if _max[0] == 1:
            stack1.pop()
            answer.append('1')
        
        if _max[0] == 2:
            stack2.pop()
            answer.append('2')
            
        if _max[0] == 3:
            stack3.pop()
            answer.append('3')
        
        
    
    return ''.join(answer)

#test1
# stack1 = [2,7]
# stack2 = [4,5]
# stack3 = [1]
# res = 12213

#test2
# stack1 = [10,20,30]
# stack2 = [8]
# stack3 = [1]
# res = 11123

# #test3
# stack1 = [7]
# stack2 = []
# stack3 = [9]
# res = 31

#test4
# stack1 = []
# stack2 = []
# stack3 = []
res = ''

# test5
stack1 = [9,9,9,9,9,9,9]
stack2 = [9,9,9,9,9,9,9]
stack3 = []

print(solution(stack1,stack2,stack3))
