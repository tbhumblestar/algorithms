n = int(input())

lst = []

for i in range(n):
    e = tuple(input().split())
    lst.append(e)
    
lst.sort(key=lambda x:int(x[1]))

for i in lst:
    print(i[0],end =' ')