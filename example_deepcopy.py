import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0][0] = 100
print(b)  # ?
print(c)  # ?