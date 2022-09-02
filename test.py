n= int(input())
num_list = list(map(int,input().split()))
num_list.sort()
print(num_list)

test = 0
for num in num_list:
    if test + 1 < num:
        break
    else:
        test += num
    print(test+1)