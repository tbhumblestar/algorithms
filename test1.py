n = int(input())
nums = list(map(int,input().split()))

sorted_array = []

def insertion_sort(arr):
    i = len(arr)-1
    while i > 0 and arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i -= 1

for num in nums:
    sorted_array.append(num)
    insertion_sort(sorted_array)
    length = len(sorted_array)
    
    if length % 2 == 0:
        idx = length // 2 -1
    else:
        idx = length // 2
    print(sorted_array)
    print(sorted_array[idx])
    # print(sorted_array[idx],end = ' ')
    
    
#t1
# 5
# 1 5 3 -1 3

#t2
# 5
# 0 -1 -2 -3 -4

#t3
# 9
# 0 3 2 1 9 -1 5 -2 3 -3 -4 7