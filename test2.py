A = [(1,3),(4,2)]

#reverse : 내림차순
A.sort(key=lambda x:x[1],reverse=True)
print(A)