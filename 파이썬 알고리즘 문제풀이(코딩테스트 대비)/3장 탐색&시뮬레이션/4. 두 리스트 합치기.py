n1 = input()
lst1 = list(map(int,input.split()))

n2 = input()
lst2 = list(map(int,input.split()))

lst = lst1 + lst2
lst.sort()
print(lst)

#testcase
# 3
# 1 3 5
# 5
# 2 3 6 7 9

#Answer1
# 1 2 3 3 5 6 7 9
