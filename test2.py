from collections import deque
from time import sleep

m,n = map(int,input().split())
res_queue = deque([])

sleep(2)
print()

for _ in range(n):
    action, size = input().split()
    size = int(size)
    
    if action == 'deposit':
        m += size
        
        
        while res_queue and res_queue[0] <= m:
            q = res_queue.popleft()
            m -= q
            print("in_while!",m,res_queue)
            # print(res_queue[0])
        
    if action == 'pay':
        if m >= size:
            m -= size
            
    if action == 'reservation':
        res_queue.append(size)
        while res_queue and res_queue[0] <= m:
            q = res_queue.popleft()
            m -= q
    print(m,res_queue)
print(m,res_queue)

# #t2
# 0 6
# deposit 10
# pay 5
# reservation 5
# reservation 5
# pay 5
# deposit 10


# #t3
# 0 9
# deposit 10
# pay 5
# reservation 5
# reservation 10
# reservation 5
# reservation 15
# reservation 5
# pay 5
# deposit 10

# #t4
# 25 13
# deposit 10
# pay 5
# reservation 5
# reservation 10
# reservation 5
# reservation 5
# reservation 5
# reservation 5
# reservation 5
# reservation 15
# reservation 5
# pay 5
# deposit 10

# #t5
# 25 14
# deposit 10
# pay 5
# reservation 5
# reservation 10
# reservation 5
# reservation 5
# reservation 5
# reservation 5
# reservation 5
# reservation 15
# reservation 5
# deposit 250
# pay 5
# deposit 10