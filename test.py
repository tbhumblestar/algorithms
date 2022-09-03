n,m = map(int,(input().split()))
num_list = list(map(int,input().split()))

count = 0

for i in range(0,len(num_list)):
    for j in range(i+1,len(num_list)):
        if num_list[i] != num_list[j]:

            count += 1           
print(count)