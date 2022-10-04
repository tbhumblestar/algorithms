letters = input()

num = ''

for let in letters:
    if let in '0123456789':
        num += let

num = int(num)
print(num)

count = 0

for i in range(1,num+1):
    if num % i == 0 :
        count +=1
        
print(count)
#testcase
#g0en2Ts8eSoft