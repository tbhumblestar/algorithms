n = str(input())

sorted_n = sorted(n)

num_list = ['1','2','3','4','5','6','7','8','9','0']

word_list = list(filter(lambda x:x not in num_list,sorted_n))
nums_list = list(map(int,filter(lambda x:x in num_list,sorted_n)))

print(''.join(word_list)+str(sum(nums_list)))