#문제종류 : 완전탐색
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/84512

#풀이
"""
-완전탐색사용 > 올 수 잇는 모든 글자를 체크
-모든 자리에 ['_','A','E','I','O','U']가 올 수 있다고 가정하되 빈칸('_')을 처리하는 게 좀 어려웠음
    만약 '_'가 등장한다면, 뒤의 글자들도 모두 '_'여야만 유효한 글자임
    따라서 단어가 생성될 때마다 모두 +1을 해주고
    만약 '_'가 등장하고 그 뒤에 '_'가 등장하지 않는다면 -1을 해줌
-또한 '_____'는 단어가 아니지만, 만든 로직에 따르면 카운트가 되어버리므로 이 경우를 무조건 한번 뺴준다
"""
def solution(word):
    
    if len(word) != 5:
        word += "_"*(5-len(word))
    
    
    cnt = 0
    letters = ['_','A','E','I','O','U']
    for i in letters:
        for j in letters:
            for p in letters:
                for q in letters:
                    for s in letters:
                            test_letters = i+j+p+q+s
                            
                            cnt += 1
                            # print("cnt_fir :",cnt)
                            
                            
                            
                            if '_' in test_letters:
                                
                                #어떤 글자가 '_'인지 체크
                                for idx in range(5):
                                    if test_letters[idx] == '_':
                                        if test_letters[idx:] != '_'*(5-idx):
                                            cnt -= 1
                                            # print("cnt_mid :",cnt)
                                            break


                            # if i == 'A':
                                # print("test_letters :",test_letters)
                                # print("cnt_lst :",cnt)
                            
                            #단어가 일치하면 count를 리턴
                            if test_letters == word:
                                #맨 첫번째 '_____'를 빼줘야 함
                                return cnt-1
                                
                            
                            
                            
                                    
                                    
    


# #t1
# word = 'AAAAE'
# #t2
# word = 'AAAE'
# #t3
# word = 'I'
# #t4
# word =  "EIO"

# ans = solution(word)
# print(ans)