n = int(input())

max_price = 0

for i in range(n):
    price = 0
    nums_count_list = [0]*6
    a,b,c = map(int,input().split())
    nums_count_list[a-1] += 1
    nums_count_list[b-1] += 1
    nums_count_list[c-1] += 1
    
    if 3 in nums_count_list:
        price = 10000 + a * 1000
        
    elif 2 in nums_count_list:
        price = 1000 + (nums_count_list.index(2)+1)*100
    else:
        price = max(a,b,c) * 100
    
    if price > max_price:
        max_price = price

print(max_price)