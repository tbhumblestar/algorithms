n = int(input())
nums = list(map(int,input().split()))

mid_array = []
sorted_array = []


for num in nums:
    sorted_array.append(num)
    sorted_array.sort()
    length = len(sorted_array)
    
    if length % 2 == 0:
        idx = length // 2 -1
    else:
        idx = length // 2
    
    mid_array.append(sorted_array[idx])
    print(sorted_array[idx],end = ' ')

