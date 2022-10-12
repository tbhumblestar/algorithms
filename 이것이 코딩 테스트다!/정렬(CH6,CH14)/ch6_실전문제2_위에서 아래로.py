n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))
    
    
lst.sort(reverse=True)
for i in lst:
    print(i,end =' ')