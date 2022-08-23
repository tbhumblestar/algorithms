

n = int(input())

num_list = list(map(int,input().split()))
avg = int(round(sum(num_list) / len(num_list),0))


index = 0

for i,v in enumerate(num_list):
    if abs(v-avg) < abs(num_list[index]-avg):
        index = i
    elif abs(v-avg) == abs(num_list[index]-avg):
        if v > num_list[index]:
            index = i

print(f'{avg} {index+1}')

# 45 73 66 87 92 67 75 79 75 80