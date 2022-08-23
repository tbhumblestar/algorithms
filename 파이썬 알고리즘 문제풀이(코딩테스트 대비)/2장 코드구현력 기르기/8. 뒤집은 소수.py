n = int(input())

def reverse(num):
    reversed_num = str(num)[::-1]
    return int(reversed_num)

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True
        
nums_list = list(map(int,input().split()))

for num in nums_list:
    if is_prime(reverse(num)):
        print(reverse(num),end = ' ')