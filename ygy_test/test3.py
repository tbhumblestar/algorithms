from optparse import check_builtin


def solution(S, C):
    
    let_dict = {}
    cnt_dict = {}
    
    for i,v in enumerate(S):
        let_dict.setdefault(v,[])
        let_dict[v].append(i)
        
        cnt_dict.setdefault(v,0)
        

    
    #개수
    check_dict_cnt = len(cnt_dict)

    cnt = 0
    
    for idx_i,i in enumerate(C):
        
        for idx,val in let_dict.items():
            
            for j_idx,j in enumerate(val):
                
                if j >= i:
                    val[j_idx] = -j
                    cnt_dict[idx] += 1
                    print("here!")
                    print(cnt_dict)
                    
                    if len(let_dict[idx]) == 1 and cnt_dict[idx] == 1:
                        cnt += 1

                    
                    elif cnt_dict[idx] == len(let_dict[idx])-1:
                        cnt += 1

                        
                        
                        if cnt == check_dict_cnt:

                            return idx_i+1
                    break   
    return -1

#t1
s = 'aabcba'
c = [1,3,2]
r = 2

#t2
# s = 'aaa'
# c = [1,2]
# r = 2

# #t3
# s = 'aabcddcb'
# c = [3,5,1,4,7]
# r = 3

# #t4
s = 'wkwk'
c = [1]
r = -1

print(solution(s,c))