from socket import AI_NUMERICSERV


n = int(input())
answer_list = list(map(int,input().split()))

score_list = [0]*(n+1)
print(score_list)
for i,v in enumerate(answer_list):
    if v == 1:
        score_list[i+1] = score_list[i]+1

print(sum(score_list))