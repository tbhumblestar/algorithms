#순열
from itertools import combinations, permutations

data = [(1, 2), (2, 2), (3, 4)]

#permutaions
permutations_result = list(permutations(data,2))
print("permutations_result : ",permutations_result)

#combinations
combinations_result = list(combinations(data,2))
print("combinations_result : ",combinations_result)