a: set[int] = set([1, 2, 3, 4, 5])
b: set[int] = set([4, 5, 6, 7, 7])

print(a | b)  # set union
print(a & b)  # set intersection
print(a - b)  # set difference
print(a ^ b)  # set symmetric difference
