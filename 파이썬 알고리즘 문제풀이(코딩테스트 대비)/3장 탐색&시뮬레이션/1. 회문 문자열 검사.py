def checker(word):
    length = len(word)
    
    for i in range(length):
        if word[i] != word[-i-1]:
            return False
        
    return True

n = int(input())
for i in range(n):
    word = input()
    if checker(word):
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
        
#testcase
# 5
# level
# moon
# abcba 
# soon 
# gooG