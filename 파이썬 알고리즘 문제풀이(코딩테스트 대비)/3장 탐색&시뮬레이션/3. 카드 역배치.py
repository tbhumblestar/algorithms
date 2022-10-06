lst = [i for i in range(1,21)]

for i in range(10):
    n1,n2 = map(int,input().split())
    print(n1,n2)
    test_lst = lst[n2-1:n1-2:-1]
    print(test_lst)
    
    for j in range(len(test_lst)):
        lst[n1-1+j] = test_lst[j]
    print(test_lst)
    
    print(lst)
        
#test
# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20

#answer
# 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20