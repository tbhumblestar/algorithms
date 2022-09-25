import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

direction = ['r','l','d','u']
dx = [0,0,+1,-1]
dy = [+1,-1,0,0]
word_list = []

def dfs(x,y,count,word,n,m,k,r,c):
    
    # print("1 x, y, word, count :",x,y,word,count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 1 or nx > n or ny <1 or ny > m:
            continue
        
        test_word = word
        test_count = count
        
        test_word += direction[i]
        test_count += 1
        
        # print("2 nx, ny, test_word, test_count :",nx,ny,test_word,test_count)
        
        if test_count == k:
            if nx == r  and ny == c:
                word_list.append(test_word)
                continue
            else:
                continue
            
        # print("3 nx, ny, test_word, test_count :",nx,ny,test_word,test_count)
        dfs(nx,ny,test_count,test_word,n,m,k,r,c)
    
#n:세로길이, m : 가로길이, x:시작점의 가로좌표, y: 시작점의 세로좌표, r: 도착점의 가로좌표, c:도착점의 세로좌표
def solution(n, m, x, y, r, c, k):
    
    dfs(x,y,0,'',n,m,k,r,c)
    
    answer = 'impossible'
    
    if word_list:
        word_list.sort()
        answer = word_list[0]
    
    return answer


#t1
n,m,x,y,r,c,k = 3,4,2,3,3,1,5

#t2
n,m,x,y,r,c,k = 2,2,1,1,2,2,2

#t3
n,m,x,y,r,c,k = 3,3,1,2,3,3,1000


answer = solution(n, m, x, y, r, c, k)
print(answer)