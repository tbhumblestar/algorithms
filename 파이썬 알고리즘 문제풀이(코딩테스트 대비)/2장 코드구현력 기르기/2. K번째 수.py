count = int(input())
for i in range(count):

    N,s,e,k = map(int,input().split())
    num_list = list(map(int,input().split()))


    
    selected_and_sorted_num_list = sorted(num_list[s-1:e])
    print(f"#{i+1} {selected_and_sorted_num_list[k-1]}")