import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 100
print(a)  # [[100, 2], [3, 4]]  <-- changed unexpectedly