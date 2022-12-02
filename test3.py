n = int(input())

contact_lst = []
for _ in range(n):
    p = input().split(' ')
    phone_number = p[1].split('-')
    phone_number.append(p[0])
    contact_lst.append(phone_number)

    
contact_lst.sort(key=lambda x:(x[3],x[1],x[2]))

for contact in contact_lst:
    print(f'{contact[3]} {contact[1]}-{contact[2]}-{contact[3]}')



## t1
# 3
# kim 010-1111-1111
# eve 010-9999-9999
# kim 010-0000-0000

#t2
# 5
# aaaa 010-7470-9619
# aaa 010-5711-7180
# aa 010-3009-2551
# a 010-4362-3829
# abc 010-4166-8204

#t3
# 7
# asdf 010-9999-9999
# dddd 010-0000-0000
# a 010-4817-2344
# b 010-0000-0001
# aaaa 010-0000-0000
# aaa 010-0000-0001
# aaa 010-0000-0002