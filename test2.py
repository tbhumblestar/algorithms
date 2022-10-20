a = "123"

from itertools import permutations

a = list(permutations(a,2))
print(a)

a = ('1','2')
b = ''.join(a)
print(b)

print(int('12'))
print(int('012'))

print(int('12') == int('012'))