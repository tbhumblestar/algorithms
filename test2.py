result = [[1,2],[3,4],[5,6]]
frame = [1,2]


result = [i for i in result if i[0] != frame[0] and i[1] != frame[1]]

print(result)