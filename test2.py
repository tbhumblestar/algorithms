dist = [1,2,3,4,5]
#이터레이터 생성
dist_iter = dist.__iter__()
print(dist_iter) # 이터레이터 확인

while True:
    try:
        print(dist_iter.__next__())
    except StopIteration as e:
        break
print("breaked")