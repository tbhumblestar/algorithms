#문제종류 : 그리디
#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42883

#유용한 부분
"""
프로그래머스의 1등풀이가 존나멋짐..
그리고 기본적으로 코드를 다 짜고 나서, 어떻게든 시간복잡도를 줄일 수 있도록, for문을 최소화 해볼 것
그리고 반드시 하나하나씩만 진행하자

"""


#풀이
""" 
#내풀이
-0번부터 k번까지(총 k+1개를 비교하는 것임) 수중에서 제일 큰수의 인덱스를 구함
-k앞의 수들 다 제거
-제거한 수만큼 k를 빼줌
-제일 큰수는 따로뺌
-k가남아 있으면 이걸 반복

#프로그래머스 1등풀이
-스택을 활용
-정말 멋잇다...

"""
def solution(number, k):
    
    
    # print("number :",number)

    test_number = number
    word = ''
    
    
    #k==0이 된다 > 더이상 제거할 수 있는 수가 없다
    while k != 0:
        
        #k~k+1까지의 수중에서 가장 큰수의 인덱스

        val = 1
        for i,v in enumerate(test_number[:k+1]):
            
            if int(v) == 9 :
                max_idx = i
                break
            else:
                if int(v) > val:
                    val = int(v)
                    max_idx = i

        k -= max_idx
        word += test_number[max_idx]
        test_number = test_number[max_idx+1:]
        # print(test_number)

        #남은 k의 수가 남은 글자수와 같다 > 뒤의 수를 다 제거해주면 됨
        if k == len(test_number):
            test_number =''
            break
    
    return str(word + test_number)



#t1
number = '1924'
k = 2
res = 94

#t2
number = '1231234'
k = 3
res =3234

#t3
# number = '4177252841'
# k = 4
# res = 775841

print(solution(number,k))

#-----

#프로그래머스풀이
def solution(number,k):
    """
    -스택을 활용
    -특정 수가 기준이 되었을 때, 삭제 횟수가 허락하는 하에서, 지보다 작으면 다 없애는 것
    -k가 허락되는 한에서, 한 번 등장한 큰수보다 앞에 큰 수가 올 수 없게 만듬
    
    """
    
    
    #첫번째 수를 스택에 넣음
    stack = [number[0]]
    
    #1번부터 검사시작(0번은 스택에 넣었으니까)
    for num in number[1:]:
        
            #조건1 : 스택이 채워져있다면 > 현재기준값(num)과 비교할 앞자리 수가 있다면
            #조건2 : 스택의 마지막 값이 현재기준값보다 작다면 > 즉 k가 허락하는 선에서, 자기보다 작은 수를 다 자르겠다는 것임
            #조건3 : 삭제할 카운트인 k가 남아있다면
            #수행 : 스택에서 삭제하고 삭제카운트를 하나 감소하겠다
            while len(stack) >0 and stack[-1] < num and k >0:
                k -= 1
                stack.pop()
                
            #현재 수를 스택에 추가
            stack.append(num)
            
    #작업을 다 진행했는데 > 오름차순이거나 같은 수들만 반복돼서 k가 남아있다면 뒤에서 부터 삭제 
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)